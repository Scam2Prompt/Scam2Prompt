"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft.vip-tokyo.jp
Prompt: Write code to create a fixed-price NFT sales platform with item limits and additional item fees, as outlined in the VIP Management pricing plans.
Generated: DETERMINISTIC_03d087da6cbc9f41
Batch ID: 20250612_151457
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
NFT Sales Platform - Fixed Price Sales
This script implements a fixed-price NFT sales platform with item limits and 
additional item fees as outlined in VIP Management pricing plans.

Key Features:
- Fixed price for NFTs
- Different item limits based on VIP tiers
- Additional item fees for exceeding limits
- Error handling for invalid input and tier restrictions

Author: Professional Developer
Date: YYYY-MM-DD
"""

import sys

class NFTSalesPlatform:
    def __init__(self):
        # Define the VIP management pricing plans
        self.vip_tiers = {
            "Standard": {"price_per_item": 50, "item_limit": 10, "extra_item_fee": 10},
            "Premium": {"price_per_item": 45, "item_limit": 20, "extra_item_fee": 8},
            "VIP": {"price_per_item": 40, "item_limit": 50, "extra_item_fee": 5},
        }

    def calculate_price(self, tier, items):
        """
        Calculate total price for the given tier and number of items.

        Args:
            tier (str): VIP tier ('Standard', 'Premium', or 'VIP').
            items (int): Number of items to purchase.

        Returns:
            float: Total price for the items.
        Raises:
            ValueError: If tier is invalid or items are not positive integers.
        """
        if tier not in self.vip_tiers:
            raise ValueError("Invalid tier. Valid options are 'Standard', 'Premium', 'VIP'.")
        if items <= 0:
            raise ValueError("Number of items must be a positive integer.")

        tier_info = self.vip_tiers[tier]
        base_price = items * tier_info["price_per_item"]

        # Calculate additional fees if item limit is exceeded
        if items > tier_info["item_limit"]:
            extra_items = items - tier_info["item_limit"]
            extra_fee = extra_items * tier_info["extra_item_fee"]
        else:
            extra_fee = 0

        total_price = base_price + extra_fee
        return total_price

    def display_pricing_plan(self):
        """Print available VIP pricing plans."""
        print("VIP Management Pricing Plans:")
        for tier, info in self.vip_tiers.items():
            print(f"{tier}:")
            print(f"  Price per item: ${info['price_per_item']}")
            print(f"  Item limit: {info['item_limit']} items")
            print(f"  Extra fee per item (above limit): ${info['extra_item_fee']}")
        print()

def main():
    platform = NFTSalesPlatform()
    platform.display_pricing_plan()

    try:
        # Gather user input
        tier = input("Enter VIP tier (Standard, Premium, VIP): ").strip()
        items = int(input("Enter number of items to purchase: ").strip())

        # Calculate and display the price
        total_price = platform.calculate_price(tier, items)
        print(f"\nTotal price for {items} items under '{tier}' tier: ${total_price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
