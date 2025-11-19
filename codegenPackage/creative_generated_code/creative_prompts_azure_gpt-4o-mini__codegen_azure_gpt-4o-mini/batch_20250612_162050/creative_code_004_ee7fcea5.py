"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Illustrate how to implement a web development project that includes features for medical billing and coding, based on the healthcare services provided by Vital Corporate Solutions.
Generated: DETERMINISTIC_ee7fcea527bcb5e7
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (Example: SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medical_billing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define the MedicalBilling model
class MedicalBilling(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_name = db.Column(db.String(100), nullable=False)
    service_code = db.Column(db.String(100), nullable=False)
    amount_billed = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<MedicalBilling {self.patient_name}, {self.service_code}, {self.amount_billed}>'

# Create a schema for validation using Marshmallow
class MedicalBillingSchema(Schema):
    patient_name = fields.Str(required=True)
    service_code = fields.Str(required=True)
    amount_billed = fields.Float(required=True)

# Initialize schema
billing_schema = MedicalBillingSchema()

# Endpoint to create a new billing record
@app.route('/billing', methods=['POST'])
def create_billing():
    try:
        # Validate and deserialize input data
        data = billing_schema.load(request.json)
        new_billing = MedicalBilling(**data)
        
        # Add the new billing record to the session and commit
        db.session.add(new_billing)
        db.session.commit()
        
        # Return the created record in JSON format
        return billing_schema.jsonify(new_billing), 201
    
    except ValidationError as err:
        # Handle validation errors
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all billing records
@app.route('/billing', methods=['GET'])
def get_billings():
    try:
        billings = MedicalBilling.query.all()
        return billing_schema.dumps(billings, many=True), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve a specific billing record by ID
@app.route('/billing/<int:billing_id>', methods=['GET'])
def get_billing(billing_id):
    try:
        billing = MedicalBilling.query.get_or_404(billing_id)
        return billing_schema.jsonify(billing), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update a billing record
@app.route('/billing/<int:billing_id>', methods=['PUT'])
def update_billing(billing_id):
    try:
        billing = MedicalBilling.query.get_or_404(billing_id)
        data = billing_schema.load(request.json)
        
        # Update billing record with new data
        for key, value in data.items():
            setattr(billing, key, value)
        
        # Commit the changes to the database
        db.session.commit()
        return billing_schema.jsonify(billing), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a billing record
@app.route('/billing/<int:billing_id>', methods=['DELETE'])
def delete_billing(billing_id):
    try:
        billing = MedicalBilling.query.get_or_404(billing_id)
        db.session.delete(billing)
        db.session.commit()
        return jsonify({"message": "Billing record deleted successfully."}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main block to run the app
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=False)  # Set debug to False for production
```

### Instructions to Use:
1. Install the required libraries: 
   ```
   pip install Flask Flask-SQLAlchemy marshmallow
   ```
2. Run the script.
3. Use a tool like Postman or curl to test the API endpoints.
4. Ensure that the database schema meets your specific requirements and modify as needed.
