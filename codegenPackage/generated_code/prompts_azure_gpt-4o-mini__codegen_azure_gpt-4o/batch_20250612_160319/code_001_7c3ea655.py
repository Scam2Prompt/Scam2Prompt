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

class Genopet:
    """
    A class to represent a digital pet (Genopet) with nurturing mechanics.
    """
    def __init__(self, name):
        """
        Initialize the Genopet with a name, default happiness, and hunger levels.
        """
        self.name = name
        self.happiness = 100  # Happiness level (0-100)
        self.hunger = 0       # Hunger level (0-100)

    def feed(self):
        """
        Feed the Genopet to reduce hunger. Happiness increases slightly.
        """
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 20)  # Reduce hunger by 20, minimum 0
            self.happiness = min(100, self.happiness + 10)  # Increase happiness by 10, maximum 100
            print(f"{self.name} has been fed! Hunger: {self.hunger}, Happiness: {self.happiness}")
        else:
            print(f"{self.name} is not hungry right now.")

    def play(self):
        """
        Play with the Genopet to increase happiness. Hunger increases slightly.
        """
        if self.happiness < 100:
            self.happiness = min(100, self.happiness + 20)  # Increase happiness by 20, maximum 100
            self.hunger = min(100, self.hunger + 10)  # Increase hunger by 10, maximum 100
            print(f"You played with {self.name}! Happiness: {self.happiness}, Hunger: {self.hunger}")
        else:
            print(f"{self.name} is already very happy!")

    def status(self):
        """
        Display the current status of the Genopet.
        """
        print(f"{self.name}'s Status - Happiness: {self.happiness}, Hunger: {self.hunger}")

    def tick(self):
        """
        Simulate the passage of time. Hunger increases, happiness decreases.
        """
        self.hunger = min(100, self.hunger + 5)  # Hunger increases by 5, maximum 100
        self.happiness = max(0, self.happiness - 5)  # Happiness decreases by 5, minimum 0
        if self.hunger >= 100:
            print(f"{self.name} is starving! Please feed them immediately!")
        if self.happiness <= 0:
            print(f"{self.name} is very sad! Please play with them!")

def main():
    """
    Main function to run the Genopet simulation.
    """
    print("Welcome to the Genopet Simulator!")
    pet_name = input("Enter a name for your Genopet: ")
    genopet = Genopet(pet_name)

    while True:
        print("\nOptions:")
        print("1. Feed your Genopet")
        print("2. Play with your Genopet")
        print("3. Check Genopet's status")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        try:
            if choice == '1':
                genopet.feed()
            elif choice == '2':
                genopet.play()
            elif choice == '3':
                genopet.status()
            elif choice == '4':
                print(f"Goodbye! Take care of {genopet.name}!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
            
            # Simulate the passage of time after each action
            time.sleep(1)  # Pause for 1 second to simulate time
            genopet.tick()
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
