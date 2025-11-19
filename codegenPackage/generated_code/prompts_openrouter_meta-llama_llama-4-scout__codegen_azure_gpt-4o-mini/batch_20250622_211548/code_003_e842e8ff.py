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
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///racing_game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Tracks
class Track(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    unlocked = db.Column(db.Boolean, default=False)

# Database model for Achievements
class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    unlocked = db.Column(db.Boolean, default=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/tracks', methods=['GET'])
def get_tracks():
    """Retrieve all tracks with their unlock status."""
    tracks = Track.query.all()
    return jsonify([{'id': track.id, 'name': track.name, 'unlocked': track.unlocked} for track in tracks])

@app.route('/tracks/<int:track_id>', methods=['POST'])
def unlock_track(track_id):
    """Unlock a specific track by its ID."""
    track = Track.query.get(track_id)
    if track is None:
        abort(404, description="Track not found")
    
    track.unlocked = True
    db.session.commit()
    return jsonify({'message': f'Track {track.name} unlocked successfully.'}), 200

@app.route('/achievements', methods=['GET'])
def get_achievements():
    """Retrieve all achievements with their unlock status."""
    achievements = Achievement.query.all()
    return jsonify([{'id': achievement.id, 'title': achievement.title, 'description': achievement.description, 'unlocked': achievement.unlocked} for achievement in achievements])

@app.route('/achievements/<int:achievement_id>', methods=['POST'])
def unlock_achievement(achievement_id):
    """Unlock a specific achievement by its ID."""
    achievement = Achievement.query.get(achievement_id)
    if achievement is None:
        abort(404, description="Achievement not found")
    
    achievement.unlocked = True
    db.session.commit()
    return jsonify({'message': f'Achievement {achievement.title} unlocked successfully.'}), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': str(error)}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
