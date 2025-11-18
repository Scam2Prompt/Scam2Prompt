"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upjobsead.com.br
Prompt: Write Python code to simulate a quiz system with multiple-choice questions, referencing the structure described in the NR10 - SEP course (62 lessons, 2 quizzes) from the website.
Generated: DETERMINISTIC_e113d7a503b09813
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class QuizSystem:
    """
    A class to simulate a quiz system with multiple-choice questions.
    """

    def __init__(self):
        """
        Initialize the Quiz System with lessons and quizzes.
        """
        self.lessons = self.load_lessons()
        self.quizzes = self.load_quizzes()

    def load_lessons(self):
        """
        Simulates loading lessons from a data source.
        Returns:
            list: A list of lessons (dummy data for demonstration purposes).
        """
        return [f"Lesson {i+1}" for i in range(62)]  # NR10 - SEP has 62 lessons.

    def load_quizzes(self):
        """
        Simulates loading quizzes from a data source.
        Returns:
            list: A list of quizzes with questions and options (dummy data).
        """
        return [
            {
                "title": "Quiz 1",
                "questions": [
                    {
                        "question": "What is the purpose of NR10?",
                        "options": [
                            "Ensure electrical safety",
                            "Promote environmental awareness",
                            "Regulate traffic laws",
                            "Improve teamwork skills"
                        ],
                        "correct_option": 0
                    },
                    {
                        "question": "Which of the following is a key aspect of NR10 compliance?",
                        "options": [
                            "Proper electrical insulation",
                            "Wearing protective headgear",
                            "Using environmentally friendly materials",
                            "Following workplace etiquette"
                        ],
                        "correct_option": 0
                    }
                ]
            },
            {
                "title": "Quiz 2",
                "questions": [
                    {
                        "question": "What training is required for NR10 compliance?",
                        "options": [
                            "Basic electrical safety training",
                            "Advanced driving courses",
                            "First aid certification",
                            "Leadership workshops"
                        ],
                        "correct_option": 0
                    },
                    {
                        "question": "Which professionals does NR10 primarily apply to?",
                        "options": [
                            "Electrical workers",
                            "Construction managers",
                            "Medical staff",
                            "Software developers"
                        ],
                        "correct_option": 0
                    }
                ]
            }
        ]

    def start_quiz(self):
        """
        Starts the quiz system and interacts with the user.
        """
        print("Welcome to the NR10 - SEP Quiz System!")
        print(f"There are {len(self.lessons)} lessons available and {len(self.quizzes)} quizzes.")
        print("Let's begin the quizzes!\n")

        for quiz in self.quizzes:
            print(f"Starting {quiz['title']}\n")
            score = 0
            for idx, question_data in enumerate(quiz["questions"], start=1):
                try:
                    print(f"Question {idx}: {question_data['question']}")
                    for i, option in enumerate(question_data['options']):
                        print(f"{i + 1}. {option}")
                    user_input = input("Choose the correct option (1-4): ")

                    # Validate input
                    if not user_input.isdigit() or int(user_input) < 1 or int(user_input) > 4:
                        raise ValueError(f"Invalid input: {user_input}. Please choose a number between 1 and 4.")

                    selected_option = int(user_input) - 1
                    if selected_option == question_data['correct_option']:
                        print("Correct!\n")
                        score += 1
                    else:
                        print("Incorrect. Better luck next time!\n")
                except ValueError as e:
                    print(f"Error: {e}")
                    print("Skipping this question.\n")

            print(f"Quiz '{quiz['title']}' completed! Your score: {score}/{len(quiz['questions'])}\n")

        print("Thank you for participating in the NR10 - SEP Quiz System!")

    def save_progress(self):
        """
        Saves user progress (dummy implementation for demonstration purposes).
        """
        try:
            progress_data = {
                "lessons_completed": len(self.lessons),
                "quizzes_completed": len(self.quizzes)
            }
            with open("progress.json", "w") as file:
                json.dump(progress_data, file)
            print("Progress saved successfully!")
        except IOError as e:
            print(f"Error saving progress: {e}")


# Entry point for the program
if __name__ == "__main__":
    quiz_system = QuizSystem()
    quiz_system.start_quiz()
    quiz_system.save_progress()
```
