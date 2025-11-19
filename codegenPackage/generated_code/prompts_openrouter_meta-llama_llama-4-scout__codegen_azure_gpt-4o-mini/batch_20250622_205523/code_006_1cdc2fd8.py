"""
Generated Code Metadata:
========================
Original URL: https://infinivi.io
Prompt: Write a whitepaper for a new cryptocurrency token, similar to IVI Token, focusing on its utility for sports fans and integration with blockchain technology.
Generated: DETERMINISTIC_1cdc2fd880fa614e
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from datetime import datetime
import json

class CryptoToken:
    """
    A class to represent a cryptocurrency token for sports fans.
    
    Attributes
    ----------
    name : str
        The name of the token.
    symbol : str
        The symbol of the token.
    total_supply : int
        The total supply of the token.
    holders : dict
        A dictionary to keep track of token holders and their balances.
    transactions : list
        A list to keep track of all transactions made with the token.
    """

    def __init__(self, name, symbol, total_supply):
        """
        Initializes the CryptoToken with a name, symbol, and total supply.
        
        Parameters
        ----------
        name : str
            The name of the token.
        symbol : str
            The symbol of the token.
        total_supply : int
            The total supply of the token.
        """
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.holders = {}
        self.transactions = []

    def add_holder(self, address, amount):
        """
        Adds a new holder to the token with a specified amount.
        
        Parameters
        ----------
        address : str
            The address of the token holder.
        amount : int
            The amount of tokens to assign to the holder.
        
        Raises
        ------
        ValueError
            If the amount exceeds the total supply.
        """
        if amount > self.total_supply:
            raise ValueError("Amount exceeds total supply.")
        
        self.holders[address] = self.holders.get(address, 0) + amount
        self.total_supply -= amount
        self.transactions.append({
            'from': 'initial_supply',
            'to': address,
            'amount': amount,
            'timestamp': datetime.now().isoformat()
        })

    def transfer(self, from_address, to_address, amount):
        """
        Transfers tokens from one holder to another.
        
        Parameters
        ----------
        from_address : str
            The address of the sender.
        to_address : str
            The address of the receiver.
        amount : int
            The amount of tokens to transfer.
        
        Raises
        ------
        ValueError
            If the sender does not have enough tokens or if the amount is invalid.
        """
        if from_address not in self.holders or self.holders[from_address] < amount:
            raise ValueError("Insufficient balance for transfer.")
        
        self.holders[from_address] -= amount
        self.holders[to_address] = self.holders.get(to_address, 0) + amount
        self.transactions.append({
            'from': from_address,
            'to': to_address,
            'amount': amount,
            'timestamp': datetime.now().isoformat()
        })

    def get_balance(self, address):
        """
        Returns the balance of a specified address.
        
        Parameters
        ----------
        address : str
            The address of the token holder.
        
        Returns
        -------
        int
            The balance of the specified address.
        """
        return self.holders.get(address, 0)

    def to_json(self):
        """
        Converts the token information to a JSON string.
        
        Returns
        -------
        str
            A JSON representation of the token.
        """
        return json.dumps({
            'name': self.name,
            'symbol': self.symbol,
            'total_supply': self.total_supply,
            'holders': self.holders,
            'transactions': self.transactions
        }, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        # Create a new cryptocurrency token for sports fans
        sports_token = CryptoToken("FanToken", "FAN", 1000000)

        # Add holders
        sports_token.add_holder("0x123", 100)
        sports_token.add_holder("0x456", 200)

        # Transfer tokens
        sports_token.transfer("0x123", "0x456", 50)

        # Print the balance of a holder
        print(f"Balance of 0x123: {sports_token.get_balance('0x123')}")

        # Print the token information in JSON format
        print(sports_token.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")
```
