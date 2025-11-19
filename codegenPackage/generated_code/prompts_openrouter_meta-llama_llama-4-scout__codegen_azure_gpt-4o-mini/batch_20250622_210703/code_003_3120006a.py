"""
Generated Code Metadata:
========================
Original URL: https://upjobsead.com.br
Prompt: "Create a quiz on workplace safety regulations, specifically NR-10 and NR-34, for a course on electrical safety in industrial settings."
Generated: DETERMINISTIC_3120006a3f85109e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

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

    def take_quiz(self):
        """
        Conducts the quiz by asking each question and collecting answers.
        """
        print(f"Welcome to the {self.title} Quiz!\n")
        for question in self.questions:
            print(question['question'])
            for idx, option in enumerate(question['options']):
                print(f"{idx + 1}. {option}")
            answer = input("Please enter the number of your answer: ")
            self.check_answer(question['correct_answer'], answer)

        self.display_score()

    def check_answer(self, correct_answer, user_answer):
        """
        Checks if the user's answer is correct and updates the score.

        :param correct_answer: The correct answer for the question
        :param user_answer: The user's answer
        """
        try:
            if int(user_answer) - 1 == correct_answer:
                print("Correct!\n")
                self.score += 1
            else:
                print("Incorrect.\n")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number corresponding to your answer.\n")

    def display_score(self):
        """
        Displays the final score of the quiz.
        """
        print(f"Your final score is: {self.score}/{len(self.questions)}")

def load_quiz_data(file_path):
    """
    Loads quiz data from a JSON file.

    :param file_path: Path to the JSON file containing quiz data
    :return: List of questions if successful, None otherwise
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data['questions']
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading quiz data: {e}")
        return None

def main():
    """
    Main function to run the quiz application.
    """
    quiz_data_path = 'quiz_data.json'
    questions = load_quiz_data(quiz_data_path)

    if questions is not None:
        quiz = Quiz("Workplace Safety Regulations Quiz (NR-10 and NR-34)", questions)
        quiz.take_quiz()

if __name__ == "__main__":
    main()
```

**Sample JSON file (quiz_data.json) structure:**
```json
{
    "questions": [
        {
            "question": "What does NR-10 regulate?",
            "options": [
                "Electrical installations and services",
                "Workplace ergonomics",
                "Chemical safety",
                "Fire safety"
            ],
            "correct_answer": 0
        },
        {
            "question": "Which of the following is a requirement of NR-34?",
            "options": [
                "Safety training for workers",
                "Regular equipment maintenance",
                "Emergency evacuation plans",
                "All of the above"
            ],
            "correct_answer": 3
        }
    ]
}
```
