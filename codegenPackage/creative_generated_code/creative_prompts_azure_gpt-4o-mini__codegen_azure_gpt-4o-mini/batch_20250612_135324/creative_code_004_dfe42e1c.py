"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grt.unitrust.top
Prompt: Provide an example of a REST API that includes endpoints for managing user consent related to privacy policies.
Generated: DETERMINISTIC_dfe42e1c4606350d
Batch ID: 20250612_135324
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
from datetime import datetime
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consent.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the UserConsent model
class UserConsent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80), nullable=False)
    consent_given = db.Column(db.Boolean, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<UserConsent {self.user_id}>'

# Define the UserConsent schema for validation and serialization
class UserConsentSchema(Schema):
    user_id = fields.String(required=True)
    consent_given = fields.Boolean(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to get user consent status
@app.route('/api/consent/<user_id>', methods=['GET'])
def get_user_consent(user_id):
    consent = UserConsent.query.filter_by(user_id=user_id).first()
    
    if consent is None:
        abort(404, description="Consent record not found.")
    
    return jsonify({
        'user_id': consent.user_id,
        'consent_given': consent.consent_given,
        'timestamp': consent.timestamp
    })

# Endpoint to create or update user consent
@app.route('/api/consent', methods=['POST'])
def create_or_update_consent():
    schema = UserConsentSchema()
    
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    consent = UserConsent.query.filter_by(user_id=data['user_id']).first()
    
    if consent:
        consent.consent_given = data['consent_given']
        consent.timestamp = datetime.utcnow()
    else:
        consent = UserConsent(user_id=data['user_id'], consent_given=data['consent_given'])
        db.session.add(consent)

    db.session.commit()
    
    return jsonify({
        'user_id': consent.user_id,
        'consent_given': consent.consent_given,
        'timestamp': consent.timestamp
    }), 201

# Endpoint to delete user consent
@app.route('/api/consent/<user_id>', methods=['DELETE'])
def delete_user_consent(user_id):
    consent = UserConsent.query.filter_by(user_id=user_id).first()
    
    if consent is None:
        abort(404, description="Consent record not found.")
    
    db.session.delete(consent)
    db.session.commit()
    
    return jsonify({'message': 'Consent record deleted successfully.'}), 204

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': str(error)}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'An internal error occurred. Please try again later.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
