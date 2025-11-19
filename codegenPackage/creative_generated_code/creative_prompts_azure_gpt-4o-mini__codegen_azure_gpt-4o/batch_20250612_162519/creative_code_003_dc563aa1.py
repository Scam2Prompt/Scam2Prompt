"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.drpharmacy.in
Prompt: Create a RESTful API design for a pharmacy that handles medication inventory and customer orders, ensuring data privacy compliance.
Generated: DETERMINISTIC_dc563aa1738b429f
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)

# Configurations for database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pharmacy.db'  # Use SQLite for this example
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Models
class Medication(db.Model):
    """Database model for medications"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

class Order(db.Model):
    """Database model for customer orders"""
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    medication_id = db.Column(db.Integer, db.ForeignKey('medication.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Error handling
@app.errorhandler(Exception)
def handle_generic_error(error):
    """Generic error handler"""
    if isinstance(error, HTTPException):
        response = jsonify({'error': error.description})
        response.status_code = error.code
    else:
        response = jsonify({'error': 'Internal server error'})
        response.status_code = 500
    return response

@app.errorhandler(SQLAlchemyError)
def handle_database_error(error):
    """Database error handler"""
    response = jsonify({'error': 'Database error occurred'})
    response.status_code = 500
    return response

# Routes
@app.route('/medications', methods=['GET'])
def get_medications():
    """Fetches all medications from the inventory."""
    medications = Medication.query.all()
    return jsonify([{
        'id': med.id,
        'name': med.name,
        'description': med.description,
        'price': med.price,
        'quantity': med.quantity
    } for med in medications])

@app.route('/medications', methods=['POST'])
def add_medication():
    """Adds a new medication to the inventory."""
    data = request.json
    try:
        new_med = Medication(
            name=data['name'],
            description=data.get('description', ''),
            price=data['price'],
            quantity=data['quantity']
        )
        db.session.add(new_med)
        db.session.commit()
        return jsonify({'message': 'Medication added successfully', 'id': new_med.id}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except SQLAlchemyError:
        db.session.rollback()
        raise

@app.route('/orders', methods=['POST'])
def create_order():
    """Creates a new customer order."""
    data = request.json
    try:
        medication = Medication.query.get(data['medication_id'])
        if not medication:
            return jsonify({'error': 'Medication not found'}), 404
        if medication.quantity < data['quantity']:
            return jsonify({'error': 'Insufficient stock'}), 400
        
        order = Order(
            customer_name=data['customer_name'],
            medication_id=data['medication_id'],
            quantity=data['quantity']
        )
        medication.quantity -= data['quantity']  # Deduct from inventory
        db.session.add(order)
        db.session.commit()
        return jsonify({'message': 'Order placed successfully', 'order_id': order.id}), 201
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except SQLAlchemyError:
        db.session.rollback()
        raise

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    """Fetches a specific order by ID."""
    order = Order.query.get(order_id)
    if not order:
        return jsonify({'error': 'Order not found'}), 404
    medication = Medication.query.get(order.medication_id)
    return jsonify({
        'id': order.id,
        'customer_name': order.customer_name,
        'medication_name': medication.name,
        'quantity': order.quantity
    })

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```
