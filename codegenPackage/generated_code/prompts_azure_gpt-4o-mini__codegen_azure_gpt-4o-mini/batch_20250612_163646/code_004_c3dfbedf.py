"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: Create a RESTful API design for a logistics company that includes features like cargo safety management and tracking, based on ENL Consortium's operational practices.
Generated: DETERMINISTIC_c3dfbedf262343d0
Batch ID: 20250612_163646
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
from flask_marshmallow import Marshmallow
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logistics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Cargo model
class Cargo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    tracking_number = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, description, status, tracking_number):
        self.description = description
        self.status = status
        self.tracking_number = tracking_number

# Cargo schema
class CargoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cargo

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint to create a new cargo entry
@app.route('/cargo', methods=['POST'])
def add_cargo():
    try:
        data = request.get_json()
        new_cargo = Cargo(
            description=data['description'],
            status=data['status'],
            tracking_number=data['tracking_number']
        )
        db.session.add(new_cargo)
        db.session.commit()
        return CargoSchema().jsonify(new_cargo), 201
    except Exception as e:
        logging.error(f"Error adding cargo: {e}")
        return jsonify({"error": "Failed to add cargo"}), 400

# Endpoint to get all cargo entries
@app.route('/cargo', methods=['GET'])
def get_cargo():
    try:
        all_cargo = Cargo.query.all()
        return CargoSchema(many=True).jsonify(all_cargo), 200
    except Exception as e:
        logging.error(f"Error fetching cargo: {e}")
        return jsonify({"error": "Failed to fetch cargo"}), 500

# Endpoint to get a specific cargo entry by tracking number
@app.route('/cargo/<tracking_number>', methods=['GET'])
def get_cargo_by_tracking(tracking_number):
    try:
        cargo = Cargo.query.filter_by(tracking_number=tracking_number).first()
        if cargo is None:
            return jsonify({"error": "Cargo not found"}), 404
        return CargoSchema().jsonify(cargo), 200
    except Exception as e:
        logging.error(f"Error fetching cargo by tracking number: {e}")
        return jsonify({"error": "Failed to fetch cargo"}), 500

# Endpoint to update cargo status
@app.route('/cargo/<tracking_number>', methods=['PUT'])
def update_cargo(tracking_number):
    try:
        data = request.get_json()
        cargo = Cargo.query.filter_by(tracking_number=tracking_number).first()
        if cargo is None:
            return jsonify({"error": "Cargo not found"}), 404
        
        cargo.status = data.get('status', cargo.status)
        db.session.commit()
        return CargoSchema().jsonify(cargo), 200
    except Exception as e:
        logging.error(f"Error updating cargo: {e}")
        return jsonify({"error": "Failed to update cargo"}), 400

# Endpoint to delete a cargo entry
@app.route('/cargo/<tracking_number>', methods=['DELETE'])
def delete_cargo(tracking_number):
    try:
        cargo = Cargo.query.filter_by(tracking_number=tracking_number).first()
        if cargo is None:
            return jsonify({"error": "Cargo not found"}), 404
        
        db.session.delete(cargo)
        db.session.commit()
        return jsonify({"message": "Cargo deleted successfully"}), 200
    except Exception as e:
        logging.error(f"Error deleting cargo: {e}")
        return jsonify({"error": "Failed to delete cargo"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
