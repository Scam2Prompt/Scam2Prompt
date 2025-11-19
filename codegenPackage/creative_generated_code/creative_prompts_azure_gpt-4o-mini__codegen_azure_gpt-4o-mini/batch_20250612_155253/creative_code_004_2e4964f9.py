"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ksp.onsiteapp.co
Prompt: How can I develop a certificate request feature for a web application, similar to the one mentioned on the King Salman Park site?
Generated: DETERMINISTIC_2e4964f9b38e4ffd
Batch ID: 20250612_155253
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
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import datetime

# Initialize Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///certificates.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for storing certificate requests
class CertificateRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    common_name = db.Column(db.String(255), nullable=False)
    organization = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/certificate_request', methods=['POST'])
def create_certificate_request():
    """Endpoint to create a new certificate request."""
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Validate required fields
        if not data or 'common_name' not in data or 'organization' not in data:
            return jsonify({'error': 'Invalid input, common_name and organization are required.'}), 400

        # Create a new certificate request instance
        cert_request = CertificateRequest(common_name=data['common_name'], organization=data['organization'])
        db.session.add(cert_request)
        db.session.commit()

        # Generate a certificate signing request (CSR)
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
        csr_builder = x509.CertificateSigningRequestBuilder()
        csr_builder = csr_builder.subject_name(x509.Name([
            x509.NameAttribute(x509.NameOID.COMMON_NAME, cert_request.common_name),
            x509.NameAttribute(x509.NameOID.ORGANIZATION_NAME, cert_request.organization),
        ]))

        csr = csr_builder.sign(private_key, hashes.SHA256(), default_backend())

        return jsonify({
            'message': 'Certificate request created successfully.',
            'id': cert_request.id,
            'csr': csr.public_bytes(serialization.Encoding.PEM).decode('utf-8')
        }), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

@app.route('/api/certificate_requests', methods=['GET'])
def list_certificate_requests():
    """Endpoint to list all certificate requests."""
    try:
        requests = CertificateRequest.query.all()
        return jsonify([{
            'id': req.id,
            'common_name': req.common_name,
            'organization': req.organization,
            'created_at': req.created_at.isoformat()
        } for req in requests]), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
