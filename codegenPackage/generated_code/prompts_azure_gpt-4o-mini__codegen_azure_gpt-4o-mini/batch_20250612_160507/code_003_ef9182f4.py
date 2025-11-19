"""
Generated Code Metadata:
========================
Original URL: https://skutersite.pl
Prompt: Develop an API recommendation for a system that protects car paint with ceramic coatings, inspired by the article's discussion on spring maintenance tips.
Generated: DETERMINISTIC_ef9182f424741ae1
Batch ID: 20250612_160507
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ceramic_coatings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the model for the ceramic coating recommendations
class CoatingRecommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)
    application_tips = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'application_tips': self.application_tips
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    """Retrieve all ceramic coating recommendations."""
    recommendations = CoatingRecommendation.query.all()
    return jsonify([rec.to_dict() for rec in recommendations]), 200

@app.route('/recommendations', methods=['POST'])
def add_recommendation():
    """Add a new ceramic coating recommendation."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'name' not in data or 'description' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    new_recommendation = CoatingRecommendation(
        name=data['name'],
        description=data['description'],
        application_tips=data.get('application_tips')
    )

    try:
        db.session.add(new_recommendation)
        db.session.commit()
        return jsonify(new_recommendation.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Recommendation already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/recommendations/<int:id>', methods=['GET'])
def get_recommendation(id):
    """Retrieve a specific ceramic coating recommendation by ID."""
    recommendation = CoatingRecommendation.query.get(id)
    if recommendation is None:
        return jsonify({'error': 'Recommendation not found'}), 404
    return jsonify(recommendation.to_dict()), 200

@app.route('/recommendations/<int:id>', methods=['PUT'])
def update_recommendation(id):
    """Update an existing ceramic coating recommendation."""
    data = request.get_json()
    recommendation = CoatingRecommendation.query.get(id)

    if recommendation is None:
        return jsonify({'error': 'Recommendation not found'}), 404

    if 'name' in data:
        recommendation.name = data['name']
    if 'description' in data:
        recommendation.description = data['description']
    if 'application_tips' in data:
        recommendation.application_tips = data.get('application_tips')

    db.session.commit()
    return jsonify(recommendation.to_dict()), 200

@app.route('/recommendations/<int:id>', methods=['DELETE'])
def delete_recommendation(id):
    """Delete a ceramic coating recommendation."""
    recommendation = CoatingRecommendation.query.get(id)
    if recommendation is None:
        return jsonify({'error': 'Recommendation not found'}), 404

    db.session.delete(recommendation)
    db.session.commit()
    return jsonify({'message': 'Recommendation deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
