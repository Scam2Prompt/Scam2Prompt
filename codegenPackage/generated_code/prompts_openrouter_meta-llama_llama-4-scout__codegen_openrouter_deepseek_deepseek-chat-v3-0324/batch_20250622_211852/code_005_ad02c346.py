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
from typing import Dict, List, Optional

class CustomerSatisfactionSurvey:
    """
    A customer satisfaction survey template for a retail IT company.
    Inspired by Retail Tech Solutions' high customer satisfaction rating.
    """

    def __init__(self):
        """Initialize the survey with default questions and options."""
        self.survey_title = "Retail IT Solutions Customer Satisfaction Survey"
        self.questions = [
            {
                "id": 1,
                "question": "How satisfied are you with our products/services?",
                "type": "rating",
                "options": ["Very Dissatisfied", "Dissatisfied", "Neutral", "Satisfied", "Very Satisfied"]
            },
            {
                "id": 2,
                "question": "How likely are you to recommend our company to others?",
                "type": "rating",
                "options": ["Very Unlikely", "Unlikely", "Neutral", "Likely", "Very Likely"]
            },
            {
                "id": 3,
                "question": "How would you rate the quality of our technical support?",
                "type": "rating",
                "options": ["Poor", "Below Average", "Average", "Good", "Excellent"]
            },
            {
                "id": 4,
                "question": "How easy was it to use our products/services?",
                "type": "rating",
                "options": ["Very Difficult", "Difficult", "Neutral", "Easy", "Very Easy"]
            },
            {
                "id": 5,
                "question": "Do you have any additional comments or suggestions?",
                "type": "text",
                "options": None
            }
        ]

    def display_survey(self) -> None:
        """Display the survey questions to the user."""
        print(f"\n{self.survey_title}\n")
        print("Please rate your experience with the following questions:\n")
        
        for question in self.questions:
            print(f"{question['id']}. {question['question']}")
            if question["type"] == "rating":
                for idx, option in enumerate(question["options"], start=1):
                    print(f"   {idx}. {option}")
            print()

    def collect_responses(self) -> Dict[int, str]:
        """
        Collect user responses for the survey.
        
        Returns:
            Dict[int, str]: A dictionary mapping question IDs to user responses.
        """
        responses = {}
        
        for question in self.questions:
            while True:
                try:
                    if question["type"] == "rating":
                        response = input(
                            f"Enter your choice for question {question['id']} (1-{len(question['options'])}): "
                        )
                        if not response.isdigit():
                            raise ValueError("Please enter a number.")
                        
                        choice = int(response)
                        if choice < 1 or choice > len(question["options"]):
                            raise ValueError(
                                f"Please enter a number between 1 and {len(question['options'])}."
                            )
                        
                        responses[question["id"]] = question["options"][choice - 1]
                    else:
                        responses[question["id"]] = input(
                            f"Enter your response for question {question['id']}: "
                        )
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please try again.")
        
        return responses

    def save_responses(self, responses: Dict[int, str], filename: str = "survey_responses.json") -> None:
        """
        Save survey responses to a JSON file.
        
        Args:
            responses (Dict[int, str]): The responses to save.
            filename (str): The name of the file to save to.
        """
        try:
            with open(filename, "w") as file:
                json.dump(responses, file, indent=4)
            print(f"\nSurvey responses saved to {filename}.")
        except IOError as e:
            print(f"\nError saving responses: {e}")

    def calculate_average_rating(self, responses: Dict[int, str]) -> Optional[float]:
        """
        Calculate the average rating from the survey responses.
        
        Args:
            responses (Dict[int, str]): The survey responses.
            
        Returns:
            Optional[float]: The average rating, or None if no rating questions were answered.
        """
        rating_questions = [
            q for q in self.questions if q["type"] == "rating" and q["id"] in responses
        ]
        if not rating_questions:
            return None
        
        total = 0
        for question in rating_questions:
            response = responses[question["id"]]
            rating = question["options"].index(response) + 1  # Convert to 1-5 scale
            total += rating
        
        return round(total / len(rating_questions), 1)

def main():
    """Run the customer satisfaction survey."""
    survey = CustomerSatisfactionSurvey()
    survey.display_survey()
    responses = survey.collect_responses()
    survey.save_responses(responses)
    
    avg_rating = survey.calculate_average_rating(responses)
    if avg_rating is not None:
        print(f"\nAverage Satisfaction Rating: {avg_rating}/5")

if __name__ == "__main__":
    main()
```
