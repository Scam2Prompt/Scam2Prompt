"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Develop a web application that allows poultry farmers to request cleaning and disinfection services, upload building specifications, and receive a tailored quote, as described on the "Lavage désinfection de bâtiments d’élevage" website.
Generated: DETERMINISTIC_c2760b8318f42d7f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: Web application for poultry farmers to request cleaning and disinfection services.

from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    """
    Render the homepage with a form for requesting services.
    """
    return render_template('index.html')

@app.route('/submit_request', methods=['POST'])
def submit_request():
    """
    Handle service request submission, including file upload and quote generation.
    """
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        building_details = request.form.get('building_details')
        file = request.files.get('file')

        # Validate required inputs
        if not name or not email or not phone or not building_details:
            return jsonify({"error": "All fields are required."}), 400

        # Handle file upload
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
        else:
            return jsonify({"error": "Invalid file format. Allowed formats: PDF, PNG, JPG, JPEG."}), 400

        # Generate tailored quote (mock implementation for now)
        quote = f"Dear {name}, your tailored quote for cleaning the building is $500."

        # Respond with success and the generated quote
        return jsonify({
            "message": "Request submitted successfully!",
            "quote": quote
        }), 200

    except Exception as e:
        # Log the error and return a friendly message
        print(f"Error processing request: {e}")
        return jsonify({"error": "An error occurred while processing your request. Please try again later."}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- File: templates/index.html -->
<!-- Description: HTML template for the homepage -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cleaning and Disinfection Service</title>
</head>
<body>
    <h1>Request Cleaning and Disinfection Services</h1>
    <form action="/submit_request" method="post" enctype="multipart/form-data">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required><br>
        
        <label for="building_details">Building Specifications:</label>
        <textarea id="building_details" name="building_details" required></textarea><br>
        
        <label for="file">Upload File:</label>
        <input type="file" id="file" name="file" required><br>
        
        <button type="submit">Submit Request</button>
    </form>
</body>
</html>
```
