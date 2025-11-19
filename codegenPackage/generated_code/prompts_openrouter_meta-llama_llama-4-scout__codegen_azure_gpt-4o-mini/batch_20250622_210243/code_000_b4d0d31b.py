"""
Generated Code Metadata:
========================
Original URL: https://procreaition.pages.dev
Prompt: What is the purpose of the Dual-SPL-Token model in Procreation AI's ecosystem, and how do $NEURA and $PAI tokens interact?
Generated: DETERMINISTIC_b4d0d31bf124e209
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DualSPLTokenModel:
    """
    A class to represent the Dual-SPL-Token model in Procreation AI's ecosystem.
    
    Attributes:
        neura_supply (float): Total supply of $NEURA tokens.
        pai_supply (float): Total supply of $PAI tokens.
        neura_balance (float): User's balance of $NEURA tokens.
        pai_balance (float): User's balance of $PAI tokens.
    """

    def __init__(self, neura_supply: float, pai_supply: float):
        """
        Initializes the DualSPLTokenModel with given token supplies.

        Args:
            neura_supply (float): Initial supply of $NEURA tokens.
            pai_supply (float): Initial supply of $PAI tokens.
        """
        self.neura_supply = neura_supply
        self.pai_supply = pai_supply
        self.neura_balance = 0.0
        self.pai_balance = 0.0

    def mint_neura(self, amount: float):
        """
        Mints new $NEURA tokens.

        Args:
            amount (float): The amount of $NEURA tokens to mint.

        Raises:
            ValueError: If the amount is negative or exceeds the available supply.
        """
        if amount < 0:
            raise ValueError("Amount to mint must be non-negative.")
        if self.neura_supply < amount:
            raise ValueError("Insufficient $NEURA supply to mint.")
        
        self.neura_balance += amount
        self.neura_supply -= amount

    def mint_pai(self, amount: float):
        """
        Mints new $PAI tokens.

        Args:
            amount (float): The amount of $PAI tokens to mint.

        Raises:
            ValueError: If the amount is negative or exceeds the available supply.
        """
        if amount < 0:
            raise ValueError("Amount to mint must be non-negative.")
        if self.pai_supply < amount:
            raise ValueError("Insufficient $PAI supply to mint.")
        
        self.pai_balance += amount
        self.pai_supply -= amount

    def transfer_neura(self, amount: float):
        """
        Transfers $NEURA tokens to another user.

        Args:
            amount (float): The amount of $NEURA tokens to transfer.

        Raises:
            ValueError: If the amount is negative or exceeds the user's balance.
        """
        if amount < 0:
            raise ValueError("Transfer amount must be non-negative.")
        if self.neura_balance < amount:
            raise ValueError("Insufficient $NEURA balance for transfer.")
        
        self.neura_balance -= amount

    def transfer_pai(self, amount: float):
        """
        Transfers $PAI tokens to another user.

        Args:
            amount (float): The amount of $PAI tokens to transfer.

        Raises:
            ValueError: If the amount is negative or exceeds the user's balance.
        """
        if amount < 0:
            raise ValueError("Transfer amount must be non-negative.")
        if self.pai_balance < amount:
            raise ValueError("Insufficient $PAI balance for transfer.")
        
        self.pai_balance -= amount

    def get_balances(self):
        """
        Returns the current balances of $NEURA and $PAI tokens.

        Returns:
            dict: A dictionary containing the balances of $NEURA and $PAI tokens.
        """
        return {
            "$NEURA": self.neura_balance,
            "$PAI": self.pai_balance
        }

# Example usage
if __name__ == "__main__":
    try:
        model = DualSPLTokenModel(neura_supply=10000, pai_supply=5000)
        model.mint_neura(100)
        model.mint_pai(50)
        print(model.get_balances())
        model.transfer_neura(30)
        model.transfer_pai(20)
        print(model.get_balances())
    except ValueError as e:
        print(f"Error: {e}")
```
