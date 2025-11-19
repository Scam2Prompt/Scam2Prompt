"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Design a cybersecurity awareness program for a small business, incorporating best practices and strategies from the PDMA Technologies' cybersecurity training.
Generated: DETERMINISTIC_1ea5e88b93b4a0d5
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Cybersecurity Awareness Program for Small Business
This script is designed to provide a cybersecurity awareness program for employees of a small business.
It incorporates best practices and strategies inspired by PDMA Technologies' cybersecurity training.
"""

import os
import logging
from datetime import datetime

# Configure logging for the program
LOG_FILE = "cybersecurity_awareness.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants for the program
TRAINING_MODULES = [
    "Phishing Awareness",
    "Password Security",
    "Device Security",
    "Safe Internet Practices",
    "Incident Reporting"
]
QUIZ_QUESTIONS = {
    "Phishing Awareness": [
        {"question": "What is phishing?", "options": ["A type of malware", "A scam to steal sensitive information", "A secure communication method"], "answer": 2},
        {"question": "How can you identify a phishing email?", "options": ["Suspicious links", "Urgent tone", "Unexpected sender", "All of the above"], "answer": 4}
    ],
    "Password Security": [
        {"question": "What is a strong password?", "options": ["123456", "password", "P@ssw0rd123!", "qwerty"], "answer": 3},
        {"question": "How often should you change your password?", "options": ["Every week", "Every month", "Every 3-6 months", "Never"], "answer": 3}
    ]
}

# Function to log program activity
def log_activity(activity):
    """
    Logs program activity to the log file.

    :param activity: Description of the activity to log
    """
    logging.info(activity)

# Function to display training modules
def display_training_modules():
    """
    Displays the list of training modules to the user.
    """
    print("Cybersecurity Awareness Training Modules:")
    for idx, module in enumerate(TRAINING_MODULES, start=1):
        print(f"{idx}. {module}")
    log_activity("Displayed training modules to the user.")

# Function to conduct a quiz
def conduct_quiz(module_name):
    """
    Conducts a quiz for the specified training module.

    :param module_name: Name of the training module
    """
    if module_name not in QUIZ_QUESTIONS:
        print(f"No quiz available for {module_name}.")
        log_activity(f"Attempted to conduct quiz for {module_name}, but no quiz was found.")
        return

    print(f"Starting quiz for {module_name}...")
    score = 0
    questions = QUIZ_QUESTIONS[module_name]

    for idx, question in enumerate(questions, start=1):
        print(f"Question {idx}: {question['question']}")
        for opt_idx, option in enumerate(question['options'], start=1):
            print(f"{opt_idx}. {option}")
        try:
            user_answer = int(input("Enter the number of your answer: "))
            if user_answer == question['answer']:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            log_activity("User entered invalid input during quiz.")

    print(f"Quiz completed. Your score: {score}/{len(questions)}")
    log_activity(f"Quiz for {module_name} completed with score: {score}/{len(questions)}.")

# Function to start the program
def start_program():
    """
    Starts the cybersecurity awareness program.
    """
    print("Welcome to the Cybersecurity Awareness Program!")
    log_activity("Program started.")

    while True:
        display_training_modules()
        try:
            choice = int(input("Enter the number of the module you want to learn about (or 0 to exit): "))
            if choice == 0:
                print("Exiting the program. Stay safe!")
                log_activity("Program exited by user.")
                break
            elif 1 <= choice <= len(TRAINING_MODULES):
                module_name = TRAINING_MODULES[choice - 1]
                print(f"You selected: {module_name}")
                conduct_quiz(module_name)
            else:
                print("Invalid choice. Please select a valid module number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            log_activity("User entered invalid input while selecting a module.")

# Entry point of the program
if __name__ == "__main__":
    try:
        start_program()
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        print("An unexpected error occurred. Please check the log file for details.")
```
