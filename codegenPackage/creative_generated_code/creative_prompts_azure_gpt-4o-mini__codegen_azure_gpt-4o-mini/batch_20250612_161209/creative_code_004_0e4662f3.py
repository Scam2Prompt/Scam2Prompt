"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starmissteenindia.com
Prompt: Generate a script that automates the collection of participant data for a modeling event, ensuring compliance with terms and conditions similar to those of Star Miss Teen India 2025.
Generated: DETERMINISTIC_0e4662f32c8533cc
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import re

class ParticipantDataCollector:
    def __init__(self, terms_file='terms_conditions.json'):
        self.terms_file = terms_file
        self.participants = []

    def load_terms(self):
        """Load the terms and conditions from a JSON file."""
        try:
            with open(self.terms_file, 'r') as file:
                terms = json.load(file)
                return terms
        except FileNotFoundError:
            raise FileNotFoundError("Terms and conditions file not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding the terms and conditions file.")

    def validate_email(self, email):
        """Validate the email format."""
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    def collect_participant_data(self, name, email, age):
        """Collect participant data and ensure compliance with terms."""
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        
        if age < 16:
            raise ValueError("Participants must be at least 16 years old.")

        participant = {
            'name': name,
            'email': email,
            'age': age
        }
        
        # Collect participant data
        self.participants.append(participant)
        return participant

    def save_participants(self, output_file='participants_data.json'):
        """Save the collected participant data to a JSON file."""
        try:
            with open(output_file, 'w') as file:
                json.dump(self.participants, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving participant data: {e}")

    def run(self):
        """Run the data collection process."""
        print("Welcome to the Participant Data Collection for the Modeling Event.")
        terms = self.load_terms()
        print("Terms and Conditions:")
        print(terms)

        while True:
            try:
                name = input("Enter participant's name: ")
                email = input("Enter participant's email: ")
                age = int(input("Enter participant's age: "))
                
                self.collect_participant_data(name, email, age)
                
                another = input("Do you want to add another participant? (yes/no): ").strip().lower()
                if another != 'yes':
                    break
            except ValueError as e:
                print(f"Error: {e}")

        self.save_participants()
        print("Participant data has been saved successfully.")

if __name__ == "__main__":
    collector = ParticipantDataCollector()
    collector.run()
```
