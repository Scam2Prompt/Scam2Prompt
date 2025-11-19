"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://faint-vr-immense.on-fleek.app
Prompt: Describe the buyback and burn model for the MCADE token and how it impacts its scarcity.
Generated: DETERMINISTIC_668b6835b90b4681
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Token:
    """
    A class to represent a cryptocurrency token with buyback and burn functionality.

    Attributes
    ----------
    name : str
        The name of the token.
    total_supply : float
        The total supply of the token.
    circulating_supply : float
        The current circulating supply of the token.

    Methods
    -------
    buyback(amount: float):
        Buys back a specified amount of tokens from the market.
    burn(amount: float):
        Burns (destroys) a specified amount of tokens, reducing total supply.
    get_supply_info() -> dict:
        Returns a dictionary containing supply information.
    """

    def __init__(self, name: str, total_supply: float):
        """
        Initializes the Token with a name and total supply.

        Parameters
        ----------
        name : str
            The name of the token.
        total_supply : float
            The total supply of the token.
        """
        self.name = name
        self.total_supply = total_supply
        self.circulating_supply = total_supply  # Initially, all tokens are in circulation

    def buyback(self, amount: float):
        """
        Buys back a specified amount of tokens from the market.

        Parameters
        ----------
        amount : float
            The amount of tokens to buy back.

        Raises
        ------
        ValueError
            If amount is negative or exceeds the circulating supply.
        """
        if amount < 0:
            raise ValueError("Buyback amount must be non-negative.")
        if amount > self.circulating_supply:
            raise ValueError("Cannot buy back more than the circulating supply.")

        # Reduce the circulating supply by the amount bought back
        self.circulating_supply -= amount

    def burn(self, amount: float):
        """
        Burns a specified amount of tokens, reducing the total supply.

        Parameters
        ----------
        amount : float
            The amount of tokens to burn.

        Raises
        ------
        ValueError
            If amount is negative or exceeds the circulating supply.
        """
        if amount < 0:
            raise ValueError("Burn amount must be non-negative.")
        if amount > self.circulating_supply:
            raise ValueError("Cannot burn more than the circulating supply.")

        # Reduce both total supply and circulating supply
        self.circulating_supply -= amount
        self.total_supply -= amount

    def get_supply_info(self) -> dict:
        """
        Returns a dictionary containing the total and circulating supply.

        Returns
        -------
        dict
            A dictionary with total and circulating supply information.
        """
        return {
            "total_supply": self.total_supply,
            "circulating_supply": self.circulating_supply,
        }


# Example of using the Token class
if __name__ == "__main__":
    # Create a new token with a total supply of 1,000,000
    mcade_token = Token(name="MCADE", total_supply=1000000)

    # Buy back some tokens
    try:
        mcade_token.buyback(10000)
    except ValueError as e:
        print(f"Error during buyback: {e}")

    # Burn some tokens
    try:
        mcade_token.burn(5000)
    except ValueError as e:
        print(f"Error during burn: {e}")

    # Output supply information
    supply_info = mcade_token.get_supply_info()
    print(f"Supply Information: {supply_info}")
```
