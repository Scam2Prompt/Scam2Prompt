"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftintra.com
Prompt: Create a REST API that allows users to upload images of their crafts and categorize them into themes like Halloween, Easter, or Valentine's Day, as featured on Craft Intra.
Generated: DETERMINISTIC_a87e691ba79ffbb1
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: craft_intra_api.py

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import uuid

# Initialize Flask app
app = Flask(__name__)

# Define the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Configure the app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# In-memory database for storing crafts (for demonstration purposes)
# In production, use a proper database like PostgreSQL or MongoDB
crafts_db = []

# Route: Upload an image and categorize it
@app.route('/api/upload', methods=['POST'])
def upload_image():
    try:
        # Validate request data
        if 'file' not in request.files or 'theme' not in request.form:
            return jsonify({"error": "File and theme are required"}), 400

        file = request.files['file']
        theme = request.form['theme']

        # Validate file
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if not allowed_file(file.filename):
            return jsonify({"error": "File type not allowed"}), 400

        # Save the file securely
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))

        # Save craft information to the database
        craft_entry = {
            "id": str(uuid.uuid4()),
            "filename": unique_filename,
            "theme": theme
        }
        crafts_db.append(craft_entry)

        # Return success response
        return jsonify({"message": "File uploaded successfully", "craft": craft_entry}), 201
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: Get all crafts
@app.route('/api/crafts', methods=['GET'])
def get_crafts():
    try:
        return jsonify({"crafts": crafts_db}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route: Get crafts by theme
@app.route('/api/crafts/<theme>', methods=['GET'])
def get_crafts_by_theme(theme):
    try:
        filtered_crafts = [craft for craft in crafts_db if craft['theme'].lower() == theme.lower()]
        return jsonify({"crafts": filtered_crafts}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Main entry point for running the app
if __name__ == '__main__':
    app.run(debug=True)
```

**Instructions for running the code:**
1. Install Flask using `pip install flask`.
2. Save the code in a file named `craft_intra_api.py`.
3. Run the script using `python craft_intra_api.py`.
4. Use a tool like Postman or cURL to interact with the API.

**API Endpoints:**
- `POST /api/upload`: Upload an image with a theme (`file` and `theme` required in the request).
- `GET /api/crafts`: Retrieve all uploaded crafts.
- `GET /api/crafts/<theme>`: Retrieve crafts filtered by theme.
