"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new-ej0.pages.dev
Prompt: Write a script to simulate the opening of a MEME Mystery Box and calculate the probability of receiving specific MEME tokens.
Generated: DETERMINISTIC_6375db64b0079def
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class MemeMysteryBox:
    def __init__(self, token_distribution):
        """
        Initializes the MemeMysteryBox with a given token distribution.
        
        :param token_distribution: A dictionary where keys are token names
                                   and values are their probabilities (0-1).
        """
        self.token_distribution = token_distribution
        self.validate_distribution()

    def validate_distribution(self):
        """
        Validates that the token distribution sums to 1.
        
        Raises:
            ValueError: If the sum of probabilities is not equal to 1.
        """
        total_probability = sum(self.token_distribution.values())
        if not (0.99 <= total_probability <= 1.01):  # Allowing for minor floating point inaccuracies
            raise ValueError("The probabilities must sum to 1.")

    def open_box(self):
        """
        Simulates opening the mystery box and returns the token received.
        
        :return: The name of the token received.
        """
        tokens = list(self.token_distribution.keys())
        probabilities = list(self.token_distribution.values())
        
        # Randomly choose a token based on defined probabilities
        chosen_token = random.choices(tokens, weights=probabilities, k=1)[0]
        return chosen_token

    def simulate_openings(self, num_openings):
        """
        Simulates opening the mystery box multiple times and calculates
        the frequency of receiving each token.
        
        :param num_openings: The number of times to open the mystery box.
        :return: A dictionary with the frequency of each token received.
        """
        if num_openings <= 0:
            raise ValueError("Number of openings must be a positive integer.")

        token_counts = {token: 0 for token in self.token_distribution.keys()}

        for _ in range(num_openings):
            token = self.open_box()
            token_counts[token] += 1

        return token_counts

    def calculate_probabilities(self, token_counts, num_openings):
        """
        Calculates the empirical probabilities of receiving each token
        based on simulation results.
        
        :param token_counts: A dictionary with the frequency of each token.
        :param num_openings: The total number of box openings.
        :return: A dictionary with the empirical probabilities for each token.
        """
        probabilities = {}
        for token, count in token_counts.items():
            probabilities[token] = count / num_openings

        return probabilities


# Example token distribution (must sum to 1)
token_distribution = {
    "MemeCoinA": 0.5,
    "MemeCoinB": 0.3,
    "MemeCoinC": 0.2
}

# Create a MemeMysteryBox instance
mystery_box = MemeMysteryBox(token_distribution)

# Simulating the opening of the box 1000 times
num_simulations = 1000
token_counts = mystery_box.simulate_openings(num_simulations)

# Calculating empirical probabilities
empirical_probabilities = mystery_box.calculate_probabilities(token_counts, num_simulations)

# Output the results
print("Token Counts:", token_counts)
print("Empirical Probabilities:", empirical_probabilities)
```
