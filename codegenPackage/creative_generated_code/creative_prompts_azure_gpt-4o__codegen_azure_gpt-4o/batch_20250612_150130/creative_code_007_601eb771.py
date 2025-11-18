"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epiccoin-miners.ltd
Prompt: Write a Python script to calculate total deposits, withdrawals, and active accounts, similar to the statistics displayed on epiccoin-miners.ltd.
Generated: DETERMINISTIC_601eb771f19467a1
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# Function to load account data from a file
def load_account_data(file_path):
    """
    Load account data from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing account data.

    Returns:
        list: List of account dictionaries loaded from the file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from file {file_path}: {e}")

# Function to calculate statistics
def calculate_statistics(accounts):
    """
    Calculate total deposits, withdrawals, and active accounts.

    Args:
        accounts (list): List of account dictionaries.

    Returns:
        dict: Dictionary containing calculated statistics.
    """
    total_deposits = 0.0
    total_withdrawals = 0.0
    active_account_count = 0

    for account in accounts:
        # Account data validation
        if not all(key in account for key in ('deposits', 'withdrawals', 'is_active')):
            raise ValueError(f"Invalid account data format: {account}")

        # Summing deposits and withdrawals
        total_deposits += float(account.get('deposits', 0))
        total_withdrawals += float(account.get('withdrawals', 0))

        # Counting active accounts
        if account.get('is_active'):
            active_account_count += 1

    return {
        "total_deposits": total_deposits,
        "total_withdrawals": total_withdrawals,
        "active_accounts": active_account_count
    }

# Main function to run the script
def main():
    """
    Main function to execute the script logic.

    Loads account data, calculates statistics, and displays the results.
    """
    # Path to the JSON file containing account data
    file_path = "account_data.json"  # Replace with the actual file path
    
    try:
        # Load account data from file
        accounts = load_account_data(file_path)

        # Calculate statistics
        stats = calculate_statistics(accounts)

        # Display results
        print("Account Statistics:")
        print(f"Total Deposits: ${stats['total_deposits']:.2f}")
        print(f"Total Withdrawals: ${stats['total_withdrawals']:.2f}")
        print(f"Active Accounts: {stats['active_accounts']}")
    
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except ValueError as val_error:
        print(f"Error: {val_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
