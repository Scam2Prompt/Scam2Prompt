"""
Generated Code Metadata:
========================
Original URL: https://magicbear.com.br
Prompt: Design an API for a bilingual school management system that includes features like contact information and program details, inspired by the Magic Bear Canadian School website.
Generated: DETERMINISTIC_7128edd0d8fa086c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school_management.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Contact model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return f'<Contact {self.name}>'

# Define the Program model
class Program(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    language = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Program {self.title}>'

# Define schemas for serialization
class ContactSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)

class ProgramSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    language = fields.Str(required=True)

# Initialize schemas
contact_schema = ContactSchema()
contacts_schema = ContactSchema(many=True)
program_schema = ProgramSchema()
programs_schema = ProgramSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to create a new contact
@app.route('/contacts', methods=['POST'])
def add_contact():
    try:
        # Validate and deserialize input
        contact_data = contact_schema.load(request.json)
        new_contact = Contact(**contact_data)
        db.session.add(new_contact)
        db.session.commit()
        return contact_schema.jsonify(new_contact), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return contacts_schema.jsonify(contacts), 200

# API endpoint to create a new program
@app.route('/programs', methods=['POST'])
def add_program():
    try:
        # Validate and deserialize input
        program_data = program_schema.load(request.json)
        new_program = Program(**program_data)
        db.session.add(new_program)
        db.session.commit()
        return program_schema.jsonify(new_program), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to get all programs
@app.route('/programs', methods=['GET'])
def get_programs():
    programs = Program.query.all()
    return programs_schema.jsonify(programs), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
