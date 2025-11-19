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
# gst_calculator.py

class GSTCalculator:
    """
    A class used to calculate GST for a given amount.

    Attributes:
    ----------
    gst_rate : float
        The GST rate as a decimal value.

    Methods:
    -------
    add_gst(amount)
        Adds GST to the given amount.
    remove_gst(amount)
        Removes GST from the given amount.
    """

    def __init__(self, gst_rate=0.18):
        """
        Initializes the GSTCalculator with a GST rate.

        Args:
        ----
        gst_rate (float, optional): The GST rate as a decimal value. Defaults to 0.18.
        """
        self.gst_rate = gst_rate

    def add_gst(self, amount):
        """
        Adds GST to the given amount.

        Args:
        ----
        amount (float): The amount to add GST to.

        Returns:
        -------
        float: The amount with GST added.

        Raises:
        ------
        ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        gst = amount * self.gst_rate
        return amount + gst

    def remove_gst(self, amount):
        """
        Removes GST from the given amount.

        Args:
        ----
        amount (float): The amount to remove GST from.

        Returns:
        -------
        float: The amount with GST removed.

        Raises:
        ------
        ValueError: If the amount is negative or if the amount is less than the GST amount.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if self.gst_rate == 0:
            return amount
        original_amount = amount / (1 + self.gst_rate)
        if original_amount < 0:
            raise ValueError("Amount is less than the GST amount")
        return original_amount


def main():
    calculator = GSTCalculator()

    while True:
        print("\nGST Calculator Menu:")
        print("1. Add GST")
        print("2. Remove GST")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter the amount: "))
                result = calculator.add_gst(amount)
                print(f"Amount with GST: {result:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                amount = float(input("Enter the amount: "))
                result = calculator.remove_gst(amount)
                print(f"Amount without GST: {result:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
