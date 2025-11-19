"""
Generated Code Metadata:
========================
Original URL: https://linea.usernames.club
Prompt: Compare the pricing for a 3-character `.linea` username versus a 5-character `.linea` username, and explain the difference in cost.
Generated: DETERMINISTIC_540e17c74e8d07b4
Batch ID: 20250622_211458
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# username_pricing_comparator.py

class UsernamePricingComparator:
    """
    Compare pricing for different length .linea usernames.
    """

    def __init__(self, base_price_per_character):
        """
        Initialize the comparator with the base price per character.

        Args:
            base_price_per_character (float): The base price per character.
        """
        self.base_price_per_character = base_price_per_character

    def calculate_username_price(self, username_length):
        """
        Calculate the price of a username based on its length.

        Args:
            username_length (int): The length of the username.

        Returns:
            float: The price of the username.
        """
        return self.base_price_per_character * username_length

    def compare_pricing(self, username_length_1, username_length_2):
        """
        Compare the pricing for two different length usernames.

        Args:
            username_length_1 (int): The length of the first username.
            username_length_2 (int): The length of the second username.

        Returns:
            dict: A dictionary containing the prices and the difference.
        """
        price_1 = self.calculate_username_price(username_length_1)
        price_2 = self.calculate_username_price(username_length_2)

        difference = abs(price_1 - price_2)
        percentage_difference = (difference / min(price_1, price_2)) * 100 if min(price_1, price_2) != 0 else 0

        return {
            "price_1": price_1,
            "price_2": price_2,
            "difference": difference,
            "percentage_difference": percentage_difference
        }


def main():
    try:
        # Assuming the base price per character is $1.00 for simplicity
        comparator = UsernamePricingComparator(base_price_per_character=1.00)

        # Define the lengths of the usernames to compare
        username_length_1 = 3  # a 3-character username
        username_length_2 = 5  # a 5-character username

        # Compare pricing
        result = comparator.compare_pricing(username_length_1, username_length_2)

        # Print the result
        print(f"Pricing comparison for .linea usernames:")
        print(f"-----------------------------------------")
        print(f"Username length: {username_length_1} characters, Price: ${result['price_1']:.2f}")
        print(f"Username length: {username_length_2} characters, Price: ${result['price_2']:.2f}")
        print(f"Difference in price: ${result['difference']:.2f}")
        print(f"Percentage difference: {result['percentage_difference']:.2f}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
