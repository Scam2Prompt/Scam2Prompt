"""
Generated Code Metadata:
========================
Original URL: https://vinescoin.com
Prompt: Develop a market research survey to understand the needs and preferences of potential customers for high-quality cooking oils, inspired by Authentic Oil's market research approach.
Generated: DETERMINISTIC_519b944058b85940
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import csv
from datetime import datetime

class Survey:
    def __init__(self, title, description):
        """
        Initialize the Survey with a title and description.
        
        :param title: Title of the survey
        :param description: Description of the survey
        """
        self.title = title
        self.description = description
        self.responses = []

    def add_response(self, response):
        """
        Add a response to the survey.
        
        :param response: A dictionary containing the survey response
        """
        self.responses.append(response)

    def save_to_json(self, filename):
        """
        Save the survey responses to a JSON file.
        
        :param filename: The name of the file to save the responses
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.responses, json_file, indent=4)
            print(f"Responses saved to {filename}")
        except IOError as e:
            print(f"Error saving to JSON: {e}")

    def save_to_csv(self, filename):
        """
        Save the survey responses to a CSV file.
        
        :param filename: The name of the file to save the responses
        """
        try:
            with open(filename, 'w', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=self.responses[0].keys())
                writer.writeheader()
                writer.writerows(self.responses)
            print(f"Responses saved to {filename}")
        except IOError as e:
            print(f"Error saving to CSV: {e}")

def main():
    # Create a survey instance
    survey = Survey(
        title="High-Quality Cooking Oils Market Research",
        description="This survey aims to understand the needs and preferences of potential customers for high-quality cooking oils."
    )

    # Sample questions for the survey
    questions = [
        "What type of cooking oil do you currently use?",
        "How often do you purchase cooking oil?",
        "What factors influence your choice of cooking oil? (e.g., price, quality, brand)",
        "What is your preferred packaging size for cooking oil?",
        "Would you be interested in trying new brands of cooking oil?",
        "What health benefits do you look for in cooking oil?"
    ]

    # Collect responses
    print(survey.title)
    print(survey.description)
    for question in questions:
        answer = input(f"{question} ")
        survey.add_response({question: answer})

    # Save responses to files
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    survey.save_to_json(f"survey_responses_{timestamp}.json")
    survey.save_to_csv(f"survey_responses_{timestamp}.csv")

if __name__ == "__main__":
    main()
```
