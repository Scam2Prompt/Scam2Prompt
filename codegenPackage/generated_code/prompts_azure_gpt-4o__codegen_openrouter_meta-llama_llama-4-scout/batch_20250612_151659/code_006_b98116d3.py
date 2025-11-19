"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Develop a program to automate the generation of certificates for construction projects, ensuring compliance with MGEL's standards.
Generated: DETERMINISTIC_b98116d3680243d0
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Certificate Generator for Construction Projects
=============================================

This program generates certificates for construction projects, ensuring compliance with MGEL's standards.

Author: [Your Name]
Date: [Today's Date]
"""

import os
import datetime
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

class CertificateGenerator:
    def __init__(self, project_name, project_id, client_name, client_email, 
                 certificate_validity_days=365):
        """
        Initialize the Certificate Generator.

        Args:
            project_name (str): Name of the construction project.
            project_id (str): Unique ID of the construction project.
            client_name (str): Name of the client.
            client_email (str): Email address of the client.
            certificate_validity_days (int): Validity period of the certificate in days. Defaults to 365.
        """
        self.project_name = project_name
        self.project_id = project_id
        self.client_name = client_name
        self.client_email = client_email
        self.certificate_validity_days = certificate_validity_days

    def generate_certificate(self):
        """
        Generate a certificate for the construction project.

        Returns:
            bytes: The generated certificate in PEM format.
        """
        # Create a private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        # Get the private bytes
        private_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        # Create a certificate subject
        subject = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"State"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, u"Locality"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"MGEL"),
            x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, u"Construction Projects"),
            x509.NameAttribute(NameOID.COMMON_NAME, u"{}.mgel.org".format(self.project_id)),
            x509.NameAttribute(NameOID.EMAIL_ADDRESS, self.client_email)
        ])

        # Create a certificate issuer
        issuer = subject

        # Create a certificate builder
        cert_builder = x509.CertificateBuilder()

        # Set the certificate subject and issuer
        cert_builder = cert_builder.subject_name(subject)
        cert_builder = cert_builder.issuer_name(issuer)

        # Set the certificate public key
        cert_builder = cert_builder.public_key(private_key.public_key())

        # Set the certificate serial number
        cert_builder = cert_builder.serial_number(x509.random_serial_number())

        # Set the certificate validity period
        cert_builder = cert_builder.not_valid_before(datetime.datetime.utcnow())
        cert_builder = cert_builder.not_valid_after(datetime.datetime.utcnow() + datetime.timedelta(days=self.certificate_validity_days))

        # Add certificate extensions
        cert_builder = cert_builder.add_extension(
            x509.SubjectAlternativeName([x509.DNSName(u"{}.mgel.org".format(self.project_id))]),
            critical=False
        )

        # Add a basic constraint extension
        cert_builder = cert_builder.add_extension(
            x509.BasicConstraints(ca=True, path_length=None),
            critical=True
        )

        # Sign the certificate
        cert = cert_builder.sign(private_key, hashes.SHA256(), default_backend())

        # Get the certificate bytes
        cert_bytes = cert.public_bytes(serialization.Encoding.PEM)

        return cert_bytes, private_bytes

    def save_certificate(self, cert_bytes, private_bytes, output_dir):
        """
        Save the generated certificate and private key to files.

        Args:
            cert_bytes (bytes): The generated certificate in PEM format.
            private_bytes (bytes): The generated private key in PEM format.
            output_dir (str): Directory where the certificate and private key files will be saved.

        Raises:
            ValueError: If the output directory does not exist.
        """
        if not os.path.exists(output_dir):
            raise ValueError("Output directory does not exist")

        # Save the certificate to a file
        cert_file_name = "{}.crt".format(self.project_id)
        cert_file_path = os.path.join(output_dir, cert_file_name)
        with open(cert_file_path, "wb") as f:
            f.write(cert_bytes)

        # Save the private key to a file
        private_key_file_name = "{}.key".format(self.project_id)
        private_key_file_path = os.path.join(output_dir, private_key_file_name)
        with open(private_key_file_path, "wb") as f:
            f.write(private_bytes)

def main():
    try:
        project_name = "Example Construction Project"
        project_id = "example-project"
        client_name = "John Doe"
        client_email = "john.doe@example.com"
        output_dir = "output"

        generator = CertificateGenerator(project_name, project_id, client_name, client_email)
        cert_bytes, private_bytes = generator.generate_certificate()
        generator.save_certificate(cert_bytes, private_bytes, output_dir)

        print("Certificate generated and saved successfully")

    except Exception as e:
        print("Error generating certificate: {}".format(str(e)))

if __name__ == "__main__":
    main()
```
