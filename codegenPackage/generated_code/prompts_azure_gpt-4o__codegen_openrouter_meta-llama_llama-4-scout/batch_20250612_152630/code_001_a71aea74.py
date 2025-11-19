"""
Generated Code Metadata:
========================
Original URL: https://catgirlwhitelist.pages.dev
Prompt: Generate code to calculate and display the drop rates for Catgirl NFT rarities (COMMON, RARE, EPIC, LEGENDARY, PAW-SOME) based on the percentages provided on the website.
Generated: DETERMINISTIC_a71aea74973af02a
Batch ID: 20250612_152630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# catgirl_nft_drop_rates.py

from enum import Enum
from typing import Dict

class Rarity(Enum):
    """Enum for Catgirl NFT rarities"""
    COMMON = "COMMON"
    RARE = "RARE"
    EPIC = "EPIC"
    LEGENDARY = "LEGENDARY"
    PAW_SOME = "PAW-SOME"

class CatgirlNFTDropRates:
    """Class to calculate and display Catgirl NFT drop rates"""

    def __init__(self, drop_rates: Dict[Rarity, float]):
        """
        Initialize the CatgirlNFTDropRates class

        Args:
        drop_rates (Dict[Rarity, float]): A dictionary of drop rates for each rarity
        """
        self.drop_rates = drop_rates

    def calculate_drop_rates(self) -> None:
        """
        Calculate and display the drop rates for each rarity
        """
        total_percentage = sum(self.drop_rates.values())
        if abs(total_percentage - 100) > 1e-6:
            raise ValueError("Drop rates do not add up to 100%")

        print("Catgirl NFT Drop Rates:")
        for rarity, percentage in self.drop_rates.items():
            print(f"{rarity.value}: {percentage:.2f}%")

    def validate_drop_rates(self) -> None:
        """
        Validate the drop rates to ensure they are within valid ranges
        """
        for rarity, percentage in self.drop_rates.items():
            if percentage < 0 or percentage > 100:
                raise ValueError(f"Invalid drop rate for {rarity.value}: {percentage}%")

def main() -> None:
    # Define the drop rates for each rarity (example percentages)
    drop_rates = {
        Rarity.COMMON: 70.0,
        Rarity.RARE: 20.0,
        Rarity.EPIC: 5.0,
        Rarity.LEGENDARY: 3.0,
        Rarity.PAW_SOME: 2.0
    }

    try:
        catgirl_nft_drop_rates = CatgirlNFTDropRates(drop_rates)
        catgirl_nft_drop_rates.validate_drop_rates()
        catgirl_nft_drop_rates.calculate_drop_rates()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
