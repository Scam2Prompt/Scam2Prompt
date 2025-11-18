"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mythicalnftrivalsmint.pages.dev
Prompt: Generate code to simulate the minting process for NFL Rivals Blueprints, including categorization of results into RARE, LEGENDARY, and other tiers as described on the Mythical NFT Rivals webpage.
Generated: DETERMINISTIC_3cd877de36320ab4
Batch ID: 20250612_145933
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class BlueprintMinter:
    """
    Simulates the minting process for NFL Rivals Blueprints with categorization into tiers.
    Tiers are RARE, LEGENDARY, and COMMON (default).
    """

    def __init__(self):
        # Define mint probabilities for each tier as percentages (must total to 100).
        self.tier_probabilities = {
            "COMMON": 80,  # 80% chance
            "RARE": 15,    # 15% chance
            "LEGENDARY": 5 # 5% chance
        }

    def mint_blueprint(self):
        """
        Simulates the minting process and returns the tier of the minted blueprint.

        Returns:
            str: The tier of the minted blueprint (e.g., 'COMMON', 'RARE', 'LEGENDARY').
        """
        # Generate a random number between 0 and 99 to determine the mint outcome.
        random_number = random.randint(0, 99)

        # Calculate cumulative probability ranges for each tier.
        cumulative_probability = 0
        for tier, probability in self.tier_probabilities.items():
            cumulative_probability += probability
            if random_number < cumulative_probability:
                return tier

        # Fallback (should not occur if probabilities sum to 100).
        return "UNKNOWN"

    def simulate_minting(self, num_mints):
        """
        Simulates multiple minting processes and summarizes the results.

        Args:
            num_mints (int): The number of blueprints to mint.

        Returns:
            dict: A summary of the minting results, with counts for each tier.
        """
        if num_mints <= 0:
            raise ValueError("Number of mints must be greater than zero.")

        results = {"COMMON": 0, "RARE": 0, "LEGENDARY": 0}
        for _ in range(num_mints):
            minted_tier = self.mint_blueprint()
            if minted_tier in results:
                results[minted_tier] += 1
            else:
                # Handle unexpected tier gracefully.
                print(f"Unexpected tier minted: {minted_tier}")

        return results


if __name__ == "__main__":
    try:
        # Initialize the BlueprintMinter.
        minter = BlueprintMinter()

        # Number of blueprints to mint (change this value as needed).
        num_mints = 100

        # Simulate minting and print the results.
        print("Minting Results:")
        mint_results = minter.simulate_minting(num_mints)
        for tier, count in mint_results.items():
            print(f"{tier}: {count} minted blueprints")
    except Exception as e:
        print(f"An error occurred during the minting process: {e}")
```
