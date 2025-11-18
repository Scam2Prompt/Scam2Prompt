"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tangganglife.pages.dev
Prompt: Recommend an API or library for implementing a leaderboard system similar to the one described on the Tang Gang Guild website, and provide example code for integrating it.
Generated: DETERMINISTIC_4c5f929d490344b2
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for the leaderboard entries
class LeaderboardEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "score": self.score}

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to get the leaderboard
@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    try:
        entries = LeaderboardEntry.query.order_by(LeaderboardEntry.score.desc()).all()
        return jsonify([entry.to_dict() for entry in entries]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to add a new entry to the leaderboard
@app.route('/leaderboard', methods=['POST'])
def add_entry():
    if not request.json or 'username' not in request.json or 'score' not in request.json:
        abort(400)  # Bad request if JSON data is missing

    username = request.json['username']
    score = request.json['score']
    
    # Check if the user already exists
    existing_entry = LeaderboardEntry.query.filter_by(username=username).first()
    if existing_entry:
        return jsonify({"error": "Username already exists"}), 400

    new_entry = LeaderboardEntry(username=username, score=score)
    try:
        db.session.add(new_entry)
        db.session.commit()
        return jsonify(new_entry.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()

# Endpoint to update an existing entry
@app.route('/leaderboard/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    if not request.json or 'score' not in request.json:
        abort(400)  # Bad request if JSON data is missing

    score = request.json['score']
    entry = LeaderboardEntry.query.get(entry_id)

    if entry is None:
        return jsonify({"error": "Entry not found"}), 404

    entry.score = score
    try:
        db.session.commit()
        return jsonify(entry.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.session.close()

# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True)
```
