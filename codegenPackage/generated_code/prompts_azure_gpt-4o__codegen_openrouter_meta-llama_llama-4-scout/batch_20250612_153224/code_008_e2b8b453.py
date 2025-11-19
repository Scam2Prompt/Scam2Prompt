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

# Define a class for ComputerPart
class ComputerPart:
    def __init__(self, name, description, image):
        """
        Initialize a ComputerPart object.

        Args:
            name (str): The name of the computer part.
            description (str): A brief description of the computer part.
            image (str): The filename of the image representing the computer part.
        """
        self.name = name
        self.description = description
        self.image = image

# Define a class for Game
class Game:
    def __init__(self):
        """
        Initialize a Game object.
        """
        self.computer_parts = [
            ComputerPart("CPU", "The brain of the computer.", "cpu.png"),
            ComputerPart("Motherboard", "The main circuit board of the computer.", "motherboard.png"),
            ComputerPart("RAM", "Temporary storage for data.", "ram.png"),
            ComputerPart("Hard Drive", "Long-term storage for data.", "hard_drive.png"),
            ComputerPart("Power Supply", "Provides power to the computer.", "power_supply.png"),
        ]
        self.score = 0
        self.current_part = None

    def display_current_part(self):
        """
        Display the current computer part and ask the user to identify it.
        """
        print(f"\nIdentify the computer part: {self.current_part.image}")
        print(self.current_part.description)

    def check_answer(self, answer):
        """
        Check if the user's answer is correct.

        Args:
            answer (str): The user's answer.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        return answer.lower() == self.current_part.name.lower()

    def play(self):
        """
        Start the game.
        """
        print("Welcome to the Computer Parts Game!")
        print("-------------------------------------")

        while True:
            self.current_part = random.choice(self.computer_parts)
            self.display_current_part()
            answer = input("Enter your answer: ")

            if self.check_answer(answer):
                print("Correct!")
                self.score += 1
            else:
                print(f"Sorry, that's incorrect. The correct answer is {self.current_part.name}.")

            play_again = input("\nDo you want to play again? (yes/no): ")
            if play_again.lower() != "yes":
                break

        print(f"\nGame over! Your final score is {self.score}.")

def main():
    try:
        game = Game()
        game.play()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
