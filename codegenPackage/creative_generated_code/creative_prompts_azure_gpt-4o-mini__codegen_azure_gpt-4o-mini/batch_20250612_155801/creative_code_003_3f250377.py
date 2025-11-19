"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berge.life
Prompt: Suggest an API for managing user consent related to privacy policies in web applications.
Generated: DETERMINISTIC_3f25037795267ad7
Batch ID: 20250612_155801
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
from werkzeug.exceptions import BadRequest, NotFound

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consent.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Consent model to store user consent data
class Consent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False, unique=True)
    consent_given = db.Column(db.Boolean, nullable=False)
    policy_version = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Consent {self.user_id}: {self.consent_given}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/consent', methods=['POST'])
def give_consent():
    """
    Endpoint to record user consent for privacy policy.

    Request Body:
    {
        "user_id": "string",
        "consent_given": true,
        "policy_version": "string"
    }
    """
    data = request.json
    
    # Validate input data
    if not all(k in data for k in ("user_id", "consent_given", "policy_version")):
        raise BadRequest("Missing required fields in the request body.")

    user_id = data["user_id"]
    
    # Check if consent already exists for the user
    existing_consent = Consent.query.filter_by(user_id=user_id).first()
    if existing_consent:
        existing_consent.consent_given = data["consent_given"]
        existing_consent.policy_version = data["policy_version"]
        db.session.commit()
        return jsonify({"message": "Consent updated successfully."}), 200

    # Create new consent record
    new_consent = Consent(user_id=user_id, consent_given=data["consent_given"], policy_version=data["policy_version"])
    db.session.add(new_consent)
    db.session.commit()

    return jsonify({"message": "Consent recorded successfully."}), 201

@app.route('/consent/<user_id>', methods=['GET'])
def get_consent(user_id):
    """
    Endpoint to retrieve user consent status.

    :param user_id: Unique identifier of the user
    :return: JSON containing consent status and policy version
    """
    consent = Consent.query.filter_by(user_id=user_id).first()
    if not consent:
        raise NotFound("Consent record not found for this user.")

    return jsonify({
        "user_id": consent.user_id,
        "consent_given": consent.consent_given,
        "policy_version": consent.policy_version
    }), 200

@app.route('/consent/<user_id>', methods=['DELETE'])
def revoke_consent(user_id):
    """
    Endpoint to revoke user consent.

    :param user_id: Unique identifier of the user
    :return: JSON message confirming revocation
    """
    consent = Consent.query.filter_by(user_id=user_id).first()
    
    if not consent:
        raise NotFound("Consent record not found for this user.")

    db.session.delete(consent)
    db.session.commit()

    return jsonify({"message": "Consent revoked successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
