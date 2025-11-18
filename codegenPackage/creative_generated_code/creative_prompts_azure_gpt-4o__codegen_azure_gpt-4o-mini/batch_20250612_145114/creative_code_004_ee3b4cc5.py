"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shoppiday.site
Prompt: Write code to calculate cashback earnings based on user purchases, incorporating features like verified discounts as described on Shoppiday.
Generated: DETERMINISTIC_ee3b4cc5394f30bb
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CashbackCalculator:
    """
    A class to calculate cashback earnings based on user purchases and verified discounts.
    """

    def __init__(self, cashback_rate=0.05):
        """
        Initializes the CashbackCalculator with a specified cashback rate.
        
        :param cashback_rate: The percentage of cashback to be earned on eligible purchases, default is 5%
        """
        if not (0 <= cashback_rate <= 1):
            raise ValueError("Cashback rate must be between 0 and 1.")
        self.cashback_rate = cashback_rate

    def calculate_cashback(self, purchases):
        """
        Calculates the total cashback based on the user's purchases.
        
        :param purchases: A list of tuples where each tuple contains the purchase amount and a boolean 
                          indicating whether the discount is verified.
        :return: The total cashback earned from verified purchases.
        """
        total_cashback = 0.0
        
        for amount, is_discount_verified in purchases:
            if amount < 0:
                raise ValueError("Purchase amount cannot be negative.")
            if is_discount_verified:
                cashback = amount * self.cashback_rate
                total_cashback += cashback
        
        return total_cashback

    def display_cashback(self, purchases):
        """
        Displays the calculated cashback for the user.
        
        :param purchases: A list of tuples where each tuple contains the purchase amount and a boolean 
                          indicating whether the discount is verified.
        :return: None
        """
        try:
            total_cashback = self.calculate_cashback(purchases)
            print(f"Total cashback earned: ${total_cashback:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

# Example usage
if __name__ == "__main__":
    purchases = [
        (100.0, True),   # $100 purchase with verified discount
        (50.0, False),   # $50 purchase without verified discount
        (200.0, True),   # $200 purchase with verified discount
    ]

    calculator = CashbackCalculator(cashback_rate=0.1)  # 10% cashback rate
    calculator.display_cashback(purchases)
```
