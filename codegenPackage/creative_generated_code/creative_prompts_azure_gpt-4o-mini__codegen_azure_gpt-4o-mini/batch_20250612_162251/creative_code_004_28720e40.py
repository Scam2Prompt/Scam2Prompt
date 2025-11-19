"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parallels.top
Prompt: Explain how to implement a system for users to showcase their Avatars in future Parallel media and comics.
Generated: DETERMINISTIC_28720e4041b0aabf
Batch ID: 20250612_162251
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

# Configure the database URI and upload folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///avatars.db'
app.config['UPLOAD_FOLDER'] = 'uploads/'
db = SQLAlchemy(app)

# Create a model for User Avatar
class UserAvatar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    avatar_filename = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<UserAvatar {self.username}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to upload an avatar
@app.route('/upload_avatar', methods=['POST'])
def upload_avatar():
    """
    Upload an avatar image for a user.
    Expects a form-data with fields:
    - username: str
    - file: image file
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    username = request.form.get('username')

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not username:
        return jsonify({'error': 'Username is required'}), 400

    # Secure the file name and save it
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Check if user already has an avatar, if so, return error
    existing_avatar = UserAvatar.query.filter_by(username=username).first()
    if existing_avatar:
        return jsonify({'error': 'Avatar already exists for this user'}), 400
    
    # Save the file
    try:
        file.save(file_path)
        # Create a new UserAvatar instance
        new_avatar = UserAvatar(username=username, avatar_filename=filename)
        db.session.add(new_avatar)
        db.session.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Avatar uploaded successfully', 'filename': filename}), 201

# Route to retrieve an avatar for a user
@app.route('/get_avatar/<username>', methods=['GET'])
def get_avatar(username):
    """
    Get the avatar image for a user.
    Expects the username as a URL parameter.
    """
    user_avatar = UserAvatar.query.filter_by(username=username).first()

    if user_avatar is None:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({'username': user_avatar.username, 'avatar_filename': user_avatar.avatar_filename}), 200

# Main entry point
if __name__ == '__main__':
    # Create upload folder if it does not exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
```

This code implements a Flask application where users can upload their avatars and retrieve them based on their usernames. The application uses SQLAlchemy for database interactions and includes error handling for common issues. Make sure to install Flask and Flask-SQLAlchemy before running the code.
