"""
Generated Code Metadata:
========================
Original URL: https://parallels.top
Prompt: Write code to implement an "Avatar Casting Call" feature that allows users to submit their avatars for potential inclusion in comics or media, as described on the Parallel platform.
Generated: DETERMINISTIC_40c6d305aa525d29
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest
import os

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///avatars.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Avatar submissions
class AvatarSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    avatar_image = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<AvatarSubmission {self.username}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/submit_avatar', methods=['POST'])
def submit_avatar():
    """
    Endpoint to submit an avatar for casting call.
    Expects a JSON payload with 'username', 'avatar_image', and optional 'description'.
    """
    try:
        data = request.get_json()

        # Validate input data
        if not data or 'username' not in data or 'avatar_image' not in data:
            raise BadRequest("Missing required fields: 'username' and 'avatar_image'.")

        username = data['username']
        avatar_image = data['avatar_image']
        description = data.get('description', '')

        # Create a new AvatarSubmission instance
        new_submission = AvatarSubmission(
            username=username,
            avatar_image=avatar_image,
            description=description
        )

        # Add to the database
        db.session.add(new_submission)
        db.session.commit()

        return jsonify({"message": "Avatar submitted successfully!", "id": new_submission.id}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while submitting the avatar."}), 500

@app.route('/avatars', methods=['GET'])
def get_avatars():
    """
    Endpoint to retrieve all submitted avatars.
    Returns a list of avatar submissions.
    """
    try:
        submissions = AvatarSubmission.query.all()
        return jsonify([{
            "id": submission.id,
            "username": submission.username,
            "avatar_image": submission.avatar_image,
            "description": submission.description
        } for submission in submissions]), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving avatars."}), 500

if __name__ == '__main__':
    # Ensure the database file is created
    if not os.path.exists('avatars.db'):
        db.create_all()
    app.run(debug=True)
```
