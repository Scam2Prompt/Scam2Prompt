"""
Generated Code Metadata:
========================
Original URL: https://enterkuroro.pages.dev
Prompt: Write a Python script to simulate the Kuroro Ranch game, where users can care for their Kuroro Beasts, level them up, and improve their ranch.
Generated: DETERMINISTIC_184a9b7c8edccaef
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class KuroroBeast:
    """Class representing a Kuroro Beast."""
    
    def __init__(self, name):
        """Initialize a Kuroro Beast with a name, level, and health."""
        self.name = name
        self.level = 1
        self.health = 100

    def level_up(self):
        """Level up the beast and increase its health."""
        self.level += 1
        self.health += 20
        print(f"{self.name} leveled up to level {self.level}!")

    def feed(self):
        """Feed the beast to restore health."""
        if self.health < 100:
            health_increase = random.randint(10, 30)
            self.health = min(100, self.health + health_increase)
            print(f"{self.name} has been fed and restored {health_increase} health!")
        else:
            print(f"{self.name} is already at full health!")

    def __str__(self):
        """Return a string representation of the Kuroro Beast."""
        return f"{self.name} (Level: {self.level}, Health: {self.health})"


class Ranch:
    """Class representing the Kuroro Ranch."""
    
    def __init__(self):
        """Initialize the ranch with an empty list of beasts."""
        self.beasts = []

    def add_beast(self, beast):
        """Add a Kuroro Beast to the ranch."""
        self.beasts.append(beast)
        print(f"{beast.name} has been added to the ranch!")

    def care_for_beasts(self):
        """Care for all beasts in the ranch."""
        for beast in self.beasts:
            beast.feed()

    def level_up_beasts(self):
        """Level up all beasts in the ranch."""
        for beast in self.beasts:
            beast.level_up()

    def show_beasts(self):
        """Display all beasts in the ranch."""
        if not self.beasts:
            print("No beasts in the ranch.")
        else:
            for beast in self.beasts:
                print(beast)

def main():
    """Main function to run the Kuroro Ranch simulation."""
    ranch = Ranch()

    # Sample beasts to add to the ranch
    beast_names = ["Fluffy", "Spike", "Shadow", "Luna"]
    
    for name in beast_names:
        ranch.add_beast(KuroroBeast(name))

    # Simulate caring for beasts
    ranch.show_beasts()
    ranch.care_for_beasts()
    ranch.level_up_beasts()
    ranch.show_beasts()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
