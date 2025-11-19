"""
Generated Code Metadata:
========================
Original URL: https://new.joss-home.com
Prompt: Generate an API endpoint for retrieving furniture details (e.g., sofas, beds, tables) with attributes like dimensions, color, and price, as described on the Joss Home website.
Generated: DETERMINISTIC_3fb399dbdc3d24e5
Batch ID: 20250612_151539
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///furniture.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Furniture model
class Furniture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    dimensions = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Furniture object to a dictionary."""
        return {
            'id': self.id,
            'type': self.type,
            'dimensions': self.dimensions,
            'color': self.color,
            'price': self.price
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/furniture', methods=['GET'])
def get_furniture():
    """API endpoint to retrieve furniture details."""
    try:
        # Retrieve all furniture items from the database
        furniture_items = Furniture.query.all()
        # Convert the items to a list of dictionaries
        furniture_list = [item.to_dict() for item in furniture_items]
        return jsonify(furniture_list), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

@app.route('/api/furniture/<int:furniture_id>', methods=['GET'])
def get_furniture_by_id(furniture_id):
    """API endpoint to retrieve a specific furniture item by ID."""
    try:
        # Retrieve the furniture item by ID
        furniture_item = Furniture.query.get_or_404(furniture_id)
        return jsonify(furniture_item.to_dict()), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
