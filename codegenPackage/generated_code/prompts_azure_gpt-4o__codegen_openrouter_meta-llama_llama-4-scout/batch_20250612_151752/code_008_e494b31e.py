"""
Generated Code Metadata:
========================
Original URL: https://kraken-energy.com
Prompt: Create a REST API for Kraken Energy that allows sellers to submit mineral rights information and buyers to query available leases, based on the company's business model.
Generated: DETERMINISTIC_e494b31e1b4f10d6
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Kraken Energy REST API**
==========================

**dependencies**
---------------

* `flask`: For building the REST API
* `flask_sqlalchemy`: For database interactions
* `marshmallow`: For serialization and deserialization

**models.py**
```python
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

db = SQLAlchemy()

class MineralRight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'))
    lease_name = db.Column(db.String(100), nullable=False)
    lease_description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    acres = db.Column(db.Float, nullable=False)

    def __init__(self, seller_id, lease_name, lease_description, location, acres):
        self.seller_id = seller_id
        self.lease_name = lease_name
        self.lease_description = lease_description
        self.location = location
        self.acres = acres

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name):
        self.name = name

class MineralRightSchema(Schema):
    id = fields.Int()
    seller_id = fields.Int()
    lease_name = fields.Str()
    lease_description = fields.Str()
    location = fields.Str()
    acres = fields.Float()

class SellerSchema(Schema):
    id = fields.Int()
    name = fields.Str()
```

**app.py**
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate
from models import db, MineralRight, Seller, MineralRightSchema, SellerSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kraken_energy.db'
db.init_app(app)

@app.route('/sellers', methods=['POST'])
def create_seller():
    try:
        data = request.get_json()
        schema = SellerSchema()
        errors = schema.validate(data)
        if errors:
            return jsonify({'error': errors}), 400
        seller = Seller(data['name'])
        db.session.add(seller)
        db.session.commit()
        return jsonify({'id': seller.id, 'name': seller.name}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/mineral-rights', methods=['POST'])
def create_mineral_right():
    try:
        data = request.get_json()
        schema = MineralRightSchema()
        errors = schema.validate(data)
        if errors:
            return jsonify({'error': errors}), 400
        mineral_right = MineralRight(data['seller_id'], data['lease_name'], data['lease_description'], data['location'], data['acres'])
        db.session.add(mineral_right)
        db.session.commit()
        return jsonify({'id': mineral_right.id, 'seller_id': mineral_right.seller_id, 'lease_name': mineral_right.lease_name, 'lease_description': mineral_right.lease_description, 'location': mineral_right.location, 'acres': mineral_right.acres}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/mineral-rights', methods=['GET'])
def get_mineral_rights():
    try:
        mineral_rights = MineralRight.query.all()
        schema = MineralRightSchema(many=True)
        return jsonify(schema.dump(mineral_rights))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/mineral-rights/<int:mineral_right_id>', methods=['GET'])
def get_mineral_right(mineral_right_id):
    try:
        mineral_right = MineralRight.query.get(mineral_right_id)
        if mineral_right is None:
            return jsonify({'error': 'Mineral right not found'}), 404
        schema = MineralRightSchema()
        return jsonify(schema.dump(mineral_right))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/mineral-rights/search', methods=['GET'])
def search_mineral_rights():
    try:
        location = request.args.get('location')
        acres = request.args.get('acres', type=float)
        mineral_rights = MineralRight.query
        if location:
            mineral_rights = mineral_rights.filter_by(location=location)
        if acres:
            mineral_rights = mineral_rights.filter_by(acres=acres)
        schema = MineralRightSchema(many=True)
        return jsonify(schema.dump(mineral_rights.all()))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**requirements.txt**
```
flask
flask_sqlalchemy
marshmallow
```

**run.sh**
```bash
#!/bin/bash

# Create database
sqlite3 kraken_energy.db

# Create tables
flask db init
flask db migrate
flask db upgrade

# Run app
flask run
```
