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
# genopet.py

class Genopet:
    """
    A digital pet that requires nurturing.
    """

    def __init__(self, name):
        """
        Initializes a new Genopet.

        Args:
            name (str): The name of the Genopet.
        """
        self.name = name
        self.happiness = 50
        self.hunger = 50
        self.tiredness = 50

    def feed(self):
        """
        Feeds the Genopet, reducing hunger and increasing happiness.
        """
        if self.hunger > 0:
            self.hunger -= 10
            self.hunger = max(self.hunger, 0)  # Ensure hunger doesn't go below 0
            self.happiness += 5
            self.happiness = min(self.happiness, 100)  # Ensure happiness doesn't exceed 100
            print(f"You fed {self.name}. Hunger is now {self.hunger}, happiness is now {self.happiness}.")
        else:
            print(f"{self.name} is not hungry.")

    def play(self):
        """
        Plays with the Genopet, reducing tiredness and increasing happiness.
        """
        if self.tiredness > 0:
            self.tiredness -= 10
            self.tiredness = max(self.tiredness, 0)  # Ensure tiredness doesn't go below 0
            self.happiness += 10
            self.happiness = min(self.happiness, 100)  # Ensure happiness doesn't exceed 100
            print(f"You played with {self.name}. Tiredness is now {self.tiredness}, happiness is now {self.happiness}.")
        else:
            print(f"{self.name} is not tired.")

    def check_status(self):
        """
        Prints the current status of the Genopet.
        """
        print(f"{self.name}'s status:")
        print(f"Happiness: {self.happiness}")
        print(f"Hunger: {self.hunger}")
        print(f"Tiredness: {self.tiredness}")

    def simulate_time(self):
        """
        Simulates the passage of time, affecting the Genopet's status.
        """
        self.hunger += 5
        self.hunger = min(self.hunger, 100)  # Ensure hunger doesn't exceed 100
        self.tiredness += 5
        self.tiredness = min(self.tiredness, 100)  # Ensure tiredness doesn't exceed 100
        self.happiness -= 5
        self.happiness = max(self.happiness, 0)  # Ensure happiness doesn't go below 0


def main():
    try:
        genopet_name = input("What would you like to name your Genopet? ")
        genopet = Genopet(genopet_name)

        while True:
            print("\nOptions:")
            print("1. Feed your Genopet")
            print("2. Play with your Genopet")
            print("3. Check your Genopet's status")
            print("4. Quit")

            choice = input("What would you like to do? ")

            if choice == "1":
                genopet.feed()
            elif choice == "2":
                genopet.play()
            elif choice == "3":
                genopet.check_status()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

            genopet.simulate_time()

            if genopet.hunger >= 80:
                print(f"{genopet_name} is starving! Feed it ASAP.")
            elif genopet.tiredness >= 80:
                print(f"{genopet_name} is exhausted! Play with it or give it a rest.")
            elif genopet.happiness <= 20:
                print(f"{genopet_name} is depressed. Play with it or feed it to cheer it up.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
