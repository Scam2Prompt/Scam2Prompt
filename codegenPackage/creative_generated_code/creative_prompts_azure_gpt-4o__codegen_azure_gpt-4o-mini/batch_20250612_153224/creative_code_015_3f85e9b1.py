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

class QuizQuestion:
    """
    A class to represent a quiz question.
    """
    def __init__(self, question: str, options: list, answer: str):
        """
        Initializes a new QuizQuestion instance.

        :param question: The quiz question.
        :param options: A list of answer options.
        :param answer: The correct answer to the question.
        """
        self.question = question
        self.options = options
        self.answer = answer

    def is_correct(self, response: str) -> bool:
        """
        Check if the provided response is correct.

        :param response: The user's answer.
        :return: True if the answer is correct, otherwise False.
        """
        return response.lower() == self.answer.lower()

class Quiz:
    """
    A class to represent the quiz game.
    """
    def __init__(self):
        """
        Initializes a new Quiz instance.
        """
        self.questions = []
        self.score = 0

    def add_question(self, question: QuizQuestion):
        """
        Adds a quiz question to the quiz.

        :param question: An instance of QuizQuestion to add.
        """
        self.questions.append(question)

    def conduct_quiz(self):
        """
        Conducts the quiz, asking each question and getting user responses.
        """
        print("Welcome to the History and Evolution of the Internet Quiz!")
        print("Please answer the following questions:\n")

        for idx, question in enumerate(self.questions):
            print(f"Q{idx + 1}: {question.question}")
            for option in question.options:
                print(f"- {option}")

            response = input("Your answer: ")
            if question.is_correct(response):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {question.answer}\n")

        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")

def main():
    """
    Main function to set up and run the quiz.
    """
    try:
        quiz = Quiz()

        # Adding questions about the history and evolution of the internet
        quiz.add_question(QuizQuestion(
            "What year was the World Wide Web introduced?",
            ["1989", "1991", "1993", "1995"],
            "1991"
        ))

        quiz.add_question(QuizQuestion(
            "Who is known as the father of the internet?",
            ["Tim Berners-Lee", "Vint Cerf", "Bill Gates", "Mark Zuckerberg"],
            "Vint Cerf"
        ))

        quiz.add_question(QuizQuestion(
            "What does 'HTTP' stand for?",
            ["HyperText Transfer Protocol", "HyperText Transport Protocol", "HighText Transfer Protocol", "None of the above"],
            "HyperText Transfer Protocol"
        ))

        quiz.add_question(QuizQuestion(
            "Which company developed the first web browser?",
            ["Microsoft", "Netscape", "Google", "Apple"],
            "Netscape"
        ))

        quiz.add_question(QuizQuestion(
            "In what year did Facebook launch?",
            ["2002", "2004", "2006", "2008"],
            "2004"
        ))

        # Conduct the quiz
        quiz.conduct_quiz()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
