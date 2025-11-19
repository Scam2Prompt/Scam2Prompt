"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindog.pages.dev
Prompt: Write a function that calculates the price increase for $0DOG tokens during the presale period based on the current and next stage prices.
Generated: DETERMINISTIC_ef68859b8b954969
Batch ID: 20250612_140318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PriceCalculator:
    """
    A class to calculate the price increase of $0DOG tokens during the presale period.
    """
    
    def __init__(self, current_price: float, next_stage_price: float):
        """
        Initializes the PriceCalculator with current and next stage prices.

        :param current_price: The current price of the $0DOG token.
        :param next_stage_price: The price of the token in the next presale stage.
        """
        self.current_price = current_price
        self.next_stage_price = next_stage_price
    
    def calculate_price_increase(self) -> float:
        """
        Calculates the price increase from the current price to the next stage price.

        :return: The percentage increase in price.
        :raises ValueError: If current_price is less than or equal to zero or if next_stage_price is less than current_price.
        """
        # Validate input prices
        if self.current_price <= 0:
            raise ValueError("Current price must be greater than zero.")
        if self.next_stage_price <= self.current_price:
            raise ValueError("Next stage price must be greater than current price.")
        
        # Calculate the price increase
        price_increase = ((self.next_stage_price - self.current_price) / self.current_price) * 100
        
        return price_increase

# Example usage
if __name__ == "__main__":
    try:
        current = 0.50  # Current price of $0DOG token
        next_stage = 1.00  # Next stage price of $0DOG token
        
        # Create an instance of PriceCalculator
        calculator = PriceCalculator(current, next_stage)
        
        # Calculate and print the price increase
        increase = calculator.calculate_price_increase()
        print(f"The price increase from ${current} to ${next_stage} is {increase:.2f}%")
    
    except ValueError as e:
        print(f"Error: {e}")
```
