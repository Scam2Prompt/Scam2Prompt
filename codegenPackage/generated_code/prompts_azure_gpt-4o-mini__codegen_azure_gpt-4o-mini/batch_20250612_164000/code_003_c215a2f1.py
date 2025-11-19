"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Develop a code snippet that simulates a test series for UPSC aspirants, focusing on General Studies and CSAT, as outlined in the Shield IAS course offerings.
Generated: DETERMINISTIC_c215a2f16da8e8e6
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json

class TestSeries:
    def __init__(self, subject):
        """
        Initializes the TestSeries with a specific subject.
        
        :param subject: str - The subject for the test series (General Studies or CSAT)
        """
        self.subject = subject
        self.questions = self.load_questions()
        self.score = 0

    def load_questions(self):
        """
        Loads questions from a JSON file based on the subject.
        
        :return: list - A list of questions for the specified subject
        """
        try:
            with open(f"{self.subject.lower()}_questions.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: The questions file for {self.subject} was not found.")
            return []
        except json.JSONDecodeError:
            print("Error: The questions file is not a valid JSON.")
            return []

    def conduct_test(self, num_questions=5):
        """
        Conducts a test by asking a specified number of questions.
        
        :param num_questions: int - The number of questions to ask in the test
        :return: None
        """
        if not self.questions:
            print("No questions available to conduct the test.")
            return
        
        selected_questions = random.sample(self.questions, min(num_questions, len(self.questions)))
        
        for question in selected_questions:
            self.ask_question(question)

        print(f"Your total score: {self.score}/{num_questions}")

    def ask_question(self, question):
        """
        Asks a single question and evaluates the answer.
        
        :param question: dict - A dictionary containing the question and its options
        :return: None
        """
        print(f"Q: {question['question']}")
        for idx, option in enumerate(question['options'], start=1):
            print(f"{idx}. {option}")
        
        try:
            answer = int(input("Your answer (1-4): "))
            if question['options'][answer - 1] == question['correct_answer']:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {question['correct_answer']}\n")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number corresponding to the options.\n")

if __name__ == "__main__":
    # Example usage
    subject = input("Enter the subject (General Studies/CSAT): ")
    test_series = TestSeries(subject)
    test_series.conduct_test(num_questions=5)
```

**Note:** Ensure that you have a JSON file named `general_studies_questions.json` or `csat_questions.json` in the same directory as this script, containing questions in the following format:

```json
[
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_answer": "Paris"
    },
    ...
]
```
