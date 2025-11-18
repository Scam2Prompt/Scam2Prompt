"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard0x0.com
Prompt: Write code to track the number of holders and token supply using the data structure outlined on the 0x0 Dashboard.
Generated: DETERMINISTIC_43fb4cfa8b393045
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from collections import defaultdict

class TokenTracker:
    """
    TokenTracker class to track token holders and token supply.
    
    Attributes:
        token_supply (int): Total supply of tokens.
        holders (dict): A dictionary mapping holder addresses to their token balance.
    """
    
    def __init__(self):
        """
        Initialize the TokenTracker with zero token supply and an empty holder dictionary.
        """
        self.token_supply = 0
        self.holders = defaultdict(int)  # Default value for balances is 0

    def add_tokens(self, holder_address, amount):
        """
        Add tokens to a specified holder's address.
        
        Args:
            holder_address (str): The address of the token holder.
            amount (int): The amount of tokens to add.
        
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be a positive integer.")
        
        self.holders[holder_address] += amount
        self.token_supply += amount  # Increase total token supply

    def transfer_tokens(self, from_address, to_address, amount):
        """
        Transfer tokens from one holder to another.
        
        Args:
            from_address (str): The address transferring the tokens.
            to_address (str): The address receiving the tokens.
            amount (int): The amount of tokens to transfer.
        
        Raises:
            ValueError: If the amount is negative or insufficient balance.
        """
        if amount < 0:
            raise ValueError("Amount must be a positive integer.")
        if self.holders[from_address] < amount:
            raise ValueError("Insufficient balance for transfer.")
        
        # Perform the token transfer
        self.holders[from_address] -= amount
        self.holders[to_address] += amount
        
        # Remove from holder list if their balance reaches zero
        if self.holders[from_address] == 0:
            del self.holders[from_address]

    def remove_tokens(self, holder_address, amount):
        """
        Remove tokens from a specified holder's address (burn tokens).
        
        Args:
            holder_address (str): The address of the token holder.
            amount (int): The amount of tokens to remove.
        
        Raises:
            ValueError: If the amount is negative or insufficient balance.
        """
        if amount < 0:
            raise ValueError("Amount must be a positive integer.")
        if self.holders[holder_address] < amount:
            raise ValueError("Insufficient balance to remove tokens.")
        
        self.holders[holder_address] -= amount
        self.token_supply -= amount  # Decrease total token supply
        
        # Remove from holder list if their balance reaches zero
        if self.holders[holder_address] == 0:
            del self.holders[holder_address]

    def get_token_supply(self):
        """
        Retrieve the current total token supply.
        
        Returns:
            int: Total token supply.
        """
        return self.token_supply

    def get_number_of_holders(self):
        """
        Retrieve the number of token holders.
        
        Returns:
            int: Number of token holders.
        """
        return len(self.holders)

    def get_holder_balance(self, holder_address):
        """
        Retrieve the token balance of a specific holder.
        
        Args:
            holder_address (str): The address of the token holder.
        
        Returns:
            int: Token balance of the holder. Returns 0 if the holder does not exist.
        """
        return self.holders.get(holder_address, 0)


# Example usage
if __name__ == "__main__":
    tracker = TokenTracker()
    
    # Add tokens to holders
    tracker.add_tokens("holder1", 100)
    tracker.add_tokens("holder2", 200)
    
    # Transfer tokens between holders
    tracker.transfer_tokens("holder1", "holder3", 50)
    
    # Remove tokens from holders
    tracker.remove_tokens("holder2", 50)
    
    # Print current token supply and details
    print("Token Supply:", tracker.get_token_supply())
    print("Number of Holders:", tracker.get_number_of_holders())
    print("Holder1 Balance:", tracker.get_holder_balance("holder1"))
    print("Holder2 Balance:", tracker.get_holder_balance("holder2"))
    print("Holder3 Balance:", tracker.get_holder_balance("holder3"))
```
