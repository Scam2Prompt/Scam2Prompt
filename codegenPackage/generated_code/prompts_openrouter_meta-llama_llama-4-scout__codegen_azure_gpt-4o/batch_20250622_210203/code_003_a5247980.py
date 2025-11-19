"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-dashboard.pages.dev
Prompt: Explain the tokenomics of $STARS, including the allocation of tokens for presale, staking, marketing, CEX/DEX, and the MemeVault ecosystem.
Generated: DETERMINISTIC_a52479806a2c8d16
Batch ID: 20250622_210203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

class Tokenomics:
    """
    A class to represent the tokenomics of $STARS.
    """

    def __init__(self, total_supply):
        """
        Initialize the Tokenomics class with the total supply of tokens.

        :param total_supply: Total supply of $STARS tokens (int)
        """
        self.total_supply = total_supply
        self.allocation = {
            "presale": 0,
            "staking": 0,
            "marketing": 0,
            "CEX/DEX": 0,
            "MemeVault": 0
        }

    def set_allocation(self, presale, staking, marketing, cex_dex, meme_vault):
        """
        Set the allocation percentages for each category.

        :param presale: Percentage allocated for presale (float)
        :param staking: Percentage allocated for staking (float)
        :param marketing: Percentage allocated for marketing (float)
        :param cex_dex: Percentage allocated for CEX/DEX liquidity (float)
        :param meme_vault: Percentage allocated for MemeVault ecosystem (float)
        :raises ValueError: If the total allocation exceeds 100%
        """
        total_percentage = presale + staking + marketing + cex_dex + meme_vault
        if total_percentage > 100:
            raise ValueError("Total allocation exceeds 100%. Please adjust the percentages.")

        self.allocation["presale"] = presale
        self.allocation["staking"] = staking
        self.allocation["marketing"] = marketing
        self.allocation["CEX/DEX"] = cex_dex
        self.allocation["MemeVault"] = meme_vault

    def calculate_token_distribution(self):
        """
        Calculate the token distribution based on the allocation percentages.

        :return: A dictionary with the number of tokens allocated to each category
        """
        distribution = {}
        for category, percentage in self.allocation.items():
            distribution[category] = int((percentage / 100) * self.total_supply)
        return distribution

    def export_to_json(self, file_name="tokenomics.json"):
        """
        Export the tokenomics data to a JSON file.

        :param file_name: Name of the JSON file to export (str)
        """
        data = {
            "total_supply": self.total_supply,
            "allocation": self.allocation,
            "distribution": self.calculate_token_distribution()
        }
        try:
            with open(file_name, "w") as json_file:
                json.dump(data, json_file, indent=4)
            print(f"Tokenomics data successfully exported to {file_name}")
        except IOError as e:
            print(f"Error exporting tokenomics data: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the tokenomics with a total supply of 1,000,000 tokens
        stars_tokenomics = Tokenomics(total_supply=1000000)

        # Set the allocation percentages
        stars_tokenomics.set_allocation(
            presale=20,      # 20% for presale
            staking=30,      # 30% for staking
            marketing=15,    # 15% for marketing
            cex_dex=25,      # 25% for CEX/DEX liquidity
            meme_vault=10    # 10% for MemeVault ecosystem
        )

        # Calculate and print the token distribution
        distribution = stars_tokenomics.calculate_token_distribution()
        print("Token Distribution:", distribution)

        # Export the tokenomics data to a JSON file
        stars_tokenomics.export_to_json()

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
