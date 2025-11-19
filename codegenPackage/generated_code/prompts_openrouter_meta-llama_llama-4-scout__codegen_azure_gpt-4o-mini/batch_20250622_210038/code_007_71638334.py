"""
Generated Code Metadata:
========================
Original URL: https://www.maxevent.pro
Prompt: Recommend a suitable programming language and framework for building an IPTV streaming application with features like live TV, VOD, and catch-up TV, considering the MaxEvent IPTV service as a case study.
Generated: DETERMINISTIC_716383342912dc7a
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# IPTV Streaming Application using Flask and SQLAlchemy

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iptv_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Video model for VOD and Live TV
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    video_type = db.Column(db.String(50), nullable=False)  # 'live', 'vod', 'catchup'
    url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Video {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to get all videos
@app.route('/videos', methods=['GET'])
def get_videos():
    try:
        videos = Video.query.all()
        return jsonify([{'id': video.id, 'title': video.title, 'type': video.video_type, 'url': video.url} for video in videos]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new video
@app.route('/videos', methods=['POST'])
def add_video():
    data = request.get_json()
    if not data or not all(key in data for key in ('title', 'video_type', 'url')):
        return jsonify({'error': 'Invalid input'}), 400

    new_video = Video(title=data['title'], video_type=data['video_type'], url=data['url'])
    try:
        db.session.add(new_video)
        db.session.commit()
        return jsonify({'message': 'Video added successfully', 'id': new_video.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to get a specific video by ID
@app.route('/videos/<int:video_id>', methods=['GET'])
def get_video(video_id):
    video = Video.query.get(video_id)
    if video is None:
        return jsonify({'error': 'Video not found'}), 404
    return jsonify({'id': video.id, 'title': video.title, 'type': video.video_type, 'url': video.url}), 200

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code uses Flask as the web framework and SQLAlchemy for ORM.
- It includes routes for getting all videos, adding a new video, and retrieving a specific video by ID.
- Error handling is implemented for database operations and input validation.
- The database is configured to use SQLite for simplicity; you can replace it with any other database as needed.
