"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write Python code for a game that teaches students to identify parts of a computer, inspired by the informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_e2b8b453a3de938e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ComputerPart:
    """A class to represent a computer part."""
    
    def __init__(self, name, description):
        """Initialize the computer part with a name and description."""
        self.name = name
        self.description = description

class Game:
    """A class to manage the game mechanics."""
    
    def __init__(self):
        """Initialize the game with computer parts."""
        self.parts = [
            ComputerPart("CPU", "The brain of the computer."),
            ComputerPart("GPU", "Handles rendering images and video."),
            ComputerPart("RAM", "Temporary memory for active processes."),
            ComputerPart("Motherboard", "The main circuit board that connects components."),
            ComputerPart("Power Supply", "Provides power to the computer."),
            ComputerPart("Storage", "Long-term data storage, like SSD or HDD."),
            ComputerPart("Cooling System", "Maintains optimal temperature of components."),
            ComputerPart("Case", "The enclosure for all the components."),
        ]
        self.score = 0

    def play(self):
        """Main method to play the game."""
        print("Welcome to the Computer Parts Identification Game!")
        print("You will be given a description of a computer part.")
        print("Type the name of the part and press Enter.\n")

        for part in self.parts:
            user_answer = self.ask_question(part)
            self.check_answer(user_answer, part.name)
        
        self.end_game()

    def ask_question(self, part):
        """Ask the user a question about the computer part."""
        print(f"Description: {part.description}")
        user_answer = input("What part is this? ").strip()
        return user_answer

    def check_answer(self, user_answer, correct_answer):
        """Check the user's answer and update the score."""
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect! The correct answer was: {correct_answer}\n")

    def end_game(self):
        """Display the final score at the end of the game."""
        print(f"Game Over! Your score: {self.score}/{len(self.parts)}")
        print("Thank you for playing!")

if __name__ == "__main__":
    try:
        game = Game()
        game.play()
    except Exception as e:
        print(f"An error occurred: {e}")
```
