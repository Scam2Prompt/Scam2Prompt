"""
Generated Code Metadata:
========================
Original URL: https://master-brain.com
Prompt: "Create a training program on understanding consumer behavior for sales teams."
Generated: DETERMINISTIC_bbfca4242ffe707f
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Training Program: Understanding Consumer Behavior for Sales Teams
This program is designed to provide a structured training module for sales teams to better understand consumer behavior.
The program includes interactive lessons, quizzes, and progress tracking.
"""

import json
import os

# Constants
TRAINING_DATA_FILE = "training_data.json"
PROGRESS_FILE = "progress.json"

# Sample training data
training_data = [
    {
        "lesson_id": 1,
        "title": "Introduction to Consumer Behavior",
        "content": "Consumer behavior refers to the study of how individuals make decisions to spend their resources...",
        "quiz": {
            "question": "What is consumer behavior?",
            "options": ["Study of spending decisions", "Study of sales techniques", "Study of marketing strategies"],
            "answer": 0
        }
    },
    {
        "lesson_id": 2,
        "title": "Factors Influencing Consumer Behavior",
        "content": "Consumer behavior is influenced by psychological, personal, social, and cultural factors...",
        "quiz": {
            "question": "Which of the following is NOT a factor influencing consumer behavior?",
            "options": ["Psychological", "Personal", "Weather"],
            "answer": 2
        }
    }
]

# Function to save training data to a file
def save_training_data():
    try:
        with open(TRAINING_DATA_FILE, "w") as file:
            json.dump(training_data, file, indent=4)
    except Exception as e:
        print(f"Error saving training data: {e}")

# Function to load training data from a file
def load_training_data():
    try:
        if os.path.exists(TRAINING_DATA_FILE):
            with open(TRAINING_DATA_FILE, "r") as file:
                return json.load(file)
        else:
            save_training_data()
            return training_data
    except Exception as e:
        print(f"Error loading training data: {e}")
        return []

# Function to save user progress
def save_progress(progress):
    try:
        with open(PROGRESS_FILE, "w") as file:
            json.dump(progress, file, indent=4)
    except Exception as e:
        print(f"Error saving progress: {e}")

# Function to load user progress
def load_progress():
    try:
        if os.path.exists(PROGRESS_FILE):
            with open(PROGRESS_FILE, "r") as file:
                return json.load(file)
        else:
            return {}
    except Exception as e:
        print(f"Error loading progress: {e}")
        return {}

# Function to display a lesson
def display_lesson(lesson):
    print(f"\nLesson {lesson['lesson_id']}: {lesson['title']}")
    print(lesson['content'])

# Function to conduct a quiz
def conduct_quiz(quiz):
    print("\nQuiz:")
    print(quiz["question"])
    for idx, option in enumerate(quiz["options"]):
        print(f"{idx + 1}. {option}")
    try:
        user_answer = int(input("Enter the number of your answer: ")) - 1
        if user_answer == quiz["answer"]:
            print("Correct!")
            return True
        else:
            print("Incorrect. The correct answer was:", quiz["options"][quiz['answer']])
            return False
    except ValueError:
        print("Invalid input. Please enter a number.")
        return False

# Main training program
def training_program():
    print("Welcome to the Consumer Behavior Training Program!")
    training_data = load_training_data()
    progress = load_progress()

    for lesson in training_data:
        lesson_id = str(lesson["lesson_id"])
        if lesson_id in progress and progress[lesson_id]["completed"]:
            print(f"\nLesson {lesson['lesson_id']} already completed. Skipping...")
            continue

        display_lesson(lesson)
        completed = conduct_quiz(lesson["quiz"])

        # Update progress
        progress[lesson_id] = {"completed": completed}
        save_progress(progress)

    print("\nTraining program completed! Check your progress in the progress file.")

# Entry point
if __name__ == "__main__":
    training_program()
```
