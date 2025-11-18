"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emarlado.com
Prompt: Generate code to calculate swap fees for Forex trading, referencing the concept of swap fees mentioned on Emarlado's website.
Generated: DETERMINISTIC_e8abcf91cd1e2af4
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ForexSwapCalculator:
    """
    A class to calculate swap fees for Forex trading.
    
    Attributes:
    ----------
    notional_amount : float
        The notional amount in the base currency.
    swap_rate : float
        The swap rate provided by the broker (can be positive or negative).
    days : int
        The number of days the position is held.
    """
    
    def __init__(self, notional_amount: float, swap_rate: float, days: int):
        """
        Initializes the ForexSwapCalculator with the given parameters.
        
        Parameters:
        ----------
        notional_amount : float
            The notional amount in the base currency.
        swap_rate : float
            The swap rate provided by the broker in points.
        days : int
            The number of days the position is held.
        """
        self.notional_amount = notional_amount
        self.swap_rate = swap_rate
        self.days = days

    def calculate_swap_fee(self) -> float:
        """
        Calculates the swap fee based on the notional amount, swap rate, and days held.
        
        Returns:
        -------
        float
            The calculated swap fee in the quote currency.
        """
        try:
            # Validate inputs
            if self.notional_amount <= 0:
                raise ValueError("Notional amount must be greater than zero.")
            if self.days < 0:
                raise ValueError("Days must be zero or a positive integer.")
            
            # Calculate the swap fee
            swap_fee = (self.notional_amount * self.swap_rate * self.days) / 10000
            return swap_fee
        
        except Exception as e:
            print(f"Error calculating swap fee: {e}")
            return 0.0

# Example usage
if __name__ == "__main__":
    # Define parameters for the swap fee calculation
    notional_amount = 10000  # Amount in base currency
    swap_rate = -2.5         # Swap rate in points (negative indicates a cost)
    days = 3                  # Position held for 3 days

    # Create a swap calculator instance
    swap_calculator = ForexSwapCalculator(notional_amount, swap_rate, days)
    
    # Calculate and print the swap fee
    swap_fee = swap_calculator.calculate_swap_fee()
    print(f"The swap fee for holding the position is: {swap_fee:.2f} in the quote currency.")
```
