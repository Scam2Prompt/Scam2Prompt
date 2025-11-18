"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Write a script to analyze betting data and generate statistics for popular games like sports betting and live casino games, as highlighted on S666.
Generated: DETERMINISTIC_15672ae811b935e3
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import sys

# Define a function to load betting data from a CSV file
def load_betting_data(file_path):
    """
    Load betting data from a CSV file into a pandas DataFrame.

    :param file_path: Path to the CSV file containing betting data
    :return: A pandas DataFrame with the loaded data
    """
    try:
        data = pd.read_csv(file_path)
        # Ensure all column names are standardized (lowercase, no spaces)
        data.columns = data.columns.str.lower().str.replace(' ', '_')
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty or corrupted.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


# Define a function to calculate basic statistics
def calculate_statistics(data):
    """
    Calculate basic statistics for betting data.

    :param data: A pandas DataFrame containing betting data
    :return: A dictionary of calculated statistics
    """
    try:
        stats = {
            'total_bets': len(data),
            'total_amount': data['amount'].sum(),
            'average_amount': data['amount'].mean(),
            'highest_bet': data['amount'].max(),
            'lowest_bet': data['amount'].min(),
            # Calculate win rate only if the column exists
            'win_rate': data['outcome'].value_counts(normalize=True).get('win', 0) * 100
        }
        return stats
    except KeyError as e:
        print(f"Error: Missing expected column in data: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during statistical calculations: {e}", file=sys.stderr)
        sys.exit(1)


# Define a function to group data by game type and calculate statistics
def analyze_by_game(data):
    """
    Analyze betting data by game type and calculate statistics.

    :param data: A pandas DataFrame containing betting data
    :return: A pandas DataFrame with statistics grouped by game type
    """
    try:
        grouped = data.groupby('game_type').agg(
            total_bets=('amount', 'count'),
            total_amount=('amount', 'sum'),
            average_amount=('amount', 'mean'),
            highest_bet=('amount', 'max'),
            lowest_bet=('amount', 'min'),
            win_rate=('outcome', lambda x: (x == 'win').mean() * 100)
        ).reset_index()
        return grouped
    except KeyError as e:
        print(f"Error: Missing expected column in data: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during game analysis: {e}", file=sys.stderr)
        sys.exit(1)


# Main function to orchestrate the analysis
def main():
    """
    Main function to load, process, and analyze betting data.
    """
    # Path to the betting data file (you can modify this path as needed)
    file_path = "betting_data.csv"

    # Load the betting data
    print("Loading betting data...")
    betting_data = load_betting_data(file_path)

    # Calculate overall statistics
    print("Calculating overall statistics...")
    overall_stats = calculate_statistics(betting_data)
    print("\nOverall Statistics:")
    for key, value in overall_stats.items():
        print(f"{key}: {value}")

    # Analyze data by game type
    print("\nAnalyzing data by game type...")
    game_stats = analyze_by_game(betting_data)
    print("\nStatistics by Game Type:")
    print(game_stats)


# Entry point of the script
if __name__ == "__main__":
    main()
```
