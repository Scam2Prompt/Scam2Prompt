"""
Generated Code Metadata:
========================
Original URL: https://skyline-ia.com
Prompt: Generate code for a web-based booking system that supports multi-country tour packages, including features for price guarantees and diverse destination management, inspired by Skyline International Agent's offerings.
Generated: DETERMINISTIC_ff226ac0f7af28c6
Batch ID: 20250612_153224
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booking_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the TourPackage model
class TourPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    price_guarantee = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<TourPackage {self.name}>'

# Initialize the database
with app.app_context():
    db.create_all()

# Route to create a new tour package
@app.route('/tour_packages', methods=['POST'])
def create_tour_package():
    try:
        data = request.get_json()
        new_package = TourPackage(
            name=data['name'],
            price=data['price'],
            destination=data['destination'],
            country=data['country'],
            price_guarantee=data.get('price_guarantee', False)
        )
        db.session.add(new_package)
        db.session.commit()
        return jsonify({'message': 'Tour package created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all tour packages
@app.route('/tour_packages', methods=['GET'])
def get_tour_packages():
    try:
        packages = TourPackage.query.all()
        return jsonify([{
            'id': pkg.id,
            'name': pkg.name,
            'price': pkg.price,
            'destination': pkg.destination,
            'country': pkg.country,
            'price_guarantee': pkg.price_guarantee
        } for pkg in packages]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update a tour package
@app.route('/tour_packages/<int:id>', methods=['PUT'])
def update_tour_package(id):
    try:
        data = request.get_json()
        package = TourPackage.query.get_or_404(id)
        package.name = data.get('name', package.name)
        package.price = data.get('price', package.price)
        package.destination = data.get('destination', package.destination)
        package.country = data.get('country', package.country)
        package.price_guarantee = data.get('price_guarantee', package.price_guarantee)
        
        db.session.commit()
        return jsonify({'message': 'Tour package updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete a tour package
@app.route('/tour_packages/<int:id>', methods=['DELETE'])
def delete_tour_package(id):
    try:
        package = TourPackage.query.get_or_404(id)
        db.session.delete(package)
        db.session.commit()
        return jsonify({'message': 'Tour package deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
