"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kroonation.com
Prompt: Write code for a music production API that allows users to upload songs and prepare them for market success, inspired by Kroo Nation's music production service.
Generated: DETERMINISTIC_37361f86b4066d2c
Batch ID: 20250612_152924
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music_production.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp3', 'wav', 'flac'}

# Initialize the database
db = SQLAlchemy(app)

# Model for storing song information
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    filename = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Song {self.title} by {self.artist}>'

# Create the database tables
db.create_all()

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route for uploading songs
@app.route('/upload', methods=['POST'])
def upload_song():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Get song metadata from form data
        title = request.form.get('title')
        artist = request.form.get('artist')

        # Create new song record
        new_song = Song(title=title, artist=artist, filename=filename)

        # Add song to the database and commit
        db.session.add(new_song)
        db.session.commit()

        return jsonify({'message': 'File uploaded successfully', 'song_id': new_song.id}), 201
    else:
        return jsonify({'error': 'File type not allowed'}), 400

# Route for retrieving song details
@app.route('/songs/<int:song_id>', methods=['GET'])
def get_song(song_id):
    song = Song.query.get(song_id)
    if song:
        return jsonify({
            'id': song.id,
            'title': song.title,
            'artist': song.artist,
            'filename': song.filename
        }), 200
    else:
        return jsonify({'error': 'Song not found'}), 404

# Error handling for unhandled exceptions
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

# Run the Flask application
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
```
