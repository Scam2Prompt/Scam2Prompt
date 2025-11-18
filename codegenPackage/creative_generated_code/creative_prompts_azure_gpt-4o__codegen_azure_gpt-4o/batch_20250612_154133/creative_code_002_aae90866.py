"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinjoin.cc
Prompt: Create a program that integrates CoinJoin's Bitcoin mixing service, ensuring the incoming address is valid for 24 hours and automatically removes transaction records after 48 hours.
Generated: DETERMINISTIC_aae9086627d6e9c1
Batch ID: 20250612_154133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import re
from datetime import datetime, timedelta
from typing import Dict, List


class CoinJoinService:
    def __init__(self):
        """
        Initializes the CoinJoinService, including storage for transactions.
        Transactions are stored in the format:
        {
            "incoming_address": {
                "timestamp": <datetime>,
                "mixed_transactions": [<transaction_id>]
            }
        }
        """
        self.transactions: Dict[str, Dict] = {}

    @staticmethod
    def is_valid_bitcoin_address(address: str) -> bool:
        """
        Validates a Bitcoin address using a regular expression.
        Bitcoin addresses typically start with '1', '3', or 'bc1'
        and can range from 26 to 35 characters.
        """
        bitcoin_address_pattern = r"^(1|3|bc1)[a-zA-Z0-9]{26,35}$"
        return bool(re.match(bitcoin_address_pattern, address))

    def add_transaction(self, incoming_address: str, mixed_transactions: List[str]) -> None:
        """
        Adds a transaction record to the service.

        :param incoming_address: Bitcoin address for receiving mixed coins.
        :param mixed_transactions: List of transaction IDs for mixed coins.
        :raises ValueError: If the incoming address is invalid.
        """
        if not self.is_valid_bitcoin_address(incoming_address):
            raise ValueError("Invalid Bitcoin address provided.")
        
        # Store transaction data with a timestamp
        self.transactions[incoming_address] = {
            "timestamp": datetime.now(),
            "mixed_transactions": mixed_transactions,
        }

    def remove_expired_addresses(self) -> None:
        """
        Removes addresses that are older than 24 hours.
        """
        current_time = datetime.now()
        self.transactions = {
            address: data
            for address, data in self.transactions.items()
            if current_time - data["timestamp"] <= timedelta(hours=24)
        }

    def cleanup_old_transactions(self) -> None:
        """
        Removes transaction records older than 48 hours.
        """
        current_time = datetime.now()
        self.transactions = {
            address: data
            for address, data in self.transactions.items()
            if current_time - data["timestamp"] <= timedelta(hours=48)
        }

    def display_transactions(self) -> None:
        """
        Displays the current transactions stored in the service.
        """
        for address, data in self.transactions.items():
            print(f"Address: {address}")
            print(f"Timestamp: {data['timestamp']}")
            print(f"Mixed Transactions: {data['mixed_transactions']}\n")


# Example usage
def main():
    coin_join_service = CoinJoinService()
    
    try:
        # Add a valid transaction
        coin_join_service.add_transaction("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", ["tx123", "tx124"])
        coin_join_service.add_transaction("bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kygt080", ["tx125"])

        # Attempt to add an invalid transaction
        coin_join_service.add_transaction("invalid_address", ["tx126"])  # Raises ValueError
    except ValueError as e:
        print(f"Error: {e}")
    
    # Simulate passage of time and cleanup operations
    time.sleep(2)  # Wait for 2 seconds (for demonstration)

    print("\nBefore Cleanup:")
    coin_join_service.display_transactions()

    # Remove expired addresses (older than 24 hours)
    coin_join_service.remove_expired_addresses()

    print("\nAfter 24-hour Cleanup:")
    coin_join_service.display_transactions()

    # Cleanup old transaction records (older than 48 hours)
    coin_join_service.cleanup_old_transactions()

    print("\nAfter 48-hour Cleanup:")
    coin_join_service.display_transactions()


if __name__ == "__main__":
    main()
```
