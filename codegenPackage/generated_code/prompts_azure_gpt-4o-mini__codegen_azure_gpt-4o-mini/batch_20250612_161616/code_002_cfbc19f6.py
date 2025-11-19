"""
Generated Code Metadata:
========================
Original URL: https://sopa.vg
Prompt: Create an API endpoint for a restaurant service that provides take-away and delivery options for healthy vegetarian meals, inspired by Sopa's offerings.
Generated: DETERMINISTIC_cfbc19f6f511bc81
Batch ID: 20250612_161616
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

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Meal model
class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_vegetarian = db.Column(db.Boolean, default=True)

    def to_dict(self):
        """Convert the Meal object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'is_vegetarian': self.is_vegetarian
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/meals', methods=['GET'])
def get_meals():
    """API endpoint to retrieve all vegetarian meals."""
    try:
        meals = Meal.query.filter_by(is_vegetarian=True).all()
        return jsonify([meal.to_dict() for meal in meals]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/meals', methods=['POST'])
def add_meal():
    """API endpoint to add a new vegetarian meal."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'name' not in data or 'description' not in data or 'price' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    new_meal = Meal(
        name=data['name'],
        description=data['description'],
        price=data['price'],
        is_vegetarian=True
    )

    try:
        db.session.add(new_meal)
        db.session.commit()
        return jsonify(new_meal.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/meals/<int:meal_id>', methods=['GET'])
def get_meal(meal_id):
    """API endpoint to retrieve a specific meal by ID."""
    meal = Meal.query.get(meal_id)
    if meal is None:
        return jsonify({'error': 'Meal not found'}), 404
    return jsonify(meal.to_dict()), 200

@app.route('/meals/<int:meal_id>', methods=['DELETE'])
def delete_meal(meal_id):
    """API endpoint to delete a specific meal by ID."""
    meal = Meal.query.get(meal_id)
    if meal is None:
        return jsonify({'error': 'Meal not found'}), 404

    try:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({'message': 'Meal deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
