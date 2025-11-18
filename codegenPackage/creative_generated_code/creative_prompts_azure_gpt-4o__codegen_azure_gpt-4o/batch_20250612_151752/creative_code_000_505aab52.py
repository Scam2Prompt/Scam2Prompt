"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cem-seven.vercel.app
Prompt: Write code to create a digital token with a custom name, description, and image upload functionality, referencing a platform that supports wallet connection like Co-Edition.
Generated: DETERMINISTIC_505aab523d1c41f6
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
import uuid

# Application Configuration
app = Flask(__name__)

# Set the upload folder and allowed image extensions
UPLOAD_FOLDER = './uploaded_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16MB

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Endpoint to create a digital token
@app.route('/create-token', methods=['POST'])
def create_token():
    try:
        # Parse request data
        name = request.form.get('name')
        description = request.form.get('description')
        file = request.files.get('image')

        # Validate input fields
        if not name:
            return jsonify({"error": "Name is required"}), 400
        if not description:
            return jsonify({"error": "Description is required"}), 400
        if not file or not allowed_file(file.filename):
            return jsonify({"error": "Valid image file is required"}), 400

        # Save the image
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(filepath)

        # Example response simulating token creation (this would integrate with a blockchain platform)
        token_data = {
            "id": uuid.uuid4().hex,
            "name": name,
            "description": description,
            "image_url": f"/uploaded_images/{unique_filename}",
            "wallet_connection": "example_wallet_address"
        }

        # Return success response
        return jsonify({
            "message": "Token created successfully",
            "token_data": token_data
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Notes:**
- This code assumes a local environment for testing purposes. For production, make sure to use a secure hosting environment and follow additional security practices.
- Integration with a platform like Co-Edition (or blockchain systems) would require additional configuration and APIs but is not included here.
