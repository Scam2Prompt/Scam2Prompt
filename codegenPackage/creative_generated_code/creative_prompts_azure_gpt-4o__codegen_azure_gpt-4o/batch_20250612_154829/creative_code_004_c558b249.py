"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xihusz.com
Prompt: Write a script to analyze betting patterns in OKX hash games and visualize the data using Python's matplotlib library.
Generated: DETERMINISTIC_c558b249ed89f88b
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import matplotlib.pyplot as plt
import numpy as np

def load_data(file_path):
    """
    Load betting data from a JSON file.

    :param file_path: Path to the JSON file containing betting data
    :return: Parsed JSON data as a Python object
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

def analyze_betting_patterns(data):
    """
    Analyze betting patterns from the loaded data.

    :param data: A list of betting records, each as a dictionary
    :return: Aggregated statistics as a dictionary
    """
    statistics = {
        "total_bets": 0,
        "average_bet_amount": 0,
        "bets_per_game": {},
        "unique_users": set()
    }

    total_bet_amount = 0

    for record in data:
        game = record.get("game_id")
        user = record.get("user_id")
        bet_amount = record.get("bet_amount")

        if not game or not user or bet_amount is None:
            continue  # Skip invalid records

        statistics["total_bets"] += 1
        total_bet_amount += bet_amount
        statistics["unique_users"].add(user)

        if game not in statistics["bets_per_game"]:
            statistics["bets_per_game"][game] = 0
        statistics["bets_per_game"][game] += 1

    if statistics["total_bets"] > 0:
        statistics["average_bet_amount"] = total_bet_amount / statistics["total_bets"]
    
    statistics["unique_users"] = len(statistics["unique_users"])
    return statistics

def visualize_data(statistics):
    """
    Visualize betting patterns using matplotlib.

    :param statistics: Aggregated betting statistics
    """
    # Bar chart for bets per game
    games = list(statistics["bets_per_game"].keys())
    bet_counts = list(statistics["bets_per_game"].values())

    plt.figure(figsize=(10, 6))
    plt.bar(games, bet_counts, color='skyblue')
    plt.xlabel('Game ID')
    plt.ylabel('Number of Bets')
    plt.title('Bets Per Game')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Pie chart for unique users
    unique_users = statistics["unique_users"]
    total_bets = statistics["total_bets"]
    labels = ['Unique Users', 'Total Bets - Users']
    sizes = [unique_users, total_bets]
    colors = ['lightgreen', 'lightcoral']

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Unique Users vs Total Bets')
    plt.show()

def main():
    """
    Main script execution function.
    """
    file_path = 'betting_data.json'  # Path to the betting data file
    data = load_data(file_path)
    if data is None:
        return

    statistics = analyze_betting_patterns(data)
    print("Betting Statistics:")
    print(f"Total Bets: {statistics['total_bets']}")
    print(f"Average Bet Amount: {statistics['average_bet_amount']:.2f}")
    print(f"Unique Users: {statistics['unique_users']}")
    print(f"Bets Per Game: {statistics['bets_per_game']}")

    visualize_data(statistics)

if __name__ == "__main__":
    main()
```
