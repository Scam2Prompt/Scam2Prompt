"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Write code to create an API that lists Ecoplast furniture products, including categories like beds, wardrobes, and kitchen cabinets, with detailed attributes such as model numbers and descriptions.
Generated: DETERMINISTIC_ce01dab3b67d7c64
Batch ID: 20250612_153224
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

# Initialize Flask application
app = Flask(__name__)

# Configuring the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecoplast_furniture.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Furniture model
class Furniture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    model_number = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the Furniture model to a dictionary."""
        return {
            'id': self.id,
            'category': self.category,
            'model_number': self.model_number,
            'description': self.description
        }

# Create the database and tables (if they don't exist)
with app.app_context():
    db.create_all()

@app.route('/api/furniture', methods=['GET'])
def get_furniture():
    """Endpoint to list all furniture products."""
    try:
        furniture_list = Furniture.query.all()
        return jsonify([item.to_dict() for item in furniture_list]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/furniture', methods=['POST'])
def add_furniture():
    """Endpoint to add new furniture product."""
    data = request.get_json()
    
    # Validate input data
    if not data or not all(k in data for k in ('category', 'model_number', 'description')):
        return jsonify({'error': 'Invalid input data'}), 400

    # Create new furniture entry
    try:
        new_furniture = Furniture(
            category=data['category'],
            model_number=data['model_number'],
            description=data['description']
        )
        db.session.add(new_furniture)
        db.session.commit()
        return jsonify(new_furniture.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """Return a custom 404 error message."""
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
