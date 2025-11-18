"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visa-pwr.com
Prompt: Develop an API-based solution for managing visa application workflows, tailored to the administrative services offered by visapwr.
Generated: DETERMINISTIC_c6f53749d9183e20
Batch ID: 20250612_150816
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
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visa_applications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Visa Application
class VisaApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    applicant_name = db.Column(db.String(100), nullable=False)
    visa_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='Pending')

    def to_dict(self):
        return {
            'id': self.id,
            'applicant_name': self.applicant_name,
            'visa_type': self.visa_type,
            'status': self.status
        }

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Create a new visa application
@app.route('/visa-applications', methods=['POST'])
def create_application():
    data = request.get_json()
    if not data or 'applicant_name' not in data or 'visa_type' not in data:
        raise BadRequest("Missing required fields: 'applicant_name' and 'visa_type'.")

    new_application = VisaApplication(
        applicant_name=data['applicant_name'],
        visa_type=data['visa_type']
    )
    db.session.add(new_application)
    db.session.commit()
    return jsonify(new_application.to_dict()), 201

# Get all visa applications
@app.route('/visa-applications', methods=['GET'])
def get_applications():
    applications = VisaApplication.query.all()
    return jsonify([app.to_dict() for app in applications]), 200

# Get a specific visa application by ID
@app.route('/visa-applications/<int:application_id>', methods=['GET'])
def get_application(application_id):
    application = VisaApplication.query.get(application_id)
    if application is None:
        raise NotFound(f"Visa application with ID {application_id} not found.")
    return jsonify(application.to_dict()), 200

# Update a visa application status
@app.route('/visa-applications/<int:application_id>', methods=['PUT'])
def update_application(application_id):
    application = VisaApplication.query.get(application_id)
    if application is None:
        raise NotFound(f"Visa application with ID {application_id} not found.")

    data = request.get_json()
    if 'status' in data:
        application.status = data['status']
    db.session.commit()
    return jsonify(application.to_dict()), 200

# Delete a visa application
@app.route('/visa-applications/<int:application_id>', methods=['DELETE'])
def delete_application(application_id):
    application = VisaApplication.query.get(application_id)
    if application is None:
        raise NotFound(f"Visa application with ID {application_id} not found.")

    db.session.delete(application)
    db.session.commit()
    return jsonify({'message': 'Visa application deleted successfully.'}), 204

# Error handling
@app.errorhandler(NotFound)
def handle_not_found(error):
    response = jsonify({'error': str(error)})
    response.status_code = 404
    return response

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    response = jsonify({'error': str(error)})
    response.status_code = 400
    return response

if __name__ == '__main__':
    app.run(debug=True)
```
