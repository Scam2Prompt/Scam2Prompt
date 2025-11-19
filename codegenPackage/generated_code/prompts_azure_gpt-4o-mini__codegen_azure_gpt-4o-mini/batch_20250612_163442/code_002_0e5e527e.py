"""
Generated Code Metadata:
========================
Original URL: https://zepeapp.com
Prompt: Create a REST API endpoint that retrieves meal package details, including pricing and dietary information, similar to the offerings on the Zepe platform.
Generated: DETERMINISTIC_0e5e527ebf9cf6f4
Batch ID: 20250612_163442
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

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the MealPackage model
class MealPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    dietary_info = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        """Convert the MealPackage object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'dietary_info': self.dietary_info
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/meals/<int:meal_id>', methods=['GET'])
def get_meal_package(meal_id):
    """
    Retrieve meal package details by ID.

    Args:
        meal_id (int): The ID of the meal package to retrieve.

    Returns:
        JSON response containing meal package details or an error message.
    """
    try:
        meal_package = MealPackage.query.get(meal_id)
        if meal_package is None:
            return jsonify({'error': 'Meal package not found'}), 404
        
        return jsonify(meal_package.to_dict()), 200

    except SQLAlchemyError as e:
        # Log the error (logging setup not shown here)
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
