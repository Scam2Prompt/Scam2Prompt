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

# Define a class for the questionnaire
class ITDMQuestionnaire:
    """
    A class to generate and manage a questionnaire for IT Decision Makers (ITDMs)
    to gather insights on technology adoption.
    """
    def __init__(self):
        """
        Initialize the questionnaire with a predefined set of questions.
        """
        self.questions = [
            {
                "id": 1,
                "text": "What is your primary role in the organization?",
                "type": "text"
            },
            {
                "id": 2,
                "text": "Which technologies has your organization adopted in the last 12 months?",
                "type": "multiselect",
                "options": ["Cloud Computing", "AI/ML", "Blockchain", "IoT", "Other"]
            },
            {
                "id": 3,
                "text": "What are the primary drivers of technology adoption in your organization?",
                "type": "multiselect",
                "options": ["Cost Savings", "Operational Efficiency", "Competitive Advantage", "Customer Demand", "Other"]
            },
            {
                "id": 4,
                "text": "What challenges does your organization face when adopting new technologies?",
                "type": "text"
            },
            {
                "id": 5,
                "text": "On a scale of 1 to 10, how satisfied are you with the current state of technology adoption in your organization?",
                "type": "rating",
                "scale": [1, 10]
            }
        ]

    def display_questionnaire(self):
        """
        Print the questionnaire in a user-friendly format.
        """
        print("IT Decision Makers Questionnaire:\n")
        for question in self.questions:
            print(f"Q{question['id']}: {question['text']}")
            if question['type'] == "multiselect":
                print("Options:", ", ".join(question['options']))
            elif question['type'] == "rating":
                print(f"Scale: {question['scale'][0]} to {question['scale'][1]}")
            print()

    def save_questionnaire(self, filepath):
        """
        Save the questionnaire to a JSON file.

        Args:
            filepath (str): The path to the file where the questionnaire should be saved.
        """
        try:
            with open(filepath, 'w') as file:
                json.dump(self.questions, file, indent=4)
            print(f"Questionnaire saved successfully to {filepath}")
        except IOError as e:
            print(f"Error saving questionnaire: {e}")

    @staticmethod
    def load_questionnaire(filepath):
        """
        Load a questionnaire from a JSON file.

        Args:
            filepath (str): The path to the file where the questionnaire is saved.

        Returns:
            list: The loaded questionnaire in the form of a list of questions.
        """
        try:
            with open(filepath, 'r') as file:
                questions = json.load(file)
            print(f"Questionnaire loaded successfully from {filepath}")
            return questions
        except IOError as e:
            print(f"Error loading questionnaire: {e}")
            return None


# Main execution block (if run as standalone script)
if __name__ == "__main__":
    # Create an instance of the questionnaire
    questionnaire = ITDMQuestionnaire()

    # Display the questionnaire to the user
    questionnaire.display_questionnaire()

    # Save the questionnaire to a file
    questionnaire.save_questionnaire("itdm_questionnaire.json")

    # Load the questionnaire from the file
    loaded_questions = ITDMQuestionnaire.load_questionnaire("itdm_questionnaire.json")
    if loaded_questions:
        print("\nLoaded Questionnaire:")
        for q in loaded_questions:
            print(q)
```
