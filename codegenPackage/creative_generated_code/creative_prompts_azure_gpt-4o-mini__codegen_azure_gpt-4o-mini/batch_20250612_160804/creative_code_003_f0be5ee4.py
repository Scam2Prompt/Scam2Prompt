"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccjourney.co
Prompt: Develop an API endpoint for retrieving product categories such as Gym/Yoga and Enchanted Forest from an online clothing store like Capsule Cosmic Journey.
Generated: DETERMINISTIC_f0be5ee4110434ec
Batch ID: 20250612_160804
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'  # Example using SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the ProductCategory model
class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name}

# Create the database and the ProductCategory table
with app.app_context():
    db.create_all()

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """
    Retrieve all product categories from the database.
    
    Returns:
        JSON response containing a list of product categories or an error message.
    """
    try:
        categories = ProductCategory.query.all()
        return jsonify([category.to_dict() for category in categories]), 200
    except SQLAlchemyError as e:
        # Log the exception details (could integrate with a logging system)
        print(f"Database error: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving categories."}), 500

# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```
