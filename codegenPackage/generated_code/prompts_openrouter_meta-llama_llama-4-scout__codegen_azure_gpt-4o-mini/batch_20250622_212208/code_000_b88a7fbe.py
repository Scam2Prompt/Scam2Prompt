"""
Generated Code Metadata:
========================
Original URL: https://redstone.cx
Prompt: Write a Python script to calculate the maximum amount of $INIT tokens that can be purchased during the presale using BNB, given the minimum and maximum purchase limits.
Generated: DETERMINISTIC_b88a7fbeb02991c1
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PresaleCalculator:
    def __init__(self, bnb_amount, min_purchase, max_purchase, token_price):
        """
        Initialize the presale calculator with the given parameters.

        :param bnb_amount: Total amount of BNB available for purchase
        :param min_purchase: Minimum amount of tokens that can be purchased
        :param max_purchase: Maximum amount of tokens that can be purchased
        :param token_price: Price of one $INIT token in BNB
        """
        self.bnb_amount = bnb_amount
        self.min_purchase = min_purchase
        self.max_purchase = max_purchase
        self.token_price = token_price

    def calculate_max_tokens(self):
        """
        Calculate the maximum number of $INIT tokens that can be purchased.

        :return: Maximum number of tokens that can be purchased
        :raises ValueError: If any of the parameters are invalid
        """
        # Validate input parameters
        if self.bnb_amount <= 0:
            raise ValueError("BNB amount must be greater than zero.")
        if self.token_price <= 0:
            raise ValueError("Token price must be greater than zero.")
        if self.min_purchase < 0 or self.max_purchase < 0:
            raise ValueError("Purchase limits must be non-negative.")
        if self.min_purchase > self.max_purchase:
            raise ValueError("Minimum purchase cannot exceed maximum purchase.")

        # Calculate the maximum tokens that can be purchased with the available BNB
        max_tokens_by_bnb = self.bnb_amount / self.token_price

        # The maximum tokens that can be purchased is limited by the purchase limits
        max_tokens = min(max_tokens_by_bnb, self.max_purchase)

        # Ensure that the purchase meets the minimum purchase requirement
        if max_tokens < self.min_purchase:
            raise ValueError("Not enough BNB to meet the minimum purchase requirement.")

        return max_tokens


def main():
    """
    Main function to execute the presale token calculation.
    """
    try:
        # Example parameters (these can be modified as needed)
        bnb_amount = 1.5  # Total BNB available
        min_purchase = 10  # Minimum tokens to purchase
        max_purchase = 100  # Maximum tokens to purchase
        token_price = 0.01  # Price of one $INIT token in BNB

        # Create an instance of the PresaleCalculator
        calculator = PresaleCalculator(bnb_amount, min_purchase, max_purchase, token_price)

        # Calculate the maximum tokens that can be purchased
        max_tokens = calculator.calculate_max_tokens()

        # Output the result
        print(f"Maximum $INIT tokens that can be purchased: {max_tokens}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
