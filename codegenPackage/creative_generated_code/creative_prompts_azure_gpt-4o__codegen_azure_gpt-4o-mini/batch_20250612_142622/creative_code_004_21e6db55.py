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
import uuid
import json
import datetime
from typing import List, Dict

class CertificateOfOrigin:
    def __init__(self, transaction_id: str, sender: str, receiver: str, amount: float, notes: str = ""):
        """
        Initialize a Certificate of Origin for a Bitcoin transaction.

        :param transaction_id: Unique identifier for the transaction
        :param sender: Bitcoin address of the sender
        :param receiver: Bitcoin address of the receiver
        :param amount: Amount of Bitcoin being transacted
        :param notes: Additional notes about the transaction
        """
        self.transaction_id = transaction_id
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.notes = notes
        self.timestamp = datetime.datetime.now().isoformat()
        self.certificate_id = str(uuid.uuid4())

    def to_dict(self) -> Dict:
        """
        Convert the certificate details to a dictionary format.

        :return: Dictionary representation of the certificate
        """
        return {
            "certificate_id": self.certificate_id,
            "transaction_id": self.transaction_id,
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "notes": self.notes,
            "timestamp": self.timestamp
        }

    def to_json(self) -> str:
        """
        Convert the certificate details to a JSON string.

        :return: JSON representation of the certificate
        """
        return json.dumps(self.to_dict(), indent=4)

class CertificateManager:
    def __init__(self):
        """
        Initialize CertificateManager to manage certificates of origin.
        """
        self.certificates: List[CertificateOfOrigin] = []

    def create_certificate(self, transaction_id: str, sender: str, receiver: str, amount: float, notes: str = "") -> CertificateOfOrigin:
        """
        Create a new certificate of origin.

        :param transaction_id: Unique identifier for the transaction
        :param sender: Bitcoin address of the sender
        :param receiver: Bitcoin address of the receiver
        :param amount: Amount of Bitcoin being transacted
        :param notes: Additional notes about the transaction
        :return: The created CertificateOfOrigin instance
        """
        # Validate input parameters
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        certificate = CertificateOfOrigin(transaction_id, sender, receiver, amount, notes)
        self.certificates.append(certificate)
        return certificate

    def get_certificate(self, certificate_id: str) -> CertificateOfOrigin:
        """
        Retrieve a certificate by its unique ID.

        :param certificate_id: The unique ID of the certificate
        :return: The CertificateOfOrigin instance
        :raises ValueError: If the certificate is not found
        """
        for cert in self.certificates:
            if cert.certificate_id == certificate_id:
                return cert
        raise ValueError("Certificate not found.")

    def list_certificates(self) -> List[Dict]:
        """
        List all certificates in a dictionary format.

        :return: List of dictionaries representing all certificates
        """
        return [cert.to_dict() for cert in self.certificates]

# Example usage
if __name__ == "__main__":
    try:
        manager = CertificateManager()
        
        # Create a new certificate
        cert = manager.create_certificate(transaction_id="txn_123456", sender="1A2B3C4D5E6F", 
                                           receiver="6F5E4D3C2B1A", amount=0.5, notes="First transaction")
        
        print("New Certificate Created:")
        print(cert.to_json())

        # List all certificates
        print("All Certificates:")
        print(json.dumps(manager.list_certificates(), indent=4))
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
```
