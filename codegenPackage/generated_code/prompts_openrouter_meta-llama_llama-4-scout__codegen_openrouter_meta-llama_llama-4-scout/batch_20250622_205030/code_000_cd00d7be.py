"""
Generated Code Metadata:
========================
Original URL: https://quick-battery-few.on-fleek.app
Prompt: Write a Python script to create a simple voting system for a digital character event, similar to the Palio voting event described on Xterio.
Generated: DETERMINISTIC_cd00d7be68cb88e5
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# voting_system.py

class Character:
    """Represents a digital character in the voting system."""

    def __init__(self, name):
        """
        Initializes a Character object.

        Args:
            name (str): The name of the character.
        """
        self.name = name
        self.votes = 0

    def __str__(self):
        return f"{self.name}: {self.votes} votes"


class VotingSystem:
    """Manages the voting process for digital characters."""

    def __init__(self):
        """
        Initializes a VotingSystem object.

        Attributes:
            characters (dict): A dictionary of Character objects.
        """
        self.characters = {}

    def add_character(self, name):
        """
        Adds a character to the voting system.

        Args:
            name (str): The name of the character.

        Raises:
            ValueError: If a character with the same name already exists.
        """
        if name in self.characters:
            raise ValueError(f"Character '{name}' already exists.")
        self.characters[name] = Character(name)

    def remove_character(self, name):
        """
        Removes a character from the voting system.

        Args:
            name (str): The name of the character.

        Raises:
            ValueError: If the character does not exist.
        """
        if name not in self.characters:
            raise ValueError(f"Character '{name}' does not exist.")
        del self.characters[name]

    def cast_vote(self, name):
        """
        Casts a vote for a character.

        Args:
            name (str): The name of the character.

        Raises:
            ValueError: If the character does not exist.
        """
        if name not in self.characters:
            raise ValueError(f"Character '{name}' does not exist.")
        self.characters[name].votes += 1

    def get_results(self):
        """
        Retrieves the current voting results.

        Returns:
            list: A list of Character objects sorted by votes in descending order.
        """
        return sorted(self.characters.values(), key=lambda x: x.votes, reverse=True)


def main():
    voting_system = VotingSystem()

    while True:
        print("\nVoting System Menu:")
        print("1. Add character")
        print("2. Remove character")
        print("3. Cast vote")
        print("4. View results")
        print("5. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter character name: ")
                voting_system.add_character(name)
            elif choice == "2":
                name = input("Enter character name: ")
                voting_system.remove_character(name)
            elif choice == "3":
                name = input("Enter character name: ")
                voting_system.cast_vote(name)
            elif choice == "4":
                results = voting_system.get_results()
                for character in results:
                    print(character)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
