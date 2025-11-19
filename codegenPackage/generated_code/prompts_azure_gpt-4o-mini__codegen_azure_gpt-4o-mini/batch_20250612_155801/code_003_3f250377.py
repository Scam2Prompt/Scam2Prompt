"""
Generated Code Metadata:
========================
Original URL: https://berge.life
Prompt: Suggest an API for managing user consent related to privacy policies in web applications.
Generated: DETERMINISTIC_3f25037795267ad7
Batch ID: 20250612_155801
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
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consent.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for User Consent
class UserConsent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    consent_given = db.Column(db.Boolean, nullable=False)
    consent_date = db.Column(db.DateTime, default=datetime.utcnow)

# Schema for validating input data
class UserConsentSchema(Schema):
    user_id = fields.Str(required=True)
    consent_given = fields.Bool(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Route to manage user consent
@app.route('/api/consent', methods=['POST'])
def manage_consent():
    """Endpoint to manage user consent for privacy policies."""
    schema = UserConsentSchema()
    
    # Validate incoming JSON data
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

    # Check if consent already exists for the user
    existing_consent = UserConsent.query.filter_by(user_id=data['user_id']).first()
    
    if existing_consent:
        # Update existing consent
        existing_consent.consent_given = data['consent_given']
        existing_consent.consent_date = datetime.utcnow()
        db.session.commit()
        return jsonify({"message": "Consent updated successfully."}), 200
    else:
        # Create new consent record
        new_consent = UserConsent(
            user_id=data['user_id'],
            consent_given=data['consent_given']
        )
        db.session.add(new_consent)
        db.session.commit()
        return jsonify({"message": "Consent recorded successfully."}), 201

# Route to retrieve user consent status
@app.route('/api/consent/<string:user_id>', methods=['GET'])
def get_consent(user_id):
    """Endpoint to retrieve user consent status."""
    consent = UserConsent.query.filter_by(user_id=user_id).first()
    
    if consent:
        return jsonify({
            "user_id": consent.user_id,
            "consent_given": consent.consent_given,
            "consent_date": consent.consent_date.isoformat()
        }), 200
    else:
        return jsonify({"message": "No consent record found for this user."}), 404

# Error handling for unexpected exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unexpected exceptions."""
    return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
