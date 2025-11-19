"""
Generated Code Metadata:
========================
Original URL: https://epep-flip.vercel.app
Prompt: Compare the transaction processes with and without wallet confirmation on EPEP, focusing on the differences in fee inclusion.
Generated: DETERMINISTIC_221fcaf75e9fd3c6
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict

class Transaction:
    def __init__(self, 
                 transaction_hash: str, 
                 block_number: int, 
                 gas_price: float, 
                 gas_used: int, 
                 transaction_fee: float):
        """
        Initialize a Transaction object.

        Args:
        transaction_hash (str): The hash of the transaction.
        block_number (int): The block number of the transaction.
        gas_price (float): The gas price of the transaction.
        gas_used (int): The gas used by the transaction.
        transaction_fee (float): The transaction fee.
        """
        self.transaction_hash = transaction_hash
        self.block_number = block_number
        self.gas_price = gas_price
        self.gas_used = gas_used
        self.transaction_fee = transaction_fee

class EPEPTransactionComparator:
    def __init__(self, 
                 transactions_with_confirmation: list, 
                 transactions_without_confirmation: list):
        """
        Initialize an EPEPTransactionComparator object.

        Args:
        transactions_with_confirmation (list): A list of Transaction objects with wallet confirmation.
        transactions_without_confirmation (list): A list of Transaction objects without wallet confirmation.
        """
        self.transactions_with_confirmation = transactions_with_confirmation
        self.transactions_without_confirmation = transactions_without_confirmation

    def compare_fee_inclusion(self) -> Dict:
        """
        Compare the transaction processes with and without wallet confirmation on EPEP.

        Returns:
        Dict: A dictionary containing the comparison results.
        """
        # Calculate total fees with and without confirmation
        total_fee_with_confirmation = sum(t.transaction_fee for t in self.transactions_with_confirmation)
        total_fee_without_confirmation = sum(t.transaction_fee for t in self.transactions_without_confirmation)

        # Calculate average fees with and without confirmation
        avg_fee_with_confirmation = total_fee_with_confirmation / len(self.transactions_with_confirmation) if self.transactions_with_confirmation else 0
        avg_fee_without_confirmation = total_fee_without_confirmation / len(self.transactions_without_confirmation) if self.transactions_without_confirmation else 0

        # Create a dictionary to store the comparison results
        comparison_results = {
            "total_fee_with_confirmation": total_fee_with_confirmation,
            "total_fee_without_confirmation": total_fee_without_confirmation,
            "avg_fee_with_confirmation": avg_fee_with_confirmation,
            "avg_fee_without_confirmation": avg_fee_without_confirmation,
        }

        return comparison_results

def load_transactions_from_json(file_path: str) -> list:
    """
    Load transactions from a JSON file.

    Args:
    file_path (str): The path to the JSON file.

    Returns:
    list: A list of Transaction objects.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            transactions = []
            for transaction_data in data:
                transaction = Transaction(
                    transaction_hash=transaction_data['transaction_hash'],
                    block_number=transaction_data['block_number'],
                    gas_price=transaction_data['gas_price'],
                    gas_used=transaction_data['gas_used'],
                    transaction_fee=transaction_data['transaction_fee']
                )
                transactions.append(transaction)
            return transactions
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return []

def main():
    # Load transactions with and without confirmation from JSON files
    transactions_with_confirmation = load_transactions_from_json('transactions_with_confirmation.json')
    transactions_without_confirmation = load_transactions_from_json('transactions_without_confirmation.json')

    # Create an EPEPTransactionComparator object
    comparator = EPEPTransactionComparator(transactions_with_confirmation, transactions_without_confirmation)

    # Compare fee inclusion
    comparison_results = comparator.compare_fee_inclusion()

    # Print comparison results
    print(json.dumps(comparison_results, indent=4))

if __name__ == "__main__":
    main()
```

**Example JSON files:**

`transactions_with_confirmation.json`:
```json
[
    {
        "transaction_hash": "0x123",
        "block_number": 100,
        "gas_price": 20.0,
        "gas_used": 1000,
        "transaction_fee": 0.02
    },
    {
        "transaction_hash": "0x456",
        "block_number": 101,
        "gas_price": 25.0,
        "gas_used": 1200,
        "transaction_fee": 0.03
    }
]
```

`transactions_without_confirmation.json`:
```json
[
    {
        "transaction_hash": "0x789",
        "block_number": 102,
        "gas_price": 15.0,
        "gas_used": 800,
        "transaction_fee": 0.012
    },
    {
        "transaction_hash": "0x012",
        "block_number": 103,
        "gas_price": 30.0,
        "gas_used": 1500,
        "transaction_fee": 0.045
    }
]
```
