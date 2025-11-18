"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-artyfact.pages.dev
Prompt: Provide a Python script to calculate the deflationary mechanism of the $ARTY token based on Play-and-Earn activities and NFT transactions.
Generated: DETERMINISTIC_4703262f3eb4c4e6
Batch ID: 20250612_151931
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

class ArtyToken:
    """
    A class to represent the ARTY token and manage its deflationary mechanism
    based on Play-and-Earn activities and NFT transactions.
    """
    
    def __init__(self, initial_supply: float):
        """
        Initializes the ARTY token with an initial supply.
        
        Args:
        - initial_supply (float): The initial supply of the ARTY token.
        """
        if initial_supply < 0:
            raise ValueError("Initial supply must be non-negative.")
        self.total_supply = initial_supply
        self.deflation_rate = 0.05  # 5% deflation rate for each transaction
        self.transaction_history: List[Dict] = []

    def play_and_earn(self, earnings: float) -> None:
        """
        Simulates a Play-and-Earn activity that adds earnings to the total supply.
        
        Args:
        - earnings (float): The amount earned from the Play-and-Earn activity.
        
        Raises:
        - ValueError: If earnings are negative.
        """
        if earnings < 0:
            raise ValueError("Earnings must be non-negative.")
        self.total_supply += earnings
        self.record_transaction("play_and_earn", earnings)

    def nft_transaction(self, nft_price: float) -> None:
        """
        Simulates an NFT transaction that triggers the deflationary mechanism.
        
        Args:
        - nft_price (float): The price of the NFT being transacted.
        
        Raises:
        - ValueError: If nft_price is negative.
        """
        if nft_price < 0:
            raise ValueError("NFT price must be non-negative.")
        deflation_amount = nft_price * self.deflation_rate
        self.total_supply -= deflation_amount
        self.record_transaction("nft_transaction", -deflation_amount)

    def record_transaction(self, transaction_type: str, amount: float) -> None:
        """
        Records a transaction in the transaction history.
        
        Args:
        - transaction_type (str): The type of transaction (e.g., "play_and_earn", "nft_transaction").
        - amount (float): The amount of the transaction.
        """
        transaction = {
            'type': transaction_type,
            'amount': amount,
            'total_supply_after': self.total_supply
        }
        self.transaction_history.append(transaction)

    def get_total_supply(self) -> float:
        """
        Returns the current total supply of the ARTY token.
        
        Returns:
        - float: The current total supply.
        """
        return self.total_supply

    def get_transaction_history(self) -> List[Dict]:
        """
        Returns the transaction history.
        
        Returns:
        - List[Dict]: A list of recorded transactions.
        """
        return self.transaction_history


if __name__ == "__main__":
    # Example usage of the ArtyToken class
    try:
        arty_token = ArtyToken(initial_supply=10000.0)
        
        # Simulating Play-and-Earn activities
        arty_token.play_and_earn(500.0)
        
        # Simulating NFT transactions
        arty_token.nft_transaction(200.0)
        
        # Output the current total supply and transaction history
        print(f"Current Total Supply: {arty_token.get_total_supply()}")
        print("Transaction History:")
        print(json.dumps(arty_token.get_transaction_history(), indent=4))
        
    except ValueError as e:
        print(f"Error: {e}")
```
