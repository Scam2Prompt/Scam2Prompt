"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://promo-ps44.github.io
Prompt: Generate a function that calculates the probability of winning for different tokens in the Degen Toy Machine.
Generated: DETERMINISTIC_8a9f8fe793383c73
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_token_probabilities(tokens, spins, token_odds):
    """
    Calculate the probability of winning for different tokens in the Degen Toy Machine.

    Args:
        tokens (list): List of token names (e.g., ['TokenA', 'TokenB', 'TokenC']).
        spins (int): Number of spins to calculate probabilities over.
        token_odds (dict): Dictionary containing token odds as percentages (e.g., {'TokenA': 50, 'TokenB': 30, 'TokenC': 20}).

    Returns:
        dict: Dictionary with token names as keys and their winning probabilities as values.
    """
    if not isinstance(tokens, list) or not isinstance(token_odds, dict):
        raise ValueError("Tokens must be a list and token_odds must be a dictionary.")

    total_odds = sum(token_odds.values())
    if total_odds != 100:
        raise ValueError("Token odds must sum up to 100%.")

    for token in tokens:
        if token not in token_odds:
            raise ValueError(f"Token '{token}' is missing from token_odds.")

    # Initialize a dictionary to count the wins for each token
    token_wins = {token: 0 for token in tokens}

    # Simulate spins
    for _ in range(spins):
        # Generate a random number between 1 and 100
        random_number = random.randint(1, 100)

        # Determine the winning token based on odds
        cumulative_odds = 0
        for token in tokens:
            cumulative_odds += token_odds[token]
            if random_number <= cumulative_odds:
                token_wins[token] += 1
                break

    # Calculate probabilities as percentages
    token_probabilities = {token: (wins / spins) * 100 for token, wins in token_wins.items()}

    return token_probabilities


# Example Usage
if __name__ == "__main__":
    # Define tokens, number of spins, and their odds
    tokens = ['TokenA', 'TokenB', 'TokenC']
    spins = 10000
    token_odds = {
        'TokenA': 50,  # 50% chance
        'TokenB': 30,  # 30% chance
        'TokenC': 20   # 20% chance
    }

    try:
        # Calculate probabilities
        probabilities = calculate_token_probabilities(tokens, spins, token_odds)
        print("Winning Probabilities:", probabilities)
    except ValueError as e:
        print("Error:", e)
```
