"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://micropets.online
Prompt: Write a Python script that simulates pet interactions, taking cues from micropets.online's approach to virtual pets.
Generated: DETERMINISTIC_33a6c6ee0045dc11
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Pet:
    """
    A class to represent a virtual pet and simulate its interactions.
    """
    def __init__(self, name: str, species: str):
        """
        Initialize the pet with a name, species, and default attributes.
        :param name: Name of the pet.
        :param species: Species of the pet.
        """
        self.name = name
        self.species = species
        self.hunger = 50  # Hunger level (0-100, lower is better)
        self.happiness = 50  # Happiness level (0-100, higher is better)
        self.energy = 50  # Energy level (0-100, higher is better)

    def feed(self):
        """
        Feed the pet to reduce hunger and increase happiness.
        """
        if self.hunger <= 10:
            print(f"{self.name} is not hungry right now!")
        else:
            self.hunger -= 10
            self.happiness += 5
            print(f"You fed {self.name}. Hunger decreased, happiness increased!")

    def play(self):
        """
        Play with the pet to increase happiness and decrease energy.
        """
        if self.energy <= 10:
            print(f"{self.name} is too tired to play!")
        else:
            self.happiness += 10
            self.energy -= 10
            print(f"You played with {self.name}. Happiness increased, but energy decreased!")

    def rest(self):
        """
        Allow the pet to rest and regain energy.
        """
        if self.energy >= 90:
            print(f"{self.name} is already fully rested!")
        else:
            self.energy += 20
            self.hunger += 5  # Resting increases hunger slightly
            print(f"{self.name} rested and regained energy. Watch out for increased hunger!")

    def status(self):
        """
        Display the current status of the pet.
        """
        print(f"--- {self.name}'s Status ---")
        print(f"Species: {self.species}")
        print(f"Hunger: {self.hunger}/100 (Lower is better)")
        print(f"Happiness: {self.happiness}/100 (Higher is better)")
        print(f"Energy: {self.energy}/100 (Higher is better)")

    def simulate_random_event(self):
        """
        Simulate a random event that affects the pet's attributes.
        """
        events = [
            ("found a treat", "hunger", -15, "happiness", +10),
            ("got scared by a loud noise", "happiness", -10, "energy", -5),
            ("took a nap", "energy", +10, "hunger", +5),
            ("learned a new trick", "happiness", +15, "energy", -5),
        ]
        event = random.choice(events)
        print(f"Random Event: {self.name} {event[0]}!")
        setattr(self, event[1], max(0, min(100, getattr(self, event[1]) + event[2])))
        setattr(self, event[3], max(0, min(100, getattr(self, event[3]) + event[4])))


def main():
    """
    Main function to simulate pet interactions.
    """
    try:
        # Initialize a pet
        name = input("Enter your pet's name: ").strip()
        species = input("Enter your pet's species: ").strip()
        pet = Pet(name, species)

        print(f"\nWelcome to the world of virtual pets! Meet {pet.name}, your new {pet.species}.\n")

        # Interaction loop
        while True:
            print("\nWhat would you like to do?")
            print("1. Feed your pet")
            print("2. Play with your pet")
            print("3. Let your pet rest")
            print("4. Check your pet's status")
            print("5. Simulate a random event")
            print("6. Quit")

            choice = input("Enter your choice (1-6): ").strip()
            if choice == "1":
                pet.feed()
            elif choice == "2":
                pet.play()
            elif choice == "3":
                pet.rest()
            elif choice == "4":
                pet.status()
            elif choice == "5":
                pet.simulate_random_event()
            elif choice == "6":
                print(f"Goodbye! {pet.name} will miss you!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 6.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again.")

if __name__ == "__main__":
    main()
```
