"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flyemiratestoursandtravels.in
Prompt: Design an API endpoint for a travel service that allows users to submit requests for certificate attestation, similar to the services offered by Fly Emirates Tours and Travels.
Generated: DETERMINISTIC_cb1dbb605ad29a23
Batch ID: 20250612_163958
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
from werkzeug.exceptions import BadRequest, InternalServerError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attestations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Certificate Attestation Requests
class CertificateRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    passport_number = db.Column(db.String(50), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    request_date = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'email': self.email,
            'passport_number': self.passport_number,
            'destination': self.destination,
            'request_date': self.request_date.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/certificate-request', methods=['POST'])
def submit_certificate_request():
    """Endpoint to submit a certificate attestation request."""
    try:
        # Extracting JSON data from the request
        data = request.get_json()
        if not data:
            raise BadRequest("Request body must be JSON.")

        # Validating required fields
        required_fields = ['user_name', 'email', 'passport_number', 'destination']
        for field in required_fields:
            if field not in data:
                raise BadRequest(f"Missing required field: {field}")

        # Creating a new certificate request
        new_request = CertificateRequest(
            user_name=data['user_name'],
            email=data['email'],
            passport_number=data['passport_number'],
            destination=data['destination']
        )

        # Adding to the database
        db.session.add(new_request)
        db.session.commit()

        # Return a success response
        return jsonify(new_request.to_dict()), 201

    except BadRequest as e:
        # Return a 400 error for invalid requests
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handling unexpected errors
        return jsonify({"error": "An internal error occurred."}), 500

if __name__ == '__main__':
    # Running the Flask application
    app.run(debug=True)
```
