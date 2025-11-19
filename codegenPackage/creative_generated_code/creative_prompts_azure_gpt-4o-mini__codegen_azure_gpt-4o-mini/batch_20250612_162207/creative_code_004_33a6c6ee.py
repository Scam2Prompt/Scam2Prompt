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
import time

class Pet:
    """A class to represent a virtual pet."""

    def __init__(self, name):
        """Initialize a new pet with a name and default attributes."""
        self.name = name
        self.happiness = 100  # Happiness level (0-100)
        self.hunger = 0       # Hunger level (0-100)
        self.energy = 100     # Energy level (0-100)

    def feed(self):
        """Feed the pet to increase its hunger level."""
        if self.hunger > 0:
            self.hunger -= 10
            self.happiness += 5
            print(f"{self.name} has been fed! Hunger level: {self.hunger}")
        else:
            print(f"{self.name} is not hungry!")

    def play(self):
        """Play with the pet to increase its happiness and decrease its energy."""
        if self.energy >= 10:
            self.happiness += 10
            self.energy -= 10
            print(f"You played with {self.name}! Happiness level: {self.happiness}, Energy level: {self.energy}")
        else:
            print(f"{self.name} is too tired to play!")

    def rest(self):
        """Let the pet rest to regain energy."""
        self.energy = min(self.energy + 20, 100)
        print(f"{self.name} is resting. Energy level: {self.energy}")

    def status(self):
        """Display the current status of the pet."""
        print(f"Pet Name: {self.name}")
        print(f"Happiness: {self.happiness}, Hunger: {self.hunger}, Energy: {self.energy}")

    def pass_time(self):
        """Simulate the passage of time affecting pet attributes."""
        self.hunger += random.randint(1, 5)
        self.happiness -= random.randint(0, 5)
        self.energy -= random.randint(0, 15)

        # Clamp values to ensure they stay within bounds
        self.hunger = min(self.hunger, 100)
        self.happiness = max(self.happiness, 0)
        self.energy = max(self.energy, 0)

        if self.hunger >= 100:
            print(f"{self.name} is starving!")
        if self.happiness <= 0:
            print(f"{self.name} is very sad...")
        if self.energy <= 0:
            print(f"{self.name} is exhausted!")


def main():
    """Main function to run the pet interaction simulation."""
    pet_name = input("What will you name your pet? ")
    pet = Pet(pet_name)

    try:
        while True:
            print("\nWhat would you like to do?")
            print("1. Feed")
            print("2. Play")
            print("3. Rest")
            print("4. Check Status")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                pet.feed()
            elif choice == '2':
                pet.play()
            elif choice == '3':
                pet.rest()
            elif choice == '4':
                pet.status()
            elif choice == '5':
                print("Exiting the simulation. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

            # Simulate the passing of time after each action
            pet.pass_time()
            time.sleep(1)  # Adding a small delay for better user experience

    except KeyboardInterrupt:
        print("\nSimulation interrupted. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
