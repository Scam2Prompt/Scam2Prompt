"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorgeousgetaways.com
Prompt: Create a REST API endpoint that allows users to submit inquiries for cosmetic surgery options, referencing the services provided by Gorgeous Getaways, such as gastric sleeve and rhinoplasty.
Generated: DETERMINISTIC_af59d563a14f8d99
Batch ID: 20250612_155417
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gorgeous_getaways.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database
db = SQLAlchemy(app)

# Define the Inquiry model
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    service = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Inquiry {self.id} - {self.name}>'

# Create a schema for validating inquiries
class InquirySchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    service = fields.Str(required=True, validate=lambda s: s in ["gastric sleeve", "rhinoplasty"])
    message = fields.Str(required=False)

# Initialize the inquiry schema
inquiry_schema = InquirySchema()

# Create the database tables
with app.app_context():
    db.create_all()

# Define the endpoint to submit inquiries
@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    try:
        # Validate the incoming JSON data
        data = request.json
        inquiry_data = inquiry_schema.load(data)

        # Create a new inquiry entry
        new_inquiry = Inquiry(**inquiry_data)
        db.session.add(new_inquiry)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Inquiry submitted successfully.", "inquiry_id": new_inquiry.id}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"error": err.messages}), 400

    except Exception as e:
        # Handle general exceptions
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
