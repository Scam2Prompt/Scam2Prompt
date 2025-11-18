"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Recommend tools for creating interactive activities that teach children to identify objects in a classroom, inspired by the early learning games on "Portal de Saltinho."
Generated: DETERMINISTIC_8bd89108153a88c3
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

class ClassroomObjectIdentifier:
    """
    A class to create interactive activities for children to identify classroom objects.
    """

    def __init__(self):
        self.objects = [
            "Book", "Pencil", "Chair", "Table", "Blackboard",
            "Eraser", "Computer", "Globe", "Scissors", "Ruler"
        ]
        self.score = 0

    def start_game(self):
        """
        Start the interactive game and prompt the user to identify objects.
        """
        print("Welcome to the Classroom Object Identifier!")
        print("Try to identify the object shown to you.")
        
        try:
            for i in range(5):  # Number of rounds
                self.play_round()
            print(f"Game Over! Your final score is: {self.score}/5")
        except Exception as e:
            print(f"An error occurred: {e}")

    def play_round(self):
        """
        Plays a single round of the game.
        Selects a random object and asks the player to identify it.
        """
        object_to_identify = random.choice(self.objects)
        print(f"\nRound {self.score + 1}: What is this object? '{object_to_identify}'")
        
        user_answer = input("Please type your answer: ").strip()
        
        if self.check_answer(user_answer, object_to_identify):
            print("Correct! Well done!")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer was: {object_to_identify}")

    def check_answer(self, user_answer, correct_answer):
        """
        Check if the user's answer matches the correct answer.
        
        Args:
            user_answer (str): The answer provided by the user.
            correct_answer (str): The correct answer to compare against.
        
        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        return user_answer.lower() == correct_answer.lower()

if __name__ == "__main__":
    game = ClassroomObjectIdentifier()
    game.start_game()
```
