"""
Generated Code Metadata:
========================
Original URL: https://play-gamer.com
Prompt: Design a simple API for a racing game that features unlocking new tracks and achievements, using the gameplay mechanics of Rally Racer Dirt as a reference.
Generated: DETERMINISTIC_e842e8ff198bd3de
Batch ID: 20250622_211548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database for tracks and achievements
tracks = [
    {"id": 1, "name": "Forest Trail", "unlocked": True},
    {"id": 2, "name": "Desert Dash", "unlocked": False},
    {"id": 3, "name": "Mountain Climb", "unlocked": False},
]

achievements = [
    {"id": 1, "name": "First Race", "unlocked": True},
    {"id": 2, "name": "Speed Demon", "unlocked": False},
    {"id": 3, "name": "Track Master", "unlocked": False},
]

# Error handling utility
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route to get all tracks
@app.route('/tracks', methods=['GET'])
def get_tracks():
    return jsonify({"tracks": tracks})

# Route to unlock a track
@app.route('/tracks/unlock/<int:track_id>', methods=['POST'])
def unlock_track(track_id):
    track = next((t for t in tracks if t["id"] == track_id), None)
    if not track:
        return error_response("Track not found", 404)
    if track["unlocked"]:
        return error_response("Track is already unlocked")
    track["unlocked"] = True
    return jsonify({"message": f"Track '{track['name']}' unlocked successfully", "track": track})

# Route to get all achievements
@app.route('/achievements', methods=['GET'])
def get_achievements():
    return jsonify({"achievements": achievements})

# Route to unlock an achievement
@app.route('/achievements/unlock/<int:achievement_id>', methods=['POST'])
def unlock_achievement(achievement_id):
    achievement = next((a for a in achievements if a["id"] == achievement_id), None)
    if not achievement:
        return error_response("Achievement not found", 404)
    if achievement["unlocked"]:
        return error_response("Achievement is already unlocked")
    achievement["unlocked"] = True
    return jsonify({"message": f"Achievement '{achievement['name']}' unlocked successfully", "achievement": achievement})

# Route to reset all tracks and achievements (for testing purposes)
@app.route('/reset', methods=['POST'])
def reset_game():
    for track in tracks:
        track["unlocked"] = track["id"] == 1  # Only the first track is unlocked by default
    for achievement in achievements:
        achievement["unlocked"] = achievement["id"] == 1  # Only the first achievement is unlocked by default
    return jsonify({"message": "Game reset successfully", "tracks": tracks, "achievements": achievements})

# Error handling for unsupported routes
@app.errorhandler(404)
def not_found(error):
    return error_response("Endpoint not found", 404)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
