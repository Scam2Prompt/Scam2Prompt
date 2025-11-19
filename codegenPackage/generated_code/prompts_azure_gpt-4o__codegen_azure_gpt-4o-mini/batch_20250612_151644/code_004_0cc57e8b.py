"""
Generated Code Metadata:
========================
Original URL: https://complyaml.com
Prompt: Develop a beginner-friendly interactive training module in Python for AML compliance, similar to the methods described on ComplyAML's website.
Generated: DETERMINISTIC_0cc57e8b11ba13c7
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class AMLTrainingModule:
    def __init__(self):
        """Initialize the training module with a set of questions and answers."""
        self.questions = [
            {
                "question": "What does AML stand for?",
                "options": ["Anti-Money Laundering", "Automated Money Loss", "Asset Management Law"],
                "answer": "Anti-Money Laundering"
            },
            {
                "question": "Which of the following is a key component of AML compliance?",
                "options": ["Customer Due Diligence", "Market Analysis", "Financial Forecasting"],
                "answer": "Customer Due Diligence"
            },
            {
                "question": "What is the purpose of a Suspicious Activity Report (SAR)?",
                "options": ["To report suspicious transactions", "To track customer purchases", "To manage employee performance"],
                "answer": "To report suspicious transactions"
            }
        ]
        self.score = 0

    def display_question(self, question_data):
        """Display a single question and its options to the user."""
        print(question_data["question"])
        for idx, option in enumerate(question_data["options"], start=1):
            print(f"{idx}. {option}")

    def get_user_answer(self):
        """Get the user's answer and validate it."""
        while True:
            try:
                answer = int(input("Select the correct option (1-3): "))
                if answer in [1, 2, 3]:
                    return answer
                else:
                    print("Invalid option. Please select a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_answer(self, question_data, user_answer):
        """Check if the user's answer is correct and update the score."""
        correct_answer = question_data["options"].index(question_data["answer"]) + 1
        if user_answer == correct_answer:
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer was: {question_data['answer']}\n")

    def run_training(self):
        """Run the training module, iterating through all questions."""
        print("Welcome to the AML Compliance Training Module!\n")
        for question in self.questions:
            self.display_question(question)
            user_answer = self.get_user_answer()
            self.check_answer(question, user_answer)

        self.display_results()

    def display_results(self):
        """Display the final score to the user."""
        print(f"Training complete! Your score: {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            print("Excellent! You have a strong understanding of AML compliance.")
        elif self.score > len(self.questions) / 2:
            print("Good job! You have a decent understanding of AML compliance.")
        else:
            print("It seems you need to review AML compliance concepts.")

if __name__ == "__main__":
    try:
        training_module = AMLTrainingModule()
        training_module.run_training()
    except Exception as e:
        print(f"An error occurred: {e}")
```
