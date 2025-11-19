"""
Generated Code Metadata:
========================
Original URL: https://ton-station-2.gitbook.io
Prompt: Generate code to implement a leaderboard system for a Web3 game, inspired by TON Station's "Storm the Leagues" Season 2 Finale event.
Generated: DETERMINISTIC_b22fe015bd5b8f7d
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leaderboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for leaderboard entries
class LeaderboardEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<LeaderboardEntry(username={self.username}, score={self.score})>"

# Schema for validating leaderboard entries
class LeaderboardEntrySchema(Schema):
    username = fields.Str(required=True)
    score = fields.Int(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Route to add a new entry to the leaderboard
@app.route('/leaderboard', methods=['POST'])
def add_entry():
    json_data = request.get_json()
    schema = LeaderboardEntrySchema()

    # Validate incoming data
    try:
        data = schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new leaderboard entry
    new_entry = LeaderboardEntry(username=data['username'], score=data['score'])

    # Add entry to the database
    try:
        db.session.add(new_entry)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Username already exists."}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

    return jsonify({"message": "Entry added successfully."}), 201

# Route to get the leaderboard
@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    entries = LeaderboardEntry.query.order_by(LeaderboardEntry.score.desc()).all()
    leaderboard = [{"username": entry.username, "score": entry.score} for entry in entries]
    return jsonify(leaderboard), 200

# Route to clear the leaderboard (for resetting the game)
@app.route('/leaderboard', methods=['DELETE'])
def clear_leaderboard():
    try:
        db.session.query(LeaderboardEntry).delete()
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

    return jsonify({"message": "Leaderboard cleared successfully."}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
