"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoindogs.pages.dev
Prompt: Create a function that calculates the price increase of $0DOG tokens every three days during the presale.
Generated: DETERMINISTIC_7c4f0bc8ae59f6e0
Batch ID: 20250612_140250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenPriceCalculator:
    def __init__(self, initial_price: float, increase_rate: float, presale_days: int):
        """
        Initializes the TokenPriceCalculator with the initial price, increase rate, and number of presale days.

        :param initial_price: The starting price of $0DOG tokens.
        :param increase_rate: The price increase every three days (in dollars).
        :param presale_days: The total number of days for the presale.
        """
        if initial_price < 0 or increase_rate < 0 or presale_days < 0:
            raise ValueError("Initial price, increase rate, and presale days must be non-negative.")
        
        self.initial_price = initial_price
        self.increase_rate = increase_rate
        self.presale_days = presale_days

    def calculate_price_increases(self):
        """
        Calculates the price of $0DOG tokens at each interval of three days during the presale.

        :return: A list of tuples containing (day, price) for each three-day interval.
        """
        price_schedule = []
        total_intervals = self.presale_days // 3
        
        for interval in range(total_intervals + 1):
            # Calculate the current price after the interval
            current_price = self.initial_price + (self.increase_rate * interval)
            price_schedule.append((interval * 3, current_price))
        
        return price_schedule

def main():
    try:
        # Example usage
        initial_price = 1.0  # Initial price of the token
        increase_rate = 0.5   # Price increase every three days
        presale_days = 30     # Total presale days

        calculator = TokenPriceCalculator(initial_price, increase_rate, presale_days)
        price_schedule = calculator.calculate_price_increases()
        
        # Print the price schedule
        for day, price in price_schedule:
            print(f"Day {day}: ${price:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
