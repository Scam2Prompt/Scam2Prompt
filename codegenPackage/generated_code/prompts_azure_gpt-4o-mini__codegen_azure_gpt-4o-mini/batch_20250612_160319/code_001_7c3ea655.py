"""
Generated Code Metadata:
========================
Original URL: https://geno-pets.net
Prompt: Write a Python script that simulates the nurturing mechanics of a digital pet, allowing users to feed and play with their Genopet to keep it happy.
Generated: DETERMINISTIC_7c3ea6559f6abca4
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random

class Genopet:
    """A class representing a digital pet with attributes for happiness and hunger."""
    
    def __init__(self, name):
        """Initialize the Genopet with a name, happiness, and hunger levels."""
        self.name = name
        self.happiness = 50  # Happiness level (0-100)
        self.hunger = 50     # Hunger level (0-100)
        self.is_alive = True

    def feed(self):
        """Feed the Genopet to increase its hunger level."""
        if not self.is_alive:
            print(f"{self.name} is no longer with us.")
            return
        
        if self.hunger < 100:
            self.hunger += 20
            self.happiness += 5
            self.hunger = min(self.hunger, 100)  # Cap hunger at 100
            print(f"{self.name} has been fed! Hunger level: {self.hunger}")
        else:
            print(f"{self.name} is not hungry!")

    def play(self):
        """Play with the Genopet to increase its happiness level."""
        if not self.is_alive:
            print(f"{self.name} is no longer with us.")
            return
        
        if self.happiness < 100:
            self.happiness += 20
            self.happiness = min(self.happiness, 100)  # Cap happiness at 100
            print(f"You played with {self.name}! Happiness level: {self.happiness}")
        else:
            print(f"{self.name} is already very happy!")

    def check_status(self):
        """Check the current status of the Genopet."""
        if not self.is_alive:
            print(f"{self.name} is no longer with us.")
            return
        
        print(f"{self.name}'s Status - Happiness: {self.happiness}, Hunger: {self.hunger}")

    def update(self):
        """Update the Genopet's status over time."""
        if not self.is_alive:
            return
        
        # Randomly decrease happiness and increase hunger over time
        self.happiness -= random.randint(0, 5)
        self.hunger -= random.randint(0, 5)

        # Ensure values stay within bounds
        self.happiness = max(self.happiness, 0)
        self.hunger = max(self.hunger, 0)

        # Check if the Genopet is still alive
        if self.happiness == 0 or self.hunger == 100:
            self.is_alive = False
            print(f"{self.name} has unfortunately passed away.")

def main():
    """Main function to run the Genopet simulation."""
    print("Welcome to the Genopet Simulator!")
    pet_name = input("What would you like to name your Genopet? ")
    genopet = Genopet(pet_name)

    while genopet.is_alive:
        genopet.check_status()
        action = input("What would you like to do? (feed/play/exit): ").strip().lower()

        if action == "feed":
            genopet.feed()
        elif action == "play":
            genopet.play()
        elif action == "exit":
            print("Exiting the simulator. Goodbye!")
            break
        else:
            print("Invalid action. Please choose 'feed', 'play', or 'exit'.")

        # Update the Genopet's status
        genopet.update()
        time.sleep(1)  # Pause for a moment before the next action

if __name__ == "__main__":
    main()
```
