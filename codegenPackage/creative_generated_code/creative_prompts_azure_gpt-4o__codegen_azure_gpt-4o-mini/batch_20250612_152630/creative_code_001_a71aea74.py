"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://catgirlwhitelist.pages.dev
Prompt: Generate code to calculate and display the drop rates for Catgirl NFT rarities (COMMON, RARE, EPIC, LEGENDARY, PAW-SOME) based on the percentages provided on the website.
Generated: DETERMINISTIC_a71aea74973af02a
Batch ID: 20250612_152630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CatgirlNFT:
    """A class to represent Catgirl NFTs and calculate drop rates based on rarity."""

    # Rarity types and their corresponding drop rates in percentages
    RARITIES = {
        "COMMON": 70,
        "RARE": 20,
        "EPIC": 7,
        "LEGENDARY": 2,
        "PAW-SOME": 1,
    }

    def __init__(self):
        """Initialize the CatgirlNFT with default rarity percentages."""
        self.drop_rates = self.calculate_drop_rates()

    def calculate_drop_rates(self):
        """Calculate and normalize the drop rates for better representation."""
        total = sum(self.RARITIES.values())
        if total <= 0:
            raise ValueError("Total drop rates must be greater than zero.")

        # Normalize the drop rates to ensure they sum up to 100%
        normalized_rates = {rarity: (rate / total) * 100 for rarity, rate in self.RARITIES.items()}
        return normalized_rates

    def display_drop_rates(self):
        """Display the drop rates for each rarity."""
        print("Catgirl NFT Drop Rates:")
        for rarity, rate in self.drop_rates.items():
            print(f"{rarity}: {rate:.2f}%")

def main():
    """Main function to execute the drop rate calculation and display."""
    try:
        catgirl_nft = CatgirlNFT()
        catgirl_nft.display_drop_rates()
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
