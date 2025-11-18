"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olliivveemmaaiinn12893891bndjdbiqw.pages.dev
Prompt: Create a function in Python to track and display metrics like "Total Deposits" and "Active Restakers," similar to the statistics shown on the webpage.
Generated: DETERMINISTIC_4a85b1b581fb4034
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, List

class MetricsTracker:
    """
    A class to track and display metrics such as 'Total Deposits' and 'Active Restakers'.
    """

    def __init__(self):
        """
        Initialize the MetricsTracker with default values.
        """
        self.total_deposits = 0.0  # Sum of all deposits
        self.active_restakers = set()  # Unique identifiers of active restakers

    def record_deposit(self, user_id: str, amount: float):
        """
        Record a deposit and update metrics.

        Args:
            user_id (str): Unique identifier for the user making the deposit.
            amount (float): The amount of deposit made.

        Raises:
            ValueError: If the deposit amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        self.total_deposits += amount
        self.active_restakers.add(user_id)

    def get_metrics(self) -> Dict[str, float or int]:
        """
        Retrieve the current metrics.

        Returns:
            dict: A dictionary containing the metrics 'Total Deposits' and 'Active Restakers'.
        """
        return {
            "Total Deposits": self.total_deposits,
            "Active Restakers": len(self.active_restakers)
        }

    def display_metrics(self):
        """
        Display the current metrics in a user-friendly format.
        """
        metrics = self.get_metrics()
        print("=== Metrics ===")
        print(f"Total Deposits: ${metrics['Total Deposits']:.2f}")
        print(f"Active Restakers: {metrics['Active Restakers']}")


# Example usage: Uncomment the lines below to test the code
# tracker = MetricsTracker()
# tracker.record_deposit("user1", 100.5)
# tracker.record_deposit("user2", 200.0)
# tracker.record_deposit("user1", 50.0)
# tracker.display_metrics()
```
