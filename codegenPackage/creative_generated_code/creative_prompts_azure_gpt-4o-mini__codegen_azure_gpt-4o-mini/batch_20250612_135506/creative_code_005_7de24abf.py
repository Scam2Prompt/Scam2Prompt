"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-etftoken.web.app
Prompt: Describe the burning mechanism of Bitcoin ETF Token (BTCETF) and its impact on token supply as Bitcoin ETF milestones are reached.
Generated: DETERMINISTIC_7de24abf72e96ec1
Batch ID: 20250612_135506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BitcoinETFToken:
    """
    A class to represent a Bitcoin ETF Token (BTCETF) and its burning mechanism.

    Attributes:
        total_supply (int): The total supply of the BTCETF tokens.
        burned_tokens (int): The total number of tokens burned.
        milestones (dict): A dictionary to hold milestones and their respective burn amounts.
    """

    def __init__(self, initial_supply: int):
        """
        Initializes the Bitcoin ETF Token with an initial supply.

        Parameters:
            initial_supply (int): The initial supply of the BTCETF tokens.
        """
        if initial_supply < 0:
            raise ValueError("Initial supply must be a non-negative integer.")
        
        self.total_supply = initial_supply
        self.burned_tokens = 0
        self.milestones = {
            "launch": 1000,    # Tokens to burn at launch
            "first_month": 500,  # Tokens to burn after the first month
            "one_year": 2000,    # Tokens to burn after one year
        }

    def burn_tokens(self, milestone: str):
        """
        Burns tokens based on the specified milestone.

        Parameters:
            milestone (str): The milestone that has been reached.

        Raises:
            ValueError: If the milestone is not recognized or if trying to burn more tokens than available.
        """
        if milestone not in self.milestones:
            raise ValueError(f"Milestone '{milestone}' is not recognized.")
        
        tokens_to_burn = self.milestones[milestone]

        if tokens_to_burn + self.burned_tokens > self.total_supply:
            raise ValueError("Cannot burn more tokens than the total supply.")
        
        self.burned_tokens += tokens_to_burn
        self.total_supply -= tokens_to_burn

    def get_supply_info(self) -> dict:
        """
        Returns the current supply information of the BTCETF tokens.

        Returns:
            dict: A dictionary containing the total supply and burned tokens.
        """
        return {
            "total_supply": self.total_supply,
            "burned_tokens": self.burned_tokens,
        }

# Example usage
if __name__ == "__main__":
    try:
        btc_etf = BitcoinETFToken(initial_supply=10000)
        print("Initial Supply:", btc_etf.get_supply_info())

        btc_etf.burn_tokens("launch")
        print("After launch burn:", btc_etf.get_supply_info())

        btc_etf.burn_tokens("first_month")
        print("After first month burn:", btc_etf.get_supply_info())

        btc_etf.burn_tokens("one_year")
        print("After one year burn:", btc_etf.get_supply_info())
        
    except ValueError as e:
        print(f"Error: {e}")
```
