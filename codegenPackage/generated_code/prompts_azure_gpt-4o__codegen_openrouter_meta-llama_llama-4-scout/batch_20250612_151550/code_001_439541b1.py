"""
Generated Code Metadata:
========================
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: Generate code to simulate the evolution of HV-MTL NFTs based on user decisions, incorporating traits like "dynamic," "bio," and "celestial."
Generated: DETERMINISTIC_439541b13833c615
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from dataclasses import dataclass

# Define an Enum for NFT traits
class TraitType(Enum):
    DYNAMIC = "dynamic"
    BIO = "bio"
    CELESTIAL = "celestial"

# Define a data class for NFT traits
@dataclass
class NFTrait:
    type: TraitType
    name: str
    description: str

# Define a data class for HV-MTL NFTs
@dataclass
class HVMTLNFT:
    id: int
    traits: list[NFTrait]

# Define a class to simulate HV-MTL NFT evolution
class HVMTLNFTEvolutionSimulator:
    def __init__(self):
        self.nfts = []
        self.trait_library = {
            TraitType.DYNAMIC: [
                NFTrait(TraitType.DYNAMIC, "Aurora", "A shimmering aurora display"),
                NFTrait(TraitType.DYNAMIC, "Nebula", "A swirling nebula pattern"),
                NFTrait(TraitType.DYNAMIC, "Galaxy", "A vibrant galaxy scene"),
            ],
            TraitType.BIO: [
                NFTrait(TraitType.BIO, "Terraverde", "A lush, green landscape"),
                NFTrait(TraitType.BIO, "Aeropex", "A futuristic, high-tech atmosphere"),
                NFTrait(TraitType.BIO, "Aquaria", "An underwater cityscape"),
            ],
            TraitType.CELESTIAL: [
                NFTrait(TraitType.CELESTIAL, "Solar Flare", "A burst of solar energy"),
                NFTrait(TraitType.CELESTIAL, "Lunar Eclipse", "A moon shrouded in shadow"),
                NFTrait(TraitType.CELESTIAL, "Stellar Alignment", "A celestial body alignment"),
            ],
        }

    def create_nft(self, id: int) -> HVMTLNFT:
        """Create a new HV-MTL NFT with random traits"""
        traits = []
        for trait_type in TraitType:
            trait = random.choice(self.trait_library[trait_type])
            traits.append(trait)
        return HVMTLNFT(id, traits)

    def evolve_nft(self, nft: HVMTLNFT) -> HVMTLNFT:
        """Evolve an existing HV-MTL NFT by changing one random trait"""
        if not nft.traits:
            raise ValueError("NFT has no traits to evolve")

        trait_type_to_change = random.choice([trait.type for trait in nft.traits])
        new_trait = random.choice([t for t in self.trait_library[trait_type_to_change] if t != next(t for t in nft.traits if t.type == trait_type_to_change)])
        
        updated_traits = [new_trait if trait.type == trait_type_to_change else trait for trait in nft.traits]
        return HVMTLNFT(nft.id, updated_traits)

    def simulate_evolution(self, num_nfts: int, num_evolutions: int):
        """Simulate the evolution of HV-MTL NFTs based on user decisions"""
        for _ in range(num_nfts):
            nft = self.create_nft(len(self.nfts) + 1)
            self.nfts.append(nft)
            print(f"Initial NFT {nft.id} Traits:")
            for trait in nft.traits:
                print(f"- {trait.type.value.capitalize()}: {trait.name} - {trait.description}")

            for _ in range(num_evolutions):
                user_input = input("Would you like to evolve this NFT? (yes/no): ")
                if user_input.lower() == "yes":
                    evolved_nft = self.evolve_nft(nft)
                    nft = evolved_nft
                    print(f"Evolved NFT {nft.id} Traits:")
                    for trait in nft.traits:
                        print(f"- {trait.type.value.capitalize()}: {trait.name} - {trait.description}")
                else:
                    break
            print()

if __name__ == "__main__":
    simulator = HVMTLNFTEvolutionSimulator()
    simulator.simulate_evolution(1, 5)
```
