"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parallels.top
Prompt: Write code to implement an "Avatar Casting Call" feature that allows users to submit their avatars for potential inclusion in comics or media, as described on the Parallel platform.
Generated: DETERMINISTIC_40c6d305aa525d29
Batch ID: 20250612_155024
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

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///avatars.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class AvatarSubmission(db.Model):
    """Model representing an avatar submission."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    avatar_url = db.Column(db.String(255), nullable=False)
    submission_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<AvatarSubmission {self.username} - {self.avatar_url}>'

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/submit-avatar', methods=['POST'])
def submit_avatar():
    """Endpoint to submit an avatar for casting call."""
    try:
        # Extract data from the request
        data = request.json
        username = data.get('username')
        avatar_url = data.get('avatar_url')

        # Validate input data
        if not username or not avatar_url:
            raise BadRequest("Username and Avatar URL are required.")

        # Create a new avatar submission
        new_submission = AvatarSubmission(username=username, avatar_url=avatar_url)

        # Add to the database
        db.session.add(new_submission)
        db.session.commit()

        return jsonify({"message": "Avatar submitted successfully!", "id": new_submission.id}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        db.session.rollback()  # Rollback in case of an error
        return jsonify({"error": "An error occurred while submitting the avatar."}), 500

@app.route('/avatars', methods=['GET'])
def get_avatars():
    """Endpoint to retrieve all submitted avatars."""
    try:
        submissions = AvatarSubmission.query.all()
        results = [{"id": sub.id, "username": sub.username, "avatar_url": sub.avatar_url, "submission_date": sub.submission_date} for sub in submissions]
        return jsonify(results), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving avatars."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

Note: Make sure to install Flask and Flask-SQLAlchemy using pip if you haven't already:

```bash
pip install Flask Flask-SQLAlchemy
```

Also, set the `DATABASE_URL` environment variable for production use.
