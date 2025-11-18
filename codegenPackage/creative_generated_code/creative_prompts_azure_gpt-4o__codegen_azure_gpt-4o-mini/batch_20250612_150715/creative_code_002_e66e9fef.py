"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.social
Prompt: Provide an example of how to use Moxie Bonding Curves to emphasize utility over speculation for Fan Tokens.
Generated: DETERMINISTIC_e66e9fefc520691d
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# This script implements a simple Moxie Bonding Curve for Fan Tokens.
# The bonding curve emphasizes utility over speculation by adjusting the token price based on demand.

class BondingCurve:
    """
    A class to represent a Moxie Bonding Curve for Fan Tokens.

    Attributes
    ----------
    reserve : float
        The total reserve of the underlying asset.
    supply : float
        The total supply of the tokens.
    token_price : float
        The current price of a single token.

    Methods
    -------
    buy_tokens(amount: int) -> None:
        Buys tokens based on the current price and updates the reserve and supply.
    
    sell_tokens(amount: int) -> None:
        Sells tokens and updates the reserve and supply.
    
    calculate_price() -> float:
        Calculates the current price of a token based on the supply and reserve.
    """

    def __init__(self, initial_reserve: float):
        """
        Initializes a new instance of BondingCurve with a given initial reserve.

        Parameters
        ----------
        initial_reserve : float
            The initial reserve amount.
        """
        if initial_reserve <= 0:
            raise ValueError("Initial reserve must be greater than zero.")
        
        self.reserve = initial_reserve
        self.supply = 0.0
        self.token_price = self.calculate_price()

    def calculate_price(self) -> float:
        """
        Calculates the current price of a token based on the supply and reserve.

        Returns
        -------
        float
            The calculated price of a token.
        """
        if self.supply == 0:
            return 0.0  # Avoid division by zero, price is zero if no tokens exist
        return self.reserve / self.supply  # Simple bonding curve formula

    def buy_tokens(self, amount: int) -> None:
        """
        Buys tokens based on the current price and updates the reserve and supply.

        Parameters
        ----------
        amount : int
            The number of tokens to buy.
        
        Raises
        ------
        ValueError
            If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        # Calculate the cost to buy the tokens
        total_cost = amount * self.calculate_price()
        
        # Update reserve and supply
        self.reserve += total_cost
        self.supply += amount
        self.token_price = self.calculate_price()  # Update token price

    def sell_tokens(self, amount: int) -> None:
        """
        Sells tokens and updates the reserve and supply.

        Parameters
        ----------
        amount : int
            The number of tokens to sell.
        
        Raises
        ------
        ValueError
            If the amount is less than or equal to zero or exceeds the supply.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if amount > self.supply:
            raise ValueError("Cannot sell more tokens than the current supply.")
        
        # Calculate the revenue from selling the tokens
        total_revenue = amount * self.calculate_price()
        
        # Update reserve and supply
        self.reserve -= total_revenue
        self.supply -= amount
        self.token_price = self.calculate_price()  # Update token price

# Usage example
if __name__ == "__main__":
    try:
        # Initializing the bonding curve with an initial reserve
        bonding_curve = BondingCurve(initial_reserve=1000.0)

        # Buying tokens
        bonding_curve.buy_tokens(10)
        print(f"Tokens bought. Current supply: {bonding_curve.supply}, Reserve: {bonding_curve.reserve}")

        # Selling tokens
        bonding_curve.sell_tokens(5)
        print(f"Tokens sold. Current supply: {bonding_curve.supply}, Reserve: {bonding_curve.reserve}")

    except ValueError as e:
        print(f"Error: {e}")
```
