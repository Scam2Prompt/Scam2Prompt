"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testul-poligraf.ro
Prompt: Write Python code to simulate a polygraph test questionnaire for pre-employment screening, including questions about integrity and background checks, as described on the Euro Poligraf Center website.
Generated: DETERMINISTIC_be0e219b917d648c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class PolygraphQuestionnaire:
    """
    A class to simulate a polygraph test questionnaire for pre-employment screening.
    """

    def __init__(self):
        self.questions = [
            {"id": 1, "question": "Have you ever stolen anything from your employer?"},
            {"id": 2, "question": "Have you ever lied on your resume?"},
            {"id": 3, "question": "Do you have a history of drug abuse?"},
            {"id": 4, "question": "Have you ever been convicted of a crime?"},
            {"id": 5, "question": "Have you ever been involved in any fraudulent activity?"}
        ]
        self.responses = {}

    def display_questions(self):
        """
        Display the questions to the user and collect their responses.
        """
        print("Please answer the following questions with 'yes' or 'no':\n")
        for question in self.questions:
            response = input(f"{question['id']}. {question['question']} ")
            self.responses[question['id']] = response.lower().strip()

    def validate_responses(self):
        """
        Validate the responses to ensure they are either 'yes' or 'no'.
        """
        invalid_responses = []
        for q_id, response in self.responses.items():
            if response not in ['yes', 'no']:
                invalid_responses.append(q_id)

        if invalid_responses:
            print(f"Invalid responses for questions: {invalid_responses}. Please answer with 'yes' or 'no'.")
            return False
        return True

    def generate_report(self):
        """
        Generate a report of the responses in JSON format.
        """
        report = {
            "responses": self.responses,
            "status": "Completed"
        }
        with open("polygraph_report.json", "w") as report_file:
            json.dump(report, report_file, indent=4)
        print("Report generated successfully: polygraph_report.json")

    def run(self):
        """
        The main method to run the questionnaire.
        """
        try:
            self.display_questions()
            if self.validate_responses():
                self.generate_report()
            else:
                print("Please restart the questionnaire to provide valid answers.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    questionnaire = PolygraphQuestionnaire()
    questionnaire.run()
```
