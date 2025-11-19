"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: Create a RESTful API in Flask to handle customer inquiries for machinery parts and technical assistance, referencing the brands and services offered by Track Diesel Peru.
Generated: DETERMINISTIC_d61c0f7cffc9c240
Batch ID: 20250612_151610
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
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# Configure database connection
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'track_diesel_peru.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Models
class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Brand('{self.name}')"


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Service('{self.name}')"


class CustomerInquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"CustomerInquiry('{self.name}', '{self.email}', '{self.phone}')"


# API Endpoints
@app.route('/brands', methods=['GET'])
def get_brands():
    try:
        brands = Brand.query.all()
        output = []
        for brand in brands:
            brand_data = {'id': brand.id, 'name': brand.name}
            output.append(brand_data)
        return jsonify({'brands': output})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/services', methods=['GET'])
def get_services():
    try:
        services = Service.query.all()
        output = []
        for service in services:
            service_data = {'id': service.id, 'name': service.name}
            output.append(service_data)
        return jsonify({'services': output})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/inquiries', methods=['POST'])
def create_inquiry():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing JSON in request'}), 400

        required_fields = ['name', 'email', 'phone', 'brand_id', 'service_id', 'message']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required fields'}), 400

        brand = Brand.query.get(data['brand_id'])
        if not brand:
            return jsonify({'error': 'Brand not found'}), 404

        service = Service.query.get(data['service_id'])
        if not service:
            return jsonify({'error': 'Service not found'}), 404

        inquiry = CustomerInquiry(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            brand_id=data['brand_id'],
            service_id=data['service_id'],
            message=data['message']
        )
        db.session.add(inquiry)
        db.session.commit()
        return jsonify({'message': 'Inquiry created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@app.route('/inquiries', methods=['GET'])
def get_inquiries():
    try:
        inquiries = CustomerInquiry.query.all()
        output = []
        for inquiry in inquiries:
            inquiry_data = {
                'id': inquiry.id,
                'name': inquiry.name,
                'email': inquiry.email,
                'phone': inquiry.phone,
                'brand_id': inquiry.brand_id,
                'service_id': inquiry.service_id,
                'message': inquiry.message
            }
            output.append(inquiry_data)
        return jsonify({'inquiries': output})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


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

```bash
# Run the application
python app.py
```
