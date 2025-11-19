"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lecarolee.it
Prompt: Develop a RESTful API endpoint that allows users to submit inquiries about the agriturismo services offered by Le Carolee, including validation for required fields.
Generated: DETERMINISTIC_c366c2f24338b9c0
Batch ID: 20250612_164000
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agriturismo.db'
db = SQLAlchemy(app)

# Model for Inquiry
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Schema for validating inquiries
class InquirySchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    message = fields.Str(required=True)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/inquiries', methods=['POST'])
def submit_inquiry():
    """
    Endpoint to submit inquiries about agriturismo services.
    Expects JSON data with 'name', 'email', and 'message'.
    """
    try:
        # Validate and deserialize input
        inquiry_data = request.get_json()
        inquiry_schema = InquirySchema()
        validated_data = inquiry_schema.load(inquiry_data)

        # Create Inquiry instance
        new_inquiry = Inquiry(**validated_data)

        # Save to database
        db.session.add(new_inquiry)
        db.session.commit()

        return jsonify({"message": "Inquiry submitted successfully!", "id": new_inquiry.id}), 201

    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        # Log the exception here (omitted for brevity)
        return jsonify({"error": "An error occurred while processing your inquiry."}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
