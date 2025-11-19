"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum24market.ru
Prompt: Develop a REST API endpoint that allows users to submit inquiries to a legal center, based on the contact functionality seen on the Arbitrum website.
Generated: DETERMINISTIC_b5fed7316e8f3159
Batch ID: 20250612_164152
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///inquiries.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for the inquiries
class Inquiry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define a schema for validating inquiries
class InquirySchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    message = fields.Str(required=True)

inquiry_schema = InquirySchema()

@app.route('/api/inquiries', methods=['POST'])
def submit_inquiry():
    """API endpoint to submit a legal inquiry."""
    try:
        # Validate and deserialize the input data
        inquiry_data = inquiry_schema.load(request.json)
        
        # Create a new inquiry instance
        new_inquiry = Inquiry(
            name=inquiry_data['name'],
            email=inquiry_data['email'],
            message=inquiry_data['message']
        )

        # Add the inquiry to the database
        db.session.add(new_inquiry)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Inquiry submitted successfully!"}), 201
        
    except ValidationError as err:
        # Handle validation errors
        return jsonify(err.messages), 400
        
    except Exception as e:
        # Handle any other exceptions
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
