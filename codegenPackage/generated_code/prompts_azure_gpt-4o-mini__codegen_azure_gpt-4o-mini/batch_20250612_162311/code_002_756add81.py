"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.web.app
Prompt: Create a sample application questionnaire for the Sui Foundation's Developer Grants Program, ensuring it emphasizes the project's impact on decentralization.
Generated: DETERMINISTIC_756add81d3aca771
Batch ID: 20250612_162311
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class DeveloperGrantsQuestionnaire:
    def __init__(self):
        """Initialize the questionnaire with predefined questions."""
        self.questions = {
            "project_name": "What is the name of your project?",
            "project_description": "Please provide a brief description of your project.",
            "decentralization_impact": "How does your project contribute to decentralization?",
            "target_audience": "Who is the target audience for your project?",
            "funding_needs": "What specific funding do you require from the Sui Foundation?",
            "timeline": "What is the expected timeline for your project?",
            "team_members": "Who are the key team members involved in this project?",
            "previous_work": "Do you have any previous work or projects that demonstrate your capability?",
            "additional_info": "Is there any additional information you would like to provide?"
        }
        self.responses = {}

    def collect_responses(self):
        """Collect responses from the user for each question."""
        print("Welcome to the Sui Foundation Developer Grants Program Questionnaire.")
        for key, question in self.questions.items():
            response = input(f"{question} ")
            self.responses[key] = response

    def validate_responses(self):
        """Validate the collected responses to ensure all required fields are filled."""
        required_fields = ["project_name", "project_description", "decentralization_impact"]
        for field in required_fields:
            if not self.responses.get(field):
                raise ValueError(f"The field '{field}' is required and cannot be empty.")

    def save_responses(self, filename='responses.json'):
        """Save the collected responses to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.responses, file, indent=4)
            print(f"Responses saved successfully to {filename}.")
        except IOError as e:
            print(f"An error occurred while saving responses: {e}")

    def run(self):
        """Run the questionnaire process."""
        try:
            self.collect_responses()
            self.validate_responses()
            self.save_responses()
        except ValueError as ve:
            print(f"Validation error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    questionnaire = DeveloperGrantsQuestionnaire()
    questionnaire.run()
```
