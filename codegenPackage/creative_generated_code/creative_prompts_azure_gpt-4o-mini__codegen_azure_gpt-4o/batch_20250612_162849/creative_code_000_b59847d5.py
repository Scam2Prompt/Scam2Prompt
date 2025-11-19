"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonfoundation.com
Prompt: How can I implement a secure buying process for domain transactions similar to the one described on tonfoundation.com?
Generated: DETERMINISTIC_b59847d560233e9e
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime
from hashlib import sha256
import hmac
import json


class DomainTransaction:
    """
    Class to handle domain buying transactions securely.
    """

    def __init__(self, domain_name, buyer_id, seller_id, price, secret_key):
        """
        Initialize the transaction object with domain details and participants.
        :param domain_name: Name of the domain being transacted
        :param buyer_id: ID of the buyer
        :param seller_id: ID of the seller
        :param price: Price of the domain
        :param secret_key: Secret key for HMAC signature validation
        """
        self.domain_name = domain_name
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.price = price
        self.secret_key = secret_key
        self.transaction_id = str(uuid.uuid4())
        self.timestamp = datetime.utcnow()
        self.is_completed = False

    def generate_signature(self):
        """
        Generate a HMAC signature for the transaction to ensure integrity.
        :return: HMAC signature as a string
        """
        message = f"{self.transaction_id}|{self.domain_name}|{self.buyer_id}|{self.seller_id}|{self.price}|{self.timestamp.isoformat()}"
        signature = hmac.new(self.secret_key.encode(), message.encode(), sha256).hexdigest()
        return signature

    def verify_signature(self, provided_signature):
        """
        Verify the HMAC signature to ensure the transaction details are intact.
        :param provided_signature: The signature to verify
        :return: True if the signature matches, False otherwise
        """
        expected_signature = self.generate_signature()
        return hmac.compare_digest(expected_signature, provided_signature)

    def complete_transaction(self):
        """
        Complete the transaction by marking it as completed and logging the details.
        :return: Transaction summary as a dictionary
        """
        if self.is_completed:
            raise Exception("Transaction already completed.")
        
        self.is_completed = True
        return {
            "transaction_id": self.transaction_id,
            "domain_name": self.domain_name,
            "buyer_id": self.buyer_id,
            "seller_id": self.seller_id,
            "price": self.price,
            "timestamp": self.timestamp.isoformat(),
            "signature": self.generate_signature(),
            "status": "completed"
        }


# Error handling example
def secure_domain_transaction(domain_name, buyer_id, seller_id, price, secret_key):
    """
    A function to securely handle a domain transaction.
    :param domain_name: Name of the domain being transacted
    :param buyer_id: ID of the buyer
    :param seller_id: ID of the seller
    :param price: Price of the domain
    :param secret_key: Secret key for HMAC signature
    :return: Transaction summary if successful, error message otherwise
    """
    try:
        # Create a transaction instance
        transaction = DomainTransaction(domain_name, buyer_id, seller_id, price, secret_key)

        # Generate and verify signature for demonstration purposes
        signature = transaction.generate_signature()
        if not transaction.verify_signature(signature):
            raise Exception("Signature verification failed.")

        # Complete the transaction
        transaction_summary = transaction.complete_transaction()
        return json.dumps(transaction_summary, indent=4)

    except Exception as e:
        return f"Error: {str(e)}"


# Example usage
if __name__ == "__main__":
    try:
        domain_name = "example.com"
        buyer_id = "buyer123"
        seller_id = "seller456"
        price = 5000
        secret_key = "supersecretkey"

        result = secure_domain_transaction(domain_name, buyer_id, seller_id, price, secret_key)
        print(result)

    except Exception as e:
        print(f"Fatal error: {str(e)}")
```
