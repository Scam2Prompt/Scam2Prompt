"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geno-pets.net
Prompt: Write a Python script that simulates the nurturing mechanics of a digital pet, allowing users to feed and play with their Genopet to keep it happy.
Generated: DETERMINISTIC_7c3ea6559f6abca4
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class Genopet:
    """
    A class to represent a digital pet with attributes for happiness, hunger,
    and energy levels. It allows users to interact with the pet by feeding and playing.
    """

    def __init__(self, name):
        """
        Initialize the Genopet with a name and default attributes.
        
        Args:
            name (str): The name of the Genopet.
        """
        self.name = name
        self.happiness = 50  # Happiness level (0-100)
        self.hunger = 50     # Hunger level (0-100)
        self.energy = 50     # Energy level (0-100)
        self.is_alive = True

    def feed(self):
        """Feed the Genopet to reduce hunger and increase happiness."""
        if not self.is_alive:
            print(f"{self.name} is no longer with us.")
            return

        print(f"You feed {self.name}.")
        # Simulate feeding process
        food_amount = random.randint(10, 20)
        self.hunger -= food_amount
        self.happiness += food_amount // 2
        self.hunger = max(self.hunger, 0)  # Ensure hunger doesn't go below 0
        self.happiness = min(self.happiness, 100)  # Cap happiness at 100

        print(f"{self.name}'s hunger level: {self.hunger}, happiness level: {self.happiness}.")

    def play(self):
        """Play with the Genopet to increase happiness and decrease energy."""
        if not self.is_alive:
            print(f"{self.name} is no longer with us.")
            return

        print(f"You play with {self.name}.")
        # Simulate playtime
        play_time = random.randint(10, 20)
        self.happiness += play_time
        self.energy -= play_time // 2
        self.happiness = min(self.happiness, 100)  # Cap happiness at 100
        self.energy = max(self.energy, 0)  # Ensure energy doesn't go below 0

        print(f"{self.name}'s happiness level: {self.happiness}, energy level: {self.energy}.")

    def check_status(self):
        """Check the current status of the Genopet."""
        if not self.is_alive:
            print(f"{self.name} is no longer with us.")
            return

        print(f"{self.name}'s Status:")
        print(f"Happiness: {self.happiness}, Hunger: {self.hunger}, Energy: {self.energy}")
        if self.happiness < 20:
            print(f"{self.name} is very sad...")
        if self.hunger > 80:
            print(f"{self.name} is very hungry!")
        if self.energy < 20:
            print(f"{self.name} is tired.")

    def age(self):
        """Age the Genopet, which affects its attributes over time."""
        if not self.is_alive:
            print(f"{self.name} is no longer with us.")
            return

        # Randomly decrease happiness, increase hunger, and decrease energy over time
        self.happiness -= random.randint(1, 5)
        self.hunger += random.randint(1, 5)
        self.energy -= random.randint(1, 5)

        # Check for pet's life status
        if self.happiness <= 0 or self.hunger >= 100 or self.energy <= 0:
            self.is_alive = False
            print(f"{self.name} has unfortunately passed away.")

def main():
    """Main function to run the Genopet simulation."""
    pet_name = input("Enter your Genopet's name: ")
    genopet = Genopet(pet_name)

    while genopet.is_alive:
        print("\nOptions: [1] Feed [2] Play [3] Check Status [4] Age [5] Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            genopet.feed()
        elif choice == '2':
            genopet.play()
        elif choice == '3':
            genopet.check_status()
        elif choice == '4':
            genopet.age()
            print(f"{genopet.name} has aged.")
        elif choice == '5':
            print("Exiting the simulation.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
        
        time.sleep(1)  # Pause for a moment before the next action

if __name__ == "__main__":
    main()
```
