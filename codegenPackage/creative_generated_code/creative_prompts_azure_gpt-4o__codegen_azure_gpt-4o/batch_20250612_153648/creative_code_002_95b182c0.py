"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aasdkfosdkfoskdo.web.app
Prompt: Provide a Python implementation to detect bots based on transaction failure rates (>=25%) and circular transaction behavior, as described in the JUР allocation criteria.
Generated: DETERMINISTIC_95b182c0ca62a725
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import collections
from typing import List, Dict, Any


class BotDetector:
    """
    A class to detect bots based on transaction failure rates and circular transaction behavior.
    """

    def __init__(self, transactions: List[Dict[str, Any]]):
        """
        Initializes the BotDetector with a list of transactions.

        Args:
            transactions (List[Dict[str, Any]]): List of transaction records.
        """
        self.transactions = transactions

    def detect_bots(self) -> List[str]:
        """
        Detects bots based on transaction failure rates and circular transaction behavior.

        Returns:
            List[str]: List of user IDs identified as bots.
        """
        # Collect transaction data per user
        user_data = collections.defaultdict(lambda: {"failures": 0, "total": 0, "targets": set()})

        for transaction in self.transactions:
            try:
                user_id = transaction["user_id"]
                target_id = transaction["target_id"]
                status = transaction["status"]

                # Update transaction counts
                user_data[user_id]["total"] += 1
                if status == "failure":
                    user_data[user_id]["failures"] += 1

                # Track targets for circular transaction detection
                user_data[user_id]["targets"].add(target_id)
            except KeyError:
                # Handle cases with missing keys in transaction data
                print("Invalid transaction format:", transaction)

        bots = []

        for user_id, data in user_data.items():
            try:
                failure_rate = data["failures"] / data["total"]

                # Check failure rate criterion (>= 25%)
                if failure_rate >= 0.25:
                    bots.append(user_id)

                # Check circular transaction behavior
                for target_id in data["targets"]:
                    if target_id in user_data and user_id in user_data[target_id]["targets"]:
                        bots.append(user_id)
                        break  # No need to add the user multiple times
            except ZeroDivisionError:
                # Handle cases where "total" is zero (no transactions)
                print(f"User {user_id} has no transactions. Skipping.")
            except Exception as e:
                # Catch any unexpected errors during processing
                print(f"Error processing user {user_id}: {e}")

        return list(set(bots))  # Remove duplicates


# Example usage
if __name__ == "__main__":
    # Sample transaction data
    transactions = [
        {"user_id": "user1", "target_id": "user2", "status": "failure"},
        {"user_id": "user1", "target_id": "user3", "status": "success"},
        {"user_id": "user2", "target_id": "user1", "status": "failure"},
        {"user_id": "user2", "target_id": "user3", "status": "success"},
        {"user_id": "user3", "target_id": "user2", "status": "failure"},
        {"user_id": "user3", "target_id": "user1", "status": "failure"},
        {"user_id": "user3", "target_id": "user2", "status": "failure"},
        {"user_id": "user1", "target_id": "user2", "status": "success"},
    ]

    detector = BotDetector(transactions)
    bot_users = detector.detect_bots()

    print("Detected bots:", bot_users)
```
