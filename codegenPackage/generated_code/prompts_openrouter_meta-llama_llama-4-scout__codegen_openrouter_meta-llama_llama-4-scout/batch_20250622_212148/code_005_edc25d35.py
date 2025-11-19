"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Design a RESTful API for a photography studio like Officine dell'Immagine to manage bookings, photo shoots, and client information.
Generated: DETERMINISTIC_edc25d353431a0f5
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Photography Studio API**
=========================

### Dependencies

* Python 3.9+
* Flask 2.0+
* Flask-SQLAlchemy 2.5+
* Marshmallow 3.10+

### Models

```python
# models.py
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

db = SQLAlchemy()

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=False)

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class ClientSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    client = db.relationship('Client', backref=db.backref('bookings', lazy=True))
    date = db.Column(db.DateTime, nullable=False)
    photo_shoot_id = db.Column(db.Integer, db.ForeignKey('photo_shoot.id'), nullable=False)
    photo_shoot = db.relationship('PhotoShoot', backref=db.backref('bookings', lazy=True))

    def __init__(self, client_id, date, photo_shoot_id):
        self.client_id = client_id
        self.date = date
        self.photo_shoot_id = photo_shoot_id

class BookingSchema(Schema):
    id = fields.Int()
    client_id = fields.Int(required=True)
    date = fields.DateTime(required=True)
    photo_shoot_id = fields.Int(required=True)

class PhotoShoot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __init__(self, name, description):
        self.name = name
        self.description = description

class PhotoShootSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    description = fields.Str(required=True)
```

### API Endpoints

```python
# app.py
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from models import db, Client, ClientSchema, Booking, BookingSchema, PhotoShoot, PhotoShootSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photography_studio.db'
db.init_app(app)
ma = Marshmallow(app)

client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)

booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)

photo_shoot_schema = PhotoShootSchema()
photo_shoots_schema = PhotoShootSchema(many=True)

# Client Endpoints

@app.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return jsonify(clients_schema.dump(clients))

@app.route('/clients', methods=['POST'])
def create_client():
    try:
        data = request.get_json()
        new_client = Client(data['name'], data['email'], data['phone'])
        db.session.add(new_client)
        db.session.commit()
        return jsonify(client_schema.dump(new_client)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/clients/<id>', methods=['GET'])
def get_client(id):
    client = Client.query.get(id)
    if client:
        return jsonify(client_schema.dump(client))
    return jsonify({'error': 'Client not found'}), 404

@app.route('/clients/<id>', methods=['PUT'])
def update_client(id):
    try:
        client = Client.query.get(id)
        if client:
            data = request.get_json()
            client.name = data['name']
            client.email = data['email']
            client.phone = data['phone']
            db.session.commit()
            return jsonify(client_schema.dump(client))
        return jsonify({'error': 'Client not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/clients/<id>', methods=['DELETE'])
def delete_client(id):
    client = Client.query.get(id)
    if client:
        db.session.delete(client)
        db.session.commit()
        return jsonify({'message': 'Client deleted'})
    return jsonify({'error': 'Client not found'}), 404

# Booking Endpoints

@app.route('/bookings', methods=['GET'])
def get_bookings():
    bookings = Booking.query.all()
    return jsonify(bookings_schema.dump(bookings))

@app.route('/bookings', methods=['POST'])
def create_booking():
    try:
        data = request.get_json()
        new_booking = Booking(data['client_id'], data['date'], data['photo_shoot_id'])
        db.session.add(new_booking)
        db.session.commit()
        return jsonify(booking_schema.dump(new_booking)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/bookings/<id>', methods=['GET'])
def get_booking(id):
    booking = Booking.query.get(id)
    if booking:
        return jsonify(booking_schema.dump(booking))
    return jsonify({'error': 'Booking not found'}), 404

@app.route('/bookings/<id>', methods=['PUT'])
def update_booking(id):
    try:
        booking = Booking.query.get(id)
        if booking:
            data = request.get_json()
            booking.client_id = data['client_id']
            booking.date = data['date']
            booking.photo_shoot_id = data['photo_shoot_id']
            db.session.commit()
            return jsonify(booking_schema.dump(booking))
        return jsonify({'error': 'Booking not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/bookings/<id>', methods=['DELETE'])
def delete_booking(id):
    booking = Booking.query.get(id)
    if booking:
        db.session.delete(booking)
        db.session.commit()
        return jsonify({'message': 'Booking deleted'})
    return jsonify({'error': 'Booking not found'}), 404

# Photo Shoot Endpoints

@app.route('/photo-shoots', methods=['GET'])
def get_photo_shoots():
    photo_shoots = PhotoShoot.query.all()
    return jsonify(photo_shoots_schema.dump(photo_shoots))

@app.route('/photo-shoots', methods=['POST'])
def create_photo_shoot():
    try:
        data = request.get_json()
        new_photo_shoot = PhotoShoot(data['name'], data['description'])
        db.session.add(new_photo_shoot)
        db.session.commit()
        return jsonify(photo_shoot_schema.dump(new_photo_shoot)), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/photo-shoots/<id>', methods=['GET'])
def get_photo_shoot(id):
    photo_shoot = PhotoShoot.query.get(id)
    if photo_shoot:
        return jsonify(photo_shoot_schema.dump(photo_shoot))
    return jsonify({'error': 'Photo shoot not found'}), 404

@app.route('/photo-shoots/<id>', methods=['PUT'])
def update_photo_shoot(id):
    try:
        photo_shoot = PhotoShoot.query.get(id)
        if photo_shoot:
            data = request.get_json()
            photo_shoot.name = data['name']
            photo_shoot.description = data['description']
            db.session.commit()
            return jsonify(photo_shoot_schema.dump(photo_shoot))
        return jsonify({'error': 'Photo shoot not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/photo-shoots/<id>', methods=['DELETE'])
def delete_photo_shoot(id):
    photo_shoot = PhotoShoot.query.get(id)
    if photo_shoot:
        db.session.delete(photo_shoot)
        db.session.commit()
        return jsonify({'message': 'Photo shoot deleted'})
    return jsonify({'error': 'Photo shoot not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

### Running the Application

1. Install dependencies: `pip install flask flask-sqlalchemy marshmallow`
2. Create database: `flask db init` and `flask db migrate`
3. Run application: `python app.py`

### API Documentation

* **GET /clients**: Retrieve all clients
* **POST /clients**: Create a new client
* **GET /clients/<id>**: Retrieve a client by ID
* **PUT /clients/<id>**: Update a client
* **DELETE /clients/<id>**: Delete a client
* **GET /bookings**: Retrieve all bookings
* **POST /bookings**: Create a new booking
* **GET /bookings/<id>**: Retrieve a booking by ID
* **PUT /bookings/<id>**: Update a booking
* **DELETE /bookings/<id>**: Delete a booking
* **GET /photo-shoots**: Retrieve all photo shoots
* **POST /photo-shoots**: Create a new photo shoot
* **GET /photo-shoots/<id>**: Retrieve a photo shoot
