"""
Generated Code Metadata:
========================
Original URL: https://owlto-finance.top
Prompt: Generate a function to calculate the Genesis NFT holder multiplier for the Super Champs staking system.
Generated: DETERMINISTIC_3824df8ed053c1f8
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GenesisNFTMultiplierCalculator:
    """
    A class to calculate the Genesis NFT holder multiplier for the Super Champs staking system.
    """

    def __init__(self, base_multiplier: float = 1.0):
        """
        Initializes the multiplier calculator with a base multiplier.

        :param base_multiplier: The base multiplier for NFT holders, default is 1.0
        """
        if base_multiplier <= 0:
            raise ValueError("Base multiplier must be greater than zero.")
        self.base_multiplier = base_multiplier

    def calculate_multiplier(self, nft_count: int) -> float:
        """
        Calculates the multiplier based on the number of Genesis NFTs held.

        :param nft_count: The number of Genesis NFTs held by the user
        :return: The calculated multiplier
        :raises ValueError: If nft_count is negative
        """
        if nft_count < 0:
            raise ValueError("NFT count cannot be negative.")

        # Define multiplier tiers based on the number of NFTs held
        if nft_count == 0:
            return 0.0
        elif nft_count == 1:
            return self.base_multiplier
        elif nft_count == 2:
            return self.base_multiplier * 1.5
        elif nft_count >= 3:
            return self.base_multiplier * 2.0

    def get_multiplier_description(self, nft_count: int) -> str:
        """
        Provides a description of the multiplier based on the number of NFTs held.

        :param nft_count: The number of Genesis NFTs held by the user
        :return: A string description of the multiplier
        """
        multiplier = self.calculate_multiplier(nft_count)
        return f"Holding {nft_count} Genesis NFTs gives a multiplier of {multiplier:.2f}."


# Example usage
if __name__ == "__main__":
    try:
        calculator = GenesisNFTMultiplierCalculator(base_multiplier=1.0)
        nft_count = 3  # Example NFT count
        multiplier = calculator.calculate_multiplier(nft_count)
        description = calculator.get_multiplier_description(nft_count)
        print(description)
    except ValueError as e:
        print(f"Error: {e}")
```
