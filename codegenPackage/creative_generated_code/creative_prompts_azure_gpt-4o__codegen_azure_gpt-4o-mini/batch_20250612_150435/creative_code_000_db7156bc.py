"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enterkuroro.pages.dev
Prompt: Write a Python script to simulate a tamagotchi-style game inspired by Kuroro Ranch, where players can feed, pet, and level up their virtual beasts. Include functionality for improving a virtual ranch.
Generated: DETERMINISTIC_db7156bc4d63a544
Batch ID: 20250612_150435
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

class VirtualBeast:
    """Class to represent a virtual beast in the Tamagotchi-style game."""
    
    def __init__(self, name):
        self.name = name
        self.hunger = 100  # Hunger level from 0 (starving) to 100 (full)
        self.happiness = 100  # Happiness level from 0 (sad) to 100 (happy)
        self.level = 1  # Beast level
        self.experience = 0  # Experience points

    def feed(self, amount):
        """Feed the beast to increase its hunger level."""
        if amount < 0:
            raise ValueError("Amount must be positive.")
        self.hunger = min(100, self.hunger + amount)
        print(f"{self.name} has been fed. Current hunger: {self.hunger}")

    def pet(self):
        """Pet the beast to increase its happiness level."""
        if self.happiness < 100:
            self.happiness += 10
            print(f"You pet {self.name}. Current happiness: {self.happiness}")
        else:
            print(f"{self.name} is already very happy!")

    def gain_experience(self):
        """Gains experience and checks for level up."""
        self.experience += random.randint(1, 10)
        if self.experience >= self.level * 100:
            self.level_up()

    def level_up(self):
        """Level up the beast and reset experience."""
        self.level += 1
        self.experience = 0
        print(f"{self.name} leveled up! Now level {self.level}!")

    def status(self):
        """Display the current status of the beast."""
        return f"{self.name} - Level: {self.level}, Hunger: {self.hunger}, Happiness: {self.happiness}"


class VirtualRanch:
    """Class to represent the player's ranch."""
    
    def __init__(self):
        self.beasts = []
        self.resources = 1000  # Starting resources for the ranch

    def add_beast(self, beast):
        """Add a virtual beast to the ranch."""
        if not isinstance(beast, VirtualBeast):
            raise TypeError("Only VirtualBeast instances can be added.")
        self.beasts.append(beast)
        print(f"{beast.name} has joined the ranch!")

    def feed_all(self, amount):
        """Feed all beasts in the ranch."""
        if self.resources < amount * len(self.beasts):
            print("Not enough resources to feed all beasts!")
            return
        for beast in self.beasts:
            beast.feed(amount)
        self.resources -= amount * len(self.beasts)
        print(f"Resources remaining: {self.resources}")

    def pet_all(self):
        """Pet all beasts in the ranch."""
        for beast in self.beasts:
            beast.pet()

    def pass_time(self):
        """Simulate the passage of time, affecting beasts' states."""
        for beast in self.beasts:
            beast.hunger -= random.randint(5, 15)
            beast.happiness -= random.randint(5, 15)
            beast.hunger = max(0, beast.hunger)
            beast.happiness = max(0, beast.happiness)
            beast.gain_experience()

    def status(self):
        """Display the status of all beasts in the ranch."""
        return [beast.status() for beast in self.beasts]


def main():
    """Main function to run the virtual ranch game."""
    ranch = VirtualRanch()
    
    # Create beasts
    beast1 = VirtualBeast("Fluffy")
    beast2 = VirtualBeast("Sparky")
    
    # Add beasts to the ranch
    ranch.add_beast(beast1)
    ranch.add_beast(beast2)

    # Game loop
    while True:
        print("\n=== Virtual Ranch Menu ===")
        print("1. Feed all beasts")
        print("2. Pet all beasts")
        print("3. Check status of beasts")
        print("4. Pass time")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        try:
            if choice == '1':
                ranch.feed_all(20)
            elif choice == '2':
                ranch.pet_all()
            elif choice == '3':
                statuses = ranch.status()
                for status in statuses:
                    print(status)
            elif choice == '4':
                ranch.pass_time()
                print("Time has passed.")
            elif choice == '5':
                print("Exiting the game. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        time.sleep(1)  # Pause for a moment before the next loop

if __name__ == "__main__":
    main()
```
