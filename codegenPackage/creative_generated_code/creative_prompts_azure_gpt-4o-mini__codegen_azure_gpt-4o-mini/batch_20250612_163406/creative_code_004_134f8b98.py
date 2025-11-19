"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Design a financial literacy quiz application that educates users on managing finances, inspired by the financial literacy programs mentioned on SGFC Finance's website.
Generated: DETERMINISTIC_134f8b982dd7a674
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Quiz:
    def __init__(self, questions_file):
        """
        Initializes the Quiz with a set of questions from a JSON file.
        
        Args:
            questions_file (str): Path to the JSON file containing quiz questions.
        """
        self.questions = self.load_questions(questions_file)
        self.score = 0

    def load_questions(self, questions_file):
        """
        Loads questions from a JSON file.
        
        Args:
            questions_file (str): Path to the JSON file.
        
        Returns:
            list: A list of questions loaded from the file.
        """
        try:
            with open(questions_file, 'r') as file:
                questions = json.load(file)
            return questions
        except FileNotFoundError:
            print(f"Error: The file {questions_file} was not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error: The file {questions_file} contains invalid JSON.")
            return []

    def ask_questions(self):
        """
        Iterates through the questions, asks the user for their answers, 
        and calculates the score.
        """
        for question in self.questions:
            self.ask_question(question)

    def ask_question(self, question):
        """
        Asks a single question and checks the answer.
        
        Args:
            question (dict): A dictionary containing the question and possible answers.
        """
        print(question['question'])
        for index, answer in enumerate(question['answers']):
            print(f"{index + 1}: {answer}")

        try:
            user_answer = int(input("Your answer (number): "))
            if user_answer - 1 == question['correct_index']:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Incorrect. The correct answer was: {question['answers'][question['correct_index']]}\n")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number corresponding to your choice.\n")

    def show_score(self):
        """Displays the user's score at the end of the quiz."""
        print(f"Your final score is: {self.score}/{len(self.questions)}")

def main():
    """
    Main function to run the Quiz application.
    """
    questions_file = 'questions.json'  # Specify the path to your questions file here
    quiz = Quiz(questions_file)
    
    if quiz.questions:  # Proceed only if questions were successfully loaded
        quiz.ask_questions()
        quiz.show_score()

if __name__ == "__main__":
    main()
```

**Sample `questions.json` format:**
```json
[
    {
        "question": "What is a budget?",
        "answers": [
            "A plan for saving and spending money",
            "A type of investment",
            "A bank account",
            "A loan"
        ],
        "correct_index": 0
    },
    {
        "question": "What is compound interest?",
        "answers": [
            "Interest on an initial principal, which also includes all of the accumulated interest from previous periods",
            "Interest that is calculated only on the principal amount",
            "Interest that is not charged",
            "A fixed rate of return"
        ],
        "correct_index": 0
    }
]
```

Make sure to create a `questions.json` file in the same directory as your script to provide the questions for the quiz.
