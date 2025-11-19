"""
Generated Code Metadata:
========================
Original URL: https://amlexplore.org
Prompt: Design a system to categorize cryptocurrency transactions into high-risk and low-risk categories based on AMLBot's risk scoring criteria, such as suspicious sources, dark market coins, and terrorist financing.
Generated: DETERMINISTIC_e020f7a7774dafe9
Batch ID: 20250622_212502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Transaction:
    """
    A class to represent a cryptocurrency transaction.
    """
    def __init__(self, transaction_id: str, amount: float, source: str, destination: str, coin_type: str):
        self.transaction_id = transaction_id
        self.amount = amount
        self.source = source
        self.destination = destination
        self.coin_type = coin_type

    def to_dict(self) -> Dict[str, Any]:
        """Convert the transaction to a dictionary."""
        return {
            "transaction_id": self.transaction_id,
            "amount": self.amount,
            "source": self.source,
            "destination": self.destination,
            "coin_type": self.coin_type
        }

class RiskCategorizer:
    """
    A class to categorize transactions based on risk criteria.
    """
    HIGH_RISK_SOURCES = {"suspicious_source_1", "suspicious_source_2"}
    DARK_MARKET_COINS = {"darkcoin1", "darkcoin2"}
    TERRORIST_FINANCING_KEYWORDS = {"terrorist", "funding"}

    @staticmethod
    def categorize_transaction(transaction: Transaction) -> str:
        """
        Categorize a transaction as 'high-risk' or 'low-risk'.
        
        Args:
            transaction (Transaction): The transaction to categorize.

        Returns:
            str: The risk category of the transaction.
        """
        if (transaction.source in RiskCategorizer.HIGH_RISK_SOURCES or
            transaction.coin_type in RiskCategorizer.DARK_MARKET_COINS or
            any(keyword in transaction.source for keyword in RiskCategorizer.TERRORIST_FINANCING_KEYWORDS)):
            return "high-risk"
        return "low-risk"

def load_transactions(file_path: str) -> List[Transaction]:
    """
    Load transactions from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing transactions.

    Returns:
        List[Transaction]: A list of Transaction objects.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Transaction(**item) for item in data]
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Error: The file {file_path} was not found.") from e
    except json.JSONDecodeError as e:
        raise ValueError("Error: The file contains invalid JSON.") from e

def categorize_transactions(transactions: List[Transaction]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Categorize a list of transactions into high-risk and low-risk.

    Args:
        transactions (List[Transaction]): The list of transactions to categorize.

    Returns:
        Dict[str, List[Dict[str, Any]]]: A dictionary containing categorized transactions.
    """
    categorized = {
        "high-risk": [],
        "low-risk": []
    }

    for transaction in transactions:
        risk_category = RiskCategorizer.categorize_transaction(transaction)
        categorized[risk_category].append(transaction.to_dict())

    return categorized

def main(file_path: str) -> None:
    """
    Main function to load, categorize, and print transactions.

    Args:
        file_path (str): The path to the JSON file containing transactions.
    """
    try:
        transactions = load_transactions(file_path)
        categorized_transactions = categorize_transactions(transactions)
        print(json.dumps(categorized_transactions, indent=4))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    # Example usage: replace 'transactions.json' with the path to your JSON file
    main('transactions.json')
```
