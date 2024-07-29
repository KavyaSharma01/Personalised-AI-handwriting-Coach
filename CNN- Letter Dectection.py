import torch
import torch.nn as nn
import torch.optim as optim
import gzip
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
import os

# Define a custom dataset class for EMNIST Letters
class EMNISTLetters(Dataset):
    def __init__(self, images_file, labels_file, mapping_file, transform=None):
        with gzip.open(labels_file, 'rb') as lbpath:
            self.labels = np.frombuffer(lbpath.read(), dtype=np.uint8, offset=8)

        with gzip.open(images_file, 'rb') as imgpath:
            self.images = np.frombuffer(imgpath.read(), dtype=np.uint8, offset=16).reshape(len(self.labels), 28, 28)

        with open(mapping_file, 'r') as mappath:
            self.mapping = {int(line.split()[0]): str(line.split()[1]) for line in mappath.readlines()}

        self.transform = transform

        self.valid_indices = [i for i, label in enumerate(self.labels) if label in self.mapping]
        self.labels = self.labels[self.valid_indices]
        self.images = self.images[self.valid_indices]

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        image = self.images[idx]
        char = self.mapping[self.labels[idx]]

        if len(char) == 1:
            label = ord(char) - ord('a')
        else:
            char = char[0]
            label = (ord(char) - ord('a')) % 26

        if self.transform:
            image = self.transform(image)

        return image, label


# Load EMNIST Letters dataset
def load_data():
    train_dataset = EMNISTLetters(
        '/Users/kavyasharma/Downloads/Emnist test/emnist-letters-train-images-idx3-ubyte',
        '/Users/kavyasharma/Downloads/Emnist test/emnist-letters-train-labels-idx1-ubyte',
        '/Users/kavyasharma/Downloads/Emnist test/emnist-letters-mapping.txt',
        transform=transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
        ])
    )

    test_dataset = EMNISTLetters(
        '/Users/kavyasharma/Downloads/Emnist test/emnist-letters-test-images-idx3-ubyte',
        '/Users/kavyasharma/Downloads/Emnist test/emnist-letters-test-labels-idx1-ubyte',
        '/Users/kavyasharma/Downloads/Emnist test/emnist-letters-mapping.txt',
        transform=transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
        ])
    )

    batch_size = 128
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    return train_loader, test_loader


class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 26)

    def forward(self, x):
        x = self.pool(nn.functional.relu(self.conv1(x)))
        x = self.pool(nn.functional.relu(self.conv2(x)))
        x = x.view(-1, 64 * 7 * 7)
        x = nn.functional.relu(self.fc1(x))
        x = self.fc2(x)
        return x


def train(model, train_loader, criterion, optimizer, epochs):
    train_losses = []
    train_accuracies = []

    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        epoch_loss = running_loss / len(train_loader)
        epoch_accuracy = 100 * correct / total
        train_losses.append(epoch_loss)
        train_accuracies.append(epoch_accuracy)

        print(f'Epoch {epoch + 1} loss: {epoch_loss:.4f}, accuracy: {epoch_accuracy:.2f}%')

    return train_losses, train_accuracies


def evaluate(model, test_loader, criterion):
    model.eval()
    running_loss = 0.0
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            loss = criterion(outputs, labels)
            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    loss = running_loss / len(test_loader)

    return loss, accuracy


def plot_metrics(train_losses, train_accuracies, test_loss, test_accuracy):
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))

    ax[0].plot(train_losses, label='Train Loss')
    ax[0].set_title('Loss')
    ax[0].legend()

    ax[1].plot(train_accuracies, label='Train Accuracy')
    ax[1].set_title('Accuracy')
    ax[1].legend()

    print(f'Test Loss: {test_loss:.4f}, Test Accuracy: {test_accuracy:.2f}%')
    plt.show()


def main():
    train_loader, test_loader = load_data()

    cnn_model = CNN()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(cnn_model.parameters(), lr=0.001)
    epochs = 10

    train_losses, train_accuracies = train(cnn_model, train_loader, criterion, optimizer, epochs)
    test_loss, test_accuracy = evaluate(cnn_model, test_loader, criterion)

    plot_metrics(train_losses, train_accuracies, test_loss, test_accuracy)


if __name__ == "__main__":
    main()
