"""
Generated Code Metadata:
========================
Original URL: https://sovads.ru
Prompt: Develop a strategy for determining the price of a premium Instagram username, taking into account factors like length, dictionary words, and demand, as seen on SovaDS.
Generated: DETERMINISTIC_89a1e761c609306c
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from collections import Counter

class UsernamePricingStrategy:
    def __init__(self):
        # Predefined factors for pricing
        self.base_price = 10  # Base price for any username
        self.length_factor = 2  # Price increase per character
        self.dictionary_word_factor = 50  # Price increase for dictionary words
        self.demand_factor = 100  # Price increase based on demand

    def is_dictionary_word(self, word):
        """
        Check if a word is a dictionary word.
        This is a simple implementation; in production, consider using a comprehensive dictionary.
        """
        dictionary = {"premium", "username", "example", "brand", "unique", "fashion", "style"}
        return word.lower() in dictionary

    def calculate_length_price(self, username):
        """
        Calculate price based on the length of the username.
        """
        return len(username) * self.length_factor

    def calculate_dictionary_word_price(self, username):
        """
        Calculate price based on the presence of dictionary words in the username.
        """
        words = re.findall(r'\w+', username)  # Extract words from the username
        return sum(self.dictionary_word_factor for word in words if self.is_dictionary_word(word))

    def calculate_demand_price(self, demand):
        """
        Calculate price based on demand.
        Demand is expected to be a value between 0 and 1, where 1 is high demand.
        """
        if not (0 <= demand <= 1):
            raise ValueError("Demand must be a value between 0 and 1.")
        return self.demand_factor * demand

    def determine_price(self, username, demand):
        """
        Determine the price of a premium Instagram username based on various factors.
        
        :param username: The Instagram username to evaluate.
        :param demand: A float representing the demand for the username (0 to 1).
        :return: The calculated price for the username.
        """
        if not isinstance(username, str) or not username:
            raise ValueError("Username must be a non-empty string.")
        
        # Calculate total price based on different factors
        length_price = self.calculate_length_price(username)
        dictionary_price = self.calculate_dictionary_word_price(username)
        demand_price = self.calculate_demand_price(demand)

        total_price = self.base_price + length_price + dictionary_price + demand_price
        return total_price

# Example usage
if __name__ == "__main__":
    pricing_strategy = UsernamePricingStrategy()
    
    try:
        username = "PremiumBrand"
        demand = 0.8  # Example demand value
        price = pricing_strategy.determine_price(username, demand)
        print(f"The price for the username '{username}' is: ${price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
