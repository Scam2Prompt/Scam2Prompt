"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Write a program to calculate GST for a given amount, allowing users to add or remove GST, as described in the GST Calculator tool on the IFSC Finder site.
Generated: DETERMINISTIC_69dcdb722053c70c
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GSTCalculator:
    """
    A class to calculate Goods and Services Tax (GST) for a given amount.
    """

    def __init__(self, gst_rate: float):
        """
        Initialize the GSTCalculator with a specific GST rate.

        :param gst_rate: The GST rate as a percentage (e.g., 18 for 18%).
        """
        if not (0 <= gst_rate <= 100):
            raise ValueError("GST rate must be between 0 and 100.")
        self.gst_rate = gst_rate

    def calculate_gst(self, amount: float) -> float:
        """
        Calculate the GST amount for a given amount.

        :param amount: The original amount before GST.
        :return: The calculated GST amount.
        """
        if amount < 0:
            raise ValueError("Amount must be a non-negative value.")
        gst_amount = amount * (self.gst_rate / 100)
        return gst_amount

    def add_gst(self, amount: float) -> float:
        """
        Add GST to a given amount.

        :param amount: The original amount before GST.
        :return: The total amount including GST.
        """
        gst_amount = self.calculate_gst(amount)
        total_amount = amount + gst_amount
        return total_amount

    def remove_gst(self, total_amount: float) -> float:
        """
        Remove GST from a total amount.

        :param total_amount: The total amount that includes GST.
        :return: The original amount before GST.
        """
        if total_amount < 0:
            raise ValueError("Total amount must be a non-negative value.")
        original_amount = total_amount / (1 + (self.gst_rate / 100))
        return original_amount


def main():
    """
    Main function to demonstrate GST calculations.
    """
    try:
        # Set the GST rate (e.g., 18%)
        gst_rate = 18.0
        calculator = GSTCalculator(gst_rate)

        # Example amount
        amount = 1000.0

        # Calculate GST
        gst_amount = calculator.calculate_gst(amount)
        print(f"GST for {amount} at {gst_rate}%: {gst_amount}")

        # Total amount including GST
        total_with_gst = calculator.add_gst(amount)
        print(f"Total amount including GST: {total_with_gst}")

        # Remove GST to get the original amount
        original_amount = calculator.remove_gst(total_with_gst)
        print(f"Original amount after removing GST: {original_amount}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
