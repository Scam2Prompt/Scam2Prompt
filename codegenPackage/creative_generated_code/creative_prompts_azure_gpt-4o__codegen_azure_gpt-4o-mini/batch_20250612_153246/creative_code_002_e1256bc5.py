"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gkcritiques.com
Prompt: Develop a questionnaire for IT Decision Makers (ITDMs) to gather insights on technology adoption, leveraging the methodology described by GK Critique Services.
Generated: DETERMINISTIC_e1256bc56e4c1f56
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
from typing import List, Dict

class Questionnaire:
    def __init__(self, title: str):
        """
        Initializes the Questionnaire with a title.
        
        :param title: Title of the questionnaire.
        """
        self.title = title
        self.questions: List[Dict] = []

    def add_question(self, question: str, question_type: str, options: List[str] = None):
        """
        Adds a question to the questionnaire.
        
        :param question: The question text.
        :param question_type: The type of the question (e.g., 'multiple_choice', 'text').
        :param options: Optional; List of answer options for multiple choice questions.
        """
        if question_type not in ['multiple_choice', 'text']:
            raise ValueError("Invalid question type. Must be 'multiple_choice' or 'text'.")
        
        question_data = {
            'question': question,
            'type': question_type,
            'options': options if options else []
        }
        self.questions.append(question_data)

    def to_json(self) -> str:
        """
        Converts the questionnaire to JSON format.
        
        :return: JSON formatted string of the questionnaire.
        """
        return json.dumps({
            'title': self.title,
            'questions': self.questions
        }, indent=4)

def create_questionnaire():
    """
    Creates a questionnaire for IT Decision Makers (ITDMs) to gather insights on technology adoption.
    
    :return: JSON string representation of the questionnaire.
    """
    try:
        # Initialize the questionnaire
        itdm_questionnaire = Questionnaire("IT Decision Makers Technology Adoption Insights")

        # Add questions related to technology adoption
        itdm_questionnaire.add_question(
            "What is your organization's primary industry?",
            "multiple_choice",
            ["Healthcare", "Finance", "Education", "Technology", "Other"]
        )
        itdm_questionnaire.add_question(
            "Which technologies are currently being used in your organization?",
            "text"
        )
        itdm_questionnaire.add_question(
            "What barriers do you face when adopting new technologies?",
            "text"
        )
        itdm_questionnaire.add_question(
            "How important is cloud technology for your organization's strategy?",
            "multiple_choice",
            ["Very Important", "Somewhat Important", "Not Important"]
        )
        itdm_questionnaire.add_question(
            "What upcoming technology trends are you most interested in?",
            "text"
        )

        # Convert to JSON
        return itdm_questionnaire.to_json()
    
    except Exception as e:
        print(f"An error occurred while creating the questionnaire: {e}")

if __name__ == "__main__":
    # Execute the questionnaire creation and print the JSON
    questionnaire_json = create_questionnaire()
    print(questionnaire_json)
```
