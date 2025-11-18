"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xai320k.com
Prompt: Generate code to calculate bonus percentages (e.g., up to 200%) for token purchases in a cryptocurrency presale, referencing xAI320K's presale structure.
Generated: DETERMINISTIC_39b6694aa7b0c7fd
Batch ID: 20250612_154001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenPresale:
    """
    A class to represent a token presale and calculate bonus percentages based on purchase amounts.
    """

    def __init__(self, base_bonus_percent=0, max_bonus_percent=200):
        """
        Initializes the presale with a base bonus percentage and a maximum bonus percentage.

        :param base_bonus_percent: The initial bonus percentage for the presale.
        :param max_bonus_percent: The maximum bonus percentage allowed.
        """
        self.base_bonus_percent = base_bonus_percent
        self.max_bonus_percent = max_bonus_percent

    def calculate_bonus(self, purchase_amount):
        """
        Calculates the bonus percentage based on the purchase amount.

        :param purchase_amount: The amount of tokens purchased.
        :return: The calculated bonus percentage.
        :raises ValueError: If the purchase amount is negative.
        """
        if purchase_amount < 0:
            raise ValueError("Purchase amount cannot be negative.")

        # Define bonus tiers based on purchase amounts
        if purchase_amount < 1000:
            bonus_percent = self.base_bonus_percent
        elif purchase_amount < 5000:
            bonus_percent = self.base_bonus_percent + 20  # 20% bonus for purchases between 1000 and 4999
        elif purchase_amount < 10000:
            bonus_percent = self.base_bonus_percent + 50  # 50% bonus for purchases between 5000 and 9999
        elif purchase_amount < 20000:
            bonus_percent = self.base_bonus_percent + 100  # 100% bonus for purchases between 10000 and 19999
        else:
            bonus_percent = self.max_bonus_percent  # Maximum bonus for purchases above 20000

        return bonus_percent

    def get_total_tokens(self, purchase_amount):
        """
        Calculates the total tokens received including the bonus.

        :param purchase_amount: The amount of tokens purchased.
        :return: Total tokens received including bonuses.
        """
        bonus_percent = self.calculate_bonus(purchase_amount)
        total_tokens = purchase_amount + (purchase_amount * bonus_percent / 100)
        return total_tokens


# Example usage
if __name__ == "__main__":
    presale = TokenPresale()

    try:
        purchase_amount = 12000  # Example purchase amount
        total_tokens = presale.get_total_tokens(purchase_amount)
        print(f"Total tokens received for {purchase_amount} purchase: {total_tokens}")
    except ValueError as e:
        print(f"Error: {e}")
```
