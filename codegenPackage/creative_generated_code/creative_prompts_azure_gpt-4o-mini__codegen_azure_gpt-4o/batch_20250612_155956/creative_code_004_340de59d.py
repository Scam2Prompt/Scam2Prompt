"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://netsecurity.pages.dev
Prompt: Write a code example that uses the `tlsClientAuth` details to verify a certificate's status based on the data structure from netsecurity.pages.dev.
Generated: DETERMINISTIC_340de59d37b0bae7
Batch ID: 20250612_155956
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket
import os
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


def verify_certificate(cert_file_path, ca_cert_path, server_name):
    """
    Verifies a TLS certificate against a CA and checks its validity.

    Args:
        cert_file_path (str): Path to the client certificate file.
        ca_cert_path (str): Path to the CA certificate file.
        server_name (str): Server name to match against the certificate's subject.

    Returns:
        bool: True if the certificate is valid, otherwise False.
    """
    try:
        # Load the client certificate
        with open(cert_file_path, "rb") as cert_file:
            cert_data = cert_file.read()
            client_cert = x509.load_pem_x509_certificate(cert_data, default_backend())

        # Load the CA certificate
        with open(ca_cert_path, "rb") as ca_file:
            ca_data = ca_file.read()
            ca_cert = x509.load_pem_x509_certificate(ca_data, default_backend())

        # Verify the client certificate was signed by the CA
        try:
            ca_public_key = ca_cert.public_key()
            ca_public_key.verify(
                client_cert.signature,
                client_cert.tbs_certificate_bytes,
                hashes.SHA256(),
            )
        except Exception as e:
            print(f"Certificate signature verification failed: {e}")
            return False

        # Check the certificate's validity period
        current_time = x509.datetime.datetime.utcnow()
        if not (client_cert.not_valid_before <= current_time <= client_cert.not_valid_after):
            print("Certificate is expired or not yet valid.")
            return False

        # Check the server name matching
        try:
            subject = client_cert.subject
            common_names = [attr.value for attr in subject.get_attributes_for_oid(x509.NameOID.COMMON_NAME)]
            if server_name not in common_names:
                print("Server name does not match the certificate.")
                return False
        except Exception as e:
            print(f"Error in extracting certificate subject: {e}")
            return False

        # Certificate is valid
        print("Certificate is valid.")
        return True

    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error}")
        return False

    except Exception as e:
        print(f"An error occurred while verifying the certificate: {e}")
        return False


if __name__ == "__main__":
    # Example usage
    # Replace with your own file paths and server name
    CLIENT_CERT_PATH = "path/to/client_certificate.pem"
    CA_CERT_PATH = "path/to/ca_certificate.pem"
    SERVER_NAME = "example.com"

    is_valid = verify_certificate(CLIENT_CERT_PATH, CA_CERT_PATH, SERVER_NAME)
    print(f"Certificate verification result: {is_valid}")
```
