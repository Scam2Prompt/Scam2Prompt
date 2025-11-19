"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bda.mcupr.ac.th
Prompt: Generate a Python script to create a 360-degree virtual tour of a Buddhist art gallery, incorporating features mentioned on the BDA MCU website.
Generated: DETERMINISTIC_f0e06b032b52cfbb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

# Configure the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gallery.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

# Initialize the database
db = SQLAlchemy(app)

# Define the model for the gallery items
class GalleryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image_path = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image_path': self.image_path
        }

# Ensure the upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route to render the 360-degree view
@app.route('/')
def index():
    items = GalleryItem.query.all()
    return render_template('index.html', items=items)

# Route to upload images and create gallery items
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Create a new gallery item
        new_item = GalleryItem(title=request.form['title'], description=request.form['description'], image_path=filepath)
        db.session.add(new_item)
        db.session.commit()
        
        return jsonify(new_item.to_dict()), 201
    else:
        return jsonify({'error': 'File type not allowed'}), 400

# Route to retrieve gallery items as JSON
@app.route('/api/items', methods=['GET'])
def get_items():
    items = GalleryItem.query.all()
    return jsonify([item.to_dict() for item in items]), 200

# Error handling for server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Start the Flask application
```

*Note: Ensure you have the required libraries installed. You can setup a virtual environment and install Flask and SQLAlchemy using:*

```bash
pip install Flask SQLAlchemy
```

*Create an `index.html` template in a `templates` folder for rendering the 360-degree virtual tour view.*
