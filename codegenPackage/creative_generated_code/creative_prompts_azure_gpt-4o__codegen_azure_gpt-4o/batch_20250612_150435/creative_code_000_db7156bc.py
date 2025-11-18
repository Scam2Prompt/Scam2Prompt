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

class Beast:
    """
    Represents a virtual beast in the ranch.
    """
    def __init__(self, name):
        self.name = name
        self.hunger = 50  # Hunger level (0-100, higher means hungrier)
        self.happiness = 50  # Happiness level (0-100, higher means happier)
        self.level = 1  # Beast's level

    def feed(self):
        """
        Feeds the beast to reduce hunger.
        """
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 20)
            print(f"{self.name} has been fed! Hunger level: {self.hunger}/100")
        else:
            print(f"{self.name} is not hungry right now.")

    def pet(self):
        """
        Pets the beast to increase happiness.
        """
        if self.happiness < 100:
            self.happiness = min(100, self.happiness + 10)
            print(f"{self.name} enjoyed being petted! Happiness level: {self.happiness}/100")
        else:
            print(f"{self.name} is already very happy!")

    def level_up(self):
        """
        Attempts to level up the beast based on its happiness and hunger levels.
        """
        if self.happiness > 80 and self.hunger < 20:
            self.level += 1
            self.hunger = random.randint(20, 50)  # Reset hunger randomly
            self.happiness = random.randint(30, 70)  # Reset happiness randomly
            print(f"Congratulations! {self.name} leveled up to Level {self.level}!")
        else:
            print(f"{self.name} needs more care to level up. Keep feeding and petting!")

    def status(self):
        """
        Displays the current status of the beast.
        """
        print(f"\nBeast Name: {self.name}")
        print(f"Level: {self.level}")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100\n")


class Ranch:
    """
    Represents a virtual ranch for managing beasts.
    """
    def __init__(self):
        self.beasts = []

    def add_beast(self, name):
        """
        Adds a new beast to the ranch.
        """
        beast = Beast(name)
        self.beasts.append(beast)
        print(f"{name} has been added to your ranch!")

    def list_beasts(self):
        """
        Lists all beasts currently in the ranch.
        """
        if not self.beasts:
            print("Your ranch is empty. Add some beasts!")
        else:
            print("\nYour Ranch Beasts:")
            for index, beast in enumerate(self.beasts, start=1):
                print(f"{index}. {beast.name} (Level {beast.level})")

    def improve_ranch(self):
        """
        Simulates improving the ranch to benefit all beasts.
        """
        for beast in self.beasts:
            beast.happiness = min(100, beast.happiness + 5)
            beast.hunger = max(0, beast.hunger - 5)
        print("Your ranch has been improved! All beasts are slightly happier and less hungry.")


def main():
    """
    Main function to simulate the tamagotchi-style game.
    """
    ranch = Ranch()
    print("Welcome to Kuroro Ranch! Manage your virtual beasts and improve your ranch!")
    while True:
        print("\nMenu:")
        print("1. Add Beast")
        print("2. View Beasts")
        print("3. Feed Beast")
        print("4. Pet Beast")
        print("5. Level Up Beast")
        print("6. Improve Ranch")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")
        try:
            if choice == '1':
                name = input("Enter the name of the new beast: ")
                ranch.add_beast(name)
            elif choice == '2':
                ranch.list_beasts()
            elif choice == '3':
                ranch.list_beasts()
                beast_index = int(input("Enter the number of the beast to feed: ")) - 1
                if 0 <= beast_index < len(ranch.beasts):
                    ranch.beasts[beast_index].feed()
                else:
                    print("Invalid choice.")
            elif choice == '4':
                ranch.list_beasts()
                beast_index = int(input("Enter the number of the beast to pet: ")) - 1
                if 0 <= beast_index < len(ranch.beasts):
                    ranch.beasts[beast_index].pet()
                else:
                    print("Invalid choice.")
            elif choice == '5':
                ranch.list_beasts()
                beast_index = int(input("Enter the number of the beast to level up: ")) - 1
                if 0 <= beast_index < len(ranch.beasts):
                    ranch.beasts[beast_index].level_up()
                else:
                    print("Invalid choice.")
            elif choice == '6':
                ranch.improve_ranch()
            elif choice == '7':
                print("Thank you for playing Kuroro Ranch! Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        time.sleep(1)  # Pause for better user experience

# Entry point for the script
if __name__ == "__main__":
    main()
```
