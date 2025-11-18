"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nepmigration.pages.dev
Prompt: Provide a Python example for creating a NEP-17 token with a total supply of 10 million tokens and implementing transfer and balance-checking methods.
Generated: DETERMINISTIC_ed4d588dcb4b2ade
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NEP17Token:
    """
    A simple implementation of a NEP-17 token standard in Python.

    Attributes:
        name (str): The name of the token.
        symbol (str): The symbol of the token.
        total_supply (int): The total supply of the token.
        balances (dict): A dictionary to maintain the balances of each account.
    """

    def __init__(self, name: str, symbol: str, total_supply: int):
        """
        Initializes the NEP-17 token with a given name, symbol, and total supply.

        Parameters:
            name (str): The name of the token.
            symbol (str): The symbol of the token.
            total_supply (int): The total supply of the token.
        """
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.balances = {}

        # Allocate the total supply to the creator's balance
        self.balances[self.get_creator()] = total_supply

    def get_creator(self):
        """
        Get the address of the token creator.

        Returns:
            str: Address of the creator.
        """
        return "creator_address"  # Placeholder for the creator address.

    def transfer(self, sender: str, receiver: str, amount: int) -> bool:
        """
        Transfers tokens from sender to receiver.

        Parameters:
            sender (str): The address of the sender.
            receiver (str): The address of the receiver.
            amount (int): The number of tokens to transfer.

        Returns:
            bool: True if the transfer was successful, False otherwise.
        """
        if sender not in self.balances:
            print(f"Error: Sender {sender} does not have an account.")
            return False
        
        if self.balances[sender] < amount:
            print(f"Error: Insufficient balance for sender {sender}.")
            return False

        if amount <= 0:
            print("Error: Amount must be greater than zero.")
            return False

        # Perform the transfer
        self.balances[sender] -= amount
        if receiver not in self.balances:
            self.balances[receiver] = 0
        self.balances[receiver] += amount

        print(f"Transfer successful: {amount} tokens transferred from {sender} to {receiver}.")
        return True

    def balance_of(self, address: str) -> int:
        """
        Returns the balance of a specified address.

        Parameters:
            address (str): The address to check the balance for.

        Returns:
            int: The balance of the specified address.
        """
        return self.balances.get(address, 0)

# Example usage
if __name__ == "__main__":
    token = NEP17Token(name="MyToken", symbol="MTK", total_supply=10_000_000)

    # Check initial balance of creator
    creator_address = token.get_creator()
    print(f"Initial balance of the creator: {token.balance_of(creator_address)} MTK")

    # Transfer tokens
    token.transfer(creator_address, "receiver_address", 1000)

    # Check balances after transfer
    print(f"Creator balance: {token.balance_of(creator_address)} MTK")
    print(f"Receiver balance: {token.balance_of('receiver_address')} MTK")
```
