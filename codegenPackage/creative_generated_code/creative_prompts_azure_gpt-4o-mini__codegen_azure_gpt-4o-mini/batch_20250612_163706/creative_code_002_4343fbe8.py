"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-shibawapp-officiall-new-3th.blogspot.com
Prompt: Create an API endpoint for an e-commerce application that retrieves product categories such as "Feminino" and "Masculino," inspired by the structure of the vidamarinhalapa site.
Generated: DETERMINISTIC_4343fbe8ca797faf
Batch ID: 20250612_163706
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
from http import HTTPStatus

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the ProductCategory model
class ProductCategory(db.Model):
    __tablename__ = 'product_categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name
        }

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """
    API endpoint to retrieve product categories.
    Returns a JSON array of product categories.
    """
    try:
        categories = ProductCategory.query.all()
        return jsonify([category.to_dict() for category in categories]), HTTPStatus.OK
    except Exception as e:
        # Log the error (In production, use a logging library)
        print(f"Error retrieving categories: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving categories."}), HTTPStatus.INTERNAL_SERVER_ERROR

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code sets up a Flask application with an SQLite database to retrieve product categories. Please ensure you have the `Flask` and `Flask-SQLAlchemy` packages installed in your environment.
