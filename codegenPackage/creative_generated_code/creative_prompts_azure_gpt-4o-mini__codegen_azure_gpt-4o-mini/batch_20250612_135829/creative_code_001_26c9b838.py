"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clashofdragonz-mint.com
Prompt: Write a function to calculate the rarity of a Clash of DragonZ NFT based on its attributes and family characteristics.
Generated: DETERMINISTIC_26c9b8389d65510b
Batch ID: 20250612_135829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NFT:
    """
    Class representing an NFT in Clash of DragonZ with its attributes
    and a method to calculate its rarity.
    """

    def __init__(self, attributes, family_characteristics):
        """
        Initializes the NFT with given attributes and family characteristics.

        :param attributes: dict containing the attributes of the NFT
        :param family_characteristics: dict containing the family characteristics
        """
        self.attributes = attributes
        self.family_characteristics = family_characteristics

    def calculate_rarity(self):
        """
        Calculates the rarity score of the NFT based on its attributes 
        and family characteristics.

        :return: float representing the rarity score
        :raises ValueError: if attributes or family characteristics are invalid
        """
        try:
            # Validate input data
            if not isinstance(self.attributes, dict) or not isinstance(self.family_characteristics, dict):
                raise ValueError("Attributes and family characteristics must be dictionaries.")

            # Calculate base rarity from attributes
            base_rarity = sum(self.attributes.values())
            # Calculate family rarity influence
            family_rarity = sum(self.family_characteristics.values())

            # Combine the base rarity and family rarity
            rarity_score = (base_rarity + family_rarity) / 2

            # Ensure rarity score is non-negative
            return max(rarity_score, 0)

        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"An error occurred while calculating rarity: {e}")
            return None


# Example Usage
if __name__ == "__main__":
    # Example attributes and family characteristics
    attributes = {
        'strength': 5,
        'agility': 10,
        'intelligence': 8
    }
    
    family_characteristics = {
        'fire_power': 7,
        'water_resistance': 3,
        'earth_affinity': 6
    }

    # Create an NFT instance
    nft = NFT(attributes, family_characteristics)

    # Calculate and print the rarity
    rarity = nft.calculate_rarity()
    if rarity is not None:
        print(f"The rarity score of the NFT is: {rarity:.2f}")
```
