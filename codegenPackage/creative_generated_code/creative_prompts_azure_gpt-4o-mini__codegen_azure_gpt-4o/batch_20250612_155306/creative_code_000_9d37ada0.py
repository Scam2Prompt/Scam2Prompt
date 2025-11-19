"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotic.eu
Prompt: Generate a code snippet that demonstrates how to implement a commission-free direct acquisition feature for a service-oriented purchase processing system.
Generated: DETERMINISTIC_9d37ada06ea051e5
Batch ID: 20250612_155306
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

class DirectAcquisitionService:
    """
    Implements a commission-free direct acquisition feature for service-oriented purchase processing.
    """

    def __init__(self):
        # Dictionary to mock a database for storing purchase records
        self.purchase_records = {}

    def generate_transaction_id(self):
        """
        Generate a unique transaction ID.
        :return: UUID string
        """
        return str(uuid.uuid4())

    def process_purchase(self, user_id, service_id, amount):
        """
        Process a service purchase without commission.
        :param user_id: ID of the user purchasing the service
        :param service_id: ID of the service being purchased
        :param amount: Amount of the purchase (float)
        :return: Purchase record as a dictionary
        """
        # Validate input parameters
        if not user_id or not service_id or amount <= 0:
            raise ValueError("Invalid purchase parameters provided.")

        # Generate a unique transaction ID
        transaction_id = self.generate_transaction_id()

        # Create a record for the purchase
        purchase_record = {
            "transaction_id": transaction_id,
            "user_id": user_id,
            "service_id": service_id,
            "amount": amount,
            "purchase_date": datetime.utcnow().isoformat(),
            "status": "SUCCESS"
        }

        # Store the record in the mock database
        self.purchase_records[transaction_id] = purchase_record

        # Return the purchase record
        return purchase_record

    def get_purchase_record(self, transaction_id):
        """
        Retrieve a purchase record by transaction ID.
        :param transaction_id: Unique transaction ID
        :return: Purchase record as a dictionary
        """
        # Check if the transaction exists
        if transaction_id not in self.purchase_records:
            raise KeyError(f"Transaction ID {transaction_id} not found.")

        # Return the record
        return self.purchase_records[transaction_id]


# Example Usage
if __name__ == "__main__":
    # Initialize the DirectAcquisitionService
    service = DirectAcquisitionService()

    try:
        # Process a purchase
        purchase = service.process_purchase(user_id="12345", service_id="service001", amount=99.99)
        print("Purchase Successful:", purchase)

        # Retrieve the purchase record
        retrieved_record = service.get_purchase_record(transaction_id=purchase["transaction_id"])
        print("Retrieved Record:", retrieved_record)

    except ValueError as ve:
        print(f"Error: {ve}")
    except KeyError as ke:
        print(f"Error: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
