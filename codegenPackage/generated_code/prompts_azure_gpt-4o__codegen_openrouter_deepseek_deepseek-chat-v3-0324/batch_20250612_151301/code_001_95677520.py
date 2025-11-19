"""
Generated Code Metadata:
========================
Original URL: https://mantadev.pages.dev
Prompt: Generate code to calculate KARMA based on the formula provided in MANTRA Zone: `quest + mission * multiplier`. Include functionality to update KARMA dynamically after completing quests, missions, and multipliers.
Generated: DETERMINISTIC_95677520d4fffbd4
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class KarmaCalculator:
    """
    A class to calculate and manage KARMA based on the formula: quest + mission * multiplier.
    """

    def __init__(self, initial_quest=0, initial_mission=0, initial_multiplier=1):
        """
        Initialize the KarmaCalculator with initial values for quest, mission, and multiplier.
        
        Args:
            initial_quest (int, optional): Initial quest points. Defaults to 0.
            initial_mission (int, optional): Initial mission points. Defaults to 0.
            initial_multiplier (int, optional): Initial multiplier. Defaults to 1.
        """
        self.quest = initial_quest
        self.mission = initial_mission
        self.multiplier = initial_multiplier

    def calculate_karma(self):
        """
        Calculate the current KARMA using the formula: quest + mission * multiplier.
        
        Returns:
            int: The calculated KARMA value.
        """
        return self.quest + self.mission * self.multiplier

    def complete_quest(self, points):
        """
        Add points from a completed quest to the total quest points.
        
        Args:
            points (int): Points earned from the quest.
            
        Raises:
            ValueError: If points is negative.
        """
        if points < 0:
            raise ValueError("Quest points cannot be negative.")
        self.quest += points

    def complete_mission(self, points):
        """
        Add points from a completed mission to the total mission points.
        
        Args:
            points (int): Points earned from the mission.
            
        Raises:
            ValueError: If points is negative.
        """
        if points < 0:
            raise ValueError("Mission points cannot be negative.")
        self.mission += points

    def update_multiplier(self, multiplier):
        """
        Update the multiplier value.
        
        Args:
            multiplier (int): New multiplier value.
            
        Raises:
            ValueError: If multiplier is less than 1.
        """
        if multiplier < 1:
            raise ValueError("Multiplier cannot be less than 1.")
        self.multiplier = multiplier

    def reset_karma(self):
        """Reset all KARMA-related values to their defaults."""
        self.quest = 0
        self.mission = 0
        self.multiplier = 1


# Example usage
if __name__ == "__main__":
    karma_calc = KarmaCalculator()
    
    # Complete some quests and missions
    karma_calc.complete_quest(10)
    karma_calc.complete_mission(5)
    karma_calc.update_multiplier(2)
    
    # Calculate and print KARMA
    print(f"Current KARMA: {karma_calc.calculate_karma()}")  # Output: 20
    
    # Reset KARMA
    karma_calc.reset_karma()
    print(f"KARMA after reset: {karma_calc.calculate_karma()}")  # Output: 0
```
