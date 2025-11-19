"""
Generated Code Metadata:
========================
Original URL: https://link-protocol.net
Prompt: Write a Python script to analyze Wattpad's writing contest data, including entry rates, win rates, and author demographics, to identify trends and insights.
Generated: DETERMINISTIC_137456dda8eb1d5a
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wattpad_contest_analysis.py

import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

# Define a function to load contest data from a CSV file
def load_contest_data(file_path):
    """
    Load Wattpad contest data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Contest data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error: Failed to parse file '{file_path}'.")
        return None

# Define a function to calculate entry rates
def calculate_entry_rates(data):
    """
    Calculate entry rates for each contest.

    Args:
        data (pd.DataFrame): Contest data.

    Returns:
        dict: Entry rates for each contest.
    """
    entry_rates = defaultdict(int)
    for contest, entries in data.groupby('contest')['entries'].sum().items():
        entry_rates[contest] = entries
    return dict(entry_rates)

# Define a function to calculate win rates
def calculate_win_rates(data):
    """
    Calculate win rates for each contest.

    Args:
        data (pd.DataFrame): Contest data.

    Returns:
        dict: Win rates for each contest.
    """
    win_rates = defaultdict(int)
    for contest, wins in data.groupby('contest')['wins'].sum().items():
        total_entries = data[data['contest'] == contest]['entries'].sum()
        win_rates[contest] = (wins / total_entries) * 100 if total_entries > 0 else 0
    return dict(win_rates)

# Define a function to analyze author demographics
def analyze_author_demographics(data):
    """
    Analyze author demographics.

    Args:
        data (pd.DataFrame): Contest data.

    Returns:
        dict: Author demographics.
    """
    demographics = {
        'age': data['author_age'].value_counts().to_dict(),
        'country': data['author_country'].value_counts().to_dict(),
        'gender': data['author_gender'].value_counts().to_dict()
    }
    return demographics

# Define a function to plot contest data
def plot_contest_data(entry_rates, win_rates):
    """
    Plot contest data.

    Args:
        entry_rates (dict): Entry rates for each contest.
        win_rates (dict): Win rates for each contest.
    """
    plt.figure(figsize=(10, 6))

    plt.subplot(1, 2, 1)
    plt.bar(entry_rates.keys(), entry_rates.values())
    plt.xlabel('Contest')
    plt.ylabel('Entry Rate')
    plt.title('Entry Rates')

    plt.subplot(1, 2, 2)
    plt.bar(win_rates.keys(), win_rates.values())
    plt.xlabel('Contest')
    plt.ylabel('Win Rate (%)')
    plt.title('Win Rates')

    plt.tight_layout()
    plt.show()

# Main function
def main():
    file_path = 'wattpad_contest_data.csv'  # replace with your CSV file path
    data = load_contest_data(file_path)

    if data is not None:
        entry_rates = calculate_entry_rates(data)
        win_rates = calculate_win_rates(data)
        demographics = analyze_author_demographics(data)

        print("Entry Rates:")
        for contest, rate in entry_rates.items():
            print(f"{contest}: {rate}")

        print("\nWin Rates:")
        for contest, rate in win_rates.items():
            print(f"{contest}: {rate:.2f}%")

        print("\nAuthor Demographics:")
        for demographic, counts in demographics.items():
            print(f"{demographic.capitalize()}: {counts}")

        plot_contest_data(entry_rates, win_rates)

if __name__ == '__main__':
    main()
```

```python
# wattpad_contest_data.csv example

contest,entries,wins,author_age,author_country,author_gender
contest1,100,5,25,USA,Female
contest1,100,5,30,Canada,Male
contest2,50,2,28,UK,Female
contest2,50,2,22,Australia,Male
contest3,200,10,35,USA,Female
contest3,200,10,40,Canada,Male
```
