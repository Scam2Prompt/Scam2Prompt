"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thecannibals.xyz
Prompt: Create a RESTful API that tracks the morale and supplies of characters on an island, referencing the unique survival challenges presented in "The Cannibals" project.
Generated: DETERMINISTIC_a0250d2870a5707c
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and the SQLAlchemy database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///island_characters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Character model to represent each character's morale and supplies
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    morale = db.Column(db.Integer, nullable=False, default=100)  # Morale ranges from 0 to 100
    supplies = db.Column(db.Integer, nullable=False, default=50)  # Supplies quantity

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'morale': self.morale,
            'supplies': self.supplies
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to get the list of characters
@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    return jsonify([character.to_dict() for character in characters]), 200

# Route to get a specific character by ID
@app.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id):
    character = Character.query.get(character_id)
    if character is None:
        abort(404, description="Character not found")
    return jsonify(character.to_dict()), 200

# Route to create a new character
@app.route('/characters', methods=['POST'])
def create_character():
    data = request.json
    if 'name' not in data:
        abort(400, description="Name is required")
    
    new_character = Character(
        name=data['name'],
        morale=data.get('morale', 100),
        supplies=data.get('supplies', 50)
    )
    
    db.session.add(new_character)
    db.session.commit()
    return jsonify(new_character.to_dict()), 201

# Route to update an existing character's morale and supplies
@app.route('/characters/<int:character_id>', methods=['PUT'])
def update_character(character_id):
    character = Character.query.get(character_id)
    if character is None:
        abort(404, description="Character not found")
    
    data = request.json
    if 'morale' in data:
        character.morale = data['morale']
    if 'supplies' in data:
        character.supplies = data['supplies']
        
    db.session.commit()
    return jsonify(character.to_dict()), 200

# Route to delete a character
@app.route('/characters/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    character = Character.query.get(character_id)
    if character is None:
        abort(404, description="Character not found")
    
    db.session.delete(character)
    db.session.commit()
    return jsonify({'message': 'Character deleted successfully'}), 204

# Error handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': 'Not found', 'message': str(error)}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({'error': 'Bad request', 'message': str(error)}), 400

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
