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
# virtual_pet_game.py

class VirtualPet:
    """
    A simple virtual pet game.

    Attributes:
        name (str): The pet's name.
        hunger (int): The pet's hunger level (0-100).
        happiness (int): The pet's happiness level (0-100).
        energy (int): The pet's energy level (0-100).
    """

    def __init__(self, name):
        """
        Initializes a new virtual pet.

        Args:
            name (str): The pet's name.
        """
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def feed(self):
        """
        Feeds the pet, reducing hunger and increasing energy.
        """
        if self.hunger > 0:
            self.hunger -= 20
            self.energy += 10
            if self.hunger < 0:
                self.hunger = 0
            if self.energy > 100:
                self.energy = 100
            print(f"You fed {self.name}. Hunger is now {self.hunger}, energy is now {self.energy}.")
        else:
            print(f"{self.name} is not hungry.")

    def play(self):
        """
        Plays with the pet, increasing happiness and reducing energy.
        """
        if self.energy > 0:
            self.happiness += 20
            self.energy -= 10
            if self.happiness > 100:
                self.happiness = 100
            if self.energy < 0:
                self.energy = 0
            print(f"You played with {self.name}. Happiness is now {self.happiness}, energy is now {self.energy}.")
        else:
            print(f"{self.name} is too tired to play.")

    def status(self):
        """
        Prints the pet's current status.
        """
        print(f"{self.name}'s status:")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")
        print(f"Energy: {self.energy}")


def main():
    print("Welcome to the virtual pet game!")
    pet_name = input("What would you like to name your pet? ")
    pet = VirtualPet(pet_name)

    while True:
        print("\nOptions:")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Check pet status")
        print("4. Quit")

        try:
            choice = int(input("What would you like to do? "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == 1:
            pet.feed()
        elif choice == 2:
            pet.play()
        elif choice == 3:
            pet.status()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Simulate time passing
        pet.hunger += 1
        pet.happiness -= 1
        pet.energy -= 1

        # Ensure stats stay within bounds
        if pet.hunger > 100:
            pet.hunger = 100
        if pet.happiness < 0:
            pet.happiness = 0
        if pet.energy < 0:
            pet.energy = 0

        # Game over condition
        if pet.hunger >= 80 or pet.happiness <= 20 or pet.energy <= 20:
            pet.status()
            print("Game over! Your pet's needs were not met.")
            break


if __name__ == "__main__":
    main()
```
