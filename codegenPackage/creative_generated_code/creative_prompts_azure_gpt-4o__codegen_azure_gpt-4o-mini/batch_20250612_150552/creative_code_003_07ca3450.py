"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retiktoken-claim.pages.dev
Prompt: Create a Python script to calculate the rewards earned by a user based on their transaction history with Retik DeFi debit cards, considering the tiered cashback system.
Generated: DETERMINISTIC_07ca3450c77c1f5a
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

# Define a class to handle the transaction processing and reward calculations
class RewardCalculator:
    def __init__(self, transaction_history: List[Dict[str, float]], cashback_tiers: Dict[str, float]):
        """
        Initializes the RewardCalculator with transaction history and cashback tiers.
        
        :param transaction_history: A list of transaction dictionaries with 'amount' and 'category'.
        :param cashback_tiers: A dictionary mapping categories to cashback percentages.
        """
        self.transaction_history = transaction_history
        self.cashback_tiers = cashback_tiers

    def calculate_rewards(self) -> float:
        """
        Calculates the total rewards based on the transaction history and cashback tiers.
        
        :return: Total cashback earned by the user.
        """
        total_cashback = 0.0
        
        for transaction in self.transaction_history:
            try:
                amount = transaction['amount']
                category = transaction['category']
                
                # Get the cashback rate for the transaction category
                cashback_rate = self.cashback_tiers.get(category, 0.0)  # Default to 0.0 if category not found
                
                # Calculate cashback for this transaction
                cashback = amount * cashback_rate
                total_cashback += cashback
                
            except KeyError as e:
                print(f"Error processing transaction: missing key {e}")
            except TypeError:
                print("Error processing transaction: invalid data type encountered")
        
        return total_cashback

def load_transaction_history(file_path: str) -> List[Dict[str, float]]:
    """
    Load the transaction history from a JSON file.
    
    :param file_path: Path to the JSON file containing transaction data.
    :return: A list of transactions.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: The file could not be decoded. Please check the file format.")
        return []

def main():
    # Define cashback tiers based on transaction categories
    cashback_tiers = {
        "groceries": 0.05,
        "entertainment": 0.03,
        "utilities": 0.02,
        "other": 0.01
    }

    # Load the transaction history from a JSON file
    transaction_history = load_transaction_history('transactions.json')

    # Instantiate the RewardCalculator
    reward_calculator = RewardCalculator(transaction_history, cashback_tiers)
    
    # Calculate total rewards
    total_rewards = reward_calculator.calculate_rewards()
    
    # Print the total cashback earned
    print(f"Total cashback earned: ${total_rewards:.2f}")

if __name__ == "__main__":
    main()
```

This script includes a main function that loads a transaction history from a JSON file, calculates the cashback based on predefined tiers, and prints the total cashback earned. Proper error handling is implemented to manage potential issues with file operations and data integrity.
