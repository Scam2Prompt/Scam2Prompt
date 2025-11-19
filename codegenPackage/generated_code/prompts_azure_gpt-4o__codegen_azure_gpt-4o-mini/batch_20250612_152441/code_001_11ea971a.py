"""
Generated Code Metadata:
========================
Original URL: https://presales-monprotocolapp.pages.dev
Prompt: Generate code to calculate the ETH price per lot for MON tokens based on the presale tiers (e.g., common, rare, epic, legendary).
Generated: DETERMINISTIC_11ea971a578d143e
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PresaleTier:
    """Class to represent a presale tier for MON tokens."""
    
    def __init__(self, name: str, eth_price_per_lot: float, lot_size: int):
        """
        Initialize a presale tier.

        :param name: The name of the presale tier (e.g., common, rare, epic, legendary).
        :param eth_price_per_lot: The price in ETH for one lot of this tier.
        :param lot_size: The number of tokens in one lot.
        """
        self.name = name
        self.eth_price_per_lot = eth_price_per_lot
        self.lot_size = lot_size

    def calculate_price_per_token(self) -> float:
        """
        Calculate the price per token based on the ETH price per lot and lot size.

        :return: The price per token in ETH.
        """
        if self.lot_size <= 0:
            raise ValueError("Lot size must be greater than zero.")
        return self.eth_price_per_lot / self.lot_size


class Presale:
    """Class to manage the presale of MON tokens."""
    
    def __init__(self):
        """Initialize the presale with predefined tiers."""
        self.tiers = {
            "common": PresaleTier("common", 0.1, 100),
            "rare": PresaleTier("rare", 0.2, 50),
            "epic": PresaleTier("epic", 0.5, 20),
            "legendary": PresaleTier("legendary", 1.0, 10),
        }

    def get_price_per_token(self, tier_name: str) -> float:
        """
        Get the price per token for a given presale tier.

        :param tier_name: The name of the presale tier.
        :return: The price per token in ETH.
        :raises ValueError: If the tier name is not valid.
        """
        if tier_name not in self.tiers:
            raise ValueError(f"Invalid tier name: {tier_name}. Valid options are: {list(self.tiers.keys())}.")
        
        return self.tiers[tier_name].calculate_price_per_token()


def main():
    """Main function to demonstrate the presale price calculation."""
    presale = Presale()
    
    # Example usage
    try:
        tier_name = "epic"
        price_per_token = presale.get_price_per_token(tier_name)
        print(f"The price per token for the '{tier_name}' tier is: {price_per_token} ETH")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
