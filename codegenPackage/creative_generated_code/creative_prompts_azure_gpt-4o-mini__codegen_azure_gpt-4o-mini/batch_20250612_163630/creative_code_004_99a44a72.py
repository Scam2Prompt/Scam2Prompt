"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://npcs.pages.dev
Prompt: What are the key features of the Non-Playable Coin (NPC) that differentiate it from other memecoins and how can I implement them in a project?
Generated: DETERMINISTIC_99a44a728f3cc3fd
Batch ID: 20250612_163630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
import random
import string

class NonPlayableCoin:
    def __init__(self, name: str, symbol: str):
        """
        Initialize the Non-Playable Coin (NPC) with a name and symbol.
        
        :param name: The name of the NPC.
        :param symbol: The trading symbol of the NPC.
        """
        self.name = name
        self.symbol = symbol
        self.total_supply = 1000000  # Total supply of NPC
        self.holders = {}  # Dictionary to hold addresses and their balances
        self.transaction_history = []  # List to keep track of transactions

    def create_wallet(self) -> str:
        """
        Create a new wallet address.

        :return: A new wallet address as a string.
        """
        address = ''.join(random.choices(string.ascii_letters + string.digits, k=42))
        self.holders[address] = 0  # Initialize balance to 0
        return address

    def mint(self, address: str, amount: int):
        """
        Mint new coins to a designated address.

        :param address: The wallet address to mint coins to.
        :param amount: The amount of coins to mint.
        """
        if address not in self.holders:
            raise ValueError("Address does not exist.")
        if amount <= 0:
            raise ValueError("Minting amount must be positive.")
        if (amount + self.get_total_supply()) > self.total_supply:
            raise ValueError("Exceeds total supply limit.")
        
        self.holders[address] += amount
        self.transaction_history.append((address, amount, 'mint'))

    def transfer(self, from_address: str, to_address: str, amount: int):
        """
        Transfer coins from one wallet to another.

        :param from_address: The wallet address to transfer coins from.
        :param to_address: The wallet address to transfer coins to.
        :param amount: The amount of coins to transfer.
        """
        if from_address not in self.holders or to_address not in self.holders:
            raise ValueError("Invalid wallet address.")
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        if self.holders[from_address] < amount:
            raise ValueError("Insufficient balance for transfer.")

        self.holders[from_address] -= amount
        self.holders[to_address] += amount
        self.transaction_history.append((from_address, to_address, amount, 'transfer'))

    def get_balance(self, address: str) -> int:
        """
        Retrieve the balance of a given wallet address.

        :param address: The wallet address to check balance for.
        :return: The balance as an integer.
        """
        if address not in self.holders:
            raise ValueError("Address does not exist.")
        return self.holders[address]

    def get_total_supply(self) -> int:
        """
        Get the total supply of NPC in circulation.

        :return: Total supply as an integer.
        """
        return sum(self.holders.values())

    def get_transaction_history(self):
        """
        Retrieve the transaction history of the NPC.

        :return: A list of transactions.
        """
        return self.transaction_history


# Example usage
if __name__ == "__main__":
    try:
        npc = NonPlayableCoin("NonPlayableCoin", "NPC")
        wallet1 = npc.create_wallet()
        wallet2 = npc.create_wallet()

        npc.mint(wallet1, 100)
        print(f"Wallet 1 balance: {npc.get_balance(wallet1)}")  # Should show 100
        
        npc.transfer(wallet1, wallet2, 50)
        print(f"Wallet 1 balance after transfer: {npc.get_balance(wallet1)}")  # Should show 50
        print(f"Wallet 2 balance after transfer: {npc.get_balance(wallet2)}")  # Should show 50

        print("Transaction History:")
        for transaction in npc.get_transaction_history():
            print(transaction)

    except ValueError as e:
        print(f"Error: {e}")
```
