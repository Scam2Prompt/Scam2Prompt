"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-foundation.web.app
Prompt: Create a sample application questionnaire for the Sui Foundation's Developer Grants Program, ensuring it emphasizes the project's impact on decentralization.
Generated: DETERMINISTIC_756add81d3aca771
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class ApplicationQuestionnaire:
    """
    A class to represent a questionnaire for the Sui Foundation's Developer Grants Program.
    """
    
    def __init__(self):
        """
        Initializes the questionnaire with predefined questions.
        """
        self.questions: List[Dict[str, str]] = [
            {
                "question": "What is the name of your project?",
                "response": ""
            },
            {
                "question": "Please describe the problem your project solves.",
                "response": ""
            },
            {
                "question": "How does your project promote decentralization?",
                "response": ""
            },
            {
                "question": "Who is your target audience?",
                "response": ""
            },
            {
                "question": "What is the expected impact of your project on the Sui ecosystem?",
                "response": ""
            },
            {
                "question": "Please outline your project's timeline and milestones.",
                "response": ""
            },
            {
                "question": "What is your budget and how do you plan to allocate it?",
                "response": ""
            },
            {
                "question": "How will you measure the success of your project?",
                "response": ""
            }
        ]

    def answer_question(self, question_index: int, answer: str) -> None:
        """
        Records the answer for a specific question.

        :param question_index: Index of the question to be answered.
        :param answer: The answer to the question.
        :raises IndexError: If the question_index is out of bounds.
        """
        if question_index < 0 or question_index >= len(self.questions):
            raise IndexError("Question index out of range.")
        self.questions[question_index]['response'] = answer

    def export_to_json(self, file_path: str) -> None:
        """
        Exports the questionnaire and responses to a JSON file.

        :param file_path: The path where the JSON file will be saved.
        :raises IOError: If there is an error writing the file.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.questions, json_file, indent=4)
        except IOError as e:
            print(f"An error occurred while writing to the file: {e}")

    def display_questionnaire(self) -> None:
        """
        Displays the questionnaire with current responses in a user-friendly format.
        """
        for i, question in enumerate(self.questions):
            print(f"{i + 1}. {question['question']}")
            print(f"   Response: {question['response']}\n")

# Example of how to use the ApplicationQuestionnaire class
if __name__ == "__main__":
    questionnaire = ApplicationQuestionnaire()
    
    # Display the questions
    questionnaire.display_questionnaire()
    
    # Example of answering questions
    questionnaire.answer_question(2, "Our project implements a decentralized voting system.")
    
    # Display updated questionnaire
    questionnaire.display_questionnaire()
    
    # Export to JSON
    questionnaire.export_to_json("application_questionnaire.json")
```
