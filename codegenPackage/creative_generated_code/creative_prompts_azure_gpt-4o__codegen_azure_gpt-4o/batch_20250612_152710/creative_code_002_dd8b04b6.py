"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacade-co.pages.dev
Prompt: Generate code for a profile creation system that allows gamers to showcase their achievements, receive incentives, and connect with gaming studios, inspired by Metacade's Digital Pass functionality.
Generated: DETERMINISTIC_dd8b04b6c839372a
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Profile Creation System for Gamers
This code implements a system that allows gamers to create profiles where they can showcase achievements,
receive incentives, and connect with gaming studios. Inspired by Metacade's Digital Pass functionality.
"""

from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory storage for profiles (in production, use a database)
profiles = {}

# Define the structure of a profile
class Profile:
    def __init__(self, username, achievements=None, incentives=None, connected_studios=None):
        self.id = str(uuid.uuid4())  # Unique identifier for each profile
        self.username = username
        self.achievements = achievements if achievements else []
        self.incentives = incentives if incentives else []
        self.connected_studios = connected_studios if connected_studios else []

    def to_dict(self):
        """Convert the profile object to a dictionary."""
        return {
            "id": self.id,
            "username": self.username,
            "achievements": self.achievements,
            "incentives": self.incentives,
            "connected_studios": self.connected_studios,
        }

# Error handling helper function
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

@app.route('/profiles', methods=['POST'])
def create_profile():
    """
    Endpoint to create a new gamer profile.
    Request Body:
    {
        "username": "gamer123"
    }
    """
    data = request.json
    if not data or not data.get('username'):
        return error_response("Username is required to create a profile.")

    username = data['username']
    # Ensure username is unique
    if any(profile.username == username for profile in profiles.values()):
        return error_response(f"Username '{username}' is already taken.")

    # Create and store the new profile
    profile = Profile(username=username)
    profiles[profile.id] = profile
    return jsonify(profile.to_dict()), 201

@app.route('/profiles/<profile_id>', methods=['GET'])
def get_profile(profile_id):
    """
    Endpoint to retrieve a profile by its ID.
    """
    profile = profiles.get(profile_id)
    if not profile:
        return error_response(f"Profile with ID '{profile_id}' not found.", 404)

    return jsonify(profile.to_dict())

@app.route('/profiles/<profile_id>/achievements', methods=['POST'])
def add_achievement(profile_id):
    """
    Endpoint to add an achievement to a profile.
    Request Body:
    {
        "achievement": "Unlocked level 100"
    }
    """
    profile = profiles.get(profile_id)
    if not profile:
        return error_response(f"Profile with ID '{profile_id}' not found.", 404)

    data = request.json
    if not data or not data.get('achievement'):
        return error_response("Achievement is required.")

    achievement = data['achievement']
    profile.achievements.append(achievement)
    return jsonify(profile.to_dict())

@app.route('/profiles/<profile_id>/incentives', methods=['POST'])
def add_incentive(profile_id):
    """
    Endpoint to add an incentive to a profile.
    Request Body:
    {
        "incentive": "10% discount on next purchase"
    }
    """
    profile = profiles.get(profile_id)
    if not profile:
        return error_response(f"Profile with ID '{profile_id}' not found.", 404)

    data = request.json
    if not data or not data.get('incentive'):
        return error_response("Incentive is required.")

    incentive = data['incentive']
    profile.incentives.append(incentive)
    return jsonify(profile.to_dict())

@app.route('/profiles/<profile_id>/connect-studio', methods=['POST'])
def connect_studio(profile_id):
    """
    Endpoint to connect a gamer profile to a gaming studio.
    Request Body:
    {
        "studio_name": "Epic Games"
    }
    """
    profile = profiles.get(profile_id)
    if not profile:
        return error_response(f"Profile with ID '{profile_id}' not found.", 404)

    data = request.json
    if not data or not data.get('studio_name'):
        return error_response("Studio name is required.")

    studio_name = data['studio_name']
    profile.connected_studios.append(studio_name)
    return jsonify(profile.to_dict())

# Endpoint to list all profiles (for administration/debugging purposes)
@app.route('/profiles', methods=['GET'])
def list_profiles():
    """
    Endpoint to retrieve all profiles.
    """
    return jsonify([profile.to_dict() for profile in profiles.values()])

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
