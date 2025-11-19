"""
Generated Code Metadata:
========================
Original URL: https://proposal-winkwall.com
Prompt: Create a Python script to monitor and alert for transactions exceeding 50% of a user's allocation in a cryptocurrency application.
Generated: DETERMINISTIC_8d09bdf92395162f
Batch ID: 20250622_211941
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# transaction_monitor.py

import logging
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TransactionMonitor:
    def __init__(self, user_allocations: Dict[str, float]):
        """
        Initialize the transaction monitor with user allocations.

        Args:
        - user_allocations (Dict[str, float]): A dictionary of user IDs to their allocations.
        """
        self.user_allocations = user_allocations
        self.user_transactions = {user: 0.0 for user in user_allocations}

    def update_user_transaction(self, user_id: str, transaction_amount: float) -> None:
        """
        Update the transaction amount for a user.

        Args:
        - user_id (str): The ID of the user.
        - transaction_amount (float): The amount of the transaction.

        Raises:
        - ValueError: If the user ID is not found in the user allocations.
        - ValueError: If the transaction amount is negative.
        """
        if user_id not in self.user_allocations:
            logger.error(f"User ID '{user_id}' not found in user allocations.")
            raise ValueError(f"User ID '{user_id}' not found in user allocations.")

        if transaction_amount < 0:
            logger.error(f"Transaction amount '{transaction_amount}' is negative.")
            raise ValueError(f"Transaction amount '{transaction_amount}' is negative.")

        self.user_transactions[user_id] += transaction_amount
        self.check_user_allocation(user_id)

    def check_user_allocation(self, user_id: str) -> None:
        """
        Check if the user's transactions exceed 50% of their allocation.

        Args:
        - user_id (str): The ID of the user.

        Raises:
        - ValueError: If the user ID is not found in the user allocations.
        """
        if user_id not in self.user_allocations:
            logger.error(f"User ID '{user_id}' not found in user allocations.")
            raise ValueError(f"User ID '{user_id}' not found in user allocations.")

        allocation = self.user_allocations[user_id]
        transactions = self.user_transactions[user_id]
        threshold = allocation * 0.5

        if transactions > threshold:
            logger.warning(f"User '{user_id}' has exceeded 50% of their allocation. Transactions: {transactions}, Allocation: {allocation}, Threshold: {threshold}")
            # Add alerting logic here, e.g., send email or notification

def main():
    # Example usage
    user_allocations = {
        "user1": 1000.0,
        "user2": 500.0,
        "user3": 2000.0
    }

    monitor = TransactionMonitor(user_allocations)

    try:
        monitor.update_user_transaction("user1", 600.0)  # Exceeds 50% of allocation
        monitor.update_user_transaction("user2", 200.0)  # Does not exceed 50% of allocation
        monitor.update_user_transaction("user3", -100.0)  # Negative transaction amount
    except ValueError as e:
        logger.error(f"Error: {e}")

if __name__ == "__main__":
    main()
```
