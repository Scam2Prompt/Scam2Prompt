"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Generate Python code for a gamified quiz on the history and evolution of the internet, inspired by the informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_3f85e9b192661248
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
        """Initialize the quiz game with questions and scores."""
        self.questions = [
            {
                "question": "What year was the first message sent over ARPANET, the precursor to the modern internet?",
                "options": ["1969", "1972", "1983", "1991"],
                "answer": "1969"
            },
            {
                "question": "Who is credited with inventing the World Wide Web?",
                "options": ["Tim Berners-Lee", "Vint Cerf", "Robert Kahn", "Marc Andreessen"],
                "answer": "Tim Berners-Lee"
            },
            {
                "question": "Which protocol is the foundation of data communication on the internet?",
                "options": ["HTTP", "FTP", "TCP/IP", "SMTP"],
                "answer": "TCP/IP"
            },
            {
                "question": "What does 'URL' stand for?",
                "options": ["Universal Resource Locator", "Uniform Resource Locator", "Unified Resource Link", "User Resource Link"],
                "answer": "Uniform Resource Locator"
            },
            {
                "question": "Which social media platform was launched in 2004 and revolutionized online networking?",
                "options": ["Facebook", "Twitter", "LinkedIn", "Instagram"],
                "answer": "Facebook"
            }
        ]
        self.score = 0

    def shuffle_questions(self):
        """Shuffle the order of the questions to add randomness."""
        random.shuffle(self.questions)

    def ask_question(self, question_data):
        """
        Ask a single question to the player and validate their answer.

        :param question_data: Dictionary containing question, options, and answer.
        :return: True if the player's answer is correct, False otherwise.
        """
        print("\n" + question_data["question"])
        for i, option in enumerate(question_data["options"], start=1):
            print(f"{i}. {option}")

        try:
            user_choice = int(input("Enter the number of your choice: "))
            if user_choice < 1 or user_choice > len(question_data["options"]):
                print("Invalid choice. Please try again.")
                return False

            selected_option = question_data["options"][user_choice - 1]
            if selected_option == question_data["answer"]:
                print("Correct!")
                return True
            else:
                print(f"Wrong! The correct answer was: {question_data['answer']}")
                return False
        except ValueError:
            print("Invalid input. Please enter a number corresponding to your choice.")
            return False

    def play(self):
        """Start the quiz game and display the final score."""
        print("Welcome to the History and Evolution of the Internet Quiz!")
        print("Answer the following questions by selecting the number corresponding to your choice.")
        print("Let's see how much you know about the internet!\n")

        self.shuffle_questions()

        for question in self.questions:
            if self.ask_question(question):
                self.score += 1

        print(f"\nQuiz complete! Your final score: {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("Excellent! You are a true internet history expert!")
        elif self.score >= len(self.questions) // 2:
            print("Good job! You know quite a bit about the internet!")
        else:
            print("Keep learning! The history of the internet is fascinating!")

if __name__ == "__main__":
    try:
        quiz_game = QuizGame()
        quiz_game.play()
    except Exception as e:
        print(f"An error occurred: {e}")
```
