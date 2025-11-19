"""
Generated Code Metadata:
========================
Original URL: https://bafybeif5xdzxzkk6hpdngckqqt4qfejabreu6fkzi4rwsnuk733woz2spu.ipfs.dweb.link
Prompt: Write code to calculate bonus interest shares for Silo Liquidity Providers based on their positions, referencing the Silo Rewards Proposal.
Generated: DETERMINISTIC_0c46ac29a5eff390
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SiloLiquidityProvider:
    """
    A class to represent a liquidity provider in the Silo system.
    
    Attributes:
        provider_id (str): Unique identifier for the liquidity provider.
        position (float): The amount of liquidity provided by the provider.
        total_supply (float): The total liquidity supplied by all providers.
        bonus_interest_rate (float): The rate at which bonus interest is calculated.
    """

    def __init__(self, provider_id: str, position: float, total_supply: float, bonus_interest_rate: float):
        """
        Initializes a new instance of SiloLiquidityProvider.

        Args:
            provider_id (str): Unique identifier for the liquidity provider.
            position (float): The amount of liquidity provided by the provider.
            total_supply (float): The total liquidity supplied by all providers.
            bonus_interest_rate (float): The rate at which bonus interest is calculated.
        """
        self.provider_id = provider_id
        self.position = position
        self.total_supply = total_supply
        self.bonus_interest_rate = bonus_interest_rate

    def calculate_bonus_interest(self) -> float:
        """
        Calculates the bonus interest for the liquidity provider based on their position.

        Returns:
            float: The calculated bonus interest.
        """
        if self.total_supply <= 0:
            raise ValueError("Total supply must be greater than zero to calculate bonus interest.")

        # Calculate the share of the total supply
        share_of_supply = self.position / self.total_supply
        
        # Calculate the bonus interest based on the share and the bonus interest rate
        bonus_interest = share_of_supply * self.bonus_interest_rate
        
        return bonus_interest


def main():
    """
    Main function to demonstrate the calculation of bonus interest for liquidity providers.
    """
    try:
        # Example data for liquidity providers
        providers = [
            SiloLiquidityProvider("provider_1", 1000, 10000, 0.05),
            SiloLiquidityProvider("provider_2", 2000, 10000, 0.05),
            SiloLiquidityProvider("provider_3", 3000, 10000, 0.05),
        ]

        # Calculate and display bonus interest for each provider
        for provider in providers:
            bonus_interest = provider.calculate_bonus_interest()
            print(f"Provider ID: {provider.provider_id}, Bonus Interest: {bonus_interest:.4f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
