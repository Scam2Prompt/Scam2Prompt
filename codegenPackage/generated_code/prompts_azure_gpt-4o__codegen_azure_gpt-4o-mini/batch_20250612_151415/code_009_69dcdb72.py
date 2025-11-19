"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Write a program to calculate GST for a given amount, allowing users to add or remove GST, as described in the GST Calculator tool on the IFSC Finder site.
Generated: DETERMINISTIC_69dcdb722053c70c
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GSTCalculator:
    """
    A class to calculate Goods and Services Tax (GST) for a given amount.
    Allows users to add or remove GST from the amount.
    """

    def __init__(self, gst_rate: float):
        """
        Initializes the GSTCalculator with a specified GST rate.

        :param gst_rate: The GST rate as a percentage (e.g., 18 for 18%).
        """
        if gst_rate < 0:
            raise ValueError("GST rate cannot be negative.")
        self.gst_rate = gst_rate / 100  # Convert percentage to decimal

    def calculate_gst(self, amount: float) -> float:
        """
        Calculates the GST for a given amount.

        :param amount: The original amount before GST.
        :return: The calculated GST amount.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        return amount * self.gst_rate

    def add_gst(self, amount: float) -> float:
        """
        Adds GST to the given amount.

        :param amount: The original amount before GST.
        :return: The total amount including GST.
        """
        gst_amount = self.calculate_gst(amount)
        return amount + gst_amount

    def remove_gst(self, amount_with_gst: float) -> float:
        """
        Removes GST from the given amount that includes GST.

        :param amount_with_gst: The total amount including GST.
        :return: The original amount before GST.
        """
        if amount_with_gst < 0:
            raise ValueError("Amount with GST cannot be negative.")
        original_amount = amount_with_gst / (1 + self.gst_rate)
        return original_amount

def main():
    """
    Main function to demonstrate the GST Calculator functionality.
    """
    try:
        # Example GST rate of 18%
        gst_calculator = GSTCalculator(gst_rate=18)

        # Input amount
        amount = float(input("Enter the amount: "))

        # Calculate and display GST
        gst_amount = gst_calculator.calculate_gst(amount)
        print(f"GST Amount: {gst_amount:.2f}")

        # Calculate and display total amount with GST
        total_with_gst = gst_calculator.add_gst(amount)
        print(f"Total Amount with GST: {total_with_gst:.2f}")

        # Calculate and display original amount without GST
        original_amount = gst_calculator.remove_gst(total_with_gst)
        print(f"Original Amount (without GST): {original_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
