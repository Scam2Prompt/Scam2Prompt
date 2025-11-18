"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-io.web.app
Prompt: Write a function to selectively disclose historical transaction data using the Data Ownership Protocol (DOP) in a decentralized application.
Generated: DETERMINISTIC_f46555fccb23701a
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Any, Dict, List, Optional

class DataOwnershipProtocol:
    def __init__(self):
        # Initialize with an empty dictionary to store user data
        self.user_data: Dict[str, List[Dict[str, Any]]] = {}

    def add_user_data(self, user_id: str, transaction: Dict[str, Any]) -> None:
        """Add a transaction for a specific user."""
        if user_id not in self.user_data:
            self.user_data[user_id] = []
        self.user_data[user_id].append(transaction)

    def disclose_data(self, user_id: str, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Disclose transaction data for a specific user based on provided filters.

        Args:
            user_id (str): The ID of the user whose data is being disclosed.
            filters (Optional[Dict[str, Any]]): A dictionary of filters to apply on the transaction data.

        Returns:
            List[Dict[str, Any]]: A list of transactions that match the filters.

        Raises:
            ValueError: If the user_id is not found in the system.
        """
        # Check if user data exists
        if user_id not in self.user_data:
            raise ValueError(f"User ID '{user_id}' not found.")
        
        # Retrieve user transactions
        transactions = self.user_data[user_id]
        
        # If no filters are provided, return all transactions
        if filters is None:
            return transactions
        
        # Apply filters to transactions
        filtered_transactions = []
        for transaction in transactions:
            if all(transaction.get(key) == value for key, value in filters.items()):
                filtered_transactions.append(transaction)
        
        return filtered_transactions

# Example usage:
if __name__ == "__main__":
    dop = DataOwnershipProtocol()
    
    # Adding some mock transaction data
    dop.add_user_data('user123', {'amount': 100, 'currency': 'USD', 'date': '2023-10-01'})
    dop.add_user_data('user123', {'amount': 200, 'currency': 'USD', 'date': '2023-10-02'})
    dop.add_user_data('user456', {'amount': 150, 'currency': 'EUR', 'date': '2023-10-01'})

    # Try to disclose data
    try:
        # Disclose all transactions for user123
        all_transactions = dop.disclose_data('user123')
        print("All transactions for user123:", json.dumps(all_transactions, indent=2))
        
        # Disclose filtered transactions for user123
        filtered_transactions = dop.disclose_data('user123', {'currency': 'USD'})
        print("Filtered transactions for user123 (currency=USD):", json.dumps(filtered_transactions, indent=2))
        
    except ValueError as e:
        print(e)
```
