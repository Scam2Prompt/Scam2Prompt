"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betbax.xyz
Prompt: Create a script that implements a cashback system for losses in a casino environment, inspired by the loyalty programs mentioned on BaxBet.
Generated: DETERMINISTIC_23bac4d9fd2b9f27
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CasinoCashback:
    """
    A class to represent a cashback system for losses in a casino environment.
    This system calculates cashback based on the user's losses over a defined period.
    """

    def __init__(self, cashback_percentage=0.05, max_cashback=100.0):
        """
        Initializes the CasinoCashback instance.

        Parameters:
        cashback_percentage (float): The percentage of losses returned as cashback.
        max_cashback (float): The maximum cashback amount that can be earned.
        """
        if cashback_percentage < 0 or cashback_percentage > 1:
            raise ValueError("Cashback percentage must be between 0 and 1.")
        if max_cashback < 0:
            raise ValueError("Maximum cashback must be non-negative.")

        self.cashback_percentage = cashback_percentage
        self.max_cashback = max_cashback
        self.losses = 0.0

    def record_loss(self, amount):
        """
        Records a loss amount.

        Parameters:
        amount (float): The amount lost by the user.

        Raises:
        ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Loss amount must be non-negative.")
        
        self.losses += amount

    def calculate_cashback(self):
        """
        Calculates the total cashback based on recorded losses.

        Returns:
        float: The total cashback amount.
        """
        cashback = self.losses * self.cashback_percentage
        return min(cashback, self.max_cashback)

    def reset_losses(self):
        """
        Resets the recorded losses.
        """
        self.losses = 0.0

    def __str__(self):
        """
        Returns a string representation of the current cashback state.
        """
        return f"Total Losses: ${self.losses:.2f}, Cashback Earned: ${self.calculate_cashback():.2f}"

# Example of using the CasinoCashback class
if __name__ == "__main__":
    try:
        cashback_system = CasinoCashback(cashback_percentage=0.1, max_cashback=50.0)
        
        # Simulating losses
        cashback_system.record_loss(200.0)
        cashback_system.record_loss(150.0)

        # Calculating and displaying cashback
        print(cashback_system)  # Total Losses and Cashback
        print(f"Cashback to claim: ${cashback_system.calculate_cashback():.2f}")

        # Resetting losses
        cashback_system.reset_losses()
        print("After reset:", cashback_system)

    except ValueError as e:
        print(f"Error: {e}")
```
