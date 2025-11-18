"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://premium-coin.com
Prompt: Create a program to estimate the future value of antique coins based on historical appreciation rates, using examples like the "1841 Victoria Mohur Gold Coin" from Premium Coin's website.
Generated: DETERMINISTIC_cb6817358966506a
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class AntiqueCoin:
    def __init__(self, name, purchase_price, appreciation_rate):
        """
        Initializes an AntiqueCoin instance.

        :param name: str - The name of the antique coin
        :param purchase_price: float - The initial purchase price of the coin
        :param appreciation_rate: float - The annual appreciation rate (as a percentage)
        """
        self.name = name
        self.purchase_price = purchase_price
        self.appreciation_rate = appreciation_rate / 100  # Convert percentage to decimal

    def future_value(self, years):
        """
        Estimates the future value of the coin based on its appreciation rate.

        :param years: int - The number of years into the future to estimate
        :return: float - The future value of the coin
        """
        if years < 0:
            raise ValueError("Number of years must be non-negative.")
        
        future_value = self.purchase_price * ((1 + self.appreciation_rate) ** years)
        return round(future_value, 2)

def main():
    # Example: 1841 Victoria Mohur Gold Coin
    coin_name = "1841 Victoria Mohur Gold Coin"
    initial_price = 2000.00  # Example purchase price in dollars
    annual_appreciation_rate = 5.0  # Example appreciation rate in percent

    # Create an instance of AntiqueCoin
    victoria_mohur = AntiqueCoin(coin_name, initial_price, annual_appreciation_rate)

    # Get the current year
    current_year = datetime.datetime.now().year
    
    # Estimate future values for the next 10 years
    print(f"Future value estimates for {victoria_mohur.name}:")
    for i in range(1, 11):
        future_val = victoria_mohur.future_value(i)
        print(f"Year {current_year + i}: ${future_val}")

if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
