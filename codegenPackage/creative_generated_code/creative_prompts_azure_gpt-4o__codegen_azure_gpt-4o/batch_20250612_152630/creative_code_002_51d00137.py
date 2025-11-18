"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://catgirlwhitelist.pages.dev
Prompt: Create a function in Python that simulates the purchase of Catgirl NFTs using $NYA and adjusts the drop rates slightly, as described in the "Rates slightly increased when buying with $NYA" feature.
Generated: DETERMINISTIC_51d00137ae1e7008
Batch ID: 20250612_152630
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class NFTMarketplace:
    """
    A class to simulate the purchase of Catgirl NFTs using $NYA or standard currency.
    """

    def __init__(self):
        # Base drop rates for Catgirl NFTs.
        # These represent the likelihood (out of 100) of receiving each rarity tier.
        self.base_drop_rates = {
            "Common": 70,   # 70% chance
            "Rare": 20,     # 20% chance
            "Epic": 8,      # 8% chance
            "Legendary": 2  # 2% chance
        }
        
        # Adjustment factor to slightly increase drop rates when using $NYA
        self.nya_bonus_factor = 1.1  # 10% boost to drop rates

    def adjust_drop_rates_for_nya(self):
        """
        Adjusts drop rates slightly when $NYA is used for purchase.
        Ensures total probability does not exceed 100.
        """
        adjusted_rates = {}
        total = 0

        # Increase rates using the bonus factor
        for rarity, rate in self.base_drop_rates.items():
            adjusted_rate = rate * self.nya_bonus_factor
            adjusted_rates[rarity] = adjusted_rate
            total += adjusted_rate

        # Normalize rates to ensure they sum to 100
        normalization_factor = 100 / total
        for rarity in adjusted_rates:
            adjusted_rates[rarity] = round(adjusted_rates[rarity] * normalization_factor)

        return adjusted_rates

    def simulate_purchase(self, use_nya=False):
        """
        Simulates the purchase of a Catgirl NFT.
        :param use_nya: bool - Whether the purchase is made using $NYA.
        :return: str - The rarity of the Catgirl NFT received.
        """
        # Get the appropriate drop rates (adjusted or base)
        drop_rates = self.adjust_drop_rates_for_nya() if use_nya else self.base_drop_rates
        
        # Create a weighted list based on drop rates
        weighted_pool = []
        for rarity, rate in drop_rates.items():
            weighted_pool.extend([rarity] * rate)
        
        # Randomly select an NFT rarity from the weighted pool
        selected_rarity = random.choice(weighted_pool)
        return selected_rarity


# Example usage:
if __name__ == "__main__":
    # Instantiate the marketplace
    marketplace = NFTMarketplace()

    # Simulate a purchase using $NYA
    print("Purchasing with $NYA...")
    nft_rarity_nya = marketplace.simulate_purchase(use_nya=True)
    print(f"Received NFT Rarity: {nft_rarity_nya}")

    # Simulate a purchase without $NYA (standard purchase)
    print("\nPurchasing without $NYA...")
    nft_rarity_standard = marketplace.simulate_purchase(use_nya=False)
    print(f"Received NFT Rarity: {nft_rarity_standard}")
```
