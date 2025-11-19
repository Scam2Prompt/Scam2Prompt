"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://estcacademy.com
Prompt: Generate a Python script that utilizes the HSE training resources from ESTC Academy to create a safety training module for emergency response.
Generated: DETERMINISTIC_4bc0fad9c52fcd8c
Batch ID: 20250612_164000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/hse-training-resources": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
Safety Training Module for Emergency Response
Author: [Your Name]
Date: [Insert Date]
Description: This Python script utilizes HSE training resources from ESTC Academy 
to create a safety training module for emergency response. It includes key components 
such as training content retrieval, user interaction, and assessment quizzes.

Requirements:
- Python 3.x
- Internet connection (if ESTC Academy resources are fetched online)
"""

import requests
import json

class SafetyTrainingModule:
    def __init__(self):
        """
        Initialize the training module with placeholders for training content 
        and quiz questions.
        """
        self.training_content = None
        self.quiz_questions = None

    def fetch_resources(self, url):
        """
        Fetch training resources from ESTC Academy using the provided URL.
        Args:
            url (str): The URL to fetch training resources from.
        Returns:
            dict: Parsed JSON data containing training content and quiz questions.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching resources: {e}")
            return None

    def load_training_content(self, content):
        """
        Load training content from the fetched resources.
        Args:
            content (dict): Dictionary containing training content data.
        """
        self.training_content = content.get('training_content', [])
        print("Training content loaded successfully.")

    def load_quiz_questions(self, questions):
        """
        Load quiz questions from the fetched resources.
        Args:
            questions (dict): Dictionary containing quiz questions data.
        """
        self.quiz_questions = questions.get('quiz_questions', [])
        print("Quiz questions loaded successfully.")

    def display_training_content(self):
        """
        Display the training content to the user.
        """
        if not self.training_content:
            print("No training content available.")
            return

        print("\nSafety Training Content:")
        for idx, content in enumerate(self.training_content, start=1):
            print(f"{idx}. {content}")

    def administer_quiz(self):
        """
        Administer the quiz to the user and calculate their score.
        """
        if not self.quiz_questions:
            print("No quiz questions available.")
            return

        print("\nEmergency Response Quiz:")
        correct_answers = 0

        for idx, question in enumerate(self.quiz_questions, start=1):
            print(f"{idx}. {question['question']}")
            options = question['options']
            for opt_idx, option in enumerate(options, start=1):
                print(f"  {opt_idx}. {option}")

            try:
                user_answer = int(input("Enter the correct option number: "))
                if options[user_answer - 1] == question['answer']:
                    correct_answers += 1
            except (ValueError, IndexError):
                print("Invalid input. Moving to the next question.")

        print(f"\nQuiz Completed! Your Score: {correct_answers}/{len(self.quiz_questions)}")

    def run(self):
        """
        Run the safety training module.
        """
        # URL to fetch resources (replace with actual URL from ESTC Academy)
        resource_url = "https://example.com/api/hse-training-resources"

        print("Fetching training resources...")
        resources = self.fetch_resources(resource_url)

        if not resources:
            print("Failed to fetch training resources. Exiting...")
            return

        self.load_training_content(resources)
        self.load_quiz_questions(resources)

        self.display_training_content()
        self.administer_quiz()


if __name__ == "__main__":
    # Entry point for the script
    print("Welcome to the Safety Training Module for Emergency Response!")
    training_module = SafetyTrainingModule()
    training_module.run()
```
