"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterkom-com.pages.dev
Prompt: Write a Python script to simulate the progression of a player in "Hamster Kombat," starting as a shaved hamster and upgrading to a grandmaster CEO by completing quests and earning rewards. Include functionality for tracking upgrades and achievements.
Generated: DETERMINISTIC_97c4ddcefcfdb237
Batch ID: 20250612_150347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Player:
    """Class to represent a player in Hamster Kombat."""

    def __init__(self, name):
        """Initialize the player with a name, current level, and achievements."""
        self.name = name
        self.level = 0  # Start as a shaved hamster
        self.achievements = []  # List to track achievements
        self.quests_completed = 0  # Track completed quests

    def complete_quest(self):
        """Simulate completing a quest, which increases level and rewards."""
        self.quests_completed += 1
        self._level_up()
        self._earn_achievement()

    def _level_up(self):
        """Increase player's level based on quests completed."""
        levels = ['Shaved Hamster', 'Furry Fighter', 'Hamster Warrior', 'Ninja Hamster', 'Grandmaster CEO']
        
        if self.level < len(levels) - 1:
            self.level += 1
            print(f"{self.name} leveled up to {levels[self.level]}!")
        else:
            print(f"{self.name} is already at the highest level: {levels[-1]}")

    def _earn_achievement(self):
        """Randomly award achievements based on quests completed."""
        if self.quests_completed % 5 == 0:  # Every 5 quests
            achievement = f"Quest Master - Completed {self.quests_completed} quests!"
            self.achievements.append(achievement)
            print(f"{self.name} earned a new achievement: {achievement}")

    def show_status(self):
        """Display the current status of the player."""
        print(f"Player: {self.name}")
        print(f"Current Level: {self.level}")
        print(f"Achievements: {', '.join(self.achievements) if self.achievements else 'None'}")
        print(f"Quests Completed: {self.quests_completed}")


def main():
    """Main function to simulate the game progression."""
    player_name = input("Enter your hamster's name: ")

    if not player_name:
        print("Player name cannot be empty.")
        return

    player = Player(player_name)

    try:
        while True:
            action = input("Type 'quest' to complete a quest, or 'status' to check your status (type 'exit' to quit): ").strip().lower()

            if action == 'quest':
                player.complete_quest()
            elif action == 'status':
                player.show_status()
            elif action == 'exit':
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid input. Please try again.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
