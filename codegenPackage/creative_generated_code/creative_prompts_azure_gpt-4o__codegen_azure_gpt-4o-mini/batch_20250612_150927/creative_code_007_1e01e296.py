"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adrop-wallet-checker.vercel.app
Prompt: Provide code to implement a feature that calculates a wallet’s chances of qualifying for airdrops based on transactional history.
Generated: DETERMINISTIC_1e01e2969c9c2812
Batch ID: 20250612_150927
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

class Transaction:
    """Represents a single transaction in the wallet."""
    
    def __init__(self, tx_id: str, amount: float, date: str):
        self.tx_id = tx_id
        self.amount = amount
        self.date = date

    def __repr__(self):
        return f"Transaction(tx_id={self.tx_id}, amount={self.amount}, date={self.date})"


class Wallet:
    """Represents a digital wallet that can assess airdrop eligibility."""
    
    def __init__(self, wallet_id: str):
        self.wallet_id = wallet_id
        self.transactions: List[Transaction] = []

    def add_transaction(self, tx_id: str, amount: float, date: str):
        """Adds a transaction to the wallet's transaction history."""
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        transaction = Transaction(tx_id, amount, date)
        self.transactions.append(transaction)

    def calculate_airdrop_eligibility(self) -> Dict[str, float]:
        """
        Calculates chances of qualifying for airdrops based on transaction history.
        
        Returns:
            A dictionary containing total transaction amount and average transaction amount.
        """
        if not self.transactions:
            return {"total_amount": 0, "average_amount": 0, "eligibility_score": 0}

        total_amount = sum(tx.amount for tx in self.transactions)
        average_amount = total_amount / len(self.transactions)
        
        # Simple eligibility score based on total amount
        eligibility_score = min(total_amount / 1000, 1)  # Assuming qualifying threshold is 1000
        
        return {
            "total_amount": total_amount,
            "average_amount": average_amount,
            "eligibility_score": eligibility_score
        }

    def to_json(self) -> str:
        """Convert wallet transactions to JSON format for easy storage or transfer."""
        transactions_data = [{'tx_id': tx.tx_id, 'amount': tx.amount, 'date': tx.date} for tx in self.transactions]
        wallet_data = {'wallet_id': self.wallet_id, 'transactions': transactions_data}
        return json.dumps(wallet_data)


# Example Usage
if __name__ == "__main__":
    try:
        wallet = Wallet("wallet_123")
        wallet.add_transaction("tx1", 300.0, "2023-01-01")
        wallet.add_transaction("tx2", 750.0, "2023-01-02")
        
        eligibility = wallet.calculate_airdrop_eligibility()
        print("Airdrop Eligibility:", eligibility)
        
        # Save wallet data to JSON
        wallet_json = wallet.to_json()
        print("Wallet JSON Data:", wallet_json)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
