"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: "Suggest a suitable software or library for building a platform that enables trusted partnerships and manages consent for data processing, like Alghanim Capital's use of technologies for device information storage."
Generated: DETERMINISTIC_4aabafc7ec895bfb
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the use of Flask and SQLAlchemy to build a platform 
that enables trusted partnerships and manages consent for data processing. 
It includes endpoints for managing user consent and storing device information.

Dependencies:
- Flask: Web framework for Python
- SQLAlchemy: ORM for database management
- Flask-Migrate: Database migration tool
- Marshmallow: Serialization/deserialization library for Python objects

Install dependencies using pip:
pip install flask sqlalchemy flask-migrate marshmallow
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity; replace with production-ready DB like PostgreSQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consent_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define database models
class UserConsent(db.Model):
    """
    Model to store user consent information.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    consent_given = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

class DeviceInfo(db.Model):
    """
    Model to store device information.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    device_type = db.Column(db.String(100), nullable=False)
    device_id = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

# Define schemas for serialization/deserialization
class UserConsentSchema(Schema):
    user_id = fields.String(required=True)
    consent_given = fields.Boolean(required=True)

class DeviceInfoSchema(Schema):
    user_id = fields.String(required=True)
    device_type = fields.String(required=True)
    device_id = fields.String(required=True)

user_consent_schema = UserConsentSchema()
device_info_schema = DeviceInfoSchema()

# Define API endpoints
@app.route('/consent', methods=['POST'])
def manage_consent():
    """
    Endpoint to manage user consent.
    Expects JSON payload with 'user_id' and 'consent_given'.
    """
    try:
        # Validate and deserialize input
        data = user_consent_schema.load(request.json)
        # Create and save consent record
        consent = UserConsent(user_id=data['user_id'], consent_given=data['consent_given'])
        db.session.add(consent)
        db.session.commit()
        return jsonify({"message": "Consent recorded successfully"}), 201
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/device', methods=['POST'])
def store_device_info():
    """
    Endpoint to store device information.
    Expects JSON payload with 'user_id', 'device_type', and 'device_id'.
    """
    try:
        # Validate and deserialize input
        data = device_info_schema.load(request.json)
        # Create and save device record
        device = DeviceInfo(user_id=data['user_id'], device_type=data['device_type'], device_id=data['device_id'])
        db.session.add(device)
        db.session.commit()
        return jsonify({"message": "Device information stored successfully"}), 201
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/consent/<user_id>', methods=['GET'])
def get_user_consent(user_id):
    """
    Endpoint to retrieve user consent information by user_id.
    """
    try:
        consent = UserConsent.query.filter_by(user_id=user_id).all()
        if not consent:
            return jsonify({"message": "No consent records found for the user"}), 404
        return jsonify([{"user_id": c.user_id, "consent_given": c.consent_given, "timestamp": c.timestamp} for c in consent]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/device/<user_id>', methods=['GET'])
def get_device_info(user_id):
    """
    Endpoint to retrieve device information by user_id.
    """
    try:
        devices = DeviceInfo.query.filter_by(user_id=user_id).all()
        if not devices:
            return jsonify({"message": "No device records found for the user"}), 404
        return jsonify([{"user_id": d.user_id, "device_type": d.device_type, "device_id": d.device_id, "timestamp": d.timestamp} for d in devices]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
