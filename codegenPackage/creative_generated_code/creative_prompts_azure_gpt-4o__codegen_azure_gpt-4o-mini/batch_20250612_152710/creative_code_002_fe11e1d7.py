"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao-9ar.pages.dev
Prompt: Generate code to calculate subscription metrics (e.g., "0.6x subscribed") for a token offering, based on deposit data and total allocation.
Generated: DETERMINISTIC_fe11e1d7b9c33a63
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SubscriptionMetrics:
    """
    A class to calculate subscription metrics for a token offering.
    """

    def __init__(self, total_allocation: float):
        """
        Initialize the SubscriptionMetrics class.

        :param total_allocation: Total amount of tokens available for distribution.
        """
        if total_allocation <= 0:
            raise ValueError("Total allocation must be greater than zero.")
        self.total_allocation = total_allocation
        self.deposits = []

    def add_deposit(self, deposit_amount: float):
        """
        Add a deposit to the subscription metrics.

        :param deposit_amount: The amount of tokens deposited by a user.
        """
        if deposit_amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.deposits.append(deposit_amount)

    def calculate_subscribed_ratio(self) -> float:
        """
        Calculate the subscribed ratio based on total deposits and total allocation.

        :return: The subscribed ratio as a float.
        """
        total_deposited = sum(self.deposits)
        if total_deposited <= 0:
            return 0.0  # No deposits have been made

        subscribed_ratio = total_deposited / self.total_allocation
        return subscribed_ratio

    def get_metrics(self) -> str:
        """
        Get a string representation of the subscription metrics.

        :return: A formatted string showing the subscribed ratio.
        """
        try:
            ratio = self.calculate_subscribed_ratio()
            return f"{ratio:.1f}x subscribed"  # Format to one decimal place
        except Exception as e:
            return f"Error calculating metrics: {str(e)}"


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize metrics with a total allocation of 1000 tokens
        metrics = SubscriptionMetrics(total_allocation=1000)
        
        # Add some deposits
        metrics.add_deposit(200)
        metrics.add_deposit(300)
        metrics.add_deposit(500)
        
        # Get and print the subscription metrics
        print(metrics.get_metrics())  # Output: "1.0x subscribed"
        
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
