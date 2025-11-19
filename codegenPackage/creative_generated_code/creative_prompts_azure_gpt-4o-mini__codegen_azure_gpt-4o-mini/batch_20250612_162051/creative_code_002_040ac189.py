"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.caag.com.br
Prompt: Create an API recommendation for a legal consultation service that aligns with the ethical standards and client dedication highlighted on the CAAG website.
Generated: DETERMINISTIC_040ac18971345389
Batch ID: 20250612_162051
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
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/legal_consultation'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a model for Legal Consultation Requests
class LegalConsultationRequest(db.Model):
    __tablename__ = 'consultation_requests'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<ConsultationRequest {self.id}>'

# Schema for input validation
class ConsultationRequestSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    message = fields.Str(required=True)

# Initialize the schema
request_schema = ConsultationRequestSchema()

# Endpoint for submitting a consultation request
@app.route('/api/consultation', methods=['POST'])
def submit_consultation():
    try:
        # Validate input data
        data = request.get_json()
        validated_data = request_schema.load(data)

        # Create a new consultation request
        consultation_request = LegalConsultationRequest(
            name=validated_data['name'],
            email=validated_data['email'],
            message=validated_data['message']
        )
        
        # Save to the database
        db.session.add(consultation_request)
        db.session.commit()

        logger.info(f'New consultation request created: {consultation_request.id}')
        return jsonify({"message": "Consultation request submitted successfully."}), 201

    except ValidationError as ve:
        # Handle validation errors
        logger.error(f'Validation error: {ve.messages}')
        return jsonify({"error": "Invalid input.", "details": ve.messages}), 400

    except Exception as e:
        # Handle unexpected errors
        logger.exception('An error occurred while processing the consultation request.')
        return jsonify({"error": "An error occurred. Please try again later."}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Run the app in production mode
```
