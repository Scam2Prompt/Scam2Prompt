"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Develop a RESTful API endpoint that allows healthcare facilities to submit job requests for nurses and support workers, based on the recruitment services provided by Amazing Grace Medical Recruitment.
Generated: DETERMINISTIC_a747d89f8a658ece
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the JobRequest model
class JobRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    facility_name = db.Column(db.String(100), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)
    number_of_positions = db.Column(db.Integer, nullable=False)
    contact_email = db.Column(db.String(100), nullable=False)

# Create a schema for validating job requests
class JobRequestSchema(Schema):
    facility_name = fields.Str(required=True)
    job_type = fields.Str(required=True, validate=lambda s: s in ["nurse", "support_worker"])
    number_of_positions = fields.Int(required=True, validate=lambda n: n > 0)
    contact_email = fields.Email(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to submit job requests
@app.route('/api/job_requests', methods=['POST'])
def submit_job_request():
    # Parse and validate the incoming JSON data
    schema = JobRequestSchema()
    try:
        job_request_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new job request instance
    new_job_request = JobRequest(
        facility_name=job_request_data['facility_name'],
        job_type=job_request_data['job_type'],
        number_of_positions=job_request_data['number_of_positions'],
        contact_email=job_request_data['contact_email']
    )

    # Add the job request to the database
    try:
        db.session.add(new_job_request)
        db.session.commit()
        logging.info(f"New job request submitted: {new_job_request}")
        return jsonify({"message": "Job request submitted successfully", "id": new_job_request.id}), 201
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error submitting job request: {e}")
        return jsonify({"error": "Failed to submit job request"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
