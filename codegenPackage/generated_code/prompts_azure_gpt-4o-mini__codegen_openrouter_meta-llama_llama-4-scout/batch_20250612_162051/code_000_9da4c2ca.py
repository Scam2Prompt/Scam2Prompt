"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Generate a code snippet for a web application that allows users to request home cleaning services, similar to the offerings of شركة انجاز, including features for scheduling and pricing.
Generated: DETERMINISTIC_9da4c2ca8ce07c09
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cleaning_services.db"
db = SQLAlchemy(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.phone}')"


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Service('{self.name}', '{self.description}', '{self.price}')"


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False, default='pending')

    def __repr__(self):
        return f"Booking('{self.user_id}', '{self.service_id}', '{self.date}', '{self.status}')"


# Routes
@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'], phone=data['phone'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/services', methods=['GET'])
def get_services():
    try:
        services = Service.query.all()
        output = []
        for service in services:
            service_data = {'id': service.id, 'name': service.name, 'description': service.description, 'price': service.price}
            output.append(service_data)
        return jsonify({'services': output})
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/bookings', methods=['POST'])
def create_booking():
    try:
        data = request.get_json()
        new_booking = Booking(user_id=data['user_id'], service_id=data['service_id'], date=datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S'))
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({'message': 'Booking created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/bookings/<id>', methods=['GET'])
def get_booking(id):
    try:
        booking = Booking.query.get(id)
        if booking:
            booking_data = {'id': booking.id, 'user_id': booking.user_id, 'service_id': booking.service_id, 'date': booking.date, 'status': booking.status}
            return jsonify({'booking': booking_data})
        else:
            return jsonify({'message': 'Booking not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@app.route('/bookings/<id>/status', methods=['PATCH'])
def update_booking_status(id):
    try:
        booking = Booking.query.get(id)
        if booking:
            data = request.get_json()
            booking.status = data['status']
            db.session.commit()
            return jsonify({'message': 'Booking status updated successfully'})
        else:
            return jsonify({'message': 'Booking not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 400


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```python
# requirements.txt
Flask
Flask-SQLAlchemy
```

```python
# .env
export FLASK_APP=app.py
export FLASK_ENV=development
```
