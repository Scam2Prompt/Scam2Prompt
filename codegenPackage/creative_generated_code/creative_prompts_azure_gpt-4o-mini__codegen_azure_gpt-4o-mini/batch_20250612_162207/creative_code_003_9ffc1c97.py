"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-bridge.pages.dev
Prompt: Explain the advanced tools available on the Portal Token Bridge for managing token transactions.
Generated: DETERMINISTIC_9ffc1c970ff57ded
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Portal Token Bridge Management Tool

class TokenBridge:
    """
    A class to manage token transactions on the Portal Token Bridge.
    It includes functionality to transfer, mint, and burn tokens, 
    as well as to check balances and transaction status.
    """

    def __init__(self):
        self.balances = {}
        self.transactions = {}

    def transfer_token(self, from_address, to_address, amount):
        """
        Transfers tokens from one address to another.

        :param from_address: The address sending the tokens.
        :param to_address: The address receiving the tokens.
        :param amount: The amount of tokens to transfer.
        :raises ValueError: If the amount is negative or exceeds balance.
        """
        if amount < 0:
            raise ValueError("Amount must be a positive number.")
        
        if from_address not in self.balances or self.balances[from_address] < amount:
            raise ValueError("Insufficient balance for transfer.")

        self.balances[from_address] -= amount
        self.balances[to_address] = self.balances.get(to_address, 0) + amount
        
        # Log transaction
        transaction_id = len(self.transactions) + 1
        self.transactions[transaction_id] = {
            'from': from_address,
            'to': to_address,
            'amount': amount,
            'status': 'completed'
        }
        return transaction_id

    def mint_token(self, address, amount):
        """
        Mints new tokens for a given address.

        :param address: The address to which the tokens will be minted.
        :param amount: The amount of tokens to mint.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be a positive number.")

        self.balances[address] = self.balances.get(address, 0) + amount
        
        # Log transaction
        transaction_id = len(self.transactions) + 1
        self.transactions[transaction_id] = {
            'from': None,
            'to': address,
            'amount': amount,
            'status': 'minted'
        }
        return transaction_id

    def burn_token(self, address, amount):
        """
        Burns tokens from a given address.

        :param address: The address from which tokens will be burned.
        :param amount: The amount of tokens to burn.
        :raises ValueError: If the amount is negative or exceeds balance.
        """
        if amount < 0:
            raise ValueError("Amount must be a positive number.")

        if address not in self.balances or self.balances[address] < amount:
            raise ValueError("Insufficient balance to burn.")

        self.balances[address] -= amount
        
        # Log transaction
        transaction_id = len(self.transactions) + 1
        self.transactions[transaction_id] = {
            'from': address,
            'to': None,
            'amount': amount,
            'status': 'burned'
        }
        return transaction_id

    def check_balance(self, address):
        """
        Checks the balance of a given address.

        :param address: The address to check the balance for.
        :return: The balance of the address.
        :raises KeyError: If the address does not exist.
        """
        if address not in self.balances:
            raise KeyError("Address not found.")
        return self.balances[address]

    def get_transaction_status(self, transaction_id):
        """
        Retrieves the status of a given transaction by ID.

        :param transaction_id: The ID of the transaction to check.
        :return: The status of the transaction.
        :raises KeyError: If the transaction ID does not exist.
        """
        if transaction_id not in self.transactions:
            raise KeyError("Transaction ID not found.")
        return self.transactions[transaction_id]['status']


# Example usage
if __name__ == "__main__":
    bridge = TokenBridge()
    
    try:
        # Mint tokens for an address
        print(f"Minting tokens: {bridge.mint_token('address_1', 100)}")
        # Check balance
        print(f"Balance of address_1: {bridge.check_balance('address_1')}")
        # Transfer tokens
        print(f"Transferring tokens: {bridge.transfer_token('address_1', 'address_2', 50)}")
        # Check balances
        print(f"Balance of address_1: {bridge.check_balance('address_1')}")
        print(f"Balance of address_2: {bridge.check_balance('address_2')}")
        # Burn tokens
        print(f"Burning tokens: {bridge.burn_token('address_1', 25)}")
        # Check final balance
        print(f"Final balance of address_1: {bridge.check_balance('address_1')}")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
