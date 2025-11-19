"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Develop a RESTful API endpoint that allows healthcare facilities to submit job requests for nurses and support workers, based on the recruitment services provided by Amazing Grace Medical Recruitment.
Generated: DETERMINISTIC_a747d89f8a658ece
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
from datetime import datetime
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Model for job requests
class JobRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facility_name = db.Column(db.String(255), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    request_date = db.Column(db.DateTime, default=datetime.utcnow)

# Schema for request validation
class JobRequestSchema(Schema):
    facility_name = fields.Str(required=True)
    position = fields.Str(required=True)
    quantity = fields.Int(required=True, validate=lambda n: n > 0)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to submit job requests
@app.route('/api/job_requests', methods=['POST'])
def submit_job_request():
    try:
        # Validate and deserialize input
        job_request_schema = JobRequestSchema()
        job_request_data = job_request_schema.load(request.json)

        # Create a new job request
        new_job_request = JobRequest(**job_request_data)

        # Add to the database
        db.session.add(new_job_request)
        db.session.commit()

        # Log the successful submission
        logging.info(f"Job request submitted: {new_job_request.id}")

        return jsonify({"message": "Job request submitted successfully", "id": new_job_request.id}), 201

    except ValidationError as err:
        # Handle validation errors
        logging.error(f"Validation error: {err.messages}")
        return jsonify({"error": "Validation error", "messages": err.messages}), 400

    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
