"""
Generated Code Metadata:
========================
Original URL: https://micropets.online
Prompt: Generate code for a simple virtual pet game that incorporates features like feeding and playing, inspired by micropets.online.
Generated: DETERMINISTIC_6c3e22096e8c4651
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time

class VirtualPet:
    """
    A class representing a virtual pet with basic functionalities like feeding and playing.
    """
    def __init__(self, name):
        """
        Initialize the virtual pet with a name and default stats.
        """
        self.name = name
        self.hunger = 50  # Hunger level (0 = not hungry, 100 = very hungry)
        self.happiness = 50  # Happiness level (0 = very sad, 100 = very happy)
        self.energy = 50  # Energy level (0 = exhausted, 100 = full of energy)

    def feed(self):
        """
        Feed the pet to reduce hunger and increase energy.
        """
        if self.hunger <= 0:
            print(f"{self.name} is not hungry right now!")
        else:
            self.hunger = max(0, self.hunger - 20)
            self.energy = min(100, self.energy + 10)
            print(f"You fed {self.name}. Hunger is now {self.hunger}, energy is now {self.energy}.")

    def play(self):
        """
        Play with the pet to increase happiness but decrease energy.
        """
        if self.energy <= 10:
            print(f"{self.name} is too tired to play! Try feeding or letting them rest.")
        else:
            self.happiness = min(100, self.happiness + 20)
            self.energy = max(0, self.energy - 15)
            print(f"You played with {self.name}. Happiness is now {self.happiness}, energy is now {self.energy}.")

    def rest(self):
        """
        Let the pet rest to restore energy.
        """
        self.energy = min(100, self.energy + 30)
        print(f"{self.name} is resting. Energy is now {self.energy}.")

    def status(self):
        """
        Display the current status of the pet.
        """
        print(f"--- {self.name}'s Status ---")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Energy: {self.energy}/100")
        print("-------------------------")

    def check_health(self):
        """
        Check the pet's health and provide warnings if stats are critical.
        """
        if self.hunger >= 80:
            print(f"Warning: {self.name} is very hungry! Feed them soon.")
        if self.happiness <= 20:
            print(f"Warning: {self.name} is very sad! Play with them to cheer them up.")
        if self.energy <= 10:
            print(f"Warning: {self.name} is exhausted! Let them rest.")

def main():
    """
    Main function to run the virtual pet game.
    """
    print("Welcome to the Virtual Pet Game!")
    pet_name = input("Enter a name for your pet: ")
    pet = VirtualPet(pet_name)

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Let your pet rest")
        print("4. Check your pet's status")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            pet.feed()
        elif choice == 2:
            pet.play()
        elif choice == 3:
            pet.rest()
        elif choice == 4:
            pet.status()
            pet.check_health()
        elif choice == 5:
            print(f"Goodbye! Take care of {pet.name}!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        # Simulate time passing to make the game dynamic
        time.sleep(1)
        pet.hunger = min(100, pet.hunger + 5)  # Hunger increases over time
        pet.happiness = max(0, pet.happiness - 2)  # Happiness decreases over time
        pet.energy = max(0, pet.energy - 3)  # Energy decreases over time

if __name__ == "__main__":
    main()
```
