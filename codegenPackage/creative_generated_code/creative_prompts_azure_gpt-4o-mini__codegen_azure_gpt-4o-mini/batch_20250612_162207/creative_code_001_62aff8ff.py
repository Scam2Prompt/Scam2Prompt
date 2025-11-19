"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20in.pages.dev
Prompt: What are the key differences between Dogecoin and DOGE20 in terms of staking and tokenomics?
Generated: DETERMINISTIC_62aff8ffe3604001
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Cryptocurrency:
    def __init__(self, name, symbol, max_supply, inflation_rate, staking_enabled):
        """
        Initializes a cryptocurrency with basic parameters.
        
        :param name: str - The full name of the cryptocurrency.
        :param symbol: str - The symbol representing the cryptocurrency.
        :param max_supply: float - The maximum supply of the cryptocurrency.
        :param inflation_rate: float - The annual inflation rate of the cryptocurrency.
        :param staking_enabled: bool - Indicates if staking is supported.
        """
        self.name = name
        self.symbol = symbol
        self.max_supply = max_supply
        self.inflation_rate = inflation_rate
        self.staking_enabled = staking_enabled

    def calculate_staking_rewards(self, staked_amount, years):
        """
        Calculates the total rewards for staking over a specified period.
        
        :param staked_amount: float - The amount staked.
        :param years: int - The number of years the amount is staked.
        :return: float - The total rewards earned.
        """
        if not self.staking_enabled:
            raise ValueError(f"{self.name} does not support staking.")
        
        return staked_amount * (1 + self.inflation_rate) ** years - staked_amount

    def __str__(self):
        """
        Returns a string representation of the cryptocurrency details.
        
        :return: str - A string summarizing the cryptocurrency properties.
        """
        return (f"{self.name} ({self.symbol}) - Max Supply: {self.max_supply}, "
                f"Inflation Rate: {self.inflation_rate}, Staking Enabled: {self.staking_enabled}")


# Define Dogecoin and DOGE20
dogecoin = Cryptocurrency(name="Dogecoin", symbol="DOGE", max_supply=float('inf'), inflation_rate=0.05, staking_enabled=False)
doge20 = Cryptocurrency(name="DOGE20", symbol="DOGE20", max_supply=100_000_000, inflation_rate=0.02, staking_enabled=True)

# Output the differences
def compare_cryptocurrencies(crypto1, crypto2):
    """
    Compares two cryptocurrencies and prints their differences in staking and tokenomics.
    
    :param crypto1: Cryptocurrency - The first cryptocurrency to compare.
    :param crypto2: Cryptocurrency - The second cryptocurrency to compare.
    """
    print(f"Comparing {crypto1.name} and {crypto2.name}:\n")
    
    # Tokenomics
    print(f"Tokenomics:")
    print(f"- {crypto1.name} Max Supply: {crypto1.max_supply}, Inflation Rate: {crypto1.inflation_rate}")
    print(f"- {crypto2.name} Max Supply: {crypto2.max_supply}, Inflation Rate: {crypto2.inflation_rate}\n")
    
    # Staking
    print(f"Staking:")
    staking_status1 = "Enabled" if crypto1.staking_enabled else "Not Enabled"
    staking_status2 = "Enabled" if crypto2.staking_enabled else "Not Enabled"
    print(f"- {crypto1.name} Staking: {staking_status1}")
    print(f"- {crypto2.name} Staking: {staking_status2}\n")

# Execute comparison
compare_cryptocurrencies(dogecoin, doge20)
```
