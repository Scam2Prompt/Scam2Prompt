"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: Generate code to simulate the evolution of HV-MTL NFTs based on user decisions, incorporating traits like "dynamic," "bio," and "celestial."
Generated: DETERMINISTIC_439541b13833c615
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json

class NFT:
    """Class representing an HV-MTL NFT with dynamic attributes."""
    
    def __init__(self, traits):
        """
        Initialize the NFT with given traits.
        
        Args:
            traits (dict): Dictionary containing NFT traits.
        """
        self.traits = traits

    def evolve(self, decisions):
        """
        Evolve the NFT based on user decisions.
        
        Args:
            decisions (list): List of user decisions affecting traits.
        """
        for decision in decisions:
            if decision in self.traits:
                self.traits[decision] = self._mutate_trait(self.traits[decision])

    def _mutate_trait(self, current_trait):
        """
        Mutate a given trait randomly to simulate evolution.
        
        Args:
            current_trait (str): The current trait value.
        
        Returns:
            str: New mutated trait value.
        """
        # Simple mutation logic: either change the trait slightly or return a new trait
        possible_mutations = [f"{current_trait}-enhanced", f"{current_trait}-reduced"]
        return random.choice(possible_mutations)

    def to_json(self):
        """Convert NFT traits to a JSON string."""
        return json.dumps(self.traits, indent=4)

def main():
    """Main function to simulate NFT evolution."""
    # Define initial traits for the NFT
    initial_traits = {
        "dynamic": "base",
        "bio": "organic",
        "celestial": "starry"
    }
    
    # Instantiate an NFT object
    nft = NFT(initial_traits)

    # User decisions to evolve the NFT
    user_decisions = ["dynamic", "bio", "celestial"]

    try:
        # Evolve the NFT based on user decisions
        nft.evolve(user_decisions)

        # Output the evolved NFT traits in JSON format
        print("Evolved NFT Traits:")
        print(nft.to_json())

    except Exception as e:
        # Handle exceptions gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
