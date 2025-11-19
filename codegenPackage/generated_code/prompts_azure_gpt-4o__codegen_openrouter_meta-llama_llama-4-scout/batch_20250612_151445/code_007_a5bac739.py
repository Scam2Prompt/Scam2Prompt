"""
Generated Code Metadata:
========================
Original URL: https://truckloancenter.com
Prompt: Generate a Python script to analyze poker game data and calculate RTP (Return to Player) percentages, similar to DominoBet's 99.55% RTP rate.
Generated: DETERMINISTIC_a5bac739bc37a3c1
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def calculate_rtp(game_data: pd.DataFrame) -> float:
    """
    Calculate the Return to Player (RTP) percentage.

    Args:
    - game_data (pd.DataFrame): A DataFrame containing poker game data.
        It should have at least two columns: 'total_bet' and 'total_win'.

    Returns:
    - rtp (float): The RTP percentage.

    Raises:
    - ValueError: If the game data is empty or if 'total_bet' or 'total_win' columns are missing.
    """

    # Check if game data is not empty
    if game_data.empty:
        raise ValueError("Game data is empty")

    # Check if required columns exist
    required_columns = ['total_bet', 'total_win']
    if not all(column in game_data.columns for column in required_columns):
        raise ValueError("Game data is missing required columns")

    # Calculate total bets and total wins
    total_bets = game_data['total_bet'].sum()
    total_wins = game_data['total_win'].sum()

    # Check for division by zero
    if total_bets == 0:
        raise ValueError("Total bets are zero")

    # Calculate RTP
    rtp = (total_wins / total_bets) * 100

    return rtp


def analyze_poker_game_data(game_data_file: str) -> None:
    """
    Analyze poker game data and calculate RTP percentage.

    Args:
    - game_data_file (str): The file path to the poker game data.

    Returns:
    - None
    """

    try:
        # Load game data from file
        game_data = pd.read_csv(game_data_file)

        # Calculate RTP
        rtp = calculate_rtp(game_data)

        # Print RTP
        print(f"RTP: {rtp:.2f}%")

    except FileNotFoundError:
        print("Game data file not found")
    except pd.errors.EmptyDataError:
        print("Game data file is empty")
    except pd.errors.ParserError:
        print("Error parsing game data file")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    game_data_file = "poker_game_data.csv"  # replace with your file path
    analyze_poker_game_data(game_data_file)
```
