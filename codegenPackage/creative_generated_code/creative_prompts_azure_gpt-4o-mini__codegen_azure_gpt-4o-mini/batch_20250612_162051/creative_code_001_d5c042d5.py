"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://velemeny.moriczdental.hu
Prompt: Write a Python script that collects user feedback on dental treatments, including fields for "doctor's communication" and "treatment effectiveness," similar to the evaluation criteria on the Móricz Dental feedback page.
Generated: DETERMINISTIC_d5c042d5f551524d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class DentalFeedback:
    """
    A class to collect and manage user feedback on dental treatments.
    """

    def __init__(self):
        self.feedback_data = []

    def collect_feedback(self):
        """
        Collects user feedback through console input.
        Prompts for doctor's communication and treatment effectiveness.
        """
        try:
            doctor_communication = input("Rate the doctor's communication (1-5): ")
            treatment_effectiveness = input("Rate the treatment effectiveness (1-5): ")

            # Validate inputs
            self.validate_input(doctor_communication)
            self.validate_input(treatment_effectiveness)

            # Store feedback
            feedback_entry = {
                "doctor_communication": int(doctor_communication),
                "treatment_effectiveness": int(treatment_effectiveness)
            }
            self.feedback_data.append(feedback_entry)
            print("Thank you for your feedback!")

        except ValueError as ve:
            print(f"Error: {ve}. Please enter a valid number between 1 and 5.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def validate_input(self, value):
        """
        Validates the input value ensuring it's an integer between 1 and 5.
        
        :param value: The input value to validate.
        :raises ValueError: If the input is not in the valid range.
        """
        if not value.isdigit() or not (1 <= int(value) <= 5):
            raise ValueError("Input must be an integer between 1 and 5.")

    def save_feedback(self, filename='feedback.json'):
        """
        Saves the collected feedback data to a JSON file.
        
        :param filename: The name of the file to save feedback.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.feedback_data, f, indent=4)
            print(f"Feedback saved to {filename}.")
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")

    def run(self):
        """
        Runs the feedback collection process until the user chooses to stop.
        """
        while True:
            self.collect_feedback()
            cont = input("Would you like to provide more feedback? (yes/no): ").strip().lower()
            if cont != 'yes':
                break
        self.save_feedback()


if __name__ == "__main__":
    feedback_app = DentalFeedback()
    feedback_app.run()
```
