"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puroworldclub.com
Prompt: Suggest an API for managing franchisee applications for the Puro World Club, including features for securely uploading documents and tracking application statuses.
Generated: DETERMINISTIC_e8722bbfd049818e
Batch ID: 20250612_153246
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
from werkzeug.utils import secure_filename
import os
import uuid
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///franchisee_applications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max file size: 16MB

# Initialize the database
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Franchisee Application model
class FranchiseeApplication(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    document_path = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='Pending')

    def __init__(self, name, email, document_path):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.document_path = document_path

# Create a schema for serializing the Franchisee Application
class FranchiseeApplicationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FranchiseeApplication

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to upload documents and create application
@app.route('/api/apply', methods=['POST'])
def apply():
    if 'document' not in request.files:
        raise BadRequest('No document part in the request')

    document = request.files['document']
    if document.filename == '':
        raise BadRequest('No selected file')

    # Secure and save the uploaded document
    filename = secure_filename(document.filename)
    document_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Create the uploads directory if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    document.save(document_path)

    # Get application details from request
    name = request.form.get('name')
    email = request.form.get('email')

    if not name or not email:
        raise BadRequest('Name and email are required')

    # Create new application
    new_application = FranchiseeApplication(name=name, email=email, document_path=document_path)
    db.session.add(new_application)
    db.session.commit()

    # Serialize the response
    application_schema = FranchiseeApplicationSchema()
    response = application_schema.dump(new_application)
    
    return jsonify(response), 201

# Endpoint to get the status of an application by ID
@app.route('/api/application/<application_id>', methods=['GET'])
def get_application(application_id):
    application = FranchiseeApplication.query.get(application_id)
    if application is None:
        return jsonify({'message': 'Application not found'}), 404

    application_schema = FranchiseeApplicationSchema()
    return jsonify(application_schema.dump(application))

# Error handler for 400 Bad Request
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({"error": str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
