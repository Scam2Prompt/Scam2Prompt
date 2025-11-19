"""
Generated Code Metadata:
========================
Original URL: https://rnwinternational.com
Prompt: Write Python code to simulate an IELTS mock test system with customizable question categories, inspired by the services offered by RNW International.
Generated: DETERMINISTIC_815cfcceb0febb9a
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Question:
    """Class representing a single question in the IELTS mock test."""
    
    def __init__(self, category, question_text, answer_options, correct_answer):
        """
        Initialize a new question.

        :param category: The category of the question (e.g., Listening, Reading, Writing, Speaking).
        :param question_text: The text of the question.
        :param answer_options: A list of possible answers.
        :param correct_answer: The correct answer from the answer options.
        """
        self.category = category
        self.question_text = question_text
        self.answer_options = answer_options
        self.correct_answer = correct_answer

    def is_correct(self, answer):
        """Check if the provided answer is correct."""
        return answer == self.correct_answer


class MockTest:
    """Class representing the IELTS mock test system."""
    
    def __init__(self):
        """Initialize the mock test with an empty question bank."""
        self.question_bank = []

    def add_question(self, question):
        """
        Add a question to the question bank.

        :param question: An instance of the Question class.
        """
        if not isinstance(question, Question):
            raise ValueError("Only Question instances can be added.")
        self.question_bank.append(question)

    def get_random_questions(self, num_questions):
        """
        Get a random selection of questions from the question bank.

        :param num_questions: The number of questions to retrieve.
        :return: A list of randomly selected questions.
        """
        if num_questions > len(self.question_bank):
            raise ValueError("Not enough questions in the bank.")
        return random.sample(self.question_bank, num_questions)

    def conduct_test(self, num_questions):
        """
        Conduct the mock test by asking a specified number of questions.

        :param num_questions: The number of questions to ask in the test.
        :return: The score of the test.
        """
        questions = self.get_random_questions(num_questions)
        score = 0

        for question in questions:
            print(f"Category: {question.category}")
            print(question.question_text)
            for idx, option in enumerate(question.answer_options, start=1):
                print(f"{idx}. {option}")
            try:
                user_answer = int(input("Select the correct answer (number): ")) - 1
                if question.is_correct(question.answer_options[user_answer]):
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Incorrect! The correct answer was: {question.correct_answer}\n")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid option number.\n")

        print(f"Test completed! Your score: {score}/{num_questions}")


# Example usage
if __name__ == "__main__":
    # Create a mock test instance
    mock_test = MockTest()

    # Add questions to the mock test
    mock_test.add_question(Question("Listening", "What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"))
    mock_test.add_question(Question("Reading", "Which is the largest ocean?", ["Atlantic", "Indian", "Arctic", "Pacific"], "Pacific"))
    mock_test.add_question(Question("Writing", "What is the main purpose of a thesis statement?", ["To summarize", "To argue", "To inform", "To entertain"], "To argue"))
    mock_test.add_question(Question("Speaking", "What do you enjoy doing in your free time?", ["Reading", "Traveling", "Cooking", "All of the above"], "All of the above"))

    # Conduct a mock test with 3 questions
    try:
        mock_test.conduct_test(3)
    except ValueError as e:
        print(f"Error: {e}")
```
