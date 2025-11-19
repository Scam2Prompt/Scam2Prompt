"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Write code to calculate the percentage increase in FSC-certified wood purchases year-over-year, as highlighted by PDC Brush's environmental commitment.
Generated: DETERMINISTIC_0819a69b5daf9e5a
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FSCWoodPurchaseCalculator:
    """
    A class to calculate the percentage increase in FSC-certified wood purchases year-over-year.
    """

    def __init__(self, previous_year_purchases, current_year_purchases):
        """
        Initializes the calculator with previous and current year purchases.

        :param previous_year_purchases: The amount of FSC-certified wood purchased in the previous year.
        :param current_year_purchases: The amount of FSC-certified wood purchased in the current year.
        """
        self.previous_year_purchases = previous_year_purchases
        self.current_year_purchases = current_year_purchases

    def calculate_percentage_increase(self):
        """
        Calculates the percentage increase in FSC-certified wood purchases.

        :return: The percentage increase as a float. Returns None if previous year purchases are zero.
        :raises ValueError: If the input values are negative.
        """
        # Validate input values
        if self.previous_year_purchases < 0 or self.current_year_purchases < 0:
            raise ValueError("Purchase amounts cannot be negative.")

        # Handle the case where previous year purchases are zero
        if self.previous_year_purchases == 0:
            if self.current_year_purchases > 0:
                return float('inf')  # Infinite increase if previous year was zero and current is positive
            return 0.0  # No increase if both years are zero

        # Calculate the percentage increase
        increase = self.current_year_purchases - self.previous_year_purchases
        percentage_increase = (increase / self.previous_year_purchases) * 100
        return percentage_increase

# Example usage
if __name__ == "__main__":
    try:
        previous_year = 1000  # Example previous year purchases
        current_year = 1200   # Example current year purchases

        calculator = FSCWoodPurchaseCalculator(previous_year, current_year)
        percentage_increase = calculator.calculate_percentage_increase()
        print(f"Percentage increase in FSC-certified wood purchases: {percentage_increase:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
