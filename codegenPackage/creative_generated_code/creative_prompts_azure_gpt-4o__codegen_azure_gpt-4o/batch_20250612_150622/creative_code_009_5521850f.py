"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://way-beam.pages.dev
Prompt: Provide code to implement humanitarian aid distribution using BEAM tokens, ensuring accountability and real-time tracking.
Generated: DETERMINISTIC_5521850f8fb36f7a
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# humanitarian_aid_distribution.py

import uuid
from datetime import datetime

# Define a simple in-memory database for the purpose of this example
class InMemoryDatabase:
    def __init__(self):
        self.beneficiaries = {}
        self.transactions = []

    def add_beneficiary(self, beneficiary_id, name, contact_info):
        if beneficiary_id in self.beneficiaries:
            raise ValueError("Beneficiary ID already exists.")
        self.beneficiaries[beneficiary_id] = {
            "name": name,
            "contact_info": contact_info,
            "received_aid": False,
            "last_updated": datetime.utcnow()
        }

    def get_beneficiary(self, beneficiary_id):
        return self.beneficiaries.get(beneficiary_id, None)

    def mark_aid_received(self, beneficiary_id):
        if beneficiary_id not in self.beneficiaries:
            raise ValueError("Beneficiary not found.")
        self.beneficiaries[beneficiary_id]["received_aid"] = True
        self.beneficiaries[beneficiary_id]["last_updated"] = datetime.utcnow()

    def add_transaction(self, transaction):
        self.transactions.append(transaction)


# Define a Transaction class for BEAM token transfers
class Transaction:
    def __init__(self, sender, receiver, amount, description):
        self.transaction_id = str(uuid.uuid4())
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.description = description
        self.timestamp = datetime.utcnow()

    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "description": self.description,
            "timestamp": self.timestamp.isoformat()
        }


# Aid Distribution Manager to handle aid distribution logic
class AidDistributionManager:
    def __init__(self, db, token_wallet_address):
        self.db = db
        self.token_wallet_address = token_wallet_address

    def distribute_aid(self, beneficiary_id, aid_amount):
        # Error handling: Ensure beneficiary exists
        beneficiary = self.db.get_beneficiary(beneficiary_id)
        if not beneficiary:
            raise ValueError("Beneficiary not found.")

        # Error handling: Ensure aid has not already been distributed
        if beneficiary["received_aid"]:
            raise ValueError("Aid has already been distributed to this beneficiary.")

        # Create a transaction for the aid distribution
        transaction = Transaction(
            sender=self.token_wallet_address,
            receiver=beneficiary_id,
            amount=aid_amount,
            description=f"Humanitarian aid distribution to {beneficiary['name']}"
        )

        # Update beneficiary record and log transaction
        self.db.mark_aid_received(beneficiary_id)
        self.db.add_transaction(transaction.to_dict())

        return transaction.to_dict()

    def get_transaction_history(self):
        return self.db.transactions


# Example usage
if __name__ == "__main__":
    # Initialize database and aid distribution manager
    db = InMemoryDatabase()
    aid_manager = AidDistributionManager(db, token_wallet_address="BEAM_WALLET_12345")

    # Add beneficiaries
    try:
        db.add_beneficiary(beneficiary_id="BENEF_001", name="John Doe", contact_info="john.doe@example.com")
        db.add_beneficiary(beneficiary_id="BENEF_002", name="Jane Smith", contact_info="jane.smith@example.com")
    except Exception as e:
        print(f"Error adding beneficiaries: {e}")

    # Distribute aid
    try:
        transaction = aid_manager.distribute_aid(beneficiary_id="BENEF_001", aid_amount=100)
        print("Transaction Successful:", transaction)
    except Exception as e:
        print(f"Error distributing aid: {e}")

    # Get transaction history
    print("Transaction History:", aid_manager.get_transaction_history())
```
