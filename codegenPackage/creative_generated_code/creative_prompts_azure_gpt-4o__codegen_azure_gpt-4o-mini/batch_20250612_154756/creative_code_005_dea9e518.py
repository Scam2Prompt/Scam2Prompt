"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stepn-walkin.com
Prompt: Create a Python program that simulates the leveling-up process in STEPN, incorporating the recommended point allocation strategies from the blog.
Generated: DETERMINISTIC_dea9e518281d4cd0
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Player:
    """A class to represent a player in the STEPN game."""

    def __init__(self, name: str):
        """
        Initialize a new player.

        Parameters:
        name (str): The name of the player.
        """
        self.name = name
        self.level = 1
        self.experience = 0
        self.points = 0
        self.point_allocation = {"speed": 0, "stamina": 0, "luck": 0}

    def gain_experience(self, amount: int):
        """
        Simulate gaining experience points.

        Parameters:
        amount (int): The amount of experience to gain.
        """
        if amount < 0:
            raise ValueError("Experience amount must be non-negative.")
        
        self.experience += amount
        print(f"{self.name} gained {amount} experience points!")

        # Check for level-up
        while self.experience >= self.level * 100:  # Assuming 100 XP needed per level
            self.level_up()

    def level_up(self):
        """Level up the player and provide point allocation options."""
        self.experience -= self.level * 100  # Deduct experience for leveling up
        self.level += 1
        print(f"{self.name} leveled up to level {self.level}!")

        # Allocate points upon leveling up
        self.allocate_points()

    def allocate_points(self):
        """Allocate points based on recommended strategies."""
        print(f"Allocating points for {self.name} at level {self.level}...")
        points_to_allocate = 5  # Number of points to allocate on level up

        # Sample allocation strategies
        if self.level <= 5:
            # Early game: focus on speed
            self.point_allocation["speed"] += points_to_allocate
        elif 6 <= self.level <= 10:
            # Mid game: balance between speed and stamina
            self.point_allocation["speed"] += points_to_allocate // 2
            self.point_allocation["stamina"] += points_to_allocate // 2
        else:
            # Late game: luck becomes important
            self.point_allocation["luck"] += points_to_allocate

        self.points += points_to_allocate
        print(f"Points allocated: {self.point_allocation}")

    def __str__(self):
        """Return a string representation of the player."""
        return (f"Player: {self.name}, Level: {self.level}, "
                f"Experience: {self.experience}, Points: {self.points}, "
                f"Allocation: {self.point_allocation}")


def main():
    """Main function to run the STEPN leveling simulation."""
    try:
        # Create a player instance
        player_name = input("Enter the player's name: ")
        player = Player(player_name)

        # Simulate gaining experience
        while True:
            exp = input("Enter experience to gain (or 'exit' to quit): ")
            if exp.lower() == 'exit':
                break
            try:
                exp_amount = int(exp)
                player.gain_experience(exp_amount)
                print(player)
            except ValueError as ve:
                print(f"Invalid input: {ve}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
