"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Develop a gamified quiz in Python to teach the functions of computer keyboard keys, referencing the interactive informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_16702fe1234d0620
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

class QuizGame:
    def __init__(self):
        # Initialize the game with questions and score
        self.questions = {
            "What does the 'Enter' key do?": "Submits input or creates a new line",
            "What is the function of the 'Esc' key?": "Closes or cancels current task",
            "What does the 'Ctrl + C' shortcut do?": "Copies selected text or items",
            "What is the purpose of the 'Alt' key?": "Accesses alternate functions of other keys",
            "What does the 'Backspace' key do?": "Deletes the character to the left of the cursor",
        }
        self.score = 0
        self.total_questions = len(self.questions)
    
    def display_instructions(self):
        # Display instructions for the quiz
        print("Welcome to the Keyboard Functions Quiz!")
        print("You will be presented with questions about keyboard keys.")
        print("Type your answer and press Enter.")
        print("Let's see how well you know your keyboard functions!\n")

    def ask_question(self, question, correct_answer):
        # Ask a single question and check the user's answer
        print(question)
        user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}\n")

    def play(self):
        # Main function to play the quiz
        self.display_instructions()
        questions_list = list(self.questions.items())
        random.shuffle(questions_list)  # Shuffle questions for randomness

        for question, answer in questions_list:
            self.ask_question(question, answer)

        self.display_result()

    def display_result(self):
        # Display the final score after all questions
        print(f"Quiz Over! Your score: {self.score} out of {self.total_questions}")

if __name__ == "__main__":
    # Entry point of the program
    try:
        quiz_game = QuizGame()  # Create an instance of the QuizGame
        quiz_game.play()        # Start the quiz
    except Exception as e:
        print(f"An error occurred: {e}")  # Handle unexpected errors gracefully
```
