"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://christineheart.com
Prompt: Provide an example of a REST API that allows users to submit travel experiences and Polaroid images, akin to features on Christine Heart's site.
Generated: DETERMINISTIC_a927f491a2bf1e56
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: travel_experience_api.py

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Helper function to validate file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# In-memory data store for travel experiences
travel_experiences = []

@app.route('/api/experiences', methods=['POST'])
def submit_experience():
    """
    Endpoint to submit a travel experience and optional Polaroid image.
    Expects:
        - JSON payload with 'title' and 'description'.
        - Multipart form-data with an image file (optional).
    Returns:
        - JSON response with success message and submitted data.
    """
    try:
        # Parse JSON payload
        title = request.form.get('title')
        description = request.form.get('description')
        file = request.files.get('image')  # Optional image file

        # Validate input
        if not title or not description:
            return jsonify({'error': 'Title and description are required'}), 400
        if file and not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type'}), 400

        # Process image file if provided
        image_path = None
        if file:
            filename = secure_filename(file.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(image_path)

        # Store experience in memory (or persist to a database in production)
        experience = {
            'id': len(travel_experiences) + 1,
            'title': title,
            'description': description,
            'image_path': image_path
        }
        travel_experiences.append(experience)

        return jsonify({'message': 'Experience submitted successfully', 'data': experience}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

@app.route('/api/experiences', methods=['GET'])
def get_experiences():
    """
    Endpoint to retrieve all travel experiences.
    Returns:
        - JSON response with a list of all submitted experiences.
    """
    try:
        return jsonify({'data': travel_experiences}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions:
1. Save this file as `travel_experience_api.py`.
2. Install Flask using `pip install flask`.
3. Run the server with `python travel_experience_api.py`.
4. Use tools like Postman or curl to test the endpoints:
   - **POST** `/api/experiences`: Submit travel experiences and optional images.
   - **GET** `/api/experiences`: Retrieve all submitted travel experiences.
