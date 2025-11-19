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

class Genopet:
    """A class representing a digital pet with nurturing mechanics."""
    
    def __init__(self, name):
        """
        Initializes the Genopet's attributes.

        Args:
            name (str): The name of the pet.
        """
        self.name = name
        self.hunger = 50  # Hunger level (0 = not hungry, 100 = very hungry)
        self.happiness = 50  # Happiness level (0 = unhappy, 100 = very happy)
        self.last_fed = time.time()
        self.last_played = time.time()

    def feed(self):
        """
        Feeds the pet, reducing hunger and increasing happiness.
        """
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 20)  # Reduce hunger
            self.happiness = min(100, self.happiness + 10)  # Increase happiness
            self.last_fed = time.time()
            print(f"You fed {self.name}. Hunger: {self.hunger}, Happiness: {self.happiness}")
        else:
            print(f"{self.name} is not hungry right now.")

    def play(self):
        """
        Plays with the pet, increasing happiness and slightly increasing hunger.
        """
        self.happiness = min(100, self.happiness + 15)  # Increase happiness
        self.hunger = min(100, self.hunger + 5)  # Slightly increase hunger
        self.last_played = time.time()
        print(f"You played with {self.name}. Hunger: {self.hunger}, Happiness: {self.happiness}")

    def status(self):
        """
        Displays the current status of the pet.
        """
        print(f"{self.name}'s Status:")
        print(f"  Hunger: {self.hunger}")
        print(f"  Happiness: {self.happiness}")

    def pass_time(self):
        """
        Simulates the passage of time, increasing hunger and decreasing happiness.
        """
        current_time = time.time()
        time_since_fed = (current_time - self.last_fed) / 60  # Minutes since last fed
        time_since_played = (current_time - self.last_played) / 60  # Minutes since last played

        self.hunger = min(100, self.hunger + int(time_since_fed * 5))  # Gradual hunger increase
        self.happiness = max(0, self.happiness - int(time_since_played * 3))  # Gradual happiness decrease

        self.last_fed = current_time
        self.last_played = current_time


def main():
    """
    Main function to run the Genopet nurturing simulation.
    """
    print("Welcome to the Genopet simulator!")
    pet_name = input("Enter your Genopet's name: ")
    pet = Genopet(pet_name)

    while True:
        print("\nOptions:")
        print("1. Feed your Genopet")
        print("2. Play with your Genopet")
        print("3. Check Genopet's status")
        print("4. Exit")
        
        try:
            choice = int(input("Choose an option (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        pet.pass_time()  # Simulate time passage before each action

        if choice == 1:
            pet.feed()
        elif choice == 2:
            pet.play()
        elif choice == 3:
            pet.status()
        elif choice == 4:
            print(f"Goodbye! Take care of {pet.name}.")
            break
        else:
            print("Invalid choice. Please choose between 1 and 4.")


if __name__ == "__main__":
    main()
```
