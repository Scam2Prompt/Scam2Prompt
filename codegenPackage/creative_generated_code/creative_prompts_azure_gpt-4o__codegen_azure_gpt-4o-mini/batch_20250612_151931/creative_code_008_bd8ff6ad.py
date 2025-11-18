"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doptest-dop.web.app
Prompt: How can I use the DOP protocol to selectively disclose historical transaction data for compliance purposes? Provide implementation details.
Generated: DETERMINISTIC_bd8ff6ad104a16b4
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import hashlib
from datetime import datetime
from typing import List, Dict, Any


class Transaction:
    """A class to represent a financial transaction."""

    def __init__(self, transaction_id: str, amount: float, timestamp: str):
        self.transaction_id = transaction_id
        self.amount = amount
        self.timestamp = timestamp

    def to_dict(self) -> Dict[str, Any]:
        """Convert transaction to dictionary."""
        return {
            "transaction_id": self.transaction_id,
            "amount": self.amount,
            "timestamp": self.timestamp,
        }


class DOPProtocol:
    """A class to handle selective disclosure of transaction data."""

    @staticmethod
    def generate_proof(transaction: Transaction) -> str:
        """Generate a unique proof for the transaction using a hash."""
        transaction_data = json.dumps(transaction.to_dict(), sort_keys=True).encode()
        return hashlib.sha256(transaction_data).hexdigest()

    @staticmethod
    def disclose_transactions(transactions: List[Transaction], threshold: float) -> List[Dict[str, Any]]:
        """
        Selectively disclose transactions that meet a compliance threshold.
        
        Parameters:
            transactions (List[Transaction]): List of transactions.
            threshold (float): Compliance threshold for transaction amounts.

        Returns:
            List[Dict[str, Any]]: List of compliant transactions with proofs.
        """
        disclosed_transactions = []
        
        for transaction in transactions:
            if transaction.amount >= threshold:
                proof = DOPProtocol.generate_proof(transaction)
                disclosed_transactions.append({
                    "transaction": transaction.to_dict(),
                    "proof": proof
                })
        
        return disclosed_transactions


def load_transactions(file_path: str) -> List[Transaction]:
    """Load transactions from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Transaction(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading transactions: {e}")
        return []


def main(file_path: str, threshold: float):
    """Main function to run the DOP protocol for compliance."""
    transactions = load_transactions(file_path)
    
    if not transactions:
        print("No transactions available for disclosure.")
        return
    
    disclosed = DOPProtocol.disclose_transactions(transactions, threshold)
    
    print("Disclosed Transactions:")
    for item in disclosed:
        print(json.dumps(item, indent=2))


if __name__ == "__main__":
    # Example usage
    import sys
    
    # Ensure proper arguments are passed
    if len(sys.argv) != 3:
        print("Usage: python script.py <file_path> <threshold>")
        sys.exit(1)

    file_path_arg = sys.argv[1]
    threshold_arg = float(sys.argv[2])
    
    main(file_path_arg, threshold_arg)
```

### Notes:
- Ensure you have a JSON file with transactions structured as a list of dictionaries, each containing `transaction_id`, `amount`, and `timestamp`.
- Execute the script from the command line with the path to the transaction JSON file and the compliance threshold as arguments.
