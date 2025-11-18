"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Write a Python script to simulate a customer satisfaction survey for an edible printing service, including fields for rating product quality and user experience.
Generated: DETERMINISTIC_5ee2c3a5bb9fd695
Batch ID: 20250612_145836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CustomerSatisfactionSurvey:
    def __init__(self):
        """Initialize the survey with default values."""
        self.responses = []

    def collect_response(self):
        """Collect a single customer's response for the survey."""
        try:
            print("Welcome to the Edible Printing Service Customer Satisfaction Survey!")
            product_quality = self.get_rating("Please rate the product quality (1 to 5): ")
            user_experience = self.get_rating("Please rate your user experience (1 to 5): ")
            comments = input("Any additional comments or suggestions? (optional): ")

            response = {
                "product_quality": product_quality,
                "user_experience": user_experience,
                "comments": comments
            }
            self.responses.append(response)
            print("Thank you for your feedback!")
        except Exception as e:
            print(f"An error occurred while collecting the response: {e}")

    def get_rating(self, prompt):
        """Get a valid rating from the user."""
        while True:
            try:
                rating = int(input(prompt))
                if 1 <= rating <= 5:
                    return rating
                else:
                    print("Please enter a valid rating between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

    def save_responses(self, filename='survey_responses.json'):
        """Save survey responses to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.responses, file, indent=4)
            print(f"Responses have been saved to {filename}.")
        except IOError as e:
            print(f"An error occurred while saving responses: {e}")

    def run_survey(self):
        """Run the survey until the user decides to stop."""
        while True:
            self.collect_response()
            continue_survey = input("Would you like to add another response? (yes/no): ").strip().lower()
            if continue_survey != 'yes':
                break
        self.save_responses()

if __name__ == "__main__":
    survey = CustomerSatisfactionSurvey()
    survey.run_survey()
```
