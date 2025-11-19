"""
Generated Code Metadata:
========================
Original URL: https://azuharu.net
Prompt: Provide a code example for a web application that allows users to book laptop rentals, based on the digital solutions mentioned in the Azuharu article about Sewa Laptop Surabaya.
Generated: DETERMINISTIC_b60bae6437bce7bf
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///laptop_rentals.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Laptop model
class Laptop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    available = db.Column(db.Boolean, default=True)

# Define the Rental model
class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    laptop_id = db.Column(db.Integer, db.ForeignKey('laptop.id'), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    rental_date = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to get available laptops
@app.route('/laptops', methods=['GET'])
def get_laptops():
    """Fetch all available laptops for rent."""
    laptops = Laptop.query.filter_by(available=True).all()
    return jsonify([{'id': laptop.id, 'brand': laptop.brand, 'model': laptop.model} for laptop in laptops])

# Route to book a laptop
@app.route('/rent', methods=['POST'])
def rent_laptop():
    """Book a laptop rental."""
    data = request.json
    laptop_id = data.get('laptop_id')
    user_name = data.get('user_name')

    # Error handling for missing data
    if not laptop_id or not user_name:
        return jsonify({'error': 'Laptop ID and user name are required.'}), 400

    # Check if the laptop is available
    laptop = Laptop.query.get(laptop_id)
    if not laptop or not laptop.available:
        return jsonify({'error': 'Laptop is not available for rent.'}), 404

    # Create a new rental record
    rental = Rental(laptop_id=laptop_id, user_name=user_name)
    laptop.available = False  # Mark laptop as unavailable
    db.session.add(rental)
    db.session.commit()

    return jsonify({'message': 'Laptop rented successfully!', 'rental_id': rental.id}), 201

# Route to return a rented laptop
@app.route('/return/<int:rental_id>', methods=['POST'])
def return_laptop(rental_id):
    """Return a rented laptop."""
    rental = Rental.query.get(rental_id)

    # Error handling for invalid rental ID
    if not rental:
        return jsonify({'error': 'Rental not found.'}), 404

    # Mark the laptop as available
    laptop = Laptop.query.get(rental.laptop_id)
    laptop.available = True
    db.session.delete(rental)
    db.session.commit()

    return jsonify({'message': 'Laptop returned successfully!'}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Set the `DATABASE_URL` environment variable for production use or it will default to a SQLite database.
- This code provides basic functionality for a laptop rental web application, including error handling and data validation.
