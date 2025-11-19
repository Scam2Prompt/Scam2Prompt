"""
Generated Code Metadata:
========================
Original URL: https://premiertradeoptions.com
Prompt: Develop a function to automate the calculation and application of Copy Stop Loss (CSL) ratios between 5% and 95%, as explained on Premier Trade Options.
Generated: DETERMINISTIC_a75827a575c5f0ab
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CopyStopLossCalculator:
    """
    A class to calculate and apply Copy Stop Loss (CSL) ratios for trading.
    """

    def __init__(self, initial_investment: float):
        """
        Initializes the CopyStopLossCalculator with an initial investment.

        :param initial_investment: The initial amount of money invested.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        self.initial_investment = initial_investment

    def calculate_csl(self, current_value: float, csl_ratio: float) -> float:
        """
        Calculates the Copy Stop Loss value based on the current value and CSL ratio.

        :param current_value: The current value of the investment.
        :param csl_ratio: The Copy Stop Loss ratio (between 5 and 95).
        :return: The calculated Copy Stop Loss value.
        """
        if not (0.05 <= csl_ratio <= 0.95):
            raise ValueError("CSL ratio must be between 5% and 95%.")

        # Calculate the stop loss value
        stop_loss_value = current_value * (1 - csl_ratio)
        return stop_loss_value

    def apply_csl(self, current_value: float, csl_ratio: float) -> float:
        """
        Applies the Copy Stop Loss to the current investment value.

        :param current_value: The current value of the investment.
        :param csl_ratio: The Copy Stop Loss ratio (between 5 and 95).
        :return: The new investment value after applying the CSL.
        """
        stop_loss_value = self.calculate_csl(current_value, csl_ratio)

        # Determine the new investment value after applying the CSL
        new_investment_value = max(stop_loss_value, 0)
        return new_investment_value


# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 10000.0  # Example initial investment
        current_value = 12000.0        # Example current value of the investment
        csl_ratio = 0.10               # Example CSL ratio (10%)

        csl_calculator = CopyStopLossCalculator(initial_investment)
        new_value = csl_calculator.apply_csl(current_value, csl_ratio)

        print(f"New investment value after applying CSL: ${new_value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
