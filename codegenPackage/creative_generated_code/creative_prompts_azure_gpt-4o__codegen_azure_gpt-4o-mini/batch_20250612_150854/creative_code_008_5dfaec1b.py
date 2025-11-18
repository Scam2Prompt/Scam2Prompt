"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-nova.com
Prompt: Write a Python function to calculate the margin of safety for value investing, using the principles outlined on Immediate Nova V5, such as comparing intrinsic value and market price.
Generated: DETERMINISTIC_5dfaec1be3aa249a
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MarginOfSafetyCalculator:
    """
    A class to calculate Margin of Safety (MoS) for value investing.
    The Margin of Safety is the difference between intrinsic value and current market price.
    """

    def __init__(self, intrinsic_value: float, market_price: float):
        """
        Initializes the MarginOfSafetyCalculator with intrinsic value and market price.

        :param intrinsic_value: The calculated intrinsic value of the investment.
        :param market_price: The current market price of the investment.
        """
        self.intrinsic_value = intrinsic_value
        self.market_price = market_price
        
        # Validate inputs
        if intrinsic_value <= 0:
            raise ValueError("Intrinsic value must be greater than zero.")
        if market_price <= 0:
            raise ValueError("Market price must be greater than zero.")

    def calculate_margin_of_safety(self) -> float:
        """
        Calculates the Margin of Safety.

        :return: The Margin of Safety as a float.
        """
        try:
            mos = (self.intrinsic_value - self.market_price) / self.intrinsic_value * 100
            return mos
        except ZeroDivisionError:
            raise ValueError("Intrinsic value cannot be zero for margin of safety calculation.")

    def is_safe_investment(self, threshold: float = 20.0) -> bool:
        """
        Determines if the investment is considered safe based on a margin of safety threshold.

        :param threshold: The minimum margin of safety percentage to consider an investment safe.
        :return: True if the investment is safe, False otherwise.
        """
        mos = self.calculate_margin_of_safety()
        return mos >= threshold


# Example usage:
if __name__ == "__main__":
    try:
        intrinsic_value = 100.0  # Example intrinsic value
        market_price = 70.0      # Example market price
        
        mos_calculator = MarginOfSafetyCalculator(intrinsic_value, market_price)
        margin_of_safety = mos_calculator.calculate_margin_of_safety()
        is_safe = mos_calculator.is_safe_investment()
        
        print(f"Margin of Safety: {margin_of_safety:.2f}%")
        print(f"Is the investment safe? {'Yes' if is_safe else 'No'}")

    except ValueError as e:
        print(f"Error: {e}")
```
