"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Develop code to generate digital certificates for food handlers based on laboratory test results, including parasitology and toxicology, as described in Medicid IPS's services.
Generated: DETERMINISTIC_056d0cef989df8c6
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend
from datetime import datetime, timedelta

class CertificateGenerator:
    def __init__(self, organization_name, organizational_unit_name, city, state, country):
        self.organization_name = organization_name
        self.organizational_unit_name = organizational_unit_name
        self.city = city
        self.state = state
        self.country = country

    def generate_private_key(self):
        # Generate a private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        return private_key

    def generate_certificate(self, private_key, test_results, holder_name, holder_id):
        # Create a certificate subject
        subject = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, self.country),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, self.state),
            x509.NameAttribute(NameOID.LOCALITY_NAME, self.city),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, self.organization_name),
            x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, self.organizational_unit_name),
            x509.NameAttribute(NameOID.COMMON_NAME, holder_name),
        ])

        # Create a certificate issuer (self-signed)
        issuer = subject

        # Create a certificate builder
        cert_builder = x509.CertificateBuilder()

        # Set certificate subject and issuer
        cert_builder = cert_builder.subject_name(subject)
        cert_builder = cert_builder.issuer_name(issuer)

        # Set certificate public key
        cert_builder = cert_builder.public_key(private_key.public_key())

        # Set certificate serial number
        cert_builder = cert_builder.serial_number(x509.random_serial_number())

        # Set certificate not before and not after dates
        cert_builder = cert_builder.not_valid_before(datetime.utcnow())
        cert_builder = cert_builder.not_valid_after(datetime.utcnow() + timedelta(days=365))

        # Add test results to certificate extensions
        test_results_extension = self._create_test_results_extension(test_results)
        cert_builder = cert_builder.add_extension(test_results_extension, critical=False)

        # Add holder ID to certificate extensions
        holder_id_extension = self._create_holder_id_extension(holder_id)
        cert_builder = cert_builder.add_extension(holder_id_extension, critical=False)

        # Sign the certificate
        cert = cert_builder.sign(private_key, hashes.SHA256(), default_backend())

        return cert

    def _create_test_results_extension(self, test_results):
        # Create a custom extension for test results
        test_results_oid = x509.ObjectIdentifier("1.3.6.1.4.1.1234567890.1")
        test_results_value = self._encode_test_results(test_results)
        return x509.Extension(test_results_oid, False, test_results_value)

    def _create_holder_id_extension(self, holder_id):
        # Create a custom extension for holder ID
        holder_id_oid = x509.ObjectIdentifier("1.3.6.1.4.1.1234567890.2")
        holder_id_value = holder_id.encode("utf-8")
        return x509.Extension(holder_id_oid, False, holder_id_value)

    def _encode_test_results(self, test_results):
        # Encode test results in a simple format
        encoded_results = ""
        for test, result in test_results.items():
            encoded_results += f"{test}: {result}\n"
        return encoded_results.encode("utf-8")

def main():
    try:
        # Set certificate details
        organization_name = "Medicid IPS"
        organizational_unit_name = "Food Safety Department"
        city = "Anytown"
        state = "Anystate"
        country = "US"

        # Set test results
        test_results = {
            "Parasitology": "Negative",
            "Toxicology": "Negative"
        }

        # Set holder details
        holder_name = "John Doe"
        holder_id = "1234567890"

        # Create a certificate generator
        cert_generator = CertificateGenerator(organization_name, organizational_unit_name, city, state, country)

        # Generate a private key
        private_key = cert_generator.generate_private_key()

        # Generate a certificate
        cert = cert_generator.generate_certificate(private_key, test_results, holder_name, holder_id)

        # Save the certificate and private key to files
        with open("certificate.pem", "wb") as f:
            f.write(cert.public_bytes(serialization.Encoding.PEM))
        with open("private_key.pem", "wb") as f:
            f.write(private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ))

        print("Certificate and private key generated successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
