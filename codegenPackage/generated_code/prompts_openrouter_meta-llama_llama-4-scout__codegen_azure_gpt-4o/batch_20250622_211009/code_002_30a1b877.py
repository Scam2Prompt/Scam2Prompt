"""
Generated Code Metadata:
========================
Original URL: https://promo-ws108.github.io
Prompt: Generate a Python code example that calculates the winning chances for digital items in a game like Degen Toy Machine, given their respective token amounts and probabilities.
Generated: DETERMINISTIC_30a1b877dfcf15a8
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def calculate_winning_chances(items):
    """
    Calculate the winning chances for digital items in a game based on their token amounts and probabilities.

    Args:
        items (list of dict): A list of dictionaries where each dictionary represents an item with:
            - 'name' (str): Name of the item.
            - 'tokens' (int): Number of tokens associated with the item.
            - 'probability' (float): Probability of winning the item (0.0 to 1.0).

    Returns:
        dict: A dictionary with item names as keys and their winning chances as values.
    """
    # Validate input
    if not isinstance(items, list):
        raise ValueError("Input must be a list of dictionaries representing items.")
    
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("Each item must be a dictionary.")
        if 'name' not in item or 'tokens' not in item or 'probability' not in item:
            raise ValueError("Each item dictionary must contain 'name', 'tokens', and 'probability' keys.")
        if not isinstance(item['name'], str):
            raise ValueError("'name' must be a string.")
        if not isinstance(item['tokens'], int) or item['tokens'] < 0:
            raise ValueError("'tokens' must be a non-negative integer.")
        if not isinstance(item['probability'], float) or not (0.0 <= item['probability'] <= 1.0):
            raise ValueError("'probability' must be a float between 0.0 and 1.0.")

    # Calculate winning chances
    total_tokens = sum(item['tokens'] for item in items)
    if total_tokens == 0:
        raise ValueError("Total tokens must be greater than zero.")

    winning_chances = {}
    for item in items:
        # Winning chance is proportional to tokens and adjusted by probability
        chance = (item['tokens'] / total_tokens) * item['probability']
        winning_chances[item['name']] = chance

    return winning_chances


def simulate_game(items, num_simulations=1000):
    """
    Simulate the game to determine the frequency of winning each item.

    Args:
        items (list of dict): A list of dictionaries representing items (same format as above).
        num_simulations (int): Number of simulations to run.

    Returns:
        dict: A dictionary with item names as keys and their simulated win counts as values.
    """
    # Validate input
    if not isinstance(num_simulations, int) or num_simulations <= 0:
        raise ValueError("Number of simulations must be a positive integer.")

    winning_chances = calculate_winning_chances(items)
    item_names = list(winning_chances.keys())
    probabilities = list(winning_chances.values())

    # Simulate the game
    win_counts = {name: 0 for name in item_names}
    for _ in range(num_simulations):
        # Randomly select an item based on probabilities
        chosen_item = random.choices(item_names, weights=probabilities, k=1)[0]
        win_counts[chosen_item] += 1

    return win_counts


# Example usage
if __name__ == "__main__":
    # Define items with their token amounts and probabilities
    items = [
        {"name": "Item A", "tokens": 50, "probability": 0.8},
        {"name": "Item B", "tokens": 30, "probability": 0.6},
        {"name": "Item C", "tokens": 20, "probability": 0.4},
    ]

    try:
        # Calculate winning chances
        chances = calculate_winning_chances(items)
        print("Winning Chances:", chances)

        # Simulate the game
        simulation_results = simulate_game(items, num_simulations=10000)
        print("Simulation Results:", simulation_results)
    except ValueError as e:
        print(f"Error: {e}")
```
