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

class HVMTLNFT:
    """
    Class to simulate HV-MTL NFT evolution based on user decisions.
    Traits: dynamic, bio, celestial
    """
    def __init__(self, name):
        self.name = name
        self.traits = {
            "dynamic": random.randint(1, 10),  # Initial score for dynamic trait
            "bio": random.randint(1, 10),     # Initial score for bio trait
            "celestial": random.randint(1, 10) # Initial score for celestial trait
        }
        self.stage = 1  # Initial evolution stage
    
    def evolve(self, decision):
        """
        Simulate evolution based on user decisions.
        Decision affects traits and may trigger stage evolution.
        """
        try:
            if decision == "explore":
                self.traits["dynamic"] += random.randint(1, 3)
                self.traits["bio"] += random.randint(0, 2)
            elif decision == "meditate":
                self.traits["celestial"] += random.randint(2, 4)
                self.traits["bio"] += random.randint(1, 3)
            elif decision == "experiment":
                self.traits["dynamic"] += random.randint(0, 2)
                self.traits["celestial"] += random.randint(1, 3)
            else:
                raise ValueError("Invalid decision. Choose 'explore', 'meditate', or 'experiment'.")
            
            # Check if traits meet threshold to evolve stage
            if all(value >= 15 for value in self.traits.values()) and self.stage < 5:
                self.stage += 1
                print(f"{self.name} has evolved to stage {self.stage}!")
        except ValueError as e:
            print(f"Error: {str(e)}")
    
    def display_status(self):
        """
        Display the current status of the NFT.
        """
        print(f"NFT Name: {self.name}")
        print(f"Stage: {self.stage}")
        print("Traits:")
        for trait, value in self.traits.items():
            print(f"  {trait.capitalize()}: {value}")

# Example usage
def main():
    print("Welcome to HV-MTL NFT Evolution Simulator!")
    nft_name = input("Enter the name of your NFT: ")
    
    nft = HVMTLNFT(nft_name)
    print("Initial Status:")
    nft.display_status()
    
    while True:
        print("\nChoose a decision to evolve your NFT:")
        print("Options: 'explore', 'meditate', 'experiment', 'quit'")
        user_decision = input("Your decision: ").lower()
        
        if user_decision == "quit":
            print("Simulation ended. Final NFT status:")
            nft.display_status()
            break
        else:
            nft.evolve(user_decision)
            print("\nUpdated Status:")
            nft.display_status()

if __name__ == "__main__":
    main()
```
