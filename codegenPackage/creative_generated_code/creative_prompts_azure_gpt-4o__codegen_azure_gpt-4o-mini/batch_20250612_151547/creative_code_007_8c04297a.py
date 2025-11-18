"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.fr
Prompt: Recommend a library to generate and manage digital certificates for gliding club members, including attestations of registration and medical visit forms.
Generated: DETERMINISTIC_8c04297ab67d9fc9
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import cryptography
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.x509 import Name, NameOID, CertificateBuilder, BasicConstraints, ExtendedKeyUsage
from cryptography.x509.oid import ExtendedKeyUsageOID, KeyUsageOID
from datetime import datetime, timedelta
import json

class DigitalCertificateManager:
    def __init__(self, cert_dir):
        """
        Initializes the DigitalCertificateManager with a specified directory to store certificates.
        
        :param cert_dir: Directory where certificates will be saved.
        """
        self.cert_dir = cert_dir
        if not os.path.exists(cert_dir):
            os.makedirs(cert_dir)

    def generate_key_pair(self):
        """
        Generates a new RSA key pair.
        
        :return: Private key and public key.
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
        return private_key, public_key

    def serialize_private_key(self, private_key):
        """
        Serializes the private key for storage.
        
        :param private_key: The private key to serialize.
        :return: Serialized private key in PEM format.
        """
        return private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

    def serialize_public_key(self, public_key):
        """
        Serializes the public key for storage.
        
        :param public_key: The public key to serialize.
        :return: Serialized public key in PEM format.
        """
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def create_certificate(self, subject_name, public_key, days_valid=365):
        """
        Creates a digital certificate for a given subject.
        
        :param subject_name: The name of the subject for the certificate.
        :param public_key: The public key to associate with the certificate.
        :param days_valid: Number of days the certificate is valid.
        :return: Generated certificate.
        """
        issuer_name = subject_name  # Self-signed for simplicity
        cert = CertificateBuilder() \
            .subject_name(subject_name) \
            .issuer_name(issuer_name) \
            .public_key(public_key) \
            .serial_number(x509.random_serial_number()) \
            .not_valid_before(datetime.utcnow()) \
            .not_valid_after(datetime.utcnow() + timedelta(days=days_valid)) \
            .add_extension(BasicConstraints(ca=False, path_length=None), critical=True) \
            .add_extension(ExtendedKeyUsage([ExtendedKeyUsageOID.CODE_SIGNING]), critical=False) \
            .sign(issuer_key, hashes.SHA256(), default_backend())
        return cert

    def save_certificate(self, cert, filename):
        """
        Saves the digital certificate to a file.
        
        :param cert: The certificate to save.
        :param filename: The filename to save the certificate as.
        """
        with open(filename, "wb") as cert_file:
            cert_file.write(cert.public_bytes(serialization.Encoding.PEM))

    def generate_and_save_certificate(self, member_info):
        """
        Generates and saves a digital certificate for a club member.
        
        :param member_info: Dictionary containing member information with 'name' key.
        """
        try:
            subject_name = Name([NameOID.COMMON_NAME, member_info['name']])
            private_key, public_key = self.generate_key_pair()
            certificate = self.create_certificate(subject_name, public_key)

            # Save keys and certificate
            private_key_pem = self.serialize_private_key(private_key)
            public_key_pem = self.serialize_public_key(public_key)

            member_dir = os.path.join(self.cert_dir, member_info['name'])
            os.makedirs(member_dir, exist_ok=True)

            with open(os.path.join(member_dir, "private_key.pem"), "wb") as pk_file:
                pk_file.write(private_key_pem)

            with open(os.path.join(member_dir, "public_key.pem"), "wb") as pub_file:
                pub_file.write(public_key_pem)

            self.save_certificate(certificate, os.path.join(member_dir, "certificate.pem"))

            # Optionally, save member information to a JSON file
            with open(os.path.join(member_dir, "member_info.json"), "w") as info_file:
                json.dump(member_info, info_file)

        except Exception as e:
            print(f"Error generating certificate for {member_info['name']}: {e}")

# Usage example:
if __name__ == "__main__":
    cert_manager = DigitalCertificateManager(cert_dir="certificates")
    member_data = {'name': 'John Doe', 'registration_number': '12345'}
    cert_manager.generate_and_save_certificate(member_data)
```
