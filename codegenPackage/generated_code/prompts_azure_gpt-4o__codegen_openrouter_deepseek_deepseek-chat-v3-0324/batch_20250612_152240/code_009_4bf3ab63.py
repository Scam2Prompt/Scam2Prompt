"""
Generated Code Metadata:
========================
Original URL: https://kocaeli.com
Prompt: Provide a solution using Flask or Django to build a backend for a website similar to Kocaeli.COM, with endpoints for retrieving data about "Devlet Daireleri" and "Spor Kulüpleri."
Generated: DETERMINISTIC_4bf3ab63185efeb6
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py - Flask backend for Kocaeli.COM-like website

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Database configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'kocaeli.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class DevletDairesi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    website = db.Column(db.String(100))
    working_hours = db.Column(db.String(100))

    def __init__(self, name, address, phone, website, working_hours):
        self.name = name
        self.address = address
        self.phone = phone
        self.website = website
        self.working_hours = working_hours

class SporKulubu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sport_type = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    website = db.Column(db.String(100))
    established_year = db.Column(db.Integer)

    def __init__(self, name, sport_type, address, phone, website, established_year):
        self.name = name
        self.sport_type = sport_type
        self.address = address
        self.phone = phone
        self.website = website
        self.established_year = established_year

# Schemas
class DevletDairesiSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'phone', 'website', 'working_hours')

class SporKulubuSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'sport_type', 'address', 'phone', 'website', 'established_year')

devlet_dairesi_schema = DevletDairesiSchema()
devlet_daireleri_schema = DevletDairesiSchema(many=True)

spor_kulubu_schema = SporKulubuSchema()
spor_kulupleri_schema = SporKulubuSchema(many=True)

# Routes
@app.route('/api/devlet-daireleri', methods=['GET'])
def get_devlet_daireleri():
    try:
        all_daireler = DevletDairesi.query.all()
        result = devlet_daireleri_schema.dump(all_daireler)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/devlet-daireleri/<id>', methods=['GET'])
def get_devlet_dairesi(id):
    try:
        daire = DevletDairesi.query.get(id)
        if not daire:
            return jsonify({'error': 'Devlet dairesi bulunamadı'}), 404
        return devlet_dairesi_schema.jsonify(daire)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/spor-kulupleri', methods=['GET'])
def get_spor_kulupleri():
    try:
        all_kulupler = SporKulubu.query.all()
        result = spor_kulupleri_schema.dump(all_kulupler)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/spor-kulupleri/<id>', methods=['GET'])
def get_spor_kulubu(id):
    try:
        kulup = SporKulubu.query.get(id)
        if not kulup:
            return jsonify({'error': 'Spor kulübü bulunamadı'}), 404
        return spor_kulubu_schema.jsonify(kulup)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/devlet-daireleri', methods=['POST'])
def add_devlet_dairesi():
    try:
        name = request.json['name']
        address = request.json['address']
        phone = request.json['phone']
        website = request.json.get('website', '')
        working_hours = request.json.get('working_hours', '')

        new_daire = DevletDairesi(name, address, phone, website, working_hours)
        db.session.add(new_daire)
        db.session.commit()
        return devlet_dairesi_schema.jsonify(new_daire), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/spor-kulupleri', methods=['POST'])
def add_spor_kulubu():
    try:
        name = request.json['name']
        sport_type = request.json['sport_type']
        address = request.json['address']
        phone = request.json['phone']
        website = request.json.get('website', '')
        established_year = request.json.get('established_year')

        new_kulup = SporKulubu(name, sport_type, address, phone, website, established_year)
        db.session.add(new_kulup)
        db.session.commit()
        return spor_kulubu_schema.jsonify(new_kulup), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
```
