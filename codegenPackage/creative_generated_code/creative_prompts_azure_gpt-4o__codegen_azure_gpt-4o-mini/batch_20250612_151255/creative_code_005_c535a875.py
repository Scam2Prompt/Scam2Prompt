"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-beef-meme.pages.dev
Prompt: Create a Python script to calculate the percentage of BEEF Coin distribution across DEX liquidity pools, CEX liquidity pools, and airdrops based on the tokenomics provided.
Generated: DETERMINISTIC_c535a875e98b0978
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tokenomics:
    """
    Class to represent the tokenomics of BEEF Coin.
    It calculates the percentage distribution across DEX, CEX, and airdrops.
    """

    def __init__(self, total_supply: float, dex_supply: float, cex_supply: float, airdrop_supply: float):
        """
        Initialize the Tokenomics class with total supply and various distributions.

        :param total_supply: Total supply of BEEF Coin.
        :param dex_supply: Supply allocated to DEX liquidity pools.
        :param cex_supply: Supply allocated to CEX liquidity pools.
        :param airdrop_supply: Supply allocated for airdrops.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if any(supply < 0 for supply in [dex_supply, cex_supply, airdrop_supply]):
            raise ValueError("Supplies must not be negative.")

        self.total_supply = total_supply
        self.dex_supply = dex_supply
        self.cex_supply = cex_supply
        self.airdrop_supply = airdrop_supply

    def calculate_distribution_percentage(self) -> dict:
        """
        Calculate the distribution percentages for DEX, CEX, and airdrops.

        :return: A dictionary with distribution percentages.
        """
        distribution = {
            'DEX': (self.dex_supply / self.total_supply) * 100,
            'CEX': (self.cex_supply / self.total_supply) * 100,
            'Airdrops': (self.airdrop_supply / self.total_supply) * 100
        }
        return distribution

    def display_distribution(self):
        """
        Display the distribution percentages in a formatted manner.
        """
        try:
            distribution = self.calculate_distribution_percentage()
            print("BEEF Coin Distribution:")
            for category, percentage in distribution.items():
                print(f"{category}: {percentage:.2f}%")
        except Exception as e:
            print(f"Error calculating distribution: {e}")


if __name__ == "__main__":
    try:
        # Example tokenomics data
        total_supply = 1000000.0  # Total supply of BEEF Coin
        dex_supply = 450000.0      # DEX liquidity pool allocation
        cex_supply = 300000.0      # CEX liquidity pool allocation
        airdrop_supply = 250000.0  # Airdrop allocation

        # Create a Tokenomics instance
        tokenomics = Tokenomics(total_supply, dex_supply, cex_supply, airdrop_supply)

        # Display the distribution percentages
        tokenomics.display_distribution()
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
