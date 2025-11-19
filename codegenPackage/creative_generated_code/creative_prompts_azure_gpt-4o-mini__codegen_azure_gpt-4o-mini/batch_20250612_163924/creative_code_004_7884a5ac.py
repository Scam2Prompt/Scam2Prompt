"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apps-eigenlayer.com
Prompt: How can I implement a quality assurance system in a manufacturing API that tracks compliance with ISO certifications, particularly for precision metal stamping services?
Generated: DETERMINISTIC_7884a5acd27642f1
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///manufacturing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Database model for ISO Certification compliance
class ISOCertification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    certification_name = db.Column(db.String(100), nullable=False)
    compliance_status = db.Column(db.Boolean, default=True)
    date_verified = db.Column(db.Date, nullable=False)

# Schema for validating input data
class ISOCertificationSchema(Schema):
    certification_name = fields.Str(required=True)
    compliance_status = fields.Bool(required=True)
    date_verified = fields.Date(required=True)

# Initialize the schema
iso_certification_schema = ISOCertificationSchema()
iso_certifications_schema = ISOCertificationSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to add a new ISO Certification record
@app.route('/api/certification', methods=['POST'])
def add_certification():
    try:
        # Validate and deserialize the input data
        data = iso_certification_schema.load(request.json)
        
        # Create a new certification instance
        new_certification = ISOCertification(
            certification_name=data['certification_name'],
            compliance_status=data['compliance_status'],
            date_verified=data['date_verified']
        )
        
        # Add to session and commit
        db.session.add(new_certification)
        db.session.commit()
        
        return jsonify(iso_certification_schema.dump(new_certification)), 201

    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error adding certification: {e}")
        return jsonify({"error": "An error occurred while adding certification."}), 500

# API endpoint to get all ISO Certifications
@app.route('/api/certifications', methods=['GET'])
def get_certifications():
    try:
        certifications = ISOCertification.query.all()
        return jsonify(iso_certifications_schema.dump(certifications)), 200
    except Exception as e:
        logging.error(f"Error retrieving certifications: {e}")
        return jsonify({"error": "An error occurred while retrieving certifications."}), 500

# API endpoint to update an existing ISO Certification
@app.route('/api/certification/<int:certification_id>', methods=['PUT'])
def update_certification(certification_id):
    try:
        certification = ISOCertification.query.get_or_404(certification_id)
        data = iso_certification_schema.load(request.json)

        # Update certification details
        certification.certification_name = data['certification_name']
        certification.compliance_status = data['compliance_status']
        certification.date_verified = data['date_verified']
        
        db.session.commit()
        
        return jsonify(iso_certification_schema.dump(certification)), 200

    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error updating certification: {e}")
        return jsonify({"error": "An error occurred while updating certification."}), 500

# API endpoint to delete an ISO Certification
@app.route('/api/certification/<int:certification_id>', methods=['DELETE'])
def delete_certification(certification_id):
    try:
        certification = ISOCertification.query.get_or_404(certification_id)
        db.session.delete(certification)
        db.session.commit()
        return jsonify({"message": "Certification deleted successfully."}), 204
    except Exception as e:
        logging.error(f"Error deleting certification: {e}")
        return jsonify({"error": "An error occurred while deleting certification."}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
