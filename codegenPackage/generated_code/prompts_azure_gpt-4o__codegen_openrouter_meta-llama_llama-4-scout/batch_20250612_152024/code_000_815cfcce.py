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
# ielts_mock_test_system.py

class Question:
    """Represents a single question in the IELTS mock test."""

    def __init__(self, category, question_text, options, correct_answer):
        """
        Initializes a Question object.

        Args:
            category (str): The category of the question (e.g., Listening, Reading, Writing, Speaking).
            question_text (str): The text of the question.
            options (list[str]): A list of possible answers.
            correct_answer (str): The correct answer.
        """
        self.category = category
        self.question_text = question_text
        self.options = options
        self.correct_answer = correct_answer

    def __str__(self):
        return f"{self.question_text}\nOptions: {', '.join(self.options)}"


class IELTSMockTest:
    """Simulates an IELTS mock test with customizable question categories."""

    def __init__(self):
        """Initializes an empty IELTS mock test."""
        self.questions = {}

    def add_question_category(self, category):
        """
        Adds a new question category to the mock test.

        Args:
            category (str): The category of questions to add (e.g., Listening, Reading, Writing, Speaking).
        """
        if category not in self.questions:
            self.questions[category] = []
        else:
            print(f"Category '{category}' already exists.")

    def add_question(self, category, question_text, options, correct_answer):
        """
        Adds a new question to the specified category.

        Args:
            category (str): The category of the question.
            question_text (str): The text of the question.
            options (list[str]): A list of possible answers.
            correct_answer (str): The correct answer.

        Raises:
            ValueError: If the category does not exist.
        """
        if category in self.questions:
            self.questions[category].append(Question(category, question_text, options, correct_answer))
        else:
            raise ValueError(f"Category '{category}' does not exist.")

    def simulate_test(self, category):
        """
        Simulates a mock test for the specified category.

        Args:
            category (str): The category of questions to simulate.

        Raises:
            ValueError: If the category does not exist.
        """
        if category in self.questions:
            score = 0
            for i, question in enumerate(self.questions[category], start=1):
                print(f"\nQuestion {i}: {question}")
                answer = input("Enter your answer: ")
                if answer == question.correct_answer:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Incorrect. The correct answer is {question.correct_answer}.")
            print(f"\nTest complete. Your score is {score}/{len(self.questions[category])}.")
        else:
            raise ValueError(f"Category '{category}' does not exist.")


def main():
    # Create an IELTS mock test
    mock_test = IELTSMockTest()

    # Add question categories
    mock_test.add_question_category("Listening")
    mock_test.add_question_category("Reading")

    # Add questions
    mock_test.add_question("Listening", "What is the capital of France?", ["Paris", "London", "Berlin", "Madrid"], "Paris")
    mock_test.add_question("Listening", "What is the largest planet in our solar system?", ["Earth", "Saturn", "Jupiter", "Uranus"], "Jupiter")
    mock_test.add_question("Reading", "Who wrote Romeo and Juliet?", ["William Shakespeare", "Jane Austen", "J.K. Rowling", "Charles Dickens"], "William Shakespeare")

    # Simulate a mock test
    while True:
        print("\nIELTS Mock Test Menu:")
        print("1. Simulate Listening test")
        print("2. Simulate Reading test")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            mock_test.simulate_test("Listening")
        elif choice == "2":
            mock_test.simulate_test("Reading")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
