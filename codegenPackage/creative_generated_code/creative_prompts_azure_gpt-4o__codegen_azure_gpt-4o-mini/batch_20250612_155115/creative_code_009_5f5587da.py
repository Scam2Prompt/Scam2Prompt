"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptomixer.at
Prompt: Create a script to calculate the percentage distribution of Bitcoin outputs for a mixing operation, ensuring privacy as described on CryptoMixer.at.
Generated: DETERMINISTIC_5f5587da006631d3
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class BitcoinMixer:
    """Class to handle Bitcoin output distribution calculations for mixing operations."""

    def __init__(self, transactions: List[Dict[str, Any]]) -> None:
        """
        Initializes the BitcoinMixer with a list of transactions.

        Args:
            transactions (List[Dict[str, Any]]): A list of transactions, each containing
            a 'value' key representing the Bitcoin output.
        """
        self.transactions = transactions

    def calculate_distribution(self) -> Dict[str, float]:
        """
        Calculates the percentage distribution of Bitcoin outputs.

        Returns:
            Dict[str, float]: A dictionary with the output values as keys and their
            percentage distribution as values.
        """
        total_value = sum(transaction['value'] for transaction in self.transactions)
        
        if total_value == 0:
            raise ValueError("Total value of transactions cannot be zero.")

        distribution = {
            str(transaction['value']): (transaction['value'] / total_value) * 100
            for transaction in self.transactions
        }

        return distribution

def load_transactions_from_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Loads Bitcoin transactions from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing transactions.

    Returns:
        List[Dict[str, Any]]: A list of transaction dictionaries.
    """
    try:
        with open(file_path, 'r') as file:
            transactions = json.load(file)
            if not isinstance(transactions, list):
                raise ValueError("Transaction data must be a list.")
            return transactions
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the file.")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {str(e)}")

def main(file_path: str) -> None:
    """
    Main function to execute the Bitcoin mixing operation distribution calculation.

    Args:
        file_path (str): The path to the JSON file containing the Bitcoin transactions.
    """
    try:
        transactions = load_transactions_from_file(file_path)
        mixer = BitcoinMixer(transactions)
        distribution = mixer.calculate_distribution()
        print("Percentage Distribution of Bitcoin Outputs:")
        for value, percentage in distribution.items():
            print(f"{value} BTC: {percentage:.2f}%")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Update the file path to your JSON file containing Bitcoin transactions.
    json_file_path = 'transactions.json'
    main(json_file_path)
```

### JSON File Format Example
```json
[
    {"value": 0.5},
    {"value": 0.2},
    {"value": 0.3}
]
```
