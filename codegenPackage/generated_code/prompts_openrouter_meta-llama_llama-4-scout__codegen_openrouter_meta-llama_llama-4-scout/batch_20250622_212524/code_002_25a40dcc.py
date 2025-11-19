"""
Generated Code Metadata:
========================
Original URL: https://dutton.co.nz
Prompt: "Write a code snippet to calculate GST (Goods and Services Tax) for New Zealand businesses."
Generated: DETERMINISTIC_25a40dcc819f40bf
Batch ID: 20250622_212524
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gst_calculator.py

class GstCalculator:
    """
    Calculates GST (Goods and Services Tax) for New Zealand businesses.

    In New Zealand, the standard GST rate is 15%.
    """

    def __init__(self, gst_rate=0.15):
        """
        Initializes the GstCalculator with a GST rate.

        Args:
            gst_rate (float, optional): The GST rate. Defaults to 0.15 (15%).
        """
        self.gst_rate = gst_rate

    def calculate_gst(self, amount):
        """
        Calculates the GST for a given amount.

        Args:
            amount (float): The amount to calculate GST for.

        Returns:
            float: The calculated GST.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")

        gst = amount * self.gst_rate
        return gst

    def calculate_total(self, amount):
        """
        Calculates the total amount including GST.

        Args:
            amount (float): The amount to calculate the total for.

        Returns:
            float: The total amount including GST.

        Raises:
            ValueError: If the amount is negative.
        """
        gst = self.calculate_gst(amount)
        total = amount + gst
        return total


def main():
    try:
        calculator = GstCalculator()
        amount = float(input("Enter the amount: $"))
        gst = calculator.calculate_gst(amount)
        total = calculator.calculate_total(amount)

        print(f"GST (15%): ${gst:.2f}")
        print(f"Total: ${total:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
