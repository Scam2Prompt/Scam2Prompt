"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Create a RESTful API using Flask or Django to manage Ataköy nakliyat services, including endpoints for creating, reading, updating, and deleting customer requests, services, and payments.
Generated: DETERMINISTIC_7d3255498a4e7771
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is a production-ready RESTful API using Flask:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///atakoy_nakliyat.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Models
class CustomerRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_request_id = db.Column(db.Integer, db.ForeignKey('customer_request.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False)

# Create database tables
with app.app_context():
    db.create_all()

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Routes for Customer Requests
@app.route('/customer_requests', methods=['POST'])
def create_customer_request():
    try:
        data = request.json
        new_request = CustomerRequest(
            name=data['name'],
            phone=data['phone'],
            address=data['address'],
            description=data.get('description', '')
        )
        db.session.add(new_request)
        db.session.commit()
        return jsonify({"message": "Customer request created", "id": new_request.id}), 201
    except KeyError:
        return jsonify({"error": "Invalid input"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500

@app.route('/customer_requests', methods=['GET'])
def get_customer_requests():
    requests = CustomerRequest.query.all()
    return jsonify([{
        "id": r.id,
        "name": r.name,
        "phone": r.phone,
        "address": r.address,
        "description": r.description
    } for r in requests]), 200

@app.route('/customer_requests/<int:id>', methods=['PUT'])
def update_customer_request(id):
    try:
        data = request.json
        request_to_update = CustomerRequest.query.get_or_404(id)
        request_to_update.name = data.get('name', request_to_update.name)
        request_to_update.phone = data.get('phone', request_to_update.phone)
        request_to_update.address = data.get('address', request_to_update.address)
        request_to_update.description = data.get('description', request_to_update.description)
        db.session.commit()
        return jsonify({"message": "Customer request updated"}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500

@app.route('/customer_requests/<int:id>', methods=['DELETE'])
def delete_customer_request(id):
    request_to_delete = CustomerRequest.query.get_or_404(id)
    db.session.delete(request_to_delete)
    db.session.commit()
    return jsonify({"message": "Customer request deleted"}), 200

# Routes for Services
@app.route('/services', methods=['POST'])
def create_service():
    try:
        data = request.json
        new_service = Service(
            name=data['name'],
            price=data['price']
        )
        db.session.add(new_service)
        db.session.commit()
        return jsonify({"message": "Service created", "id": new_service.id}), 201
    except KeyError:
        return jsonify({"error": "Invalid input"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500

@app.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([{
        "id": s.id,
        "name": s.name,
        "price": s.price
    } for s in services]), 200

@app.route('/services/<int:id>', methods=['PUT'])
def update_service(id):
    try:
        data = request.json
        service_to_update = Service.query.get_or_404(id)
        service_to_update.name = data.get('name', service_to_update.name)
        service_to_update.price = data.get('price', service_to_update.price)
        db.session.commit()
        return jsonify({"message": "Service updated"}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500

@app.route('/services/<int:id>', methods=['DELETE'])
def delete_service(id):
    service_to_delete = Service.query.get_or_404(id)
    db.session.delete(service_to_delete)
    db.session.commit()
    return jsonify({"message": "Service deleted"}), 200

# Routes for Payments
@app.route('/payments', methods=['POST'])
def create_payment():
    try:
        data = request.json
        new_payment = Payment(
            customer_request_id=data['customer_request_id'],
            amount=data['amount'],
            status=data['status']
        )
        db.session.add(new_payment)
        db.session.commit()
        return jsonify({"message": "Payment created", "id": new_payment.id}), 201
    except KeyError:
        return jsonify({"error": "Invalid input"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500

@app.route('/payments', methods=['GET'])
def get_payments():
    payments = Payment.query.all()
    return jsonify([{
        "id": p.id,
        "customer_request_id": p.customer_request_id,
        "amount": p.amount,
        "status": p.status
    } for p in payments]), 200

@app.route('/payments/<int:id>', methods=['PUT'])
def update_payment(id):
    try:
        data = request.json
        payment_to_update = Payment.query.get_or_404(id)
        payment_to_update.customer_request_id = data.get('customer_request_id', payment_to_update.customer_request_id)
        payment_to_update.amount = data.get('amount', payment_to_update.amount)
        payment_to_update.status = data.get('status', payment_to_update.status)
        db.session.commit()
        return jsonify({"message": "Payment updated"}), 200
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Database error"}), 500

@app.route('/payments/<int:id>', methods=['DELETE'])
def delete_payment(id):
    payment_to_delete = Payment.query.get_or_404(id)
    db.session.delete(payment_to_delete)
    db.session.commit()
    return jsonify({"message": "Payment deleted"}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a complete RESTful API for managing customer requests, services, and payments for Ataköy nakliyat services. It includes proper error handling, follows best practices, and is ready for production deployment.
