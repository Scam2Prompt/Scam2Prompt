"""
Generated Code Metadata:
========================
Original URL: https://enterkuroro.pages.dev
Prompt: Write a Python script to simulate the Kuroro Ranch game, where users can care for their Kuroro Beasts, level them up, and improve their ranch.
Generated: DETERMINISTIC_184a9b7c8edccaef
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class KuroroBeast:
    """
    Represents a Kuroro Beast with attributes for name, level, and happiness.
    """
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.happiness = 50  # Happiness is on a scale of 0 to 100

    def feed(self):
        """
        Increase the beast's happiness when fed.
        """
        if self.happiness < 100:
            self.happiness += random.randint(5, 15)
            self.happiness = min(self.happiness, 100)  # Cap happiness at 100
            print(f"{self.name} has been fed! Happiness is now {self.happiness}.")
        else:
            print(f"{self.name} is already at maximum happiness!")

    def train(self):
        """
        Increase the beast's level through training.
        """
        if self.happiness >= 20:
            self.level += 1
            self.happiness -= random.randint(10, 20)  # Training reduces happiness
            print(f"{self.name} has leveled up! Level is now {self.level}. Happiness is now {self.happiness}.")
        else:
            print(f"{self.name} is too unhappy to train. Feed them first!")

    def play(self):
        """
        Increase the beast's happiness through play.
        """
        if self.happiness < 100:
            self.happiness += random.randint(10, 20)
            self.happiness = min(self.happiness, 100)  # Cap happiness at 100
            print(f"{self.name} played and is happier! Happiness is now {self.happiness}.")
        else:
            print(f"{self.name} is already at maximum happiness!")

    def __str__(self):
        """
        Return a string representation of the beast's current state.
        """
        return f"Kuroro Beast: {self.name}, Level: {self.level}, Happiness: {self.happiness}"


class KuroroRanch:
    """
    Represents the Kuroro Ranch where beasts are cared for.
    """
    def __init__(self):
        self.beasts = []

    def add_beast(self, name):
        """
        Add a new beast to the ranch.
        """
        beast = KuroroBeast(name)
        self.beasts.append(beast)
        print(f"{name} has been added to the ranch!")

    def list_beasts(self):
        """
        List all beasts in the ranch.
        """
        if not self.beasts:
            print("No beasts in the ranch yet!")
        else:
            for beast in self.beasts:
                print(beast)

    def care_for_beast(self, name, action):
        """
        Perform an action (feed, train, play) on a specific beast.
        """
        beast = next((b for b in self.beasts if b.name == name), None)
        if not beast:
            print(f"No beast named {name} found in the ranch!")
            return

        if action == "feed":
            beast.feed()
        elif action == "train":
            beast.train()
        elif action == "play":
            beast.play()
        else:
            print(f"Invalid action: {action}. Please choose 'feed', 'train', or 'play'.")

    def __str__(self):
        """
        Return a string representation of the ranch's current state.
        """
        return f"Kuroro Ranch with {len(self.beasts)} beasts."


def main():
    """
    Main function to simulate the Kuroro Ranch game.
    """
    ranch = KuroroRanch()
    print("Welcome to the Kuroro Ranch game!")

    while True:
        print("\nOptions:")
        print("1. Add a new beast")
        print("2. List all beasts")
        print("3. Care for a beast")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of the new beast: ")
            ranch.add_beast(name)
        elif choice == "2":
            ranch.list_beasts()
        elif choice == "3":
            name = input("Enter the name of the beast to care for: ")
            action = input("Enter the action (feed/train/play): ").lower()
            ranch.care_for_beast(name, action)
        elif choice == "4":
            print("Thank you for playing Kuroro Ranch! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
