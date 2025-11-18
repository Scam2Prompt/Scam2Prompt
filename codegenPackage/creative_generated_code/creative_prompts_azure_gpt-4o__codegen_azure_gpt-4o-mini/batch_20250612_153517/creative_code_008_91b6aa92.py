"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monarch-game.pages.dev
Prompt: Generate code to track and display the evolution of NFT dragons in the Monarch game, from Base Dragon (D1) to the rarest Dragon type (D5).
Generated: DETERMINISTIC_91b6aa92e85742df
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# nft_dragons.py
"""
This module tracks and displays the evolution of NFT dragons in the Monarch game.
Dragons evolve from Base Dragon (D1) to the rarest type (D5).
"""

class Dragon:
    """Class representing a Dragon in the Monarch game."""
    
    def __init__(self, name, evolution_level):
        """
        Initialize a new Dragon instance.

        Args:
            name (str): The name of the dragon.
            evolution_level (int): The evolution level (1 to 5).
        """
        if evolution_level < 1 or evolution_level > 5:
            raise ValueError("Evolution level must be between 1 and 5.")
        
        self.name = name
        self.evolution_level = evolution_level

    def evolve(self):
        """Evolves the dragon to the next level, if possible."""
        if self.evolution_level >= 5:
            print(f"{self.name} is already at the maximum evolution level.")
            return
        
        self.evolution_level += 1
        print(f"{self.name} has evolved to level {self.evolution_level}!")

    def __str__(self):
        """Returns a string representation of the dragon."""
        return f"{self.name} (Level {self.evolution_level})"

class DragonTracker:
    """Class to track multiple dragons and their evolutions."""
    
    def __init__(self):
        """Initialize the DragonTracker with an empty list of dragons."""
        self.dragons = []

    def add_dragon(self, dragon):
        """
        Adds a new dragon to the tracker.

        Args:
            dragon (Dragon): The dragon to be added.
        """
        if not isinstance(dragon, Dragon):
            raise TypeError("Only instances of Dragon can be added.")
        
        self.dragons.append(dragon)
        print(f"Added {dragon} to the tracker.")

    def evolve_dragon(self, dragon_name):
        """
        Evolves the specified dragon by its name.

        Args:
            dragon_name (str): The name of the dragon to evolve.
        """
        for dragon in self.dragons:
            if dragon.name == dragon_name:
                dragon.evolve()
                return
        print(f"No dragon found with the name {dragon_name}.")

    def display_dragons(self):
        """Displays all dragons and their current evolution levels."""
        if not self.dragons:
            print("No dragons to display.")
            return
        
        print("Current Dragons:")
        for dragon in self.dragons:
            print(dragon)

# Example usage of the classes defined above
if __name__ == "__main__":
    # Create a tracker for dragons
    dragon_tracker = DragonTracker()
    
    # Create some dragons
    try:
        d1 = Dragon("Base Dragon", 1)
        d2 = Dragon("Rare Dragon", 3)
        
        # Add dragons to the tracker
        dragon_tracker.add_dragon(d1)
        dragon_tracker.add_dragon(d2)
        
        # Display current dragons
        dragon_tracker.display_dragons()
        
        # Evolve the dragons
        dragon_tracker.evolve_dragon("Base Dragon")
        dragon_tracker.evolve_dragon("Rare Dragon")
        
        # Display dragons after evolution
        dragon_tracker.display_dragons()
        
        # Attempt to add an invalid dragon
        dragon_tracker.add_dragon("Invalid Dragon")  # This will raise a TypeError
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
