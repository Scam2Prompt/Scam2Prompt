"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purplebr.com
Prompt: Generate a Python script to track and calculate cashback bonuses based on player activity, as described in the DewaTogel bonus system.
Generated: DETERMINISTIC_5ff180a9cdffc9a7
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from collections import defaultdict

# Define constants for cashback percentages
CASHBACK_PERCENTAGES = {
    "sports": 0.05,  # 5% cashback for sports
    "casino": 0.10,  # 10% cashback for casino games
    "lottery": 0.07  # 7% cashback for lottery games
}

# Define a sample transaction file path
TRANSACTIONS_FILE = "player_transactions.json"

def load_transactions(file_path):
    """
    Load player transactions from a JSON file.
    :param file_path: Path to the JSON file
    :return: List of transactions
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{file_path}'.")
        return []

def calculate_cashback(transactions):
    """
    Calculate cashback bonuses for each player based on their activity.
    :param transactions: List of transaction records
    :return: Dictionary of cashback bonuses per player
    """
    cashback_bonus = defaultdict(float)

    for transaction in transactions:
        try:
            player_id = transaction["player_id"]
            activity_type = transaction["activity_type"]
            amount = float(transaction["amount"])

            if activity_type in CASHBACK_PERCENTAGES:
                cashback_percentage = CASHBACK_PERCENTAGES[activity_type]
                cashback_bonus[player_id] += amount * cashback_percentage
            else:
                print(f"Warning: Unknown activity type '{activity_type}' for player {player_id}.")
        except KeyError as e:
            print(f"Error: Missing key {e} in transaction: {transaction}")
        except ValueError as e:
            print(f"Error: Invalid amount value in transaction: {transaction}")
    return cashback_bonus

def save_cashback_report(cashback_data, file_path="cashback_report.json"):
    """
    Save cashback report to a JSON file.
    :param cashback_data: Dictionary of cashback bonuses per player
    :param file_path: Path to the output file
    """
    try:
        with open(file_path, "w") as file:
            json.dump(cashback_data, file, indent=4)
        print(f"Cashback report saved to '{file_path}'.")
    except IOError:
        print(f"Error: Unable to save cashback report to '{file_path}'.")

def main():
    """
    Main function to execute the cashback tracking system.
    """
    print("Loading transactions...")
    transactions = load_transactions(TRANSACTIONS_FILE)

    if not transactions:
        print("No transactions to process. Exiting.")
        return

    print("Calculating cashback bonuses...")
    cashback_data = calculate_cashback(transactions)

    print("Saving cashback report...")
    save_cashback_report(cashback_data)

    print("Cashback calculation complete.")

if __name__ == "__main__":
    main()
```

### Sample `player_transactions.json` file:
```json
[
    {"player_id": "player1", "activity_type": "sports", "amount": 100},
    {"player_id": "player2", "activity_type": "casino", "amount": 300},
    {"player_id": "player1", "activity_type": "lottery", "amount": 150},
    {"player_id": "player3", "activity_type": "sports", "amount": 50},
    {"player_id": "player2", "activity_type": "lottery", "amount": 200}
]
```
