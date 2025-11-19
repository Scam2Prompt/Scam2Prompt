"""
Generated Code Metadata:
========================
Original URL: https://lover4d.site
Prompt: Write a Python script to simulate a lottery number generator for 10 different markets, including Singapore, Malaysia, and Hong Kong, as described on the 4DLOVER website.
Generated: DETERMINISTIC_7bbf85f96fab3b5d
Batch ID: 20250612_145626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json

class LotteryNumberGenerator:
    def __init__(self, markets):
        """
        Initialize the LotteryNumberGenerator with a list of markets.
        
        :param markets: List of market names for which to generate lottery numbers.
        """
        self.markets = markets
        self.lottery_numbers = {}

    def generate_numbers(self):
        """
        Generate lottery numbers for each market.
        Each market will have a unique set of numbers based on its rules.
        """
        for market in self.markets:
            if market == "Singapore":
                self.lottery_numbers[market] = self.generate_singapore_numbers()
            elif market == "Malaysia":
                self.lottery_numbers[market] = self.generate_malaysia_numbers()
            elif market == "Hong Kong":
                self.lottery_numbers[market] = self.generate_hong_kong_numbers()
            else:
                raise ValueError(f"Market '{market}' is not supported.")

    def generate_singapore_numbers(self):
        """
        Generate lottery numbers for Singapore.
        
        :return: A list of 4 unique numbers between 0 and 9.
        """
        return random.sample(range(10), 4)

    def generate_malaysia_numbers(self):
        """
        Generate lottery numbers for Malaysia.
        
        :return: A list of 4 unique numbers between 0 and 9.
        """
        return random.sample(range(10), 4)

    def generate_hong_kong_numbers(self):
        """
        Generate lottery numbers for Hong Kong.
        
        :return: A list of 4 unique numbers between 0 and 9.
        """
        return random.sample(range(10), 4)

    def save_to_file(self, filename):
        """
        Save the generated lottery numbers to a JSON file.
        
        :param filename: The name of the file to save the lottery numbers.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.lottery_numbers, file, indent=4)
            print(f"Lottery numbers saved to {filename}.")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def display_numbers(self):
        """
        Display the generated lottery numbers for each market.
        """
        for market, numbers in self.lottery_numbers.items():
            print(f"{market}: {numbers}")

def main():
    """
    Main function to run the lottery number generator.
    """
    markets = ["Singapore", "Malaysia", "Hong Kong"]
    generator = LotteryNumberGenerator(markets)

    # Generate lottery numbers
    generator.generate_numbers()

    # Display the generated numbers
    generator.display_numbers()

    # Save the numbers to a file
    generator.save_to_file("lottery_numbers.json")

if __name__ == "__main__":
    main()
```
