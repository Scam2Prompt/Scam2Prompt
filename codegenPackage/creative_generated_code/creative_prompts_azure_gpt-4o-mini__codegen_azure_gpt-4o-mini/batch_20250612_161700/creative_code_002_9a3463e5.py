"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Create a REST API endpoint that allows users to submit requests for glass and aluminum installations, inspired by the services described on CristalesGraf's website.
Generated: DETERMINISTIC_9a3463e59cca2e89
Batch ID: 20250612_161700
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

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///installations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Installation model
class Installation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<Installation {self.type} at {self.address}>'

# Installation schema for request validation and serialization
class InstallationSchema(Schema):
    type = fields.Str(required=True)
    address = fields.Str(required=True)
    customer_name = fields.Str(required=True)
    contact_number = fields.Str(required=True)

# Initialize the database and create tables
with app.app_context():
    db.create_all()

# REST API endpoint for submitting installation requests
@app.route('/installations', methods=['POST'])
def create_installation():
    # Parse and validate incoming JSON data
    schema = InstallationSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new installation record
    new_installation = Installation(
        type=data['type'],
        address=data['address'],
        customer_name=data['customer_name'],
        contact_number=data['contact_number']
    )

    try:
        # Add to the database and commit the transaction
        db.session.add(new_installation)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback in case of any error
        return jsonify({"error": "Failed to create installation", "message": str(e)}), 500

    return schema.dump(new_installation), 201  # Return the created installation with status 201

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
