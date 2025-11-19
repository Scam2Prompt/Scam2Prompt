"""
Generated Code Metadata:
========================
Original URL: https://testul-poligraf.ro
Prompt: Write Python code to simulate a polygraph test questionnaire for pre-employment screening, including questions about integrity and background checks, as described on the Euro Poligraf Center website.
Generated: DETERMINISTIC_be0e219b917d648c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class PolygraphTest:
    def __init__(self):
        """Initialize the PolygraphTest with a set of questions."""
        self.questions = [
            {
                "question": "Have you ever stolen anything?",
                "type": "boolean"
            },
            {
                "question": "Have you ever lied on a job application?",
                "type": "boolean"
            },
            {
                "question": "Have you ever been convicted of a crime?",
                "type": "boolean"
            },
            {
                "question": "Do you have any undisclosed financial issues?",
                "type": "boolean"
            },
            {
                "question": "Have you ever used illegal drugs?",
                "type": "boolean"
            },
            {
                "question": "Have you ever been fired from a job?",
                "type": "boolean"
            },
            {
                "question": "Do you have any pending legal issues?",
                "type": "boolean"
            }
        ]
        self.responses = {}

    def ask_questions(self):
        """Ask each question and store the responses."""
        for question in self.questions:
            response = self.get_response(question)
            self.responses[question["question"]] = response

    def get_response(self, question):
        """Get a boolean response from the user for a given question."""
        while True:
            try:
                answer = input(f"{question['question']} (yes/no): ").strip().lower()
                if answer not in ['yes', 'no']:
                    raise ValueError("Response must be 'yes' or 'no'.")
                return answer == 'yes'
            except ValueError as e:
                print(f"Error: {e}. Please try again.")

    def save_responses(self, filename='responses.json'):
        """Save the responses to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.responses, file, indent=4)
            print(f"Responses saved to {filename}.")
        except IOError as e:
            print(f"Error saving responses: {e}")

    def run(self):
        """Run the polygraph test questionnaire."""
        print("Welcome to the Polygraph Test Questionnaire.")
        self.ask_questions()
        self.save_responses()

if __name__ == "__main__":
    polygraph_test = PolygraphTest()
    polygraph_test.run()
```
