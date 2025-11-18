"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anonymix.co
Prompt: Write code to generate and manage a certificate of origin for mixed Bitcoin transactions, similar to the feature offered by Anonymix.co.
Generated: DETERMINISTIC_21e6db55723db25e
Batch ID: 20250612_142622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import uuid
import datetime
import json
import os
from typing import Dict, Any

# Define constants
CERTIFICATES_DIR = "certificates"  # Directory to store generated certificates

# Ensure certificates directory exists
if not os.path.exists(CERTIFICATES_DIR):
    os.makedirs(CERTIFICATES_DIR)

class CertificateOfOrigin:
    """
    Class to generate and manage certificates of origin for mixed Bitcoin transactions.
    """

    def __init__(self, transaction_id: str, input_addresses: list, output_addresses: list):
        """
        Initialize the certificate generator.
        
        Args:
            transaction_id (str): Unique transaction ID.
            input_addresses (list): List of input Bitcoin addresses involved in the transaction.
            output_addresses (list): List of output Bitcoin addresses resulting from the transaction.
        """
        self.transaction_id = transaction_id
        self.input_addresses = input_addresses
        self.output_addresses = output_addresses
        self.timestamp = datetime.datetime.utcnow().isoformat()
        self.certificate_id = str(uuid.uuid4())

    def generate_certificate(self) -> Dict[str, Any]:
        """
        Generate a certificate of origin for the mixed transaction.
        
        Returns:
            dict: Certificate details including transaction hash.
        """
        # Create certificate details
        certificate_data = {
            "certificate_id": self.certificate_id,
            "transaction_id": self.transaction_id,
            "input_addresses": self.input_addresses,
            "output_addresses": self.output_addresses,
            "timestamp": self.timestamp
        }

        # Generate a unique hash for the certificate (SHA256)
        certificate_json = json.dumps(certificate_data, sort_keys=True)
        certificate_hash = hashlib.sha256(certificate_json.encode("utf-8")).hexdigest()
        certificate_data["certificate_hash"] = certificate_hash

        # Save the certificate to a file
        self._save_certificate_to_file(certificate_data)
        
        return certificate_data

    def _save_certificate_to_file(self, certificate_data: Dict[str, Any]):
        """
        Save the certificate details to a JSON file.

        Args:
            certificate_data (dict): Certificate data to save.
        """
        file_name = f"{CERTIFICATES_DIR}/{self.certificate_id}.json"
        try:
            with open(file_name, "w") as file:
                json.dump(certificate_data, file, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save certificate to file: {e}")

    @staticmethod
    def load_certificate(certificate_id: str) -> Dict[str, Any]:
        """
        Load a certificate of origin from a file.

        Args:
            certificate_id (str): Unique certificate ID.
        
        Returns:
            dict: Loaded certificate details.
        """
        file_name = f"{CERTIFICATES_DIR}/{certificate_id}.json"
        try:
            with open(file_name, "r") as file:
                certificate_data = json.load(file)
            return certificate_data
        except FileNotFoundError:
            raise FileNotFoundError(f"Certificate with ID {certificate_id} not found.")
        except Exception as e:
            raise IOError(f"Failed to load certificate: {e}")

# Example usage:
if __name__ == "__main__":
    # Example transaction details
    transaction_id = "tx123456789abcdef"
    input_addresses = ["1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"]
    output_addresses = ["3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy", "bc1qw4xxrd35xv7u4rjvdwl7vcl7d6df8sp4z5r8fh"]

    # Generate certificate
    certificate = CertificateOfOrigin(transaction_id, input_addresses, output_addresses)
    generated_certificate = certificate.generate_certificate()
    
    print("Generated Certificate:")
    print(json.dumps(generated_certificate, indent=4))

    # Load the certificate by its ID
    loaded_certificate = CertificateOfOrigin.load_certificate(generated_certificate["certificate_id"])
    print("\nLoaded Certificate:")
    print(json.dumps(loaded_certificate, indent=4))
```
