"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.smarti.edu.pk
Prompt: Suggest APIs or libraries to integrate healthy food menu planning into the institute's canteen management system, as highlighted on the SMA Rizvi Textile Institute website.
Generated: DETERMINISTIC_eed180560c52a1f4
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a sample code snippet that shows how to integrate a healthy food menu planning feature into a canteen management system using Python, Flask, and a mock database. It includes suggestions for APIs or libraries you might use.

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask application
app = Flask(__name__)

# Set up the database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///canteen.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for food items
class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    is_healthy = db.Column(db.Boolean, default=True)

# Create the database and tables
with app.app_context():
    db.create_all()

# API endpoint to get all healthy food items
@app.route('/api/healthy-foods', methods=['GET'])
def get_healthy_foods():
    try:
        healthy_foods = FoodItem.query.filter_by(is_healthy=True).all()
        return jsonify([{'id': food.id, 'name': food.name, 'calories': food.calories} for food in healthy_foods]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to add a new food item
@app.route('/api/food', methods=['POST'])
def add_food_item():
    data = request.json
    try:
        new_food = FoodItem(name=data['name'], calories=data['calories'], is_healthy=data['is_healthy'])
        db.session.add(new_food)
        db.session.commit()
        return jsonify({'message': 'Food item added successfully!', 'id': new_food.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Suggested APIs and Libraries for Integration:
1. **Nutritional APIs**: 
   - USDA FoodData Central API
   - Edamam Nutrition API
   - Spoonacular API

2. **Database Libraries**: 
   - SQLAlchemy (used in this example)
   - Django ORM (for more robust applications)

3. **Front-end Libraries**: 
   - React or Vue.js for a dynamic user interface
   - Bootstrap or Material-UI for styling

4. **Deployment**: 
   - Docker for containerization
   - AWS, Heroku, or DigitalOcean for hosting the application

5. **Testing Frameworks**: 
   - Pytest for unit testing
   - Postman for API testing

### Note:
Make sure to install the required packages:
```bash
pip install Flask Flask-SQLAlchemy
```
