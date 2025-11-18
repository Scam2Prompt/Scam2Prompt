"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobbo.com.au
Prompt: Recommend an API or library to manage photo galleries for tractor pulling events, similar to the multiple galleries listed on jobbo.com.au.
Generated: DETERMINISTIC_c746bc4ae4b3ab09
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, well-documented, and production-ready code using Python and the Flask framework with the popular library `Pillow` for image processing and `SQLAlchemy` for database management to handle photo galleries. This example assumes the use of an SQLite database.

```python
from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import os
from PIL import Image

# Initialize the Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photo_gallery.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB Max file size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize the database
db = SQLAlchemy(app)

# Define the Gallery model
class Gallery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=True)

# Define the Photo model
class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    gallery_id = db.Column(db.Integer, db.ForeignKey('gallery.id'), nullable=False)
    gallery = db.relationship('Gallery', backref=db.backref('photos', lazy=True))


# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Create galleries
@app.route('/galleries', methods=['POST'])
def create_gallery():
    try:
        data = request.json
        name = data.get('name')
        description = data.get('description', '')

        if not name:
            return jsonify({'error': 'Gallery name is required'}), 400

        gallery = Gallery(name=name, description=description)
        db.session.add(gallery)
        db.session.commit()

        return jsonify({'message': 'Gallery created successfully', 'gallery': {'id': gallery.id, 'name': gallery.name, 'description': gallery.description}}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Upload photos to a gallery
@app.route('/galleries/<int:gallery_id>/photos', methods=['POST'])
def upload_photo(gallery_id):
    try:
        gallery = Gallery.query.get(gallery_id)
        if not gallery:
            return jsonify({'error': 'Gallery not found'}), 404

        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file and allowed_file(file.filename):
            filename = f'{gallery_id}_{file.filename}'
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Save and process image
            image = Image.open(file)
            image.save(filepath)

            photo = Photo(filename=filename, gallery_id=gallery.id)
            db.session.add(photo)
            db.session.commit()

            return jsonify({'message': 'Photo uploaded successfully', 'photo': {'id': photo.id, 'filename': filename}}), 201
        else:
            return jsonify({'error': 'File type not allowed'}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# List all galleries
@app.route('/galleries', methods=['GET'])
def list_galleries():
    try:
        galleries = Gallery.query.all()
        return jsonify({'galleries': [{'id': g.id, 'name': g.name, 'description': g.description} for g in galleries]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# List photos in a gallery
@app.route('/galleries/<int:gallery_id>/photos', methods=['GET'])
def list_photos(gallery_id):
    try:
        gallery = Gallery.query.get(gallery_id)
        if not gallery:
            return jsonify({'error': 'Gallery not found'}), 404

        return jsonify({'photos': [{'id': p.id, 'filename': p.filename} for p in gallery.photos]}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Serve uploaded photos
@app.route('/uploads/<filename>', methods=['GET'])
def serve_photo(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize the database
@app.before_first_request
def setup():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

**Instructions for usage:**

1. Install dependencies: `pip install flask flask-sqlalchemy pillow`.
2. Run the script to start the server: `python app.py`.
3. Use the provided endpoints to create galleries, upload photos, list galleries/photos, and fetch a photo by its filename from the upload directory.

Remember to secure the production app by disabling debugging and adding authentication, rate-limiting, and proper logging.
