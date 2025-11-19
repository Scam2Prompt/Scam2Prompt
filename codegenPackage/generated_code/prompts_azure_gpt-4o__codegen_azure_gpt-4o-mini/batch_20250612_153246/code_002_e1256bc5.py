"""
Generated Code Metadata:
========================
Original URL: https://gkcritiques.com
Prompt: Develop a questionnaire for IT Decision Makers (ITDMs) to gather insights on technology adoption, leveraging the methodology described by GK Critique Services.
Generated: DETERMINISTIC_e1256bc56e4c1f56
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class Questionnaire:
    """
    A class to represent a questionnaire for IT Decision Makers (ITDMs).
    """

    def __init__(self, title: str):
        """
        Initializes the Questionnaire with a title and an empty list of questions.

        Args:
            title (str): The title of the questionnaire.
        """
        self.title = title
        self.questions: List[Dict[str, str]] = []

    def add_question(self, question: str, question_type: str, options: List[str] = None):
        """
        Adds a question to the questionnaire.

        Args:
            question (str): The question text.
            question_type (str): The type of question (e.g., 'text', 'multiple-choice').
            options (List[str], optional): The options for multiple-choice questions. Defaults to None.

        Raises:
            ValueError: If the question type is not supported.
        """
        if question_type not in ['text', 'multiple-choice']:
            raise ValueError("Unsupported question type. Use 'text' or 'multiple-choice'.")

        self.questions.append({
            'question': question,
            'type': question_type,
            'options': options
        })

    def to_json(self) -> str:
        """
        Converts the questionnaire to a JSON string.

        Returns:
            str: A JSON representation of the questionnaire.
        """
        return json.dumps({
            'title': self.title,
            'questions': self.questions
        }, indent=4)

    def save_to_file(self, filename: str):
        """
        Saves the questionnaire to a file in JSON format.

        Args:
            filename (str): The name of the file to save the questionnaire.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                file.write(self.to_json())
        except IOError as e:
            print(f"Error saving questionnaire to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create a new questionnaire for IT Decision Makers
    itdm_questionnaire = Questionnaire("IT Decision Makers Technology Adoption Survey")

    # Add questions to the questionnaire
    itdm_questionnaire.add_question("What is your primary role in IT?", "text")
    itdm_questionnaire.add_question("Which technologies are you currently adopting?", "multiple-choice", 
                                    options=["Cloud Computing", "AI/ML", "Cybersecurity", "IoT"])
    itdm_questionnaire.add_question("What challenges do you face in technology adoption?", "text")

    # Save the questionnaire to a JSON file
    itdm_questionnaire.save_to_file("itdm_questionnaire.json")
```
