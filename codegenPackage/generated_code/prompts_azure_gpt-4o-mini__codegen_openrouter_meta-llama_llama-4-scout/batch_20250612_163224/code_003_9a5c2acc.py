"""
Generated Code Metadata:
========================
Original URL: https://stayolud.io
Prompt: Explain how to set up a fee split mechanism for a social engagement platform inspired by Loud's 4% fee structure after Meteora.
Generated: DETERMINISTIC_9a5c2accfff6af53
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fee_splitter.py

class FeeSplitter:
    """
    A class to handle fee splitting for a social engagement platform.

    The fee structure is inspired by Loud's 4% fee structure after Meteora.
    """

    def __init__(self, total_amount, platform_fee_percentage=0.04):
        """
        Initialize the FeeSplitter.

        Args:
        - total_amount (float): The total amount to be split.
        - platform_fee_percentage (float, optional): The platform fee percentage. Defaults to 0.04.
        """
        self.total_amount = total_amount
        self.platform_fee_percentage = platform_fee_percentage

    def calculate_platform_fee(self):
        """
        Calculate the platform fee.

        Returns:
        - float: The platform fee amount.
        """
        return self.total_amount * self.platform_fee_percentage

    def calculate_creator_amount(self):
        """
        Calculate the creator's amount after deducting the platform fee.

        Returns:
        - float: The creator's amount.
        """
        platform_fee = self.calculate_platform_fee()
        return self.total_amount - platform_fee

    def split_fee(self, split_percentage):
        """
        Split the platform fee among multiple recipients.

        Args:
        - split_percentage (dict): A dictionary with recipient names as keys and their respective percentages as values.

        Returns:
        - dict: A dictionary with recipient names as keys and their respective amounts as values.

        Raises:
        - ValueError: If the split percentages do not add up to 100%.
        """
        platform_fee = self.calculate_platform_fee()
        total_percentage = sum(split_percentage.values())

        if abs(total_percentage - 100) > 1e-6:
            raise ValueError("Split percentages do not add up to 100%")

        split_amounts = {}
        for recipient, percentage in split_percentage.items():
            split_amounts[recipient] = platform_fee * (percentage / 100)

        return split_amounts


def main():
    try:
        total_amount = 1000.0
        fee_splitter = FeeSplitter(total_amount)

        print(f"Total Amount: ${total_amount:.2f}")
        print(f"Platform Fee: ${fee_splitter.calculate_platform_fee():.2f}")
        print(f"Creator Amount: ${fee_splitter.calculate_creator_amount():.2f}")

        split_percentage = {
            "Recipient A": 50,
            "Recipient B": 30,
            "Recipient C": 20
        }

        split_amounts = fee_splitter.split_fee(split_percentage)

        print("\nSplit Amounts:")
        for recipient, amount in split_amounts.items():
            print(f"{recipient}: ${amount:.2f}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
