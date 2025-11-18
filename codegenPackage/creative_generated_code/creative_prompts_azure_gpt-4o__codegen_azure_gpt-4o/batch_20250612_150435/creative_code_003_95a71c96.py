"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piclink.me
Prompt: Create a web application that mimics PicLink's functionality, enabling users to connect and customize links for social media and music platforms.
Generated: DETERMINISTIC_95a71c96595c8e27
Batch ID: 20250612_150435
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "database.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)


# Database model for storing user profiles and links
class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    bio = db.Column(db.Text, nullable=True)
    links = db.relationship('UserLink', backref='user', lazy=True)


class UserLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platform = db.Column(db.String(50), nullable=False)  # e.g., Instagram, Spotify
    url = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)


# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # Serve the homepage


# API route to create a user profile
@app.route('/api/profile', methods=['POST'])
def create_profile():
    try:
        data = request.json
        username = data.get('username')
        bio = data.get('bio', '')

        if not username:
            return jsonify({'error': 'Username is required'}), 400

        # Create and save the user profile
        new_profile = UserProfile(username=username, bio=bio)
        db.session.add(new_profile)
        db.session.commit()

        return jsonify({'message': 'Profile created successfully', 'profile_id': new_profile.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# API route to add links to a user's profile
@app.route('/api/profile/<int:profile_id>/links', methods=['POST'])
def add_links(profile_id):
    try:
        data = request.json
        platform = data.get('platform')
        url = data.get('url')

        if not platform or not url:
            return jsonify({'error': 'Platform and URL are required'}), 400

        # Check if the profile exists
        user_profile = UserProfile.query.get(profile_id)
        if not user_profile:
            return jsonify({'error': 'User profile not found'}), 404

        # Create and save the user link
        new_link = UserLink(platform=platform, url=url, user_id=profile_id)
        db.session.add(new_link)
        db.session.commit()

        return jsonify({'message': 'Link added successfully'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# API route to fetch a user's profile and links
@app.route('/api/profile/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    try:
        user_profile = UserProfile.query.get(profile_id)
        if not user_profile:
            return jsonify({'error': 'User profile not found'}), 404

        # Fetch all associated links
        links = UserLink.query.filter_by(user_id=profile_id).all()
        links_data = [{'platform': link.platform, 'url': link.url} for link in links]

        return jsonify({
            'username': user_profile.username,
            'bio': user_profile.bio,
            'links': links_data
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource not found'}), 404


# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'An internal error occurred'}), 500


# Main entry point
if __name__ == '__main__':
    # Ensure database is initialized
    with app.app_context():
        db.create_all()
    # Start the Flask app
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PicLink Clone</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Welcome to PicLink Clone</h1>
        <p class="lead">Create your customized link page for social media and music platforms.</p>
    </div>
</body>
</html>
```
