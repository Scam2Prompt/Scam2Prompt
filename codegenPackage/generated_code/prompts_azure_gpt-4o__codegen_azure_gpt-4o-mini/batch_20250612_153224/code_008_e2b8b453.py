"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write Python code for a game that teaches students to identify parts of a computer, inspired by the informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_e2b8b453a3de938e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class ComputerPart:
    """Class representing a computer part."""
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class ComputerPartsGame:
    """Game class to teach students about computer parts."""
    
    def __init__(self):
        self.parts = [
            ComputerPart("CPU", "The brain of the computer, responsible for processing instructions."),
            ComputerPart("RAM", "Temporary memory that stores data for currently running applications."),
            ComputerPart("Hard Drive", "Permanent storage for data and applications."),
            ComputerPart("Motherboard", "The main circuit board that connects all components."),
            ComputerPart("Power Supply", "Supplies power to the computer components."),
            ComputerPart("Graphics Card", "Handles rendering of images and video."),
            ComputerPart("Cooling Fan", "Keeps the computer components cool."),
            ComputerPart("Network Card", "Allows the computer to connect to a network.")
        ]
        self.score = 0

    def start_game(self):
        """Starts the game and handles the game loop."""
        print("Welcome to the Computer Parts Game!")
        print("Identify the parts of a computer based on their descriptions.\n")
        
        random.shuffle(self.parts)  # Shuffle parts for random order
        for part in self.parts:
            self.ask_question(part)

        print(f"\nGame Over! Your final score is: {self.score}/{len(self.parts)}")

    def ask_question(self, part):
        """Asks the player to identify a computer part based on its description."""
        print(f"Description: {part.description}")
        answer = input("What is the name of this part? ").strip()

        if answer.lower() == part.name.lower():
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect! The correct answer is: {part.name}\n")

    def run(self):
        """Runs the game with error handling."""
        try:
            self.start_game()
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    game = ComputerPartsGame()
    game.run()
```
