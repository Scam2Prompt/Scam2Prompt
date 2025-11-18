"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xcad-staked.pages.dev
Prompt: Write a program to simulate the opening of NFT Moment packs from XCAD Network and calculate the probability of obtaining rare collectibles.
Generated: DETERMINISTIC_c423f52f6a61710b
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from collections import Counter

# Constants representing the probabilities of obtaining different rarity levels
RARITY_PROBABILITIES = {
    "common": 0.5,
    "uncommon": 0.3,
    "rare": 0.15,
    "legendary": 0.05
}

# A class to represent a single NFT moment
class NFTMoment:
    def __init__(self, rarity):
        self.rarity = rarity
    
    def __repr__(self):
        return f"NFTMoment(rarity='{self.rarity}')"

# Function to simulate opening a pack of NFT moments
def open_nft_pack(num_moments=5):
    """Simulates opening a pack containing a specified number of NFT moments.

    Args:
        num_moments (int): The number of NFT moments in the pack.

    Returns:
        List[NFTMoment]: A list of NFT moments obtained from the pack.
    """
    moments = []
    for _ in range(num_moments):
        rarity = random.choices(
            population=list(RARITY_PROBABILITIES.keys()),
            weights=list(RARITY_PROBABILITIES.values()),
            k=1
        )[0]
        moments.append(NFTMoment(rarity))
    return moments

# Function to calculate the probabilities of obtaining each rarity from multiple packs
def calculate_probabilities(num_packs=1000):
    """Calculates the probabilities of obtaining each rarity level after opening multiple packs.

    Args:
        num_packs (int): The number of packs to simulate opening.
    
    Returns:
        Dict[str, float]: A dictionary with rarities as keys and their probabilities as values.
    """
    rarity_count = Counter()
    
    for _ in range(num_packs):
        moments = open_nft_pack()
        rarity_count.update(moment.rarity for moment in moments)

    total_moments = num_packs * 5  # Assuming each pack contains 5 moments
    probabilities = {rarity: count / total_moments for rarity, count in rarity_count.items()}
    return probabilities

# Main function to run the simulation
def main():
    """Main function to execute the NFT pack opening simulation and display results."""
    try:
        num_packs = int(input("Enter the number of NFT packs to simulate opening: "))
        if num_packs <= 0:
            raise ValueError("The number of packs must be a positive integer.")
        
        probabilities = calculate_probabilities(num_packs)
        
        # Display the calculated probabilities
        print("\nProbability of obtaining each rarity:")
        for rarity, probability in probabilities.items():
            print(f"{rarity.capitalize()}: {probability:.2%}")
    
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()
```
