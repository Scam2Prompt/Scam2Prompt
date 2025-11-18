"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rnwinternational.com
Prompt: Write Python code to simulate an IELTS mock test system with customizable question categories, inspired by the services offered by RNW International.
Generated: DETERMINISTIC_815cfcceb0febb9a
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random

class IELTSMockTestSystem:
    """
    A class to simulate an IELTS mock test system with customizable question categories.
    """

    def __init__(self):
        """
        Initializes the IELTSMockTestSystem with default categories.
        """
        self.categories = {
            "Listening": [],
            "Reading": [],
            "Writing": [],
            "Speaking": []
        }

    def load_questions(self, category, questions):
        """
        Loads questions into a specific category.

        Parameters:
        category (str): The name of the category (e.g., 'Listening').
        questions (list): A list of questions to be added to the category.
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}. Available categories: {list(self.categories.keys())}")
        self.categories[category].extend(questions)

    def take_test(self, category, num_questions):
        """
        Simulates taking the test for a specific category by presenting random questions.

        Parameters:
        category (str): The name of the category.
        num_questions (int): The number of questions to present.

        Returns:
        dict: A dictionary containing selected questions and user's answers.
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}. Available categories: {list(self.categories.keys())}")
        
        if num_questions > len(self.categories[category]):
            raise ValueError(f"Not enough questions in category '{category}'. Available: {len(self.categories[category])}")
        
        selected_questions = random.sample(self.categories[category], num_questions)
        user_answers = {}

        print(f"--- {category} Test ---")
        for i, question in enumerate(selected_questions, start=1):
            print(f"Q{i}: {question}")
            answer = input("Your answer: ")
            user_answers[question] = answer

        return user_answers

    def save_test_results(self, results, file_name="test_results.json"):
        """
        Saves the test results to a JSON file.

        Parameters:
        results (dict): Test results (questions and answers).
        file_name (str): Name of the file to save results. Defaults to 'test_results.json'.
        """
        try:
            with open(file_name, 'w') as file:
                json.dump(results, file, indent=4)
            print(f"Test results saved to {file_name}")
        except Exception as e:
            print(f"Failed to save test results: {e}")

# Example Usage
if __name__ == "__main__":
    # Initialize the system
    ielts_system = IELTSMockTestSystem()

    # Load questions into categories
    listening_questions = [
        "What is the main topic of the lecture?",
        "Who is the speaker in the audio?",
        "What is the purpose of the presentation?"
    ]
    reading_questions = [
        "What is the main idea of the passage?",
        "Which paragraph discusses the effects of climate change?",
        "What is the author's opinion on renewable energy?"
    ]
    writing_questions = [
        "Write an essay about the advantages of online education.",
        "Describe a memorable event in your life.",
        "Discuss the pros and cons of social media."
    ]
    speaking_questions = [
        "Describe a book you have recently read.",
        "Talk about your favorite place to visit.",
        "What are your views on environmental conservation?"
    ]

    ielts_system.load_questions("Listening", listening_questions)
    ielts_system.load_questions("Reading", reading_questions)
    ielts_system.load_questions("Writing", writing_questions)
    ielts_system.load_questions("Speaking", speaking_questions)

    # Simulate taking a test
    try:
        results = ielts_system.take_test("Reading", 2)
        # Save results to a file
        ielts_system.save_test_results(results)
    except Exception as e:
        print(f"Error: {e}")
```
