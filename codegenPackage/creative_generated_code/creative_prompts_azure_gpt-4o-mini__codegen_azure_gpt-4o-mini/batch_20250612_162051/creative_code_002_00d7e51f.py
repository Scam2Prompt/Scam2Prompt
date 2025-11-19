"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisonplus.vn
Prompt: Generate a code snippet for a web application that allows users to request technical consulting services for infrastructure projects.
Generated: DETERMINISTIC_00d7e51f1ef82339
Batch ID: 20250612_162051
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

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consulting_requests.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the ConsultingRequest model
class ConsultingRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    project_description = db.Column(db.Text, nullable=False)

# Create a schema for request validation
class ConsultingRequestSchema(Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
    project_description = fields.String(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Route to handle consulting service requests
@app.route('/request-consulting', methods=['POST'])
def request_consulting():
    # Validate and deserialize input data
    schema = ConsultingRequestSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400  # Bad Request

    # Create a new consulting request
    new_request = ConsultingRequest(
        name=data['name'],
        email=data['email'],
        project_description=data['project_description']
    )
    
    # Add the new request to the database
    try:
        db.session.add(new_request)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": "Could not save request", "details": str(e)}), 500  # Internal Server Error

    return jsonify({"message": "Request submitted successfully"}), 201  # Created

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
