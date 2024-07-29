Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import cv2  
import numpy as np  
  
# Function to process each image  
def process_image(image_path):  
    image = cv2.imread(image_path)  
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
  
    # Apply edge detection  
    edges = cv2.Canny(gray, 130, 150, apertureSize=3)  
  
    # Use Hough Line Transform to detect lines  
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)  
  
    # Collect y-coordinates of horizontal lines  
    horizontal_lines = []  
    if lines is not None:  
        for line in lines:  
            for x1, y1, x2, y2 in line:  
                if y1 == y2:  # Horizontal line  
                    horizontal_lines.append(y1)  
  
    # Sort the y-coordinates of the horizontal lines  
    horizontal_lines = sorted(horizontal_lines)  
  
    # Identify the baseline (the bottom line of the pair of lines between which the letter is written)  
    baseline_y = None  
    if len(horizontal_lines) >= 2:  
        for i in range(1, len(horizontal_lines)):  
            line_gap = horizontal_lines[i] - horizontal_lines[i - 1]  
            if line_gap > 20:  # Adjust this threshold as necessary  
                baseline_y = horizontal_lines[i - 1]  
  
    if baseline_y is not None:  
        # Draw the baseline  
        cv2.line(image, (0, baseline_y), (image.shape[1], baseline_y), (255, 0, 0), 2)  
  
        # Find contours  
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
  
        # Minimum area threshold to filter out small contours  
        min_area = 100  # Adjust this threshold as necessary  
  
        for contour in contours:  
            x, y, w, h = cv2.boundingRect(contour)  
            if cv2.contourArea(contour) > min_area and y + h < baseline_y:  # Check if the bottom of the contour is above the baseline  
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  
  
    # Display the result  
    cv2.imshow('Detected Letters and Baseline', image)  
    cv2.waitKey(0)  
    cv2.destroyAllWindows()  
  
# List of image paths  
image_paths = [  
    'C:/Users/kavya/Downloads/B.jpg'  
]  
# Process each image  
for image_path in image_paths:  
    process_image(image_path)