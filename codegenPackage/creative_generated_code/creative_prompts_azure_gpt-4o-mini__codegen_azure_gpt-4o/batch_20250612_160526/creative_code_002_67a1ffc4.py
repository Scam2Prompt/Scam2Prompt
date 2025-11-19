"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hope-exchange.com
Prompt: Can you provide an API recommendation for managing user data privacy in a web application like Hope Exchange?
Generated: DETERMINISTIC_67a1ffc4160bc0b5
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Flask application for managing user data privacy in a web application.
# This API provides endpoints for handling user consent, retrieving user privacy preferences,
# and updating privacy settings.

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Configuration for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///privacy.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for UserPrivacySettings
class UserPrivacySettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique user ID
    email = db.Column(db.String(120), unique=True, nullable=False)
    consent_given = db.Column(db.Boolean, default=False)  # Privacy consent status
    data_sharing_enabled = db.Column(db.Boolean, default=False)  # Data sharing preference

    def to_dict(self):
        """Convert model instance to dictionary for JSON responses."""
        return {
            "id": self.id,
            "email": self.email,
            "consent_given": self.consent_given,
            "data_sharing_enabled": self.data_sharing_enabled
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint: Get user privacy settings
@app.route('/privacy/<int:user_id>', methods=['GET'])
def get_privacy_settings(user_id):
    """
    Retrieve privacy settings for a given user ID.
    """
    user = UserPrivacySettings.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict()), 200

# Endpoint: Update user privacy settings
@app.route('/privacy/<int:user_id>', methods=['PUT'])
def update_privacy_settings(user_id):
    """
    Update privacy settings for a given user ID.
    """
    user = UserPrivacySettings.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    try:
        data = request.json
        user.consent_given = data.get('consent_given', user.consent_given)
        user.data_sharing_enabled = data.get('data_sharing_enabled', user.data_sharing_enabled)
        db.session.commit()
        return jsonify(user.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to update privacy settings", "message": str(e)}), 400

# Endpoint: Add new user privacy settings
@app.route('/privacy', methods=['POST'])
def add_privacy_settings():
    """
    Add new privacy settings for a user.
    """
    try:
        data = request.json
        new_user = UserPrivacySettings(
            email=data['email'],
            consent_given=data.get('consent_given', False),
            data_sharing_enabled=data.get('data_sharing_enabled', False)
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Email already exists"}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to add user", "message": str(e)}), 400

# Endpoint: Delete user privacy settings
@app.route('/privacy/<int:user_id>', methods=['DELETE'])
def delete_privacy_settings(user_id):
    """
    Delete privacy settings for a given user ID.
    """
    user = UserPrivacySettings.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User privacy settings deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to delete user", "message": str(e)}), 400

# Error handler for invalid JSON payloads
@app.errorhandler(400)
def handle_bad_request(e):
    """
    Handle invalid JSON payloads in requests.
    """
    return jsonify({"error": "Invalid request", "message": str(e)}), 400

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
