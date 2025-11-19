"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sopa.vg
Prompt: Create an API endpoint for a restaurant service that provides take-away and delivery options for healthy vegetarian meals, inspired by Sopa's offerings.
Generated: DETERMINISTIC_cfbc19f6f511bc81
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
db = SQLAlchemy(app)

# Model for the meal
class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    is_vegetarian = db.Column(db.Boolean, default=True)

# Schema for meal validation
class MealSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    is_vegetarian = fields.Bool()

# Initialize schema
meal_schema = MealSchema()
meals_schema = MealSchema(many=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to get all vegetarian meals
@app.route('/api/meals', methods=['GET'])
def get_meals():
    """Retrieve all vegetarian meals from the database."""
    meals = Meal.query.filter_by(is_vegetarian=True).all()
    return meals_schema.dump(meals), 200

# API endpoint to add a new meal
@app.route('/api/meals', methods=['POST'])
def add_meal():
    """Add a new meal to the database."""
    try:
        # Validate and deserialize input data
        meal_data = meal_schema.load(request.json)
        new_meal = Meal(**meal_data)
        db.session.add(new_meal)
        db.session.commit()
        return meal_schema.dump(new_meal), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
