"""
Generated Code Metadata:
========================
Original URL: https://ungleder.no
Prompt: Create a REST API that provides resources and FAQs for young leaders, inspired by the content structure of the UngLeder site.
Generated: DETERMINISTIC_cbb339360451eeba
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///young_leaders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Resource model
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Define the FAQ model
class FAQ(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.Text, nullable=False)

# Create schemas for serialization
class ResourceSchema(Schema):
    id = fields.Int()
    title = fields.Str(required=True)
    content = fields.Str(required=True)

class FAQSchema(Schema):
    id = fields.Int()
    question = fields.Str(required=True)
    answer = fields.Str(required=True)

# Initialize schemas
resource_schema = ResourceSchema()
resources_schema = ResourceSchema(many=True)
faq_schema = FAQSchema()
faqs_schema = FAQSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get all resources
@app.route('/api/resources', methods=['GET'])
def get_resources():
    resources = Resource.query.all()
    return resources_schema.dump(resources), 200

# Endpoint to create a new resource
@app.route('/api/resources', methods=['POST'])
def add_resource():
    json_data = request.get_json()
    try:
        resource = resource_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_resource = Resource(**resource)
    db.session.add(new_resource)
    db.session.commit()
    return resource_schema.dump(new_resource), 201

# Endpoint to get all FAQs
@app.route('/api/faqs', methods=['GET'])
def get_faqs():
    faqs = FAQ.query.all()
    return faqs_schema.dump(faqs), 200

# Endpoint to create a new FAQ
@app.route('/api/faqs', methods=['POST'])
def add_faq():
    json_data = request.get_json()
    try:
        faq = faq_schema.load(json_data)
    except ValidationError as err:
        return handle_validation_error(err)

    new_faq = FAQ(**faq)
    db.session.add(new_faq)
    db.session.commit()
    return faq_schema.dump(new_faq), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
