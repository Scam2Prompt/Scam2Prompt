"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maratonadoenem.com.br
Prompt: Write code to design a mock exam platform that mimics the ENEM exam structure, including long questions and time constraints, as highlighted in the Maratona do ENEM simulados.
Generated: DETERMINISTIC_8aec755d515a1eb6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading

class MockExamPlatform:
    def __init__(self, exam_name, questions, time_limit_minutes):
        """
        Initializes the mock exam platform.

        Parameters:
        exam_name (str): The name of the exam.
        questions (list): A list of dictionaries containing questions and their options.
                          Each dictionary should have keys: 'question', 'options', and 'answer'.
        time_limit_minutes (int): Time limit for the exam in minutes.
        """
        self.exam_name = exam_name
        self.questions = questions
        self.time_limit_minutes = time_limit_minutes
        self.answers = {}
        self.remaining_time = time_limit_minutes * 60  # Convert minutes to seconds
        self.exam_started = False

    def start_exam(self):
        """
        Starts the exam and begins the countdown timer.
        """
        print(f"Starting '{self.exam_name}' mock exam...")
        self.exam_started = True
        threading.Thread(target=self._start_timer, daemon=True).start()  # Timer runs in a separate thread
        self._display_questions()

    def _start_timer(self):
        """
        Starts the countdown timer for the exam.
        """
        while self.remaining_time > 0:
            self.remaining_time -= 1
            time.sleep(1)
        print("\nTime's up! The exam has ended.\n")
        self._end_exam()

    def _display_questions(self):
        """
        Displays the questions to the user and collects their answers.
        """
        print(f"\nYou have {self.time_limit_minutes} minutes to complete the exam.")
        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i + 1}: {question['question']}")
            for idx, option in enumerate(question['options']):
                print(f"{idx + 1}. {option}")
            while True:
                try:
                    user_answer = int(input("Enter your answer (number): "))
                    if user_answer < 1 or user_answer > len(question['options']):
                        raise ValueError("Invalid option. Please choose a number corresponding to the options.")
                    self.answers[i + 1] = user_answer
                    break
                except ValueError as e:
                    print(e)

            # Exit if timer runs out
            if self.remaining_time <= 0:
                print("\nTime's up! The exam has ended.\n")
                self._end_exam()
                return
        self._end_exam()

    def _end_exam(self):
        """
        Ends the exam and displays the user's answers and the correct answers.
        """
        if self.exam_started:
            self.exam_started = False
            print("\nExam Completed!")
            print("\nYour answers:")
            for i, answer in self.answers.items():
                print(f"Question {i}: Option {answer}")

            print("\nCorrect answers:")
            for i, question in enumerate(self.questions):
                print(f"Question {i + 1}: Option {question['answer']}")

            print("\nThank you for participating in the mock exam!")

# Mock data for questions
questions = [
    {
        "question": "What is the capital of Brazil?",
        "options": ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"],
        "answer": 2  # Correct option index
    },
    {
        "question": "Which of the following is a programming language?",
        "options": ["Python", "HTML", "CSS", "Photoshop"],
        "answer": 1  # Correct option index
    },
    {
        "question": "What is the result of 5 + 3?",
        "options": ["5", "7", "8", "10"],
        "answer": 3  # Correct option index
    }
]

# Example usage
if __name__ == "__main__":
    exam_name = "Maratona do ENEM Simulado"
    time_limit_minutes = 5  # Set a time limit of 5 minutes
    mock_exam = MockExamPlatform(exam_name, questions, time_limit_minutes)
    mock_exam.start_exam()
```
