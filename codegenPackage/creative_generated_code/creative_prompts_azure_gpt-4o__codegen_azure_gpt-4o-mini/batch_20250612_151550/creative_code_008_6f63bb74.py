"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: Write a program to calculate the rarity score of HV-MTL NFTs based on their traits and evolution stage.
Generated: DETERMINISTIC_6f63bb747678ce65
Batch ID: 20250612_151550
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
    A class to represent a HV-MTL NFT.

    Attributes:
        traits (dict): A dictionary containing trait names and their associated rarity scores.
        evolution_stage (int): An integer representing the evolution stage of the NFT (1-5).
    """

    def __init__(self, traits, evolution_stage):
        """
        Initializes the NFT with traits and evolution stage.

        Parameters:
            traits (dict): A dictionary of traits and their rarity scores.
            evolution_stage (int): The evolution stage of the NFT (1-5).

        Raises:
            ValueError: If the evolution stage is not between 1 and 5.
        """
        if not (1 <= evolution_stage <= 5):
            raise ValueError("Evolution stage must be between 1 and 5.")

        self.traits = traits
        self.evolution_stage = evolution_stage

    def calculate_rarity_score(self):
        """
        Calculates the rarity score based on traits and evolution stage.

        Returns:
            float: The computed rarity score of the NFT.
        """
        base_score = sum(self.traits.values())
        evolution_multiplier = 1 + (self.evolution_stage - 1) * 0.1
        rarity_score = base_score * evolution_multiplier
        return rarity_score


def main():
    """
    Main function to create an NFT instance and calculate its rarity score.
    """
    try:
        # Sample traits with their respective rarity scores
        traits = {
            'Background': 10,
            'Body': 20,
            'Clothing': 15,
            'Accessory': 25,
        }

        # Example evolution stage (between 1 and 5)
        evolution_stage = 3

        # Create an instance of NFT
        nft = NFT(traits, evolution_stage)

        # Calculate and display the rarity score
        rarity_score = nft.calculate_rarity_score()
        print(f"The rarity score of the NFT is: {rarity_score:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
