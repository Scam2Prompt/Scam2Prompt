"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Generate a code snippet that demonstrates how to implement a digital support system for cultural access based on the initiatives of the Sophia Loisirs & Vie association.
Generated: DETERMINISTIC_9017967927e0cfaa
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cultural_access.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model for cultural initiatives
class Initiative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Initiative object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/initiatives', methods=['POST'])
def add_initiative():
    """Endpoint to add a new cultural initiative."""
    data = request.get_json()
    try:
        new_initiative = Initiative(
            title=data['title'],
            description=data['description'],
            category=data['category']
        )
        db.session.add(new_initiative)
        db.session.commit()
        return jsonify(new_initiative.to_dict()), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/initiatives', methods=['GET'])
def get_initiatives():
    """Endpoint to retrieve all cultural initiatives."""
    initiatives = Initiative.query.all()
    return jsonify([initiative.to_dict() for initiative in initiatives]), 200

@app.route('/initiatives/<int:init_id>', methods=['GET'])
def get_initiative(init_id):
    """Endpoint to retrieve a specific cultural initiative by ID."""
    initiative = Initiative.query.get_or_404(init_id)
    return jsonify(initiative.to_dict()), 200

@app.route('/initiatives/<int:init_id>', methods=['PUT'])
def update_initiative(init_id):
    """Endpoint to update a specific cultural initiative."""
    data = request.get_json()
    initiative = Initiative.query.get_or_404(init_id)
    try:
        initiative.title = data.get('title', initiative.title)
        initiative.description = data.get('description', initiative.description)
        initiative.category = data.get('category', initiative.category)
        db.session.commit()
        return jsonify(initiative.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/initiatives/<int:init_id>', methods=['DELETE'])
def delete_initiative(init_id):
    """Endpoint to delete a specific cultural initiative."""
    initiative = Initiative.query.get_or_404(init_id)
    db.session.delete(initiative)
    db.session.commit()
    return jsonify({'message': 'Initiative deleted successfully'}), 204

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
