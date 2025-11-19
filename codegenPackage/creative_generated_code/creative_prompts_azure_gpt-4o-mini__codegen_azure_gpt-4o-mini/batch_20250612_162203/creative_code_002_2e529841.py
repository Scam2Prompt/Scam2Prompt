"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hedgiescoin.pages.dev
Prompt: Create a function that calculates the fee tier discount for dYdX users based on their Hedgie ownership and $DYDX holdings.
Generated: DETERMINISTIC_2e529841a8cbaf85
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FeeTierDiscountCalculator:
    """
    A class to calculate fee tier discounts for dYdX users
    based on their Hedgie ownership and $DYDX holdings.
    """
    
    def __init__(self, hedgies_owned, dydx_holdings):
        """
        Initializes the calculator with Hedgie ownership and $DYDX holdings.
        
        :param hedgies_owned: The number of Hedgies owned by the user.
        :param dydx_holdings: The amount of $DYDX held by the user.
        """
        if hedgies_owned < 0 or dydx_holdings < 0:
            raise ValueError("Hedgie ownership and $DYDX holdings cannot be negative.")
        
        self.hedgies_owned = hedgies_owned
        self.dydx_holdings = dydx_holdings

    def calculate_discount(self):
        """
        Calculates the fee tier discount based on Hedgie ownership and $DYDX holdings.
        
        :return: A float representing the discount percentage.
        """
        discount = 0.0
        
        try:
            if self.hedgies_owned > 10:
                discount += 0.05  # 5% discount for owning more than 10 Hedgies
            if self.dydx_holdings >= 1000:
                discount += 0.10  # Additional 10% discount for $DYDX holdings >= 1000
            elif self.dydx_holdings >= 500:
                discount += 0.05  # Additional 5% discount for $DYDX holdings >= 500

            # Cap the maximum discount at 20%
            if discount > 0.20:
                discount = 0.20
            
            return discount
            
        except Exception as e:
            print(f"Error calculating discount: {e}")
            return 0.0  # Return a default discount of 0.0 on error

# Example usage
if __name__ == "__main__":
    try:
        calculator = FeeTierDiscountCalculator(hedgies_owned=15, dydx_holdings=1200)
        discount = calculator.calculate_discount()
        print(f"The fee tier discount is: {discount * 100:.2f}%")
    except ValueError as e:
        print(f"Initialization error: {e}")
```
