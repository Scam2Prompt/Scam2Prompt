"""
Generated Code Metadata:
========================
Original URL: https://www.rtspos.net
Prompt: "Develop a customer satisfaction survey template for a retail IT company, inspired by Retail Tech Solutions' 4.9/5 customer satisfaction rating."
Generated: DETERMINISTIC_ad02c3469d8898f3
Batch ID: 20250622_211852
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

class CustomerSatisfactionSurvey:
    """
    A class to represent a customer satisfaction survey for a retail IT company.
    """

    def __init__(self, company_name: str):
        """
        Initializes the survey with the company name.

        :param company_name: Name of the company conducting the survey.
        """
        self.company_name = company_name
        self.questions = self.create_survey_template()

    def create_survey_template(self) -> List[Dict[str, str]]:
        """
        Creates a template for the customer satisfaction survey.

        :return: A list of questions in the survey.
        """
        return [
            {
                "question": "How satisfied are you with our products?",
                "type": "rating",
                "scale": 5
            },
            {
                "question": "How satisfied are you with our customer service?",
                "type": "rating",
                "scale": 5
            },
            {
                "question": "How likely are you to recommend us to a friend?",
                "type": "rating",
                "scale": 5
            },
            {
                "question": "What features do you value the most?",
                "type": "open-ended"
            },
            {
                "question": "What can we improve?",
                "type": "open-ended"
            }
        ]

    def collect_responses(self) -> Dict[str, str]:
        """
        Collects responses from the user for each question in the survey.

        :return: A dictionary containing the user's responses.
        """
        responses = {}
        for question in self.questions:
            if question["type"] == "rating":
                response = self.get_rating_response(question)
            else:
                response = input(f"{question['question']} ")
            responses[question['question']] = response
        return responses

    def get_rating_response(self, question: Dict[str, str]) -> int:
        """
        Prompts the user for a rating response and validates the input.

        :param question: The question dictionary containing the question and scale.
        :return: A validated rating response.
        """
        while True:
            try:
                response = int(input(f"{question['question']} (1-{question['scale']}): "))
                if 1 <= response <= question['scale']:
                    return response
                else:
                    print(f"Please enter a number between 1 and {question['scale']}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def save_responses(self, responses: Dict[str, str], filename: str) -> None:
        """
        Saves the collected responses to a JSON file.

        :param responses: The responses to save.
        :param filename: The name of the file to save the responses to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(responses, file, indent=4)
            print(f"Responses saved to {filename}.")
        except IOError as e:
            print(f"Error saving responses: {e}")

    def run_survey(self) -> None:
        """
        Runs the customer satisfaction survey.
        """
        print(f"Welcome to the {self.company_name} Customer Satisfaction Survey!")
        responses = self.collect_responses()
        self.save_responses(responses, 'customer_satisfaction_responses.json')


if __name__ == "__main__":
    survey = CustomerSatisfactionSurvey("Retail Tech Solutions")
    survey.run_survey()
```
