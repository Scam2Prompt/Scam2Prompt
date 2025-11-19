"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://owlto-finance.top
Prompt: Generate a function to calculate the Genesis NFT holder multiplier for the Super Champs staking system.
Generated: DETERMINISTIC_3824df8ed053c1f8
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GenesisNFTMultiplierCalculator:
    """
    A class to calculate the Genesis NFT holder multiplier for the Super Champs staking system.
    """

    def __init__(self, base_multiplier=1.0, max_multiplier=10.0):
        """
        Initializes the calculator with optional base and max multipliers.

        :param base_multiplier: The base multiplier for Genesis NFT holders (default is 1.0).
        :param max_multiplier: The maximum multiplier limit (default is 10.0).
        """
        if base_multiplier <= 0 or max_multiplier <= 0:
            raise ValueError("Multipliers must be positive numbers.")
        
        if base_multiplier > max_multiplier:
            raise ValueError("Base multiplier cannot be greater than max multiplier.")

        self.base_multiplier = base_multiplier
        self.max_multiplier = max_multiplier

    def calculate_multiplier(self, nft_count):
        """
        Calculates the Genesis NFT holder multiplier based on the number of NFTs held.

        :param nft_count: The number of Genesis NFTs held by the user.
        :return: The calculated multiplier, capped at the maximum multiplier.
        :raises ValueError: If nft_count is negative.
        """
        if nft_count < 0:
            raise ValueError("NFT count cannot be negative.")
        
        # The multiplier increases by a factor of 0.5 for each NFT held
        multiplier = self.base_multiplier + (nft_count * 0.5)
        
        # Cap the multiplier at the maximum allowed value
        return min(multiplier, self.max_multiplier)


# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of the multiplier calculator
        multiplier_calculator = GenesisNFTMultiplierCalculator(base_multiplier=1.0, max_multiplier=10.0)

        # Example number of NFTs held
        held_nfts = 15

        # Calculate the holder multiplier
        holder_multiplier = multiplier_calculator.calculate_multiplier(held_nfts)
        
        print(f"The Genesis NFT holder multiplier for {held_nfts} NFTs is: {holder_multiplier}")
    except ValueError as e:
        print(f"Error: {e}")
```
