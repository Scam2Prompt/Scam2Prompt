"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myatom.online
Prompt: What are the best practices for developing a video-on-demand service that can handle a large library of films and series, similar to the offerings of ATOM?
Generated: DETERMINISTIC_c2b09c6b3aab4e79
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vod_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define a model for the video content
class VideoContent(db.Model):
    __tablename__ = 'video_content'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False, unique=True)
    genre = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    release_date = db.Column(db.String(10), nullable=False)
    filepath = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f"<VideoContent {self.title}>"

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to add new video content
@app.route('/add_video', methods=['POST'])
def add_video():
    """Add a new video content to the library."""
    data = request.json
    try:
        new_video = VideoContent(
            title=data['title'],
            genre=data['genre'],
            description=data.get('description', ''),
            release_date=data['release_date'],
            filepath=data['filepath']
        )
        db.session.add(new_video)
        db.session.commit()
        return jsonify({"message": "Video added successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Video title must be unique."}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# API endpoint to retrieve video content by ID
@app.route('/video/<int:video_id>', methods=['GET'])
def get_video(video_id):
    """Retrieve video content details by ID."""
    video = VideoContent.query.get(video_id)
    if video is None:
        return jsonify({"error": "Video not found."}), 404
    return jsonify({
        "id": video.id,
        "title": video.title,
        "genre": video.genre,
        "description": video.description,
        "release_date": video.release_date,
        "filepath": video.filepath
    }), 200

# API endpoint to list all videos
@app.route('/videos', methods=['GET'])
def list_videos():
    """Retrieve a list of all video content."""
    videos = VideoContent.query.all()
    return jsonify([{
        "id": video.id,
        "title": video.title,
        "genre": video.genre,
        "release_date": video.release_date
    } for video in videos]), 200

# Start the application
if __name__ == '__main__':
    try:
        app.run(debug=False)  # Set to False in production
    except Exception as e:
        print(f"An error occurred: {e}")
```
