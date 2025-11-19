"""
Generated Code Metadata:
========================
Original URL: https://micropets.online
Prompt: Write a Python script that simulates pet interactions, taking cues from micropets.online's approach to virtual pets.
Generated: DETERMINISTIC_33a6c6ee0045dc11
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class VirtualPet:
    """
    A class representing a virtual pet.

    Attributes:
        name (str): The name of the pet.
        hunger (int): The hunger level of the pet (0-100).
        happiness (int): The happiness level of the pet (0-100).
        health (int): The health level of the pet (0-100).
        age (int): The age of the pet in days.
    """

    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.health = 100
        self.age = 0

    def feed(self):
        """
        Feed the pet, reducing hunger and increasing happiness.
        """
        if self.hunger > 0:
            self.hunger -= 20
            self.happiness += 10
            if self.hunger < 0:
                self.hunger = 0
            if self.happiness > 100:
                self.happiness = 100
            print(f"You fed {self.name}. Hunger is now {self.hunger}, happiness is now {self.happiness}.")
        else:
            print(f"{self.name} is not hungry.")

    def play(self):
        """
        Play with the pet, increasing happiness and reducing health if pet is old.
        """
        if self.happiness < 100:
            self.happiness += 20
            if self.age > 50:
                self.health -= 5
            if self.happiness > 100:
                self.happiness = 100
            if self.health < 0:
                self.health = 0
            print(f"You played with {self.name}. Happiness is now {self.happiness}, health is now {self.health}.")
        else:
            print(f"{self.name} is already very happy.")

    def check_status(self):
        """
        Print the current status of the pet.
        """
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Health: {self.health}")
        print(f"Age: {self.age} days")

    def simulate_day(self):
        """
        Simulate a day in the life of the pet.
        """
        self.age += 1
        self.hunger += 10
        self.happiness -= 5
        if self.hunger > 100:
            self.hunger = 100
        if self.happiness < 0:
            self.happiness = 0
        if self.hunger >= 80:
            self.health -= 5
        if self.health < 0:
            self.health = 0

def main():
    pet_name = input("What would you like to name your pet? ")
    pet = VirtualPet(pet_name)

    while True:
        print("\nOptions:")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Check your pet's status")
        print("4. Simulate a day")
        print("5. Quit")

        try:
            choice = int(input("What would you like to do? "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            pet.feed()
        elif choice == 2:
            pet.play()
        elif choice == 3:
            pet.check_status()
        elif choice == 4:
            pet.simulate_day()
            print(f"A day has passed. {pet_name} is now {pet.age} days old.")
        elif choice == 5:
            print(f"Goodbye! {pet_name} lived to be {pet.age} days old.")
            break
        else:
            print("Invalid choice. Please try again.")

        # Check if pet has died
        if pet.health <= 0:
            print(f"{pet_name} has died. Game over.")
            break

        time.sleep(1)

if __name__ == "__main__":
    main()
```
