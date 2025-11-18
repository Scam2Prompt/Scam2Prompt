"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supercore-7hg.pages.dev
Prompt: Write a script to calculate slippage tolerance for token swaps and display warnings if the tolerance exceeds 0.5%.
Generated: DETERMINISTIC_e399ac7233aeb127
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class SlippageCalculator:
    """
    A class to calculate slippage tolerance for token swaps.
    """

    def __init__(self, expected_price: float, actual_price: float):
        """
        Initialize the SlippageCalculator with expected and actual prices.

        :param expected_price: The expected price of the token swap.
        :param actual_price: The actual price after the swap.
        """
        self.expected_price = expected_price
        self.actual_price = actual_price

    def calculate_slippage(self) -> float:
        """
        Calculate the slippage as a percentage.

        :return: The slippage percentage.
        """
        if self.expected_price <= 0:
            raise ValueError("Expected price must be greater than zero.")
        
        slippage = ((self.actual_price - self.expected_price) / self.expected_price) * 100
        return slippage

    def check_slippage_tolerance(self, tolerance: float = 0.5) -> None:
        """
        Check if the calculated slippage exceeds the specified tolerance.

        :param tolerance: The maximum allowable slippage tolerance in percentage.
        """
        try:
            slippage = self.calculate_slippage()
            print(f"Calculated slippage: {slippage:.2f}%")

            if abs(slippage) > tolerance:
                print(f"Warning: Slippage tolerance exceeded! (Tolerance: {tolerance}%)")
            else:
                print("Slippage is within the acceptable range.")

        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    # Example usage of the SlippageCalculator
    try:
        expected_price = float(input("Enter expected price: "))
        actual_price = float(input("Enter actual price: "))

        slippage_calculator = SlippageCalculator(expected_price, actual_price)
        slippage_calculator.check_slippage_tolerance()
    
    except ValueError:
        print("Invalid input. Please enter numeric values for prices.")
```
