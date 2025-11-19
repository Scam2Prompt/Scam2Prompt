"""
Generated Code Metadata:
========================
Original URL: https://peaq-token.pages.dev
Prompt: "Explain the role of the PEAQ token in the Economy of Things and its utility in network operations."
Generated: DETERMINISTIC_aafbbc72a71a9145
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PEAQToken:
    """
    A class to represent the PEAQ token in the Economy of Things (EoT).
    
    Attributes:
        name (str): The name of the token.
        symbol (str): The symbol of the token.
        total_supply (float): The total supply of the token.
        balance (dict): A dictionary to hold the balance of each user.
    """

    def __init__(self, name: str, symbol: str, total_supply: float):
        """
        Initializes the PEAQ token with a name, symbol, and total supply.
        
        Args:
            name (str): The name of the token.
            symbol (str): The symbol of the token.
            total_supply (float): The total supply of the token.
        """
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.balance = {}

    def mint(self, user: str, amount: float) -> None:
        """
        Mints new tokens for a user.
        
        Args:
            user (str): The user to mint tokens for.
            amount (float): The amount of tokens to mint.
        
        Raises:
            ValueError: If the amount is negative or exceeds total supply.
        """
        if amount < 0:
            raise ValueError("Amount to mint must be non-negative.")
        if amount + self.get_total_balance() > self.total_supply:
            raise ValueError("Minting exceeds total supply.")
        
        if user in self.balance:
            self.balance[user] += amount
        else:
            self.balance[user] = amount

    def transfer(self, from_user: str, to_user: str, amount: float) -> None:
        """
        Transfers tokens from one user to another.
        
        Args:
            from_user (str): The user sending tokens.
            to_user (str): The user receiving tokens.
            amount (float): The amount of tokens to transfer.
        
        Raises:
            ValueError: If the amount is negative or exceeds the sender's balance.
        """
        if amount < 0:
            raise ValueError("Transfer amount must be non-negative.")
        if from_user not in self.balance or self.balance[from_user] < amount:
            raise ValueError("Insufficient balance for transfer.")
        
        self.balance[from_user] -= amount
        if to_user in self.balance:
            self.balance[to_user] += amount
        else:
            self.balance[to_user] = amount

    def get_balance(self, user: str) -> float:
        """
        Returns the balance of a user.
        
        Args:
            user (str): The user whose balance is to be retrieved.
        
        Returns:
            float: The balance of the user.
        """
        return self.balance.get(user, 0.0)

    def get_total_balance(self) -> float:
        """
        Returns the total balance of all users.
        
        Returns:
            float: The total balance of all users.
        """
        return sum(self.balance.values())

    def __str__(self) -> str:
        """
        Returns a string representation of the PEAQ token.
        
        Returns:
            str: A string representation of the token.
        """
        return f"{self.name} ({self.symbol}): Total Supply: {self.total_supply}, Total Balance: {self.get_total_balance()}"


# Example usage
if __name__ == "__main__":
    try:
        peaq = PEAQToken("PEAQ Token", "PEAQ", 1000000.0)
        peaq.mint("Alice", 500.0)
        peaq.mint("Bob", 300.0)
        peaq.transfer("Alice", "Bob", 200.0)
        
        print(peaq)
        print(f"Alice's balance: {peaq.get_balance('Alice')}")
        print(f"Bob's balance: {peaq.get_balance('Bob')}")
    except ValueError as e:
        print(f"Error: {e}")
```
