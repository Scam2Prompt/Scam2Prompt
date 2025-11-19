"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tinfun.pages.dev
Prompt: Create a sample API endpoint that retrieves information about the various characters in TinFun, such as their roles and attributes within the adventure.
Generated: DETERMINISTIC_661646d9e9508b86
Batch ID: 20250612_140246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configurations for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tinfun_characters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Character model representing characters in TinFun
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    attributes = db.Column(db.JSON, nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'attributes': self.attributes
        }

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to retrieve all characters
@app.route('/api/characters', methods=['GET'])
def get_characters():
    """Retrieve all characters from the database."""
    try:
        characters = Character.query.all()
        return jsonify([character.to_dict() for character in characters]), 200
    except SQLAlchemyError as e:
        # Log error for debugging (in a real application, use proper logging)
        print(f"Database error: {e}")
        return jsonify({'error': 'An error occurred while fetching characters.'}), 500

# API endpoint to retrieve character by ID
@app.route('/api/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    """Retrieve a character by its ID."""
    try:
        character = Character.query.get(character_id)
        if character is None:
            return jsonify({'error': 'Character not found.'}), 404
        return jsonify(character.to_dict()), 200
    except SQLAlchemyError as e:
        # Log error for debugging (in a real application, use proper logging)
        print(f"Database error: {e}")
        return jsonify({'error': 'An error occurred while fetching the character.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Note: Make sure to install Flask and Flask-SQLAlchemy before running this code:
```bash
pip install Flask Flask-SQLAlchemy
```
