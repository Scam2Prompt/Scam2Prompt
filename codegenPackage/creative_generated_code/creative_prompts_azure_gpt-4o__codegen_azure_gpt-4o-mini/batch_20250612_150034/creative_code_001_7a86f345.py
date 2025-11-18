"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dymwizard.top
Prompt: Generate code to calculate the Genesis NFT holder multiplier based on the staking details provided on the Super Champs HQ platform.
Generated: DETERMINISTIC_7a86f3457c98a6f3
Batch ID: 20250612_150034
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
    A class to calculate the Genesis NFT holder multiplier based on staking details.
    """

    def __init__(self, base_multiplier: float, staking_details: dict):
        """
        Initializes the calculator with a base multiplier and staking details.

        :param base_multiplier: The base multiplier for Genesis NFT holders.
        :param staking_details: A dictionary containing staking information.
        """
        self.base_multiplier = base_multiplier
        self.staking_details = staking_details

    def validate_staking_details(self):
        """
        Validates the staking details to ensure they are in the correct format.

        :raises ValueError: If the staking details are invalid.
        """
        if not isinstance(self.staking_details, dict):
            raise ValueError("Staking details must be a dictionary.")

        required_keys = ['nft_count', 'staking_duration', 'bonus_multiplier']
        for key in required_keys:
            if key not in self.staking_details:
                raise ValueError(f"Missing required key: {key}")

        if not isinstance(self.staking_details['nft_count'], int) or self.staking_details['nft_count'] < 0:
            raise ValueError("NFT count must be a non-negative integer.")

        if not isinstance(self.staking_details['staking_duration'], int) or self.staking_details['staking_duration'] < 0:
            raise ValueError("Staking duration must be a non-negative integer.")

        if not isinstance(self.staking_details['bonus_multiplier'], float) or self.staking_details['bonus_multiplier'] < 0:
            raise ValueError("Bonus multiplier must be a non-negative float.")

    def calculate_multiplier(self) -> float:
        """
        Calculates the total multiplier based on the staking details.

        :return: The calculated multiplier.
        """
        self.validate_staking_details()

        nft_count = self.staking_details['nft_count']
        staking_duration = self.staking_details['staking_duration']
        bonus_multiplier = self.staking_details['bonus_multiplier']

        # Calculate the multiplier based on the number of NFTs and duration
        multiplier = self.base_multiplier + (nft_count * 0.1) + (staking_duration * 0.05) + bonus_multiplier

        # Ensure the multiplier does not fall below zero
        return max(multiplier, 0)

if __name__ == "__main__":
    # Example usage of the GenesisNFTMultiplierCalculator class
    try:
        base_multiplier = 1.0  # Base multiplier
        staking_info = {
            'nft_count': 5,             # Number of NFTs held
            'staking_duration': 30,      # Duration in days
            'bonus_multiplier': 0.5      # Additional bonus multiplier
        }
        
        # Initialize the calculator
        calculator = GenesisNFTMultiplierCalculator(base_multiplier, staking_info)

        # Calculate and print the multiplier
        total_multiplier = calculator.calculate_multiplier()
        print(f"Total Genesis NFT Holder Multiplier: {total_multiplier:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
