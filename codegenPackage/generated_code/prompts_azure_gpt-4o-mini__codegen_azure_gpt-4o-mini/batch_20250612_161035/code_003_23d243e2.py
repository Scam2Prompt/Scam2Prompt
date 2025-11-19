"""
Generated Code Metadata:
========================
Original URL: https://sparkarabia.net
Prompt: Create a REST API endpoint that retrieves information about Spark Arabia's heavy equipment rental options and customized rental packages.
Generated: DETERMINISTIC_23d243e2b185c7f4
Batch ID: 20250612_161035
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

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///equipment_rental.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Equipment model
class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    rental_price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        """Convert the Equipment object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'rental_price': self.rental_price,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/equipment', methods=['GET'])
def get_equipment():
    """Retrieve all heavy equipment rental options."""
    try:
        equipment_list = Equipment.query.all()
        return jsonify([equip.to_dict() for equip in equipment_list]), 200
    except SQLAlchemyError as e:
        # Log the error (logging not implemented here for brevity)
        return jsonify({'error': 'Database error occurred'}), 500

@app.route('/api/equipment/<int:equipment_id>', methods=['GET'])
def get_equipment_by_id(equipment_id):
    """Retrieve a specific piece of equipment by its ID."""
    try:
        equipment = Equipment.query.get_or_404(equipment_id)
        return jsonify(equipment.to_dict()), 200
    except SQLAlchemyError as e:
        # Log the error (logging not implemented here for brevity)
        return jsonify({'error': 'Database error occurred'}), 500

@app.route('/api/rental-packages', methods=['GET'])
def get_rental_packages():
    """Retrieve customized rental packages (dummy data for example)."""
    packages = [
        {
            'package_name': 'Basic Package',
            'description': 'Includes basic equipment for small projects.',
            'price': 500
        },
        {
            'package_name': 'Premium Package',
            'description': 'Includes premium equipment for large projects.',
            'price': 1500
        }
    ]
    return jsonify(packages), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
