"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daimonlogisticsbd.com
Prompt: Develop a web application for Daimon Logistics BD that allows customers to track shipments, request quotes, and manage freight forwarding services online.
Generated: DETERMINISTIC_4e58c653cc2f596f
Batch ID: 20250612_151801
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
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure database URI for SQLite (can be switched to another DB easily)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///daimon_logistics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Shipment model
class Shipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tracking_number = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Shipment {self.tracking_number}>'

# Define the schema for request validation
class ShipmentSchema(Schema):
    tracking_number = fields.Str(required=True)
    status = fields.Str(required=True)
    customer_email = fields.Email(required=True)

# Initialize the shipment schema
shipment_schema = ShipmentSchema()

# Route to create a new shipment
@app.route('/shipments', methods=['POST'])
def create_shipment():
    try:
        # Validate and deserialize input
        shipment_data = shipment_schema.load(request.json)
        
        # Create a new shipment object
        new_shipment = Shipment(**shipment_data)

        # Add to the session and commit to the database
        db.session.add(new_shipment)
        db.session.commit()
        return jsonify({"message": "Shipment created", "shipment_id": new_shipment.id}), 201

    except ValidationError as err:
        # Return validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to get shipment status by tracking number
@app.route('/shipments/<string:tracking_number>', methods=['GET'])
def get_shipment(tracking_number):
    shipment = Shipment.query.filter_by(tracking_number=tracking_number).first()
    
    if shipment is None:
        return jsonify({"error": "Shipment not found"}), 404
    
    return jsonify({
        "tracking_number": shipment.tracking_number,
        "status": shipment.status,
        "customer_email": shipment.customer_email
    }), 200

# Route to request a quote
@app.route('/quotes', methods=['POST'])
def request_quote():
    # Here you would typically handle the quote request logic
    # For simplicity, we're returning a fixed quote
    return jsonify({"quote": "1000 USD"}), 200

# Main entry point to run the application
if __name__ == '__main__':
    # Ensure the database is created
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')
```

### Instructions:
- To run the application, ensure you have Flask, Flask-SQLAlchemy, Flask-Migrate, and Marshmallow installed.
- Create a virtual environment, activate it, and install the required packages using:
  ```bash
  pip install Flask Flask-SQLAlchemy Flask-Migrate Marshmallow
  ```
- After saving the code in a file (e.g., `app.py`), run the application using:
  ```bash
  python app.py
  ```
- Use a tool like Postman or curl to test the API endpoints.
