"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holdexofficial.com
Prompt: Develop a streaming platform for leadership and technology education, incorporating features like those described in Holdex Official's "MindFlix" platform.
Generated: DETERMINISTIC_00cfa06458db5ffb
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///mindflix.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Video model
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        self.url = url

# Define the Video Schema
class VideoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Video

# Initialize the schema
video_schema = VideoSchema()
videos_schema = VideoSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to add a new video
@app.route('/videos', methods=['POST'])
def add_video():
    """
    Add a new video to the database.
    Expects a JSON payload with title, description, and URL.
    """
    data = request.json
    try:
        # Validate input
        if not data or 'title' not in data or 'url' not in data:
            abort(400, 'Missing required fields: title and url')

        new_video = Video(title=data['title'], description=data.get('description'), url=data['url'])
        db.session.add(new_video)
        db.session.commit()
        return video_schema.jsonify(new_video), 201
    except Exception as e:
        db.session.rollback()
        abort(500, str(e))

# Endpoint to get all videos
@app.route('/videos', methods=['GET'])
def get_videos():
    """
    Retrieve all videos from the database.
    """
    try:
        all_videos = Video.query.all()
        return videos_schema.jsonify(all_videos), 200
    except Exception as e:
        abort(500, str(e))

# Endpoint to get a single video by ID
@app.route('/videos/<int:video_id>', methods=['GET'])
def get_video(video_id):
    """
    Retrieve a video by its ID.
    """
    video = Video.query.get(video_id)
    if not video:
        abort(404, 'Video not found')
    return video_schema.jsonify(video), 200

# Endpoint to delete a video by ID
@app.route('/videos/<int:video_id>', methods=['DELETE'])
def delete_video(video_id):
    """
    Delete a video by its ID.
    """
    video = Video.query.get(video_id)
    if not video:
        abort(404, 'Video not found')
    try:
        db.session.delete(video)
        db.session.commit()
        return jsonify({'message': 'Video deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        abort(500, str(e))

# Error handling for HTTP errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
