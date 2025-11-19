"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Create an API that allows users to explore different planetary environments and their unique agricultural challenges, inspired by the diverse ecosystems in Stellar Crop.
Generated: DETERMINISTIC_8add0076ed47690b
Batch ID: 20250612_162535
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

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///planets.db'  # Database URI for SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define Planet model
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    environment = db.Column(db.String(100), nullable=False)
    agriculture_challenges = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """Convert the Planet object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'environment': self.environment,
            'agriculture_challenges': self.agriculture_challenges
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/planets', methods=['GET'])
def get_planets():
    """Get a list of all planets and their agricultural challenges."""
    try:
        planets = Planet.query.all()
        return jsonify([planet.to_dict() for planet in planets]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    """Get details of a specific planet by its ID."""
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({'error': 'Planet not found'}), 404
    return jsonify(planet.to_dict()), 200

@app.route('/planets', methods=['POST'])
def create_planet():
    """Create a new planet with its environment and agricultural challenges."""
    data = request.get_json()
    
    if not data or 'name' not in data or 'environment' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_planet = Planet(
        name=data['name'],
        environment=data['environment'],
        agriculture_challenges=data.get('agriculture_challenges')
    )
    
    try:
        db.session.add(new_planet)
        db.session.commit()
        return jsonify(new_planet.to_dict()), 201
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/planets/<int:planet_id>', methods=['PUT'])
def update_planet(planet_id):
    """Update an existing planet's environment and agricultural challenges."""
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({'error': 'Planet not found'}), 404

    data = request.get_json()
    
    if 'name' in data:
        planet.name = data['name']
    if 'environment' in data:
        planet.environment = data['environment']
    if 'agriculture_challenges' in data:
        planet.agriculture_challenges = data.get('agriculture_challenges')

    try:
        db.session.commit()
        return jsonify(planet.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/planets/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    """Delete a planet by its ID."""
    planet = Planet.query.get(planet_id)
    if planet is None:
        return jsonify({'error': 'Planet not found'}), 404

    try:
        db.session.delete(planet)
        db.session.commit()
        return jsonify({'message': 'Planet deleted successfully'}), 204
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
