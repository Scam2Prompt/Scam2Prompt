"""
Generated Code Metadata:
========================
Original URL: https://www.madoniaoli.it
Prompt: "Create a RESTful API endpoint to retrieve a list of olive oil products with their corresponding prices and descriptions, using a framework like Flask or Django."
Generated: DETERMINISTIC_1c76b4b071c4d357
Batch ID: 20250622_210655
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

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///olive_oil.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the OliveOil model
class OliveOil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        """Convert the OliveOil object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/api/olive_oils', methods=['GET'])
def get_olive_oils():
    """Retrieve a list of olive oil products with their prices and descriptions."""
    try:
        # Query all olive oil products
        olive_oils = OliveOil.query.all()
        # Convert the results to a list of dictionaries
        return jsonify([olive_oil.to_dict() for olive_oil in olive_oils]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
