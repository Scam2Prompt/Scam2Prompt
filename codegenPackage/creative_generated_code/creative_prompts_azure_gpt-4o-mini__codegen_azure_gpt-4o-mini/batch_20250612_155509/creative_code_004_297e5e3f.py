"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qwaliconnect.com
Prompt: Suggest an API that could be used to manage a mailing list similar to the one mentioned in the contact section of Qwali Connect's webpage.
Generated: DETERMINISTIC_297e5e3f7dc7db41
Batch ID: 20250612_155509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mailing_list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Mailing List model
class MailingList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Create a schema for validating input data
class MailingListSchema(Schema):
    email = fields.Email(required=True, validate=validate.Length(max=120))

# Initialize the schema
mailing_list_schema = MailingListSchema()
mailing_list_schema_many = MailingListSchema(many=True)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/api/mailing_list', methods=['POST'])
def add_email():
    """Add an email to the mailing list."""
    data = request.get_json()
    errors = mailing_list_schema.validate(data)
    
    if errors:
        # Return a 400 Bad Request error if validation fails
        return jsonify(errors), 400
    
    email = data['email']
    # Check if the email already exists
    if MailingList.query.filter_by(email=email).first():
        return jsonify({"message": "Email already exists."}), 409

    # Create a new mailing list entry
    new_entry = MailingList(email=email)
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({"message": "Email added successfully."}), 201

@app.route('/api/mailing_list', methods=['GET'])
def get_emails():
    """Retrieve all emails from the mailing list."""
    entries = MailingList.query.all()
    return mailing_list_schema_many.dump(entries), 200

@app.route('/api/mailing_list/<int:id>', methods=['DELETE'])
def delete_email(id):
    """Remove an email from the mailing list by ID."""
    entry = MailingList.query.get(id)
    if entry is None:
        # Return a 404 Not Found error if the ID does not exist
        return jsonify({"message": "Email not found."}), 404

    db.session.delete(entry)
    db.session.commit()
    
    return jsonify({"message": "Email removed successfully."}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
