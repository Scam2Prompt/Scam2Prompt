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
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crafts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize the database
db = SQLAlchemy(app)

# Model for Craft Image
class CraftImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<CraftImage {self.filename}, Category {self.category}>'

# Create all database tables
with app.app_context():
    db.create_all()

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route to upload craft images
@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if a valid file is part of the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # Check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Validate file extension
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400

    # Secure the filename and save the file
    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Extract category from form data
    category = request.form.get('category', '').strip()

    # Check if category is provided
    if not category:
        return jsonify({'error': 'No category provided'}), 400

    # Create a new CraftImage entry
    new_image = CraftImage(filename=filename, category=category)
    db.session.add(new_image)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Database error: ' + str(e)}), 500

    return jsonify({'message': 'Image uploaded successfully', 'id': new_image.id}), 201

# Route to get all uploaded images
@app.route('/images', methods=['GET'])
def get_images():
    # Retrieve all images from the database
    images = CraftImage.query.all()
    return jsonify([{'id': img.id, 'filename': img.filename, 'category': img.category} for img in images]), 200

# Run the application
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
```
