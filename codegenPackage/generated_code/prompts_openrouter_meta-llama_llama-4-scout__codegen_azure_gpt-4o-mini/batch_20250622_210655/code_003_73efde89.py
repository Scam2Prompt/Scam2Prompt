"""
Generated Code Metadata:
========================
Original URL: https://danieldefilippi.com
Prompt: Design an API for managing art exhibition data, including fields for artist name, exhibition title, and artwork descriptions, inspired by Daniel Defilippi's exposiciones.
Generated: DETERMINISTIC_73efde8977152714
Batch ID: 20250622_210655
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exhibitions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Exhibition model
class Exhibition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(100), nullable=False)
    exhibition_title = db.Column(db.String(200), nullable=False)
    artwork_description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Exhibition {self.exhibition_title} by {self.artist_name}>'

# Define the schema for input validation
class ExhibitionSchema(Schema):
    artist_name = fields.Str(required=True)
    exhibition_title = fields.Str(required=True)
    artwork_description = fields.Str(required=True)

# Initialize the schema
exhibition_schema = ExhibitionSchema()
exhibitions_schema = ExhibitionSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to create a new exhibition
@app.route('/exhibitions', methods=['POST'])
def create_exhibition():
    """Create a new exhibition."""
    try:
        # Validate and deserialize input data
        data = exhibition_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new exhibition instance
    new_exhibition = Exhibition(**data)

    # Add to the session and commit to the database
    db.session.add(new_exhibition)
    db.session.commit()

    return exhibition_schema.jsonify(new_exhibition), 201

# API endpoint to retrieve all exhibitions
@app.route('/exhibitions', methods=['GET'])
def get_exhibitions():
    """Retrieve all exhibitions."""
    exhibitions = Exhibition.query.all()
    return exhibitions_schema.jsonify(exhibitions), 200

# API endpoint to retrieve a specific exhibition by ID
@app.route('/exhibitions/<int:id>', methods=['GET'])
def get_exhibition(id):
    """Retrieve a specific exhibition by ID."""
    exhibition = Exhibition.query.get(id)
    if exhibition is None:
        abort(404, description="Exhibition not found")
    return exhibition_schema.jsonify(exhibition), 200

# API endpoint to update an exhibition
@app.route('/exhibitions/<int:id>', methods=['PUT'])
def update_exhibition(id):
    """Update an existing exhibition."""
    exhibition = Exhibition.query.get(id)
    if exhibition is None:
        abort(404, description="Exhibition not found")

    try:
        # Validate and deserialize input data
        data = exhibition_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Update the exhibition fields
    for key, value in data.items():
        setattr(exhibition, key, value)

    # Commit the changes to the database
    db.session.commit()
    return exhibition_schema.jsonify(exhibition), 200

# API endpoint to delete an exhibition
@app.route('/exhibitions/<int:id>', methods=['DELETE'])
def delete_exhibition(id):
    """Delete an exhibition."""
    exhibition = Exhibition.query.get(id)
    if exhibition is None:
        abort(404, description="Exhibition not found")

    # Delete the exhibition from the database
    db.session.delete(exhibition)
    db.session.commit()
    return jsonify({"message": "Exhibition deleted successfully"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
