"""
Generated Code Metadata:
========================
Original URL: https://micropets-migration.pages.dev
Prompt: Design a rarity system for an NFT collection, similar to MicroPets, with 8 unique items ranging from Common to Mythic, and provide a probability distribution for each item.
Generated: DETERMINISTIC_079821a3be8f5df2
Batch ID: 20250622_204657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from collections import namedtuple

# Define a named tuple to represent each NFT item
NFTItem = namedtuple('NFTItem', ['name', 'rarity', 'probability'])

# Define the rarity levels and their corresponding probabilities
RARITY_LEVELS = {
    'Common': 0.50,    # 50% chance
    'Uncommon': 0.25,  # 25% chance
    'Rare': 0.15,      # 15% chance
    'Epic': 0.07,      # 7% chance
    'Legendary': 0.02, # 2% chance
    'Mythic': 0.01     # 1% chance
}

# Create a list of NFT items with their respective rarities
nft_items = [
    NFTItem(name='Common Item 1', rarity='Common', probability=RARITY_LEVELS['Common']),
    NFTItem(name='Common Item 2', rarity='Common', probability=RARITY_LEVELS['Common']),
    NFTItem(name='Uncommon Item 1', rarity='Uncommon', probability=RARITY_LEVELS['Uncommon']),
    NFTItem(name='Rare Item 1', rarity='Rare', probability=RARITY_LEVELS['Rare']),
    NFTItem(name='Epic Item 1', rarity='Epic', probability=RARITY_LEVELS['Epic']),
    NFTItem(name='Legendary Item 1', rarity='Legendary', probability=RARITY_LEVELS['Legendary']),
    NFTItem(name='Mythic Item 1', rarity='Mythic', probability=RARITY_LEVELS['Mythic']),
    NFTItem(name='Mythic Item 2', rarity='Mythic', probability=RARITY_LEVELS['Mythic']),
]

def get_random_nft_item():
    """
    Selects a random NFT item based on the defined rarity probabilities.
    
    Returns:
        NFTItem: A randomly selected NFT item.
    """
    # Generate a random number between 0 and 1
    rand_value = random.random()
    cumulative_probability = 0.0

    # Iterate through the items and their probabilities
    for item in nft_items:
        cumulative_probability += item.probability
        if rand_value <= cumulative_probability:
            return item

    # In case of an error in probability distribution, raise an exception
    raise ValueError("Probability distribution is incorrect. Ensure probabilities sum to 1.")

def main():
    """
    Main function to demonstrate the NFT rarity system.
    """
    try:
        # Simulate drawing an NFT item
        selected_item = get_random_nft_item()
        print(f"Selected NFT Item: {selected_item.name} (Rarity: {selected_item.rarity})")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
