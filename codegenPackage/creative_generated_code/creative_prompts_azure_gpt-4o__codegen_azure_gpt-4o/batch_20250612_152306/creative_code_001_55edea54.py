"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rspbharat.com
Prompt: Recommend libraries or APIs for building a certificate verification system for vocational training programs, as described on the RSP Bharat website.
Generated: DETERMINISTIC_55edea54b89f4531
Batch ID: 20250612_152306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

To recommend libraries and APIs, I’ll provide a Python-based code example using a certificate verification application. This uses Flask for the web framework, SQLAlchemy for database handling, and cryptography for verifying signatures. 

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
import os

# Flask app initialization
app = Flask(__name__)

# Database setup
engine = create_engine('sqlite:///certificates.db')  # Using SQLite for simplicity
Base = declarative_base()

# Certificate model definition
class Certificate(Base):
    __tablename__ = 'certificates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    certificate_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    course = Column(String, nullable=False)
    issued_date = Column(String, nullable=False)
    signature = Column(String, nullable=False)

# Create database table if not exists
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Generate RSA keys for signing
def generate_rsa_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()

    # Save keys to files
    with open('private_key.pem', 'wb') as private_file:
        private_file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    with open('public_key.pem', 'wb') as public_file:
        public_file.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

# Generate keys if not already present
if not os.path.exists('private_key.pem') or not os.path.exists('public_key.pem'):
    generate_rsa_keys()

# Load public and private keys
with open('private_key.pem', 'rb') as private_file:
    private_key = load_pem_private_key(private_file.read(), password=None)

with open('public_key.pem', 'rb') as public_file:
    public_key = load_pem_public_key(public_file.read())

# Endpoint to issue a certificate
@app.route('/issue_certificate', methods=['POST'])
def issue_certificate():
    try:
        data = request.json
        certificate_id = data['certificate_id']
        name = data['name']
        course = data['course']
        issued_date = data['issued_date']

        # Create a digest for signing
        message = f"{certificate_id}{name}{course}{issued_date}".encode()
        signature = private_key.sign(
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        # Save certificate to database
        session = Session()
        certificate = Certificate(
            certificate_id=certificate_id,
            name=name,
            course=course,
            issued_date=issued_date,
            signature=signature.hex()
        )
        session.add(certificate)
        session.commit()
        
        return jsonify({'message': 'Certificate issued successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to verify a certificate
@app.route('/verify_certificate', methods=['POST'])
def verify_certificate():
    try:
        data = request.json
        certificate_id = data['certificate_id']

        # Retrieve certificate from database
        session = Session()
        certificate = session.query(Certificate).filter_by(certificate_id=certificate_id).first()

        if not certificate:
            return jsonify({'message': 'Certificate not found'}), 404

        # Verify the signature
        message = f"{certificate.certificate_id}{certificate.name}{certificate.course}{certificate.issued_date}".encode()
        signature = bytes.fromhex(certificate.signature)

        try:
            public_key.verify(
                signature,
                message,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return jsonify({'message': 'Certificate is valid'}), 200
        except:
            return jsonify({'message': 'Certificate verification failed'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Libraries Used:
1. **Flask**: For building REST APIs.
2. **SQLAlchemy**: For interacting with the database.
3. **cryptography**: For digital signature handling.

This code provides endpoints for issuing and verifying certificates, ensuring security with RSA-based signatures.
