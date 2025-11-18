"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://as-media.rs
Prompt: Provide a solution for integrating a "No Ads" premium feature into a digital radio platform, similar to Radio S's "Radio bez reklama" option, using Python or JavaScript.
Generated: DETERMINISTIC_c9e12d935cf52ac0
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python solution for integrating a "No Ads" premium feature into a digital radio platform:

```python
from flask import Flask, jsonify, request

# Initialize Flask app
app = Flask(__name__)

# Simulated database for users and their subscription status
users_db = {
    "user1": {"name": "Alice", "premium": True},
    "user2": {"name": "Bob", "premium": False},
}

# Simulated playlist with ads
playlist_with_ads = [
    {"id": 1, "title": "Song A", "artist": "Artist 1"},
    {"id": 2, "title": "Ad 1", "type": "advertisement"},
    {"id": 3, "title": "Song B", "artist": "Artist 2"},
    {"id": 4, "title": "Ad 2", "type": "advertisement"},
    {"id": 5, "title": "Song C", "artist": "Artist 3"},
]

def get_user_by_id(user_id):
    """
    Fetch user details by user_id.
    """
    return users_db.get(user_id)

def get_playlist_for_user(user):
    """
    Generate a playlist based on the user's subscription status.
    If the user is a premium user, return the playlist without ads.
    """
    if user["premium"]:
        # Filter out advertisements for premium users
        return [item for item in playlist_with_ads if item.get("type") != "advertisement"]
    return playlist_with_ads

@app.route('/api/playlist', methods=['GET'])
def get_playlist():
    """
    API endpoint to fetch the playlist based on user subscription status.
    Expects a 'user_id' query parameter.
    """
    user_id = request.args.get("user_id")
    
    # Validate user_id parameter
    if not user_id:
        return jsonify({"error": "Missing user_id parameter"}), 400
    
    # Fetch user data
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    # Generate playlist for the user
    playlist = get_playlist_for_user(user)
    return jsonify({"playlist": playlist})

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

This code creates a simple Flask-based API to handle fetching a playlist with or without ads, depending on whether the user is a premium subscriber.
