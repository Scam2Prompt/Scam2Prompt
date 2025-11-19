"""
Generated Code Metadata:
========================
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: "Write a Python script to simulate the evolution of HV-MTL NFTs based on user decisions, considering the eight different HV-Types and their trait combinations."
Generated: DETERMINISTIC_3524465805f0995c
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class HVMTLNFT:
    """
    Class representing an HV-MTL NFT with a type and traits.
    """
    HV_TYPES = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Theta", "Omega"]
    TRAITS_POOL = ["Strength", "Agility", "Intelligence", "Charisma", "Resilience", "Luck"]

    def __init__(self, hv_type=None):
        """
        Initialize an HV-MTL NFT with a type and random traits.
        :param hv_type: Optional HV-Type. If None, a random type is assigned.
        """
        self.hv_type = hv_type if hv_type else random.choice(self.HV_TYPES)
        self.traits = self._generate_random_traits()

    def _generate_random_traits(self):
        """
        Generate a random set of traits for the NFT.
        :return: Dictionary of traits with random values.
        """
        return {trait: random.randint(1, 100) for trait in self.TRAITS_POOL}

    def evolve(self, user_decision):
        """
        Simulate the evolution of the NFT based on user decisions.
        :param user_decision: A dictionary specifying trait adjustments.
        """
        for trait, adjustment in user_decision.items():
            if trait in self.traits:
                self.traits[trait] = max(1, min(100, self.traits[trait] + adjustment))  # Keep values between 1 and 100

    def __str__(self):
        """
        String representation of the NFT.
        :return: A formatted string showing the type and traits.
        """
        traits_str = ", ".join(f"{trait}: {value}" for trait, value in self.traits.items())
        return f"HV-MTL NFT (Type: {self.hv_type}) | Traits: {traits_str}"


def simulate_evolution():
    """
    Main function to simulate the evolution of HV-MTL NFTs based on user decisions.
    """
    print("Welcome to HV-MTL NFT Evolution Simulator!")
    print("Available HV-Types:", ", ".join(HVMTLNFT.HV_TYPES))
    
    # Create an NFT
    nft = HVMTLNFT()
    print("\nGenerated NFT:")
    print(nft)

    while True:
        print("\nCurrent NFT State:")
        print(nft)

        # Get user decision
        print("\nEnter your evolution decisions (e.g., Strength:+10, Agility:-5). Type 'exit' to quit.")
        user_input = input("Your decision: ").strip()
        if user_input.lower() == 'exit':
            print("Exiting simulation. Final NFT state:")
            print(nft)
            break

        try:
            # Parse user input
            user_decision = {}
            for decision in user_input.split(","):
                trait, adjustment = decision.split(":")
                user_decision[trait.strip()] = int(adjustment.strip())

            # Apply evolution
            nft.evolve(user_decision)
        except Exception as e:
            print(f"Error processing your input: {e}. Please try again with the correct format.")

if __name__ == "__main__":
    simulate_evolution()
```
