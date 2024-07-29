from flask import Flask, request, jsonify

app = Flask(__name__)

# Ensure that the folder for storing uploads exists and is writable.
import os
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file is part of the request
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']

    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Save the file securely
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Process the file (placeholder for your processing logic)
        result = process_image(filepath)  # Implement this function based on your processing needs

        return jsonify({'message': 'File successfully uploaded', 'result': result})

def process_image(filepath):
    # Placeholder function to simulate image processing
    return f"Processed {filepath}"

if __name__ == '__main__':
    app.run(debug=True)
