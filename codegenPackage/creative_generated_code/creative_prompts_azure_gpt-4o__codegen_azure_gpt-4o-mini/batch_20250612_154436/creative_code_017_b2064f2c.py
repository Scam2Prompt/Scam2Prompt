"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exchange68.com
Prompt: Generate code to calculate the utility token benefits and functions, referencing the Blockchain 101 insights from Exchange68.com.
Generated: DETERMINISTIC_b2064f2c56c9c3cb
Batch ID: 20250612_154436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class UtilityToken:
    def __init__(self, name, symbol, total_supply):
        """
        Initialize a new utility token.
        
        :param name: str - The name of the utility token.
        :param symbol: str - The symbol representing the utility token.
        :param total_supply: int - The total supply of the utility token.
        """
        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.balances = {}
    
    def issue_token(self, recipient, amount):
        """
        Issue tokens to a recipient.
        
        :param recipient: str - The address of the recipient.
        :param amount: int - The number of tokens to issue.
        :raises ValueError: If the amount exceeds the total supply.
        """
        if amount < 0:
            raise ValueError("Amount to issue cannot be negative.")
        if amount + self.total_supply > 1_000_000_000:  # Example limit
            raise ValueError("Issuing this amount exceeds total supply limit.")
        
        self.total_supply += amount
        if recipient in self.balances:
            self.balances[recipient] += amount
        else:
            self.balances[recipient] = amount

    def transfer(self, sender, recipient, amount):
        """
        Transfer tokens from one address to another.
        
        :param sender: str - The address of the sender.
        :param recipient: str - The address of the recipient.
        :param amount: int - The amount to transfer.
        :raises ValueError: If the sender has insufficient balance or amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount to transfer cannot be negative.")
        if sender not in self.balances or self.balances[sender] < amount:
            raise ValueError("Insufficient balance for the transfer.")
        
        self.balances[sender] -= amount
        if recipient in self.balances:
            self.balances[recipient] += amount
        else:
            self.balances[recipient] = amount

    def get_balance(self, address):
        """
        Get the balance of a specific address.
        
        :param address: str - The address to check the balance for.
        :return: int - The balance of the address.
        """
        return self.balances.get(address, 0)

    def get_total_supply(self):
        """
        Get the total supply of the utility token.
        
        :return: int - The total supply of the token.
        """
        return self.total_supply

# Example Usage
if __name__ == "__main__":
    # Create an instance of UtilityToken
    token = UtilityToken(name="ExampleToken", symbol="ETKN", total_supply=0)

    # Issue tokens to a recipient
    try:
        token.issue_token(recipient="0x123", amount=10000)
        print(f"Tokens issued. New total supply: {token.get_total_supply()}")
    except ValueError as e:
        print(f"Error issuing tokens: {e}")

    # Transfer tokens
    try:
        token.transfer(sender="0x123", recipient="0x456", amount=5000)
        print(f"Transfer successful. Sender balance: {token.get_balance('0x123')}, Recipient balance: {token.get_balance('0x456')}")
    except ValueError as e:
        print(f"Error during transfer: {e}")

    # Check balances
    print(f"Balance of 0x123: {token.get_balance('0x123')}")
    print(f"Balance of 0x456: {token.get_balance('0x456')}")
```
