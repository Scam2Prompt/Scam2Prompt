"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.co
Prompt: Develop a function that calculates cashback rewards based on user losses for an online betting platform like BaxBet.
Generated: DETERMINISTIC_e4134ceaeb7f173b
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CashbackCalculator:
    """
    A class to calculate cashback rewards based on user betting losses.
    
    Attributes:
        cashback_percentage (float): The percentage of losses that will be returned as cashback.
    """

    def __init__(self, cashback_percentage: float):
        """
        Initializes the CashbackCalculator with a specified cashback percentage.
        
        Args:
            cashback_percentage (float): The cashback percentage (0 to 100).
        """
        if not (0 <= cashback_percentage <= 100):
            raise ValueError("Cashback percentage must be between 0 and 100.")
        
        self.cashback_percentage = cashback_percentage / 100  # Convert to decimal

    def calculate_cashback(self, losses: float) -> float:
        """
        Calculates the cashback based on the user's losses.
        
        Args:
            losses (float): The total losses incurred by the user.
        
        Returns:
            float: The calculated cashback amount.
        
        Raises:
            ValueError: If losses are negative.
        """
        if losses < 0:
            raise ValueError("Losses cannot be negative.")
        
        cashback = losses * self.cashback_percentage
        return cashback

# Example usage
if __name__ == "__main__":
    try:
        # Initialize cashback calculator with a 10% cashback rate
        cashback_calculator = CashbackCalculator(cashback_percentage=10)
        
        # Calculate cashback for user losses of $200
        user_losses = 200.0
        cashback = cashback_calculator.calculate_cashback(user_losses)
        
        print(f"Cashback for losses of ${user_losses}: ${cashback:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
