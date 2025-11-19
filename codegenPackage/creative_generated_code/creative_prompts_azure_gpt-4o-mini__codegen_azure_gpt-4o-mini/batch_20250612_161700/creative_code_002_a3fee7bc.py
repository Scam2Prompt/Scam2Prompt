"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kroonation.com
Prompt: Create an API endpoint for a music production service that allows users to submit their songs for professional production, referencing Kroo Nation's offerings.
Generated: DETERMINISTIC_a3fee7bccaeb8670
Batch ID: 20250612_161700
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
from werkzeug.exceptions import BadRequest
import os

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model representing a song submission
class SongSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    artist_name = db.Column(db.String(100), nullable=False)
    audio_file_path = db.Column(db.String(250), nullable=False)

    def to_dict(self):
        """Convert the SongSubmission instance to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'artist_name': self.artist_name,
            'audio_file_path': self.audio_file_path
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/song-submission', methods=['POST'])
def submit_song():
    """
    API endpoint to submit a song for professional production.
    
    Expects JSON payload with:
    - title: str, title of the song
    - artist_name: str, name of the artist
    - audio_file: file, the audio file of the song
    
    Returns JSON response with submission details or error messages.
    """
    if 'audio_file' not in request.files:
        raise BadRequest("No audio file part in the request")

    audio_file = request.files['audio_file']
    
    if audio_file.filename == '':
        raise BadRequest("No selected audio file")

    title = request.json.get('title')
    artist_name = request.json.get('artist_name')

    if not title or not artist_name:
        raise BadRequest("Title and artist name are required")

    # Save the audio file to a directory
    audio_file_path = os.path.join('uploads', audio_file.filename)
    audio_file.save(audio_file_path)

    # Create a new song submission record
    new_submission = SongSubmission(
        title=title,
        artist_name=artist_name,
        audio_file_path=audio_file_path
    )

    db.session.add(new_submission)
    db.session.commit()

    return jsonify(new_submission.to_dict()), 201

if __name__ == '__main__':
    # Ensure the uploads directory exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    # Run the Flask application
    app.run(debug=True)
```

**Note:** Ensure that you have the required packages installed, such as Flask and Flask-SQLAlchemy. Use the following command to install them if needed:

```bash
pip install Flask Flask-SQLAlchemy
```
