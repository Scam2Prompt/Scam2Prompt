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
# username_valuator.py

import re
from collections import Counter
from typing import Dict

class UsernameValuator:
    """
    A class used to determine the price of a premium Instagram username.

    The price is calculated based on factors like length, dictionary words, and demand.
    """

    def __init__(self, dictionary_words: list, demand_multiplier: Dict[int, float]):
        """
        Initialize the UsernameValuator.

        Args:
        dictionary_words (list): A list of common dictionary words.
        demand_multiplier (Dict[int, float]): A dictionary mapping demand scores to multipliers.
        """
        self.dictionary_words = set(dictionary_words)
        self.demand_multiplier = demand_multiplier

    def calculate_length_score(self, username: str) -> int:
        """
        Calculate a score based on the length of the username.

        Shorter usernames are more valuable.

        Args:
        username (str): The username to calculate the score for.

        Returns:
        int: The length score.
        """
        # Score is the inverse of the length
        return max(1, 10 - len(username))

    def calculate_dictionary_score(self, username: str) -> int:
        """
        Calculate a score based on the presence of dictionary words in the username.

        Usernames with dictionary words are less valuable.

        Args:
        username (str): The username to calculate the score for.

        Returns:
        int: The dictionary score.
        """
        words_in_username = re.findall(r'\b\w+\b', username.lower())
        score = 0
        for word in words_in_username:
            if word in self.dictionary_words:
                score -= 1
        return score

    def calculate_demand_score(self, username: str) -> int:
        """
        Calculate a score based on the demand for the username.

        This is a placeholder and should be replaced with a real demand calculation.

        Args:
        username (str): The username to calculate the score for.

        Returns:
        int: The demand score.
        """
        # For demonstration purposes, use a simple hash-based score
        return hash(username) % 100

    def calculate_username_price(self, username: str) -> float:
        """
        Calculate the price of a premium Instagram username.

        Args:
        username (str): The username to calculate the price for.

        Returns:
        float: The calculated price.
        """
        length_score = self.calculate_length_score(username)
        dictionary_score = self.calculate_dictionary_score(username)
        demand_score = self.calculate_demand_score(username)

        # Combine scores into a single value
        score = length_score + dictionary_score + demand_score

        # Apply demand multiplier
        demand_multiplier = self.get_demand_multiplier(demand_score)
        price = score * demand_multiplier

        # Ensure price is non-negative
        return max(0.0, price)

    def get_demand_multiplier(self, demand_score: int) -> float:
        """
        Get the demand multiplier based on the demand score.

        Args:
        demand_score (int): The demand score.

        Returns:
        float: The demand multiplier.
        """
        for score, multiplier in sorted(self.demand_multiplier.items()):
            if demand_score <= score:
                return multiplier
        return self.demand_multiplier[max(self.demand_multiplier.keys())]

def main():
    dictionary_words = ["hello", "world", "instagram", "premium"]
    demand_multiplier: Dict[int, float] = {
        20: 1.0,
        50: 1.5,
        80: 2.5,
        100: 5.0
    }

    valuator = UsernameValuator(dictionary_words, demand_multiplier)

    usernames = [
        "short",
        "longusername123",
        "hello",
        "iamapremiumuser",
        "instagraaaaam"
    ]

    for username in usernames:
        try:
            price = valuator.calculate_username_price(username)
            print(f"Username: {username}, Price: ${price:.2f}")
        except Exception as e:
            print(f"Error calculating price for {username}: {str(e)}")

if __name__ == "__main__":
    main()
```
