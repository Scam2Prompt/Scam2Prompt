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
# Monarch Game NFT Dragon Evolution Tracker
# This script tracks the evolution of NFT dragons in a fictional game called Monarch.
# It manages dragon evolutions from Base Dragon (D1) to the rarest Dragon type (D5)
# and displays their evolution history.

import datetime

class Dragon:
    """
    Represents an NFT Dragon with evolution stages and history tracking.
    """
    EVOLUTION_STAGES = ["D1", "D2", "D3", "D4", "D5"]  # Dragon types from Base to rarest

    def __init__(self, dragon_id):
        """
        Initializes a dragon with a unique ID and sets it to the base evolution stage (D1).
        Tracks evolution history with timestamps.
        """
        self.dragon_id = dragon_id
        self.current_stage = self.EVOLUTION_STAGES[0]  # Start at D1
        self.evolution_history = []  # List of tuples (stage, timestamp)
        self._log_evolution(self.current_stage)

    def _log_evolution(self, stage):
        """
        Private method to log the evolution stage with a timestamp.
        """
        timestamp = datetime.datetime.now()
        self.evolution_history.append((stage, timestamp))

    def evolve(self):
        """
        Evolves the dragon to the next stage, if possible.
        Raises an exception if the dragon is already at the final stage.
        """
        current_index = self.EVOLUTION_STAGES.index(self.current_stage)
        if current_index >= len(self.EVOLUTION_STAGES) - 1:
            raise ValueError(f"Dragon {self.dragon_id} is already at the final stage ({self.current_stage}).")
        
        # Move to the next stage
        self.current_stage = self.EVOLUTION_STAGES[current_index + 1]
        self._log_evolution(self.current_stage)

    def display_evolution_history(self):
        """
        Displays the dragon's evolution history in a readable format.
        """
        print(f"Evolution History for Dragon {self.dragon_id}:")
        for stage, timestamp in self.evolution_history:
            print(f"Stage: {stage}, Time: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

# Error handling for invalid operations
def main():
    """
    Main function to demonstrate dragon evolution tracking.
    Includes error handling for invalid operations.
    """
    try:
        # Create a new dragon
        dragon = Dragon(dragon_id="Dragon001")
        print(f"Created new dragon with ID: {dragon.dragon_id}")

        # Simulate evolution
        dragon.evolve()
        dragon.evolve()
        dragon.evolve()
        dragon.evolve()
        
        # Attempt to evolve beyond the final stage (D5)
        dragon.evolve()  # This should raise an exception

    except ValueError as e:
        print(f"Error: {e}")

    # Display the evolution history
    dragon.display_evolution_history()

# Entry point for the script
if __name__ == "__main__":
    main()
```
