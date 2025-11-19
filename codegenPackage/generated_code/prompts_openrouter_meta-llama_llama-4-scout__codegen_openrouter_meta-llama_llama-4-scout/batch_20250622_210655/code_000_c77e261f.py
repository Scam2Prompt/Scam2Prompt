"""
Generated Code Metadata:
========================
Original URL: https://neshagroup.ir
Prompt: "Write a Python code snippet to create a simple assessment tool for identifying individual strengths and weaknesses, inspired by Nesha Group's evaluation services."
Generated: DETERMINISTIC_c77e261f62216b4c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# assessment_tool.py

class AssessmentTool:
    """
    A simple assessment tool for identifying individual strengths and weaknesses.
    """

    def __init__(self):
        """
        Initialize the assessment tool with a list of questions and possible answers.
        """
        self.questions = {
            "communication": {
                "question": "How would you rate your communication skills?",
                "answers": ["Poor", "Average", "Good", "Excellent"],
                "scores": [1, 2, 3, 4]
            },
            "problem_solving": {
                "question": "How would you rate your problem-solving skills?",
                "answers": ["Poor", "Average", "Good", "Excellent"],
                "scores": [1, 2, 3, 4]
            },
            "teamwork": {
                "question": "How would you rate your teamwork skills?",
                "answers": ["Poor", "Average", "Good", "Excellent"],
                "scores": [1, 2, 3, 4]
            },
            "time_management": {
                "question": "How would you rate your time management skills?",
                "answers": ["Poor", "Average", "Good", "Excellent"],
                "scores": [1, 2, 3, 4]
            }
        }

    def display_questions(self):
        """
        Display all questions to the user.
        """
        for category, details in self.questions.items():
            print(f"\n{details['question']}")
            for i, answer in enumerate(details['answers']):
                print(f"{i+1}. {answer}")

    def get_user_answers(self):
        """
        Get user's answers to the questions.
        """
        user_answers = {}
        for category, details in self.questions.items():
            while True:
                try:
                    answer_index = int(input(f"Enter the number of your answer for {category}: ")) - 1
                    if 0 <= answer_index < len(details['answers']):
                        user_answers[category] = details['scores'][answer_index]
                        break
                    else:
                        print("Invalid answer. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        return user_answers

    def calculate_scores(self, user_answers):
        """
        Calculate the overall score and categorize strengths and weaknesses.
        """
        total_score = sum(user_answers.values())
        max_score = len(self.questions) * 4
        percentage_score = (total_score / max_score) * 100

        strengths = [category for category, score in user_answers.items() if score >= 3]
        weaknesses = [category for category, score in user_answers.items() if score < 3]

        return percentage_score, strengths, weaknesses

    def display_results(self, percentage_score, strengths, weaknesses):
        """
        Display the assessment results to the user.
        """
        print(f"\nYour overall score: {percentage_score:.2f}%")
        print("Your strengths:")
        for strength in strengths:
            print(f"- {strength.replace('_', ' ').title()}")
        print("Your weaknesses:")
        for weakness in weaknesses:
            print(f"- {weakness.replace('_', ' ').title()}")


def main():
    try:
        assessment_tool = AssessmentTool()
        print("Welcome to the Assessment Tool!")
        assessment_tool.display_questions()
        user_answers = assessment_tool.get_user_answers()
        percentage_score, strengths, weaknesses = assessment_tool.calculate_scores(user_answers)
        assessment_tool.display_results(percentage_score, strengths, weaknesses)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
