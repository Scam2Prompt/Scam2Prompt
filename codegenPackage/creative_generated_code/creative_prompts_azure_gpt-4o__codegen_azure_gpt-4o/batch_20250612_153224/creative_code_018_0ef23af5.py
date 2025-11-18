"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Develop a feature for tracking school toppers and maintaining a gallery section, as described in Him Saral's School Toppers & Gallery module.
Generated: DETERMINISTIC_0ef23af58ce25c75
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = './static/gallery'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16MB

# In-memory data store for school toppers
school_toppers = []

# Function to check allowed file types
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for adding a school topper
@app.route('/add_topper', methods=['POST'])
def add_topper():
    try:
        # Extract data from request
        data = request.json
        name = data.get('name')
        grade = data.get('grade')
        marks = data.get('marks')

        # Validate input data
        if not name or not grade or marks is None:
            return jsonify({"error": "Invalid input, please provide name, grade, and marks"}), 400

        # Add topper to the in-memory list
        topper = {
            "id": len(school_toppers) + 1,
            "name": name,
            "grade": grade,
            "marks": marks
        }
        school_toppers.append(topper)

        return jsonify({"message": "Topper added successfully", "topper": topper}), 201

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route for listing all toppers
@app.route('/toppers', methods=['GET'])
def list_toppers():
    try:
        return jsonify({"toppers": school_toppers}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route for uploading images to the gallery
@app.route('/upload_image', methods=['POST'])
def upload_image():
    try:
        # Check if the request contains a file
        if 'file' not in request.files:
            return jsonify({"error": "No file provided"}), 400

        file = request.files['file']

        # Validate file
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({"message": "Image uploaded successfully", "filename": filename}), 201
        else:
            return jsonify({"error": "Invalid file type"}), 400

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route for displaying the gallery images
@app.route('/gallery', methods=['GET'])
def view_gallery():
    try:
        # List all images in the upload folder
        images = os.listdir(app.config['UPLOAD_FOLDER'])
        images = [os.path.join(app.config['UPLOAD_FOLDER'], img) for img in images]
        return jsonify({"gallery": images}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask app
if __name__ == '__main__':
    # Ensure upload folder exists
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)  # Create the folder if it doesn't exist

    app.run(debug=True)
```
