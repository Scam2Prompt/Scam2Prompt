"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itscool.srv.br
Prompt: What are the key features of a school meal program that ensures quality and safety, as outlined by It's Cool Foods? Provide examples of how to integrate these features into an API.
Generated: DETERMINISTIC_ac380781af4baf5a
Batch ID: 20250612_161616
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

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_meals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Meal model
class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    allergens = db.Column(db.String(100))
    nutritional_info = db.Column(db.String(200))

    def __repr__(self):
        return f'<Meal {self.meal_name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API route to add a new meal
@app.route('/meals', methods=['POST'])
def add_meal():
    try:
        data = request.get_json()
        new_meal = Meal(
            meal_name=data['meal_name'],
            ingredients=data['ingredients'],
            allergens=data.get('allergens', ''),
            nutritional_info=data.get('nutritional_info', '')
        )
        db.session.add(new_meal)
        db.session.commit()
        return jsonify({'message': 'Meal added successfully!'}), 201
    except (KeyError, TypeError) as e:
        return jsonify({'error': 'Invalid data provided!'}), 400
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error!'}), 500

# API route to get all meals
@app.route('/meals', methods=['GET'])
def get_meals():
    try:
        meals = Meal.query.all()
        return jsonify([{
            'id': meal.id,
            'meal_name': meal.meal_name,
            'ingredients': meal.ingredients,
            'allergens': meal.allergens,
            'nutritional_info': meal.nutritional_info
        } for meal in meals]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error!'}), 500

# API route to get a specific meal by ID
@app.route('/meals/<int:id>', methods=['GET'])
def get_meal(id):
    try:
        meal = Meal.query.get_or_404(id)
        return jsonify({
            'id': meal.id,
            'meal_name': meal.meal_name,
            'ingredients': meal.ingredients,
            'allergens': meal.allergens,
            'nutritional_info': meal.nutritional_info
        }), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error!'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
