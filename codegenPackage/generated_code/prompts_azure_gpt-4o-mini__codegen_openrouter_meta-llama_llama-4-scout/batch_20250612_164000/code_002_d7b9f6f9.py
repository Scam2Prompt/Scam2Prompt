"""
Generated Code Metadata:
========================
Original URL: https://shieldias.in
Prompt: Create a quiz application that tests users on the monthly current affairs topics covered by Shield IAS, including features for tracking performance.
Generated: DETERMINISTIC_d7b9f6f9318f3a53
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Quiz Application in Python**
```python
# Import required libraries
import json
import os
import random

class QuizApplication:
    def __init__(self, quiz_data_file='quiz_data.json'):
        """
        Initialize the quiz application.

        Args:
            quiz_data_file (str): Path to the quiz data file.
        """
        self.quiz_data_file = quiz_data_file
        self.quiz_data = self.load_quiz_data()
        self.user_scores = {}

    def load_quiz_data(self):
        """
        Load quiz data from the JSON file.

        Returns:
            dict: Quiz data.
        """
        try:
            with open(self.quiz_data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: Quiz data file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in quiz data file.")
            return {}

    def save_quiz_data(self):
        """
        Save quiz data to the JSON file.
        """
        try:
            with open(self.quiz_data_file, 'w') as file:
                json.dump(self.quiz_data, file, indent=4)
        except Exception as e:
            print(f"Error: Failed to save quiz data - {str(e)}")

    def add_quiz_question(self, topic, question, options, correct_answer):
        """
        Add a new quiz question.

        Args:
            topic (str): Topic of the question.
            question (str): Question text.
            options (list): List of options.
            correct_answer (str): Correct answer.
        """
        if topic not in self.quiz_data:
            self.quiz_data[topic] = []
        self.quiz_data[topic].append({
            'question': question,
            'options': options,
            'correct_answer': correct_answer
        })
        self.save_quiz_data()

    def take_quiz(self, topic, num_questions):
        """
        Take a quiz on a specific topic.

        Args:
            topic (str): Topic to take the quiz on.
            num_questions (int): Number of questions to attempt.

        Returns:
            int: Score achieved.
        """
        if topic not in self.quiz_data:
            print("Error: Topic not found.")
            return 0

        questions = self.quiz_data[topic]
        random_questions = random.sample(questions, min(num_questions, len(questions)))
        score = 0

        for question in random_questions:
            print(question['question'])
            for i, option in enumerate(question['options']):
                print(f"{i+1}. {option}")
            answer = input("Enter your answer (1/2/3/4): ")
            if question['options'][int(answer) - 1] == question['correct_answer']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Incorrect. Correct answer was {question['correct_answer']}.\n")

        return score

    def track_performance(self, user_name):
        """
        Track user performance.

        Args:
            user_name (str): User name.
        """
        if user_name not in self.user_scores:
            self.user_scores[user_name] = []
        print(f"Performance for {user_name}:")
        for i, score in enumerate(self.user_scores[user_name]):
            print(f"Quiz {i+1}: {score} points")

    def save_user_score(self, user_name, score):
        """
        Save user score.

        Args:
            user_name (str): User name.
            score (int): Score achieved.
        """
        if user_name not in self.user_scores:
            self.user_scores[user_name] = []
        self.user_scores[user_name].append(score)

def main():
    quiz_app = QuizApplication()

    while True:
        print("1. Add quiz question")
        print("2. Take quiz")
        print("3. Track performance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            topic = input("Enter topic: ")
            question = input("Enter question: ")
            options = input("Enter options (comma-separated): ").split(',')
            options = [option.strip() for option in options]
            correct_answer = input("Enter correct answer: ")
            quiz_app.add_quiz_question(topic, question, options, correct_answer)
        elif choice == '2':
            topic = input("Enter topic: ")
            num_questions = int(input("Enter number of questions: "))
            user_name = input("Enter your name: ")
            score = quiz_app.take_quiz(topic, num_questions)
            quiz_app.save_user_score(user_name, score)
            print(f"Your score is {score} points.")
        elif choice == '3':
            user_name = input("Enter your name: ")
            quiz_app.track_performance(user_name)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
```
**quiz_data.json**
```json
{
    "topic1": [
        {
            "question": "What is the capital of France?",
            "options": ["Paris", "London", "Berlin", "Rome"],
            "correct_answer": "Paris"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Saturn", "Jupiter", "Uranus"],
            "correct_answer": "Jupiter"
        }
    ]
}
```
