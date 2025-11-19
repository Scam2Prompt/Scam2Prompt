"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellyjelly.web.app
Prompt: Generate a function that calculates the rarity of a Jelly NFT based on the criteria outlined on the Jelly site.
Generated: DETERMINISTIC_465eaca3d47842f8
Batch ID: 20250612_162521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class JellyNFT:
    def __init__(self, traits: dict):
        """
        Initializes a JellyNFT instance with specified traits.

        :param traits: A dictionary where keys are trait types and values are trait values.
        """
        self.traits = traits

    def calculate_rarity(self, trait_database: dict) -> float:
        """
        Calculates the rarity score of the Jelly NFT based on its traits.

        :param trait_database: A dictionary containing the total count of each trait type in the collection.
        :return: A float representing the rarity score of the NFT.
        """
        if not isinstance(trait_database, dict):
            raise ValueError("trait_database must be a dictionary.")

        rarity_score = 1.0  # Initial score, will be multiplied by trait rarities

        for trait_type, trait_value in self.traits.items():
            # Check if the trait type exists in the database
            if trait_type not in trait_database:
                raise KeyError(f"Trait type '{trait_type}' not found in the trait database.")

            # Get the total count for the specific trait
            total_count = trait_database[trait_type].get(trait_value, 0)

            if total_count <= 0:
                raise ValueError(f"Trait value '{trait_value}' under trait type '{trait_type}' has a count of 0.")

            # Update rarity score using the formula: score *= (total traits) / (count of this trait)
            rarity_score *= (sum(trait_database[trait_type].values()) / total_count)

        return rarity_score


# Example usage:
if __name__ == "__main__":
    # Define a trait database with counts of traits
    trait_database = {
        "Color": {"Red": 10, "Blue": 5, "Green": 2},
        "Shape": {"Round": 8, "Square": 3},
    }

    # Create a Jelly NFT with specific traits
    jelly_nft = JellyNFT(traits={"Color": "Red", "Shape": "Round"})
    
    try:
        # Calculate the rarity of the NFT
        rarity = jelly_nft.calculate_rarity(trait_database)
        print(f"The rarity score of the Jelly NFT is: {rarity:.2f}")
    except (ValueError, KeyError) as e:
        print(f"Error calculating rarity: {e}")
```
