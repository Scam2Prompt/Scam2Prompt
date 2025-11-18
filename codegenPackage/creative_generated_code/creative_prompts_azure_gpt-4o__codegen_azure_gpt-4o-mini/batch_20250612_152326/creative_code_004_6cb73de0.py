"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.events
Prompt: Write code using Flask or Django to create a backend system for managing vendor applications for a festival, including booth assignments and application statuses.
Generated: DETERMINISTIC_6cb73de013a9a7a7
Batch ID: 20250612_152326
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///festival_vendors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration library
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Vendor model for the database
class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    booth_number = db.Column(db.String(10), nullable=False, unique=True)
    application_status = db.Column(db.String(20), default='Pending')

# Vendor schema for validation and serialization
class VendorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    booth_number = fields.Str(required=True)
    application_status = fields.Str(default='Pending')

# Initialize schemas
vendor_schema = VendorSchema()
vendors_schema = VendorSchema(many=True)

# Endpoint to create a new vendor application
@app.route('/vendors', methods=['POST'])
def create_vendor():
    try:
        # Validate and deserialize input data
        data = vendor_schema.load(request.json)
        new_vendor = Vendor(**data)
        db.session.add(new_vendor)
        db.session.commit()
        return vendor_schema.jsonify(new_vendor), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all vendor applications
@app.route('/vendors', methods=['GET'])
def get_vendors():
    try:
        vendors = Vendor.query.all()
        return vendors_schema.jsonify(vendors), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update vendor application status
@app.route('/vendors/<int:id>', methods=['PUT'])
def update_vendor_status(id):
    try:
        vendor = Vendor.query.get_or_404(id)
        vendor.application_status = request.json.get('application_status', vendor.application_status)
        db.session.commit()
        return vendor_schema.jsonify(vendor), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a vendor application
@app.route('/vendors/<int:id>', methods=['DELETE'])
def delete_vendor(id):
    try:
        vendor = Vendor.query.get_or_404(id)
        db.session.delete(vendor)
        db.session.commit()
        return jsonify({"message": "Vendor deleted successfully"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
Make sure to install the required packages:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate marshmallow
```

### Database Initialization
You may need to initialize the database before running the application:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
``` 

### Running the Application
To run the application, execute the following command:
```bash
python app.py
``` 

This will start the Flask server and you can use tools like Postman or curl to interact with the endpoints.
