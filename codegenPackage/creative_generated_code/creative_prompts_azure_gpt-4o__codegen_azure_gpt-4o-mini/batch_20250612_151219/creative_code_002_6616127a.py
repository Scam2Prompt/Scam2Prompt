"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micropets-migration.pages.dev
Prompt: Create a function to calculate the probability distribution for minting MicroPets NFTs based on their rarity and opening chances. Include the ability to visualize the results in a chart.
Generated: DETERMINISTIC_6616127a94e0de7a
Batch ID: 20250612_151219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class MicroPetsNFT:
    """
    Class to represent a MicroPet NFT and its minting probabilities.
    """
    def __init__(self, rarity, chance):
        """
        Initialize the MicroPet NFT with rarity and opening chance.
        
        :param rarity: Rarity level of the NFT (string)
        :param chance: Opening chance of the NFT (float, should be between 0 and 1)
        """
        self.rarity = rarity
        self.chance = chance

def calculate_probability_distribution(nfts):
    """
    Calculate the probability distribution of minting MicroPet NFTs.

    :param nfts: List of MicroPetsNFT instances
    :return: Dictionary with rarity as keys and their corresponding probabilities
    """
    total_chances = sum(nft.chance for nft in nfts)
    
    if total_chances == 0:
        raise ValueError("Total chances must be greater than zero to calculate probabilities.")
    
    probabilities = {}
    for nft in nfts:
        probabilities[nft.rarity] = nft.chance / total_chances
    
    return probabilities

def visualize_probabilities(probabilities):
    """
    Visualize the probability distribution using a bar chart.
    
    :param probabilities: Dictionary with rarity as keys and their corresponding probabilities
    """
    try:
        rarities = list(probabilities.keys())
        probs = list(probabilities.values())
        
        plt.bar(rarities, probs, color='skyblue')
        plt.xlabel('Rarity')
        plt.ylabel('Probability')
        plt.title('Probability Distribution of Minting MicroPets NFTs')
        plt.xticks(rotation=45)
        plt.ylim(0, max(probs) + 0.1)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error while visualizing probabilities: {e}")

# Example usage
if __name__ == "__main__":
    # Define some MicroPet NFTs with their rarities and chances
    nfts = [
        MicroPetsNFT("Common", 0.5),
        MicroPetsNFT("Rare", 0.3),
        MicroPetsNFT("Epic", 0.15),
        MicroPetsNFT("Legendary", 0.05)
    ]
    
    try:
        # Calculate the probability distribution
        probabilities = calculate_probability_distribution(nfts)
        print("Calculated probabilities:", probabilities)

        # Visualize the probability distribution
        visualize_probabilities(probabilities)
    except Exception as error:
        print(f"An error occurred: {error}")
```
