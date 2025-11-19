"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testtt-ba0.pages.dev
Prompt: Develop a REST API endpoint that allows players to manage their Wolves and Sheep, including breeding and resource production.
Generated: DETERMINISTIC_f67f2a31903ff9ef
Batch ID: 20250612_163502
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Models
class Animal(db.Model):
    """Model representing an animal in the game."""
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)  # 'wolf' or 'sheep'
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, default=0)  # Age of the animal

    def to_dict(self):
        """Convert the Animal instance to a dictionary."""
        return {
            'id': self.id,
            'type': self.type,
            'name': self.name,
            'age': self.age
        }

# Initialize the database
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/animals', methods=['GET'])
def get_animals():
    """Retrieve all animals."""
    animals = Animal.query.all()
    return jsonify([animal.to_dict() for animal in animals]), 200

@app.route('/animals', methods=['POST'])
def add_animal():
    """Add a new animal."""
    data = request.get_json()
    if not data or 'type' not in data or 'name' not in data:
        abort(400, description="Invalid input - 'type' and 'name' are required.")
    
    animal = Animal(type=data['type'], name=data['name'])
    db.session.add(animal)
    db.session.commit()
    
    return jsonify(animal.to_dict()), 201

@app.route('/animals/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    """Update an existing animal."""
    animal = Animal.query.get_or_404(animal_id)
    data = request.get_json()

    if 'name' in data:
        animal.name = data['name']
    if 'age' in data:
        animal.age = data['age']

    db.session.commit()
    return jsonify(animal.to_dict()), 200

@app.route('/animals/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    """Delete an animal."""
    animal = Animal.query.get_or_404(animal_id)
    db.session.delete(animal)
    db.session.commit()
    return jsonify({'message': 'Animal deleted successfully'}), 200

@app.route('/breed', methods=['POST'])
def breed_animals():
    """Breed animals to produce a new one."""
    data = request.get_json()
    if not data or 'parent1_id' not in data or 'parent2_id' not in data:
        abort(400, description="Invalid input - 'parent1_id' and 'parent2_id' are required.")
    
    parent1 = Animal.query.get_or_404(data['parent1_id'])
    parent2 = Animal.query.get_or_404(data['parent2_id'])

    if parent1.type != parent2.type:
        abort(400, description="Cannot breed different types of animals.")

    # Basic breeding logic
    child_name = f"Offspring of {parent1.name} and {parent2.name}"
    child = Animal(type=parent1.type, name=child_name)
    db.session.add(child)
    db.session.commit()

    return jsonify(child.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
