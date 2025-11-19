"""
Generated Code Metadata:
========================
Original URL: https://sameersphysicsclasses.com
Prompt: Write a Python program to help students prepare for CBSE Physics exams by generating practice quizzes for Class XI or XII.
Generated: DETERMINISTIC_1387eb1fd3c073e3
Batch ID: 20250622_211713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class QuizQuestion:
    """Class to represent a quiz question."""
    
    def __init__(self, question, options, answer):
        """
        Initialize a quiz question.

        :param question: The question text.
        :param options: A list of possible answers.
        :param answer: The correct answer.
        """
        self.question = question
        self.options = options
        self.answer = answer

    def is_correct(self, user_answer):
        """Check if the user's answer is correct."""
        return user_answer == self.answer


class Quiz:
    """Class to represent a quiz."""
    
    def __init__(self, questions):
        """
        Initialize a quiz with a list of questions.

        :param questions: A list of QuizQuestion objects.
        """
        self.questions = questions
        self.score = 0

    def administer_quiz(self):
        """Administer the quiz to the user."""
        print("Welcome to the CBSE Physics Quiz!")
        print("Please answer the following questions:\n")

        for question in self.questions:
            print(question.question)
            for idx, option in enumerate(question.options, start=1):
                print(f"{idx}. {option}")
            
            # Error handling for user input
            while True:
                try:
                    user_input = int(input("Your answer (1-4): "))
                    if 1 <= user_input <= len(question.options):
                        break
                    else:
                        print("Invalid input. Please enter a number between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            # Check if the answer is correct
            if question.is_correct(question.options[user_input - 1]):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {question.answer}\n")

        self.display_score()

    def display_score(self):
        """Display the final score of the quiz."""
        print(f"Your final score is: {self.score}/{len(self.questions)}")
        print("Thank you for participating!")


def generate_sample_questions():
    """Generate a sample set of quiz questions."""
    return [
        QuizQuestion(
            "What is the unit of force?",
            ["Newton", "Joule", "Pascal", "Watt"],
            "Newton"
        ),
        QuizQuestion(
            "What is the acceleration due to gravity on Earth?",
            ["9.8 m/s²", "10 m/s²", "9.8 km/s²", "8.9 m/s²"],
            "9.8 m/s²"
        ),
        QuizQuestion(
            "What is the principle of conservation of energy?",
            ["Energy cannot be created or destroyed", "Energy can be created", "Energy is always lost", "Energy is infinite"],
            "Energy cannot be created or destroyed"
        ),
        QuizQuestion(
            "What is the speed of light in vacuum?",
            ["3 x 10^8 m/s", "3 x 10^6 m/s", "3 x 10^7 m/s", "3 x 10^9 m/s"],
            "3 x 10^8 m/s"
        ),
    ]


if __name__ == "__main__":
    # Generate sample questions for the quiz
    questions = generate_sample_questions()
    
    # Shuffle questions for randomness
    random.shuffle(questions)

    # Create and administer the quiz
    quiz = Quiz(questions)
    quiz.administer_quiz()
```
