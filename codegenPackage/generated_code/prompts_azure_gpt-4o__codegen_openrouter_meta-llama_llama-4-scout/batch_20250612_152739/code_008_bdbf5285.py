"""
Generated Code Metadata:
========================
Original URL: https://metis2020.com
Prompt: Create a Python script to automate the calculation of "slot gacor maxwin" probabilities based on game data, referencing Satria4D's focus on high-winning slots.
Generated: DETERMINISTIC_bdbf528597ddcb98
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

def calculate_slot_gacor_maxwin_probabilities(game_data):
    """
    Calculate 'slot gacor maxwin' probabilities based on game data.

    Parameters:
    game_data (pandas.DataFrame): A DataFrame containing game data.
        It should have the following columns:
            - 'game_id' (int): Unique game identifier.
            - 'win_amount' (float): The amount won in a game.
            - 'max_win_amount' (float): The maximum possible win amount in a game.
            - 'total_spins' (int): The total number of spins in a game.

    Returns:
    pandas.DataFrame: A DataFrame containing the calculated probabilities.
    """

    # Check if the input data is a pandas DataFrame
    if not isinstance(game_data, pd.DataFrame):
        raise ValueError("Game data must be a pandas DataFrame")

    # Check if the required columns exist in the game data
    required_columns = ['game_id', 'win_amount', 'max_win_amount', 'total_spins']
    if not all(column in game_data.columns for column in required_columns):
        raise ValueError("Game data is missing required columns")

    # Calculate the win rate for each game
    game_data['win_rate'] = game_data['win_amount'] / game_data['max_win_amount']

    # Calculate the spin-to-win ratio for each game
    game_data['spin_to_win_ratio'] = game_data['total_spins'] / game_data['win_amount']

    # Calculate the 'slot gacor maxwin' probability for each game
    game_data['slot_gacor_maxwin_probability'] = game_data['win_rate'] / game_data['spin_to_win_ratio']

    # Normalize the probabilities to ensure they add up to 1
    probabilities = game_data['slot_gacor_maxwin_probability']
    probabilities = probabilities / probabilities.sum()

    # Update the game data with the normalized probabilities
    game_data['slot_gacor_maxwin_probability'] = probabilities

    return game_data

def main():
    # Example game data
    game_data = pd.DataFrame({
        'game_id': [1, 2, 3],
        'win_amount': [1000, 2000, 3000],
        'max_win_amount': [10000, 20000, 30000],
        'total_spins': [100, 200, 300]
    })

    try:
        # Calculate the 'slot gacor maxwin' probabilities
        game_data_with_probabilities = calculate_slot_gacor_maxwin_probabilities(game_data)

        # Print the game data with probabilities
        print(game_data_with_probabilities)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
