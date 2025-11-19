"""
Generated Code Metadata:
========================
Original URL: https://www.thompsonestateathletics.com.au
Prompt: Develop an API endpoint for managing membership registrations and inquiries for a running club, similar to the features offered by Thompson Estate Athletics.
Generated: DETERMINISTIC_f91270ead353990f
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///members.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Membership model
class Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    inquiry = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<Membership {self.name}>'

# Create the database
with app.app_context():
    db.create_all()

# Define the Membership schema for validation
class MembershipSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    inquiry = fields.Str(required=False)

membership_schema = MembershipSchema()
memberships_schema = MembershipSchema(many=True)

# API endpoint to register a new member
@app.route('/api/members', methods=['POST'])
def register_member():
    """Register a new member."""
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = membership_schema.load(data)

        # Create a new membership instance
        new_member = Membership(**validated_data)
        db.session.add(new_member)
        db.session.commit()

        return jsonify(membership_schema.dump(new_member)), 201
    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error registering member: {str(e)}")
        return jsonify({"error": "An error occurred while registering the member."}), 500

# API endpoint to get all members
@app.route('/api/members', methods=['GET'])
def get_members():
    """Retrieve all members."""
    try:
        members = Membership.query.all()
        return jsonify(members_schema.dump(members)), 200
    except Exception as e:
        logging.error(f"Error retrieving members: {str(e)}")
        return jsonify({"error": "An error occurred while retrieving members."}), 500

# API endpoint to inquire about membership
@app.route('/api/inquiries', methods=['POST'])
def inquire_membership():
    """Inquire about membership."""
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = membership_schema.load(data)

        # Create a new inquiry instance
        new_inquiry = Membership(**validated_data)
        db.session.add(new_inquiry)
        db.session.commit()

        return jsonify(membership_schema.dump(new_inquiry)), 201
    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error inquiring about membership: {str(e)}")
        return jsonify({"error": "An error occurred while processing the inquiry."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
