"""
Generated Code Metadata:
========================
Original URL: https://sgfcfinance.com
Prompt: Design a financial literacy quiz application that educates users on managing finances, inspired by the financial literacy programs mentioned on SGFC Finance's website.
Generated: DETERMINISTIC_134f8b982dd7a674
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class QuizQuestion:
    """Class to represent a single quiz question."""
    
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def is_correct(self, user_answer):
        """Check if the user's answer is correct."""
        return user_answer == self.answer


class FinancialLiteracyQuiz:
    """Class to manage the financial literacy quiz."""
    
    def __init__(self):
        self.questions = []
        self.load_questions()

    def load_questions(self):
        """Load quiz questions from a JSON file."""
        try:
            with open('questions.json', 'r') as file:
                data = json.load(file)
                for item in data['questions']:
                    question = QuizQuestion(item['question'], item['options'], item['answer'])
                    self.questions.append(question)
        except FileNotFoundError:
            print("Error: Questions file not found.")
        except json.JSONDecodeError:
            print("Error: Failed to decode JSON from questions file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def start_quiz(self):
        """Start the quiz and handle user interaction."""
        score = 0
        for idx, question in enumerate(self.questions):
            print(f"Q{idx + 1}: {question.question}")
            for i, option in enumerate(question.options):
                print(f"  {i + 1}. {option}")
            user_input = input("Your answer (number): ")
            try:
                user_answer = question.options[int(user_input) - 1]
                if question.is_correct(user_answer):
                    print("Correct!\n")
                    score += 1
                else:
                    print(f"Wrong! The correct answer was: {question.answer}\n")
            except (IndexError, ValueError):
                print("Invalid input. Please enter a number corresponding to the options.\n")

        self.display_score(score)

    def display_score(self, score):
        """Display the final score to the user."""
        total_questions = len(self.questions)
        print(f"Quiz completed! Your score: {score}/{total_questions}")


if __name__ == "__main__":
    quiz = FinancialLiteracyQuiz()
    quiz.start_quiz()
```

**Sample `questions.json` file format:**
```json
{
    "questions": [
        {
            "question": "What is a budget?",
            "options": ["A plan for spending money", "A type of investment", "A loan from the bank"],
            "answer": "A plan for spending money"
        },
        {
            "question": "What is compound interest?",
            "options": ["Interest on the original principal only", "Interest on interest", "A type of savings account"],
            "answer": "Interest on interest"
        }
    ]
}
```
