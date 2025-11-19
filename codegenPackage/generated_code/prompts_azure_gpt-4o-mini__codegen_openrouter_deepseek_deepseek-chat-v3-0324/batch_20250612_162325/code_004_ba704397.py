"""
Generated Code Metadata:
========================
Original URL: https://monarch-game.pages.dev
Prompt: Create a code example that simulates the leveling up of a Dragon from D1 to D5 in the Monarch Dungeon based on game activity.
Generated: DETERMINISTIC_ba70439734f5c0d9
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Dragon:
    """
    Represents a Dragon in the Monarch Dungeon with leveling capabilities.
    """
    
    def __init__(self, name: str, level: int = 1):
        """
        Initialize a Dragon with a name and starting level (default: 1).
        
        Args:
            name (str): Name of the dragon.
            level (int, optional): Starting level of the dragon. Defaults to 1.
        """
        self.name = name
        self.level = level
        self.max_level = 5  # Maximum level the dragon can reach
    
    def level_up(self) -> bool:
        """
        Attempt to level up the dragon by one level.
        
        Returns:
            bool: True if level up was successful, False if already at max level.
        """
        if self.level < self.max_level:
            self.level += 1
            return True
        return False
    
    def simulate_activity(self, activity_points: int) -> None:
        """
        Simulate game activity to potentially level up the dragon.
        
        Args:
            activity_points (int): Points earned from game activity.
        
        Raises:
            ValueError: If activity_points is negative.
        """
        if activity_points < 0:
            raise ValueError("Activity points cannot be negative.")
        
        # Each level requires 100 points per current level to level up
        required_points = self.level * 100
        
        while activity_points >= required_points and self.level < self.max_level:
            activity_points -= required_points
            self.level_up()
            required_points = self.level * 100  # Update required points for new level
    
    def __str__(self) -> str:
        """Return a string representation of the dragon."""
        return f"Dragon {self.name} (Level D{self.level})"


def simulate_dragon_leveling(dragon_name: str, total_activity_points: int) -> Dragon:
    """
    Simulate a dragon's leveling from D1 to D5 based on activity points.
    
    Args:
        dragon_name (str): Name of the dragon to simulate.
        total_activity_points (int): Total activity points to apply.
    
    Returns:
        Dragon: The leveled up dragon instance.
    
    Raises:
        ValueError: If total_activity_points is negative.
    """
    dragon = Dragon(dragon_name)
    dragon.simulate_activity(total_activity_points)
    return dragon


# Example usage
if __name__ == "__main__":
    try:
        # Create a dragon and simulate leveling with 1000 activity points
        dragon = simulate_dragon_leveling("Firebrand", 1000)
        print(dragon)  # Expected output depends on points (e.g., 1000 points = D4)
    except ValueError as e:
        print(f"Error: {e}")
```
