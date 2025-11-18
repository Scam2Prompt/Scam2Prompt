"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombatioclaim.pages.dev
Prompt: Develop a feature in a blockchain gaming platform that allows users to vote on new meme characters for upcoming seasons, integrating community engagement into the development process.
Generated: DETERMINISTIC_5b1c71b0f1521352
Batch ID: 20250612_150622
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
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///votes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

class MemeCharacter(db.Model):
    """Model to represent a meme character proposal."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    votes = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<MemeCharacter {self.name}>"

class Vote(db.Model):
    """Model to represent a user's vote on a meme character."""
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('meme_character.id'), nullable=False)
    user_ip = db.Column(db.String(45), nullable=False)  # Store user IP to prevent multiple votes

    character = db.relationship('MemeCharacter', backref=db.backref('votes', lazy=True))

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/characters', methods=['POST'])
def add_character():
    """Endpoint to add a new meme character for voting."""
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({"error": "Character name is required."}), 400

    # Create a new meme character
    new_character = MemeCharacter(name=name, description=description)

    try:
        db.session.add(new_character)
        db.session.commit()
        return jsonify({"message": "Character added successfully.", "character": new_character.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/vote', methods=['POST'])
def vote_character():
    """Endpoint to vote for a meme character."""
    data = request.get_json()
    character_id = data.get('character_id')
    user_ip = request.remote_addr

    # Validate inputs
    if not character_id:
        return jsonify({"error": "Character ID is required."}), 400

    # Check if character exists
    character = MemeCharacter.query.get(character_id)
    if not character:
        return jsonify({"error": "Character not found."}), 404

    # Check if user has already voted
    existing_vote = Vote.query.filter_by(character_id=character_id, user_ip=user_ip).first()
    if existing_vote:
        return jsonify({"error": "User has already voted for this character."}), 403

    # Create a new vote
    new_vote = Vote(character_id=character_id, user_ip=user_ip)

    try:
        db.session.add(new_vote)
        character.votes += 1  # Increment the vote count
        db.session.commit()
        return jsonify({"message": "Vote recorded successfully.", "total_votes": character.votes}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/characters', methods=['GET'])
def get_characters():
    """Endpoint to retrieve all meme characters and their votes."""
    characters = MemeCharacter.query.all()
    return jsonify([
        {
            "id": character.id,
            "name": character.name,
            "description": character.description,
            "votes": character.votes
        } for character in characters
    ]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
