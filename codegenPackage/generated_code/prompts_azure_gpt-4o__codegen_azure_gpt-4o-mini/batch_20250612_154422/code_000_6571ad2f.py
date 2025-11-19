"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Write Python code to create a quiz application for UPSC IAS preparation, including features like "The Hindu Monthly Quiz" and current affairs questions as described on Shield IAS.
Generated: DETERMINISTIC_6571ad2f1d86ffd5
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random

class Quiz:
    def __init__(self, title, questions):
        """
        Initializes the Quiz with a title and a list of questions.

        :param title: Title of the quiz
        :param questions: List of questions (dicts) for the quiz
        """
        self.title = title
        self.questions = questions
        self.score = 0

    def ask_question(self, question):
        """
        Asks a single question and checks the user's answer.

        :param question: A dictionary containing the question and its options
        :return: None
        """
        print(f"\n{question['question']}")
        for idx, option in enumerate(question['options'], start=1):
            print(f"{idx}. {option}")

        try:
            answer = int(input("Your answer (1-4): "))
            if question['options'][answer - 1] == question['answer']:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {question['answer']}")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 4.")

    def start_quiz(self):
        """
        Starts the quiz by asking all questions in random order.

        :return: None
        """
        print(f"Welcome to the {self.title}!")
        random.shuffle(self.questions)
        for question in self.questions:
            self.ask_question(question)
        print(f"\nYour final score is: {self.score}/{len(self.questions)}")

def load_questions(file_path):
    """
    Loads questions from a JSON file.

    :param file_path: Path to the JSON file containing questions
    :return: List of questions
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []

def main():
    """
    Main function to run the quiz application.

    :return: None
    """
    questions_file = 'questions.json'  # Path to the questions file
    questions = load_questions(questions_file)

    if questions:
        quiz = Quiz("UPSC IAS Preparation Quiz", questions)
        quiz.start_quiz()
    else:
        print("No questions available to start the quiz.")

if __name__ == "__main__":
    main()
```

### Sample JSON Structure for `questions.json`
```json
[
    {
        "question": "What is the capital of India?",
        "options": ["Delhi", "Mumbai", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Who is known as the Father of the Nation in India?",
        "options": ["Jawaharlal Nehru", "Mahatma Gandhi", "Sardar Patel", "B.R. Ambedkar"],
        "answer": "Mahatma Gandhi"
    }
]
```

### Notes
- Ensure that the `questions.json` file is in the same directory as the script or provide the correct path.
- The quiz application is designed to be simple and can be expanded with more features as needed.
