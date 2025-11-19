"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Create an API that allows users to explore different planetary environments and their unique agricultural challenges, inspired by the diverse ecosystems in Stellar Crop.
Generated: DETERMINISTIC_8add0076ed47690b
Batch ID: 20250612_162535
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Planet model
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    environment = db.Column(db.String(200), nullable=False)
    agricultural_challenges = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the Planet object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'environment': self.environment,
            'agricultural_challenges': self.agricultural_challenges
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/planets', methods=['GET'])
def get_planets():
    """Retrieve a list of all planets and their agricultural challenges."""
    try:
        planets = Planet.query.all()
        return jsonify([planet.to_dict() for planet in planets]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    """Retrieve a specific planet by its ID."""
    try:
        planet = Planet.query.get_or_404(planet_id)
        return jsonify(planet.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/planets', methods=['POST'])
def create_planet():
    """Create a new planet with its agricultural challenges."""
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'environment', 'agricultural_challenges')):
        return jsonify({'error': 'Invalid input'}), 400

    new_planet = Planet(
        name=data['name'],
        environment=data['environment'],
        agricultural_challenges=data['agricultural_challenges']
    )

    try:
        db.session.add(new_planet)
        db.session.commit()
        return jsonify(new_planet.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/planets/<int:planet_id>', methods=['PUT'])
def update_planet(planet_id):
    """Update an existing planet's information."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input'}), 400

    try:
        planet = Planet.query.get_or_404(planet_id)
        if 'name' in data:
            planet.name = data['name']
        if 'environment' in data:
            planet.environment = data['environment']
        if 'agricultural_challenges' in data:
            planet.agricultural_challenges = data['agricultural_challenges']

        db.session.commit()
        return jsonify(planet.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/planets/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    """Delete a planet by its ID."""
    try:
        planet = Planet.query.get_or_404(planet_id)
        db.session.delete(planet)
        db.session.commit()
        return jsonify({'message': 'Planet deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
