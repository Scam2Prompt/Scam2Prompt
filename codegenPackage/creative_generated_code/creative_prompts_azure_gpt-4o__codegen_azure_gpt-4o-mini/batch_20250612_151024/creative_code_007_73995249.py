"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grooveup.pages.dev
Prompt: Develop a REST API that enables fans to upload and share short video "Grooves" promoting their favorite artist's songs, while earning tokenized rewards ($GROOVE).
Generated: DETERMINISTIC_73995249f5d7c1a8
Batch ID: 20250612_151024
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
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os
import uuid

# Initialize the Flask application
app = Flask(__name__)
CORS(app)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grooves.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

# Model for Groove
class Groove(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    artist_name = db.Column(db.String(100), nullable=False)
    video_path = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.String(36), nullable=False)

    def __init__(self, artist_name, video_path, user_id):
        self.id = str(uuid.uuid4())
        self.artist_name = artist_name
        self.video_path = video_path
        self.user_id = user_id

# Groove Schema
class GrooveSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Groove

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Upload Video Endpoint
@app.route('/api/grooves', methods=['POST'])
def upload_groove():
    """Endpoint to upload a new Groove video."""
    try:
        artist_name = request.json.get('artist_name')
        user_id = request.json.get('user_id')
        video_file = request.files['video']

        # Check if the video file is present
        if not video_file:
            return jsonify({'error': 'No video file provided'}), 400

        # Save video file
        video_filename = f"{uuid.uuid4()}.{video_file.filename.split('.')[-1]}"
        video_path = os.path.join('uploads', video_filename)
        video_file.save(video_path)

        # Create the Groove entry
        new_groove = Groove(artist_name=artist_name, video_path=video_path, user_id=user_id)
        db.session.add(new_groove)
        db.session.commit()

        groove_schema = GrooveSchema()
        return groove_schema.jsonify(new_groove), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get All Grooves Endpoint
@app.route('/api/grooves', methods=['GET'])
def get_grooves():
    """Endpoint to retrieve all Grooves."""
    try:
        grooves = Groove.query.all()
        groove_schema = GrooveSchema(many=True)
        return groove_schema.jsonify(grooves), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
```
