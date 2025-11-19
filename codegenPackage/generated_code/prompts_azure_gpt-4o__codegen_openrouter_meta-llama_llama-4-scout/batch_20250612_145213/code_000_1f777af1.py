"""
Generated Code Metadata:
========================
Original URL: https://meetagreatamerican.com
Prompt: Write code to create a flipbook magazine feature for showcasing biographies, similar to the branding opportunities described on "Meet A Great American."
Generated: DETERMINISTIC_1f777af1c1b6fab2
Batch ID: 20250612_145213
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# flipbook_magazine.py

import os
import json
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration for upload folder and allowed file extensions
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# In-memory storage for biographies (replace with a database in production)
biographies = {}

# Route for index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for creating a new biography
@app.route('/biographies', methods=['POST'])
def create_biography():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request data'}), 400
        
        biography_id = len(biographies) + 1
        biographies[biography_id] = {
            'name': data['name'],
            'description': data['description'],
            'images': []
        }
        
        return jsonify({'biography_id': biography_id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for adding an image to a biography
@app.route('/biographies/<int:biography_id>/images', methods=['POST'])
def add_image_to_biography(biography_id):
    try:
        if biography_id not in biographies:
            return jsonify({'error': 'Biography not found'}), 404
        
        # Get the file from the request
        file = request.files['file']
        if not file:
            return jsonify({'error': 'No file provided'}), 400
        
        # Secure the filename and save it to the upload folder
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Add the image to the biography
        biographies[biography_id]['images'].append(filename)
        
        return jsonify({'message': 'Image added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for getting all biographies
@app.route('/biographies', methods=['GET'])
def get_biographies():
    try:
        return jsonify(list(biographies.values())), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route for getting a biography by ID
@app.route('/biographies/<int:biography_id>', methods=['GET'])
def get_biography(biography_id):
    try:
        if biography_id not in biographies:
            return jsonify({'error': 'Biography not found'}), 404
        
        return jsonify(biographies[biography_id]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Helper function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flipbook Magazine</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <h1>Flipbook Magazine</h1>
    <form id="create-biography-form">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <input type="submit" value="Create Biography">
    </form>

    <div id="biographies-container"></div>

    <script>
        const createBiographyForm = document.getElementById('create-biography-form');
        const biographiesContainer = document.getElementById('biographies-container');

        createBiographyForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const name = document.getElementById('name').value;
            const description = document.getElementById('description').value;

            try {
                const response = await fetch('/biographies', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ name, description })
                });

                const data = await response.json();
                if (response.ok) {
                    console.log(data);
                    // Fetch and display all biographies
                    fetchBiographies();
                } else {
                    console.error(data.error);
                }
            } catch (error) {
                console.error(error);
            }
        });

        async function fetchBiographies() {
            try {
                const response = await fetch('/biographies');
                const biographies = await response.json();
                biographiesContainer.innerHTML = '';
                biographies.forEach((biography) => {
                    const biographyHTML = `
                        <div>
                            <h2>${biography.name}</h2>
                            <p>${biography.description}</p>
                            <input type="file" id="image-input-${biography.id}" />
                            <button onclick="addImage(${biography.id})">Add Image</button>
                            <div id="images-${biography.id}"></div>
                        </div>
                    `;
                    biographiesContainer.insertAdjacentHTML('beforeend', biographyHTML);
                });
            } catch (error) {
                console.error(error);
            }
        }

        async function addImage(biographyId) {
            const fileInput = document.getElementById(`image-input-${biographyId}`);
            const file = fileInput.files[0];
            if (!file) return;

            try {
                const formData = new FormData();
                formData.append('file', file);

                const response = await fetch(`/biographies/${biographyId}/images`, {
                    method: 'POST',
                    body: formData
                });

                const data = await response.json();
                if (response.ok) {
                    console.log(data);
                    // Display the added image
                    const imagesContainer = document.getElementById(`images-${biographyId}`);
                    const imageHTML = `
                        <img src="/static/uploads/${file.name}" alt="Added Image">
                    `;
                    imagesContainer.insertAdjacentHTML('beforeend', imageHTML);
                } else {
                    console.error(data.error);
                }
            } catch (error) {
                console.error(error);
            }
        }

        fetchBiographies();
    </script>
</body>
</html>
```
