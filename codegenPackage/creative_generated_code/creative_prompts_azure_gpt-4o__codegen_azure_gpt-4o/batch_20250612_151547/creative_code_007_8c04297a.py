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
# gliding_club_certificates.py

"""
This script provides functionality to generate and manage digital certificates for gliding club members.
It uses the `cryptography` library to create self-signed certificates, track member registration attestations,
and verify forms such as medical visit attestations.
"""

from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
import datetime
import os


class CertificateManager:
    """
    CertificateManager class for generating and managing digital certificates for gliding club members.
    """

    def __init__(self, cert_folder="certificates"):
        """
        Initializes the CertificateManager instance.

        :param cert_folder: Folder to store certificates.
        """
        self.cert_folder = cert_folder
        if not os.path.exists(cert_folder):
            os.makedirs(cert_folder)

    def generate_certificate(self, member_name, member_id):
        """
        Generates a self-signed digital certificate for a gliding club member.

        :param member_name: Full name of the gliding club member.
        :param member_id: Unique identifier of the gliding club member.
        :return: File paths for the generated certificate and private key.
        """
        try:
            # Generate RSA private key
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048
            )

            # Build certificate subject and issuer details
            subject = x509.Name([
                x509.NameAttribute(NameOID.COMMON_NAME, member_name),
                x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Gliding Club"),
                x509.NameAttribute(NameOID.USER_ID, member_id),
            ])

            issuer = subject  # Self-signed certificate, issuer is the same as subject

            # Create the certificate
            certificate = x509.CertificateBuilder().subject_name(
                subject
            ).issuer_name(
                issuer
            ).public_key(
                private_key.public_key()
            ).serial_number(
                x509.random_serial_number()
            ).not_valid_before(
                datetime.datetime.utcnow()
            ).not_valid_after(
                datetime.datetime.utcnow() + datetime.timedelta(days=365)
            ).add_extension(
                x509.SubjectAlternativeName([x509.DNSName("glidingclub.local")]),
                critical=False,
            ).sign(private_key, hashes.SHA256())

            # Save the private key and certificate to files
            private_key_path = os.path.join(self.cert_folder, f"{member_id}_private_key.pem")
            cert_path = os.path.join(self.cert_folder, f"{member_id}_certificate.pem")

            with open(private_key_path, "wb") as key_file:
                key_file.write(private_key.private_bytes(
                    encoding=Encoding.PEM,
                    format=PrivateFormat.PKCS8,
                    encryption_algorithm=NoEncryption()
                ))

            with open(cert_path, "wb") as cert_file:
                cert_file.write(certificate.public_bytes(Encoding.PEM))

            return cert_path, private_key_path

        except Exception as e:
            raise RuntimeError(f"Failed to generate certificate: {e}")

    def validate_attestation(self, attestation_file):
        """
        Stub method for attestation validation. Placeholder for attestation verification logic.

        :param attestation_file: Path to the attestation form file (e.g., medical visit forms).
        :return: True if attestation is valid, else False.
        """
        # TODO: Implement attestation validation logic, e.g., signature verification.
        # Currently returns True as a placeholder.
        return True


if __name__ == "__main__":
    # Example usage of the CertificateManager class.
    try:
        manager = CertificateManager()

        # Generate a certificate for a sample member
        cert, key = manager.generate_certificate(
            member_name="John Doe",
            member_id="12345"
        )
        print(f"Certificate saved at: {cert}")
        print(f"Private key saved at: {key}")

        # Validate a sample attestation (stub implementation)
        is_valid = manager.validate_attestation("sample_medical_form.pdf")
        print(f"Attestation valid: {is_valid}")

    except Exception as e:
        print(f"Error: {e}")
```

### Requirements:
To run this code, make sure you install the `cryptography` library:
```bash
pip install cryptography
```
