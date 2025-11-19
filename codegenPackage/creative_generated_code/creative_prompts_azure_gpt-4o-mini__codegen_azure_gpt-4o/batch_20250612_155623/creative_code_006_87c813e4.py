"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://legatoltd.net
Prompt: What libraries can I use to build a web application that helps victims of online fraud report their cases, taking cues from The Legato's approach?
Generated: DETERMINISTIC_87c813e41ccf3832
Batch ID: 20250612_155623
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
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fraud_reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the database model for fraud reports
class FraudReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    description = db.Column(db.String(500), nullable=False)

# Define a schema using Marshmallow for validation
class FraudReportSchema(Schema):
    name = fields.String(required=True, validate=lambda x: len(x) > 0)
    email = fields.Email(required=True)
    phone = fields.String(validate=lambda x: len(x) <= 15)
    description = fields.String(required=True, validate=lambda x: len(x) > 0)

# Initialize the schema
fraud_report_schema = FraudReportSchema()

@app.route('/report', methods=['POST'])
def report_fraud():
    """
    Endpoint to submit a new fraud report.
    Accepts JSON payload with name, email, phone (optional), and description.
    """
    try:
        # Parse and validate the incoming JSON data
        data = request.get_json()
        # Validate data using schema
        validated_data = fraud_report_schema.load(data)
        
        # Create a new fraud report entry
        fraud_report = FraudReport(
            name=validated_data['name'],
            email=validated_data['email'],
            phone=validated_data.get('phone'),
            description=validated_data['description']
        )
        
        # Add the report to the database
        db.session.add(fraud_report)
        db.session.commit()
        
        # Return success response
        logging.info(f"Fraud report successfully created: {fraud_report.id}")
        return jsonify({"message": "Fraud report submitted successfully!", "id": fraud_report.id}), 201
    
    except ValidationError as err:
        # Handle validation errors
        logging.error(f"Validation error: {err.messages}")
        return jsonify({"errors": err.messages}), 400
    
    except Exception as e:
        # Handle general errors
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500

@app.route('/reports', methods=['GET'])
def get_reports():
    """
    Endpoint to fetch all fraud reports.
    Returns a list of all submitted fraud reports.
    """
    try:
        # Query all fraud reports from the database
        reports = FraudReport.query.all()
        # Serialize reports
        reports_data = [fraud_report_schema.dump(report) for report in reports]
        
        # Return the list of reports
        logging.info(f"Fetched {len(reports)} reports.")
        return jsonify(reports_data), 200

    except Exception as e:
        # Handle general errors
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500

# Run the application
if __name__ == '__main__':
    # Ensure the database is created
    with app.app_context():
        db.create_all()
    
    # Start the Flask server
    app.run(debug=True)
```

### Key Libraries Used:
1. **Flask**: Lightweight web framework for building APIs and web applications.
2. **SQLAlchemy**: ORM for interacting with the database.
3. **Marshmallow**: Library for data validation and serialization.
4. **Logging**: Standard Python library for logging application events/errors.
