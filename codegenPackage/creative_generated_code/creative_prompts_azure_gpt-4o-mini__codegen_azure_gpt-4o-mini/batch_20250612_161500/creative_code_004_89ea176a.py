"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dre-8x7.pages.dev
Prompt: Implement a calculator that determines how many DRE tokens can be bought with varying amounts of FTM, ensuring it adheres to the presale structure mentioned on the site.
Generated: DETERMINISTIC_89ea176a7bdf2aaa
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenCalculator:
    """
    A class to calculate the number of DRE tokens that can be purchased
    with a given amount of FTM during a presale.
    """

    def __init__(self, price_per_token: float, min_ftm: float, max_ftm: float):
        """
        Initializes the TokenCalculator with the pricing structure.

        :param price_per_token: The price of a single DRE token in FTM.
        :param min_ftm: The minimum amount of FTM required to buy tokens.
        :param max_ftm: The maximum amount of FTM allowed for token purchase.
        """
        self.price_per_token = price_per_token
        self.min_ftm = min_ftm
        self.max_ftm = max_ftm

    def calculate_tokens(self, ftm_amount: float) -> int:
        """
        Calculates the number of DRE tokens that can be purchased
        based on the given FTM amount.

        :param ftm_amount: The amount of FTM to use for purchasing tokens.
        :return: The number of DRE tokens that can be bought.
        :raises ValueError: If the FTM amount is outside the allowed range.
        """
        if ftm_amount < self.min_ftm:
            raise ValueError(f"FTM amount must be at least {self.min_ftm}.")
        if ftm_amount > self.max_ftm:
            raise ValueError(f"FTM amount must not exceed {self.max_ftm}.")

        tokens = ftm_amount / self.price_per_token
        return int(tokens)  # Return the number of tokens as an integer

    def display_purchase(self, ftm_amount: float):
        """
        Displays the purchase information for the given FTM amount.

        :param ftm_amount: The amount of FTM used for purchasing tokens.
        """
        try:
            tokens = self.calculate_tokens(ftm_amount)
            print(f"With {ftm_amount} FTM, you can purchase {tokens} DRE tokens.")
        except ValueError as e:
            print(f"Error: {e}")


# Example of usage
if __name__ == "__main__":
    # Presale parameters
    price_per_token = 0.1  # Example price in FTM
    min_ftm = 1.0          # Minimum FTM to spend
    max_ftm = 10.0         # Maximum FTM to spend

    # Create a TokenCalculator instance
    calculator = TokenCalculator(price_per_token, min_ftm, max_ftm)

    # Test with various FTM amounts
    amounts_to_test = [0.5, 1.0, 5.0, 10.0, 15.0]  # Various test amounts

    for amount in amounts_to_test:
        calculator.display_purchase(amount)
```
