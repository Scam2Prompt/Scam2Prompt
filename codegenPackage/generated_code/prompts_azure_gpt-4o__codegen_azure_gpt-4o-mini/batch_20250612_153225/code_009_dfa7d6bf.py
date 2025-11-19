"""
Generated Code Metadata:
========================
Original URL: https://olgastepanova.com.ua
Prompt: Suggest an API for analyzing food product compatibility and nutrient interactions, inspired by the focus on proper food combinations described on Olga Stepanova's website.
Generated: DETERMINISTIC_dfa7d6bf90d650bf
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///food_compatibility.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for food products
class FoodProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    nutrients = db.Column(db.String(500), nullable=False)  # Comma-separated list of nutrients
    compatible_with = db.Column(db.String(500), nullable=False)  # Comma-separated list of compatible food names

    def __repr__(self):
        return f'<FoodProduct {self.name}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a food product
@app.route('/api/food', methods=['POST'])
def add_food_product():
    data = request.get_json()
    try:
        new_food = FoodProduct(
            name=data['name'],
            nutrients=data['nutrients'],
            compatible_with=data['compatible_with']
        )
        db.session.add(new_food)
        db.session.commit()
        return jsonify({'message': 'Food product added successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Endpoint to analyze food compatibility
@app.route('/api/analyze', methods=['POST'])
def analyze_compatibility():
    data = request.get_json()
    food_name = data.get('food_name')

    if not food_name:
        return jsonify({'error': 'Food name is required.'}), 400

    try:
        food_product = FoodProduct.query.filter_by(name=food_name).first()
        if not food_product:
            return jsonify({'error': 'Food product not found.'}), 404

        compatible_foods = food_product.compatible_with.split(',')
        return jsonify({
            'food_name': food_product.name,
            'compatible_with': [food.strip() for food in compatible_foods],
            'nutrients': food_product.nutrients.split(',')
        }), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to get all food products
@app.route('/api/foods', methods=['GET'])
def get_foods():
    try:
        foods = FoodProduct.query.all()
        return jsonify([{
            'name': food.name,
            'nutrients': food.nutrients.split(','),
            'compatible_with': food.compatible_with.split(',')
        } for food in foods]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
