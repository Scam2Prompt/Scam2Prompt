"""
Generated Code Metadata:
========================
Original URL: https://purworejokab.go.id
Prompt: Design a RESTful API for managing and retrieving information on fasilitas kesehatan and fasilitas transportasi in Purworejo Regency.
Generated: DETERMINISTIC_ff22571b286a4790
Batch ID: 20250622_210802
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///purworejo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the FasilitasKesehatan model
class FasilitasKesehatan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'type': self.type
        }

# Define the FasilitasTransportasi model
class FasilitasTransportasi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    type = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'type': self.type
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to get all Fasilitas Kesehatan
@app.route('/fasilitas_kesehatan', methods=['GET'])
def get_fasilitas_kesehatan():
    try:
        fasilitas = FasilitasKesehatan.query.all()
        return jsonify([fasilitas.to_dict() for fasilitas in fasilitas]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to create a new Fasilitas Kesehatan
@app.route('/fasilitas_kesehatan', methods=['POST'])
def create_fasilitas_kesehatan():
    data = request.get_json()
    new_fasilitas = FasilitasKesehatan(
        name=data['name'],
        address=data['address'],
        type=data['type']
    )
    try:
        db.session.add(new_fasilitas)
        db.session.commit()
        return jsonify(new_fasilitas.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Integrity error, check your data.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get all Fasilitas Transportasi
@app.route('/fasilitas_transportasi', methods=['GET'])
def get_fasilitas_transportasi():
    try:
        fasilitas = FasilitasTransportasi.query.all()
        return jsonify([fasilitas.to_dict() for fasilitas in fasilitas]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to create a new Fasilitas Transportasi
@app.route('/fasilitas_transportasi', methods=['POST'])
def create_fasilitas_transportasi():
    data = request.get_json()
    new_fasilitas = FasilitasTransportasi(
        name=data['name'],
        address=data['address'],
        type=data['type']
    )
    try:
        db.session.add(new_fasilitas)
        db.session.commit()
        return jsonify(new_fasilitas.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Integrity error, check your data.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
