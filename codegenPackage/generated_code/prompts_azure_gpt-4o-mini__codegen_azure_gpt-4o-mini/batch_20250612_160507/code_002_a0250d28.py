"""
Generated Code Metadata:
========================
Original URL: https://thecannibals.xyz
Prompt: Create a RESTful API that tracks the morale and supplies of characters on an island, referencing the unique survival challenges presented in "The Cannibals" project.
Generated: DETERMINISTIC_a0250d2870a5707c
Batch ID: 20250612_160507
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///island_characters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Character model
class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    morale = db.Column(db.Integer, nullable=False)
    supplies = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Character {self.name}>'

# Create a schema for serialization
class CharacterSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    morale = fields.Int(required=True)
    supplies = fields.Int(required=True)

# Initialize the schema
character_schema = CharacterSchema()
characters_schema = CharacterSchema(many=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get all characters
@app.route('/characters', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    return characters_schema.dump(characters), 200

# Route to get a character by ID
@app.route('/characters/<int:id>', methods=['GET'])
def get_character(id):
    character = Character.query.get(id)
    if character is None:
        abort(404, description="Character not found")
    return character_schema.dump(character), 200

# Route to create a new character
@app.route('/characters', methods=['POST'])
def create_character():
    try:
        data = character_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_character = Character(**data)
    db.session.add(new_character)
    db.session.commit()
    return character_schema.dump(new_character), 201

# Route to update a character's morale and supplies
@app.route('/characters/<int:id>', methods=['PUT'])
def update_character(id):
    character = Character.query.get(id)
    if character is None:
        abort(404, description="Character not found")

    try:
        data = character_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    character.morale = data.get('morale', character.morale)
    character.supplies = data.get('supplies', character.supplies)
    db.session.commit()
    return character_schema.dump(character), 200

# Route to delete a character
@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    character = Character.query.get(id)
    if character is None:
        abort(404, description="Character not found")

    db.session.delete(character)
    db.session.commit()
    return jsonify({"message": "Character deleted"}), 204

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": str(error)}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
