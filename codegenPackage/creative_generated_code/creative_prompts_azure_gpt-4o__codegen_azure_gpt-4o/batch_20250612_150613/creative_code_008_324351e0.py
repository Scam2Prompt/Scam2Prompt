"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-zielchain.vercel.app
Prompt: Write a program to detect and prevent prohibited activities, such as double NFT transfers or falsifying information, as specified in ZIELCHAIN's prohibited acts section.
Generated: DETERMINISTIC_324351e0ee8b1521
Batch ID: 20250612_150613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List

class NFTTransactionValidator:
    """
    Class to validate and detect prohibited activities in NFT transactions.
    """

    def __init__(self):
        # A database/mock store of NFT transactions
        self.nft_transactions = {}
        # List of prohibited activities
        self.prohibited_activities = [
            "double_transfer",
            "falsified_information",
        ]

    def load_nft_transactions(self, transactions: List[Dict]) -> None:
        """
        Load existing NFT transactions into the system.
        
        Args:
            transactions (List[Dict]): List of NFT transactions.
        """
        for transaction in transactions:
            nft_id = transaction.get("nft_id")
            if nft_id:
                self.nft_transactions[nft_id] = transaction

    def validate_transaction(self, new_transaction: Dict) -> Dict:
        """
        Validate a new NFT transaction for prohibited activities.

        Args:
            new_transaction (Dict): The new transaction to validate.

        Returns:
            Dict: Result indicating whether the transaction is valid or prohibited.
        """
        try:
            nft_id = new_transaction.get("nft_id")
            sender = new_transaction.get("sender")
            receiver = new_transaction.get("receiver")
            metadata = new_transaction.get("metadata")

            # Check for missing required fields
            if not nft_id or not sender or not receiver or not metadata:
                return {
                    "status": "error",
                    "message": "Missing required fields in transaction.",
                }

            # Check for double transfer
            if nft_id in self.nft_transactions:
                existing_receiver = self.nft_transactions[nft_id].get("receiver")
                if existing_receiver and existing_receiver != sender:
                    return {
                        "status": "prohibited",
                        "activity": "double_transfer",
                        "message": "NFT has already been transferred to a different receiver.",
                    }

            # Check for falsified information (basic example: tampered metadata)
            if "tampered" in metadata.lower():
                return {
                    "status": "prohibited",
                    "activity": "falsified_information",
                    "message": "Transaction contains falsified information.",
                }

            # Transaction is valid
            self.nft_transactions[nft_id] = new_transaction  # Update transaction history
            return {
                "status": "valid",
                "message": "Transaction is valid and recorded successfully.",
            }

        except Exception as e:
            # Handle unexpected errors in the transaction validation process
            return {
                "status": "error",
                "message": f"An error occurred during validation: {str(e)}",
            }

    def list_prohibited_activities(self) -> List[str]:
        """
        List all prohibited activities defined in the system.

        Returns:
            List[str]: List of prohibited activities.
        """
        return self.prohibited_activities


# Example usage of the NFTTransactionValidator class
if __name__ == "__main__":
    # Initialize the transaction validator
    validator = NFTTransactionValidator()

    # Load existing transactions (mock data)
    existing_transactions = [
        {"nft_id": "NFT001", "sender": "Alice", "receiver": "Bob", "metadata": "Original Metadata"},
    ]
    validator.load_nft_transactions(existing_transactions)

    # Validate a new transaction
    new_transaction = {
        "nft_id": "NFT001",
        "sender": "Bob",
        "receiver": "Charlie",
        "metadata": "Original Metadata",
    }
    result = validator.validate_transaction(new_transaction)
    print(json.dumps(result, indent=4))

    # Validate a transaction with tampered metadata
    tampered_transaction = {
        "nft_id": "NFT002",
        "sender": "Alice",
        "receiver": "Bob",
        "metadata": "Tampered Metadata",
    }
    result = validator.validate_transaction(tampered_transaction)
    print(json.dumps(result, indent=4))

    # Output all prohibited activities
    print("Prohibited Activities:", validator.list_prohibited_activities())
```
