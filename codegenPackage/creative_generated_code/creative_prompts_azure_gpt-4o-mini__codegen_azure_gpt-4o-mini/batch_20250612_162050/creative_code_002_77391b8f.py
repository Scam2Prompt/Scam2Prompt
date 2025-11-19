"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://southernbrass.com
Prompt: Create a REST API endpoint for a mobile application that allows builders to select and order door hardware and bath accessories.
Generated: DETERMINISTIC_77391b8f6489a4d1
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hardware.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the DoorHardware model
class DoorHardware(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Define the BathAccessory model
class BathAccessory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Create a schema for validating incoming data
class DoorHardwareSchema(Schema):
    name = fields.String(required=True)
    price = fields.Float(required=True)

class BathAccessorySchema(Schema):
    name = fields.String(required=True)
    price = fields.Float(required=True)

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to order door hardware
@app.route('/api/door-hardware', methods=['POST'])
def order_door_hardware():
    schema = DoorHardwareSchema()
    try:
        # Validate and deserialize input data
        data = schema.load(request.json)
        new_hardware = DoorHardware(**data)
        db.session.add(new_hardware)
        db.session.commit()
        return jsonify({"message": "Door hardware ordered successfully!", "id": new_hardware.id}), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to order bath accessories
@app.route('/api/bath-accessories', methods=['POST'])
def order_bath_accessory():
    schema = BathAccessorySchema()
    try:
        # Validate and deserialize input data
        data = schema.load(request.json)
        new_accessory = BathAccessory(**data)
        db.session.add(new_accessory)
        db.session.commit()
        return jsonify({"message": "Bath accessory ordered successfully!", "id": new_accessory.id}), 201
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
