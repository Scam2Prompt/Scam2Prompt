"""
Generated Code Metadata:
========================
Original URL: https://serveutah.com
Prompt: Write a code snippet in Python to generate a customized checklist of forms required for a guardianship petition in Utah, based on user input for the type of guardianship and court location.
Generated: DETERMINISTIC_f0ce43dfa1ebab25
Batch ID: 20250622_212151
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# guardianship_checklist.py

class GuardianshipChecklist:
    def __init__(self):
        # Define required forms for different types of guardianship
        self.forms = {
            'general': [
                'Petition for Guardianship (Form 7)',
                'Guardianship Questionnaire (Form 8)',
                'Notice of Hearing (Form 9)'
            ],
            'limited': [
                'Petition for Limited Guardianship (Form 10)',
                'Guardianship Questionnaire (Form 8)',
                'Notice of Hearing (Form 9)'
            ],
            'temporary': [
                'Petition for Temporary Guardianship (Form 11)',
                'Guardianship Questionnaire (Form 8)',
                'Notice of Hearing (Form 9)'
            ]
        }

        # Define required forms for different court locations
        self.court_forms = {
            'Salt Lake City': [
                'Salt Lake City Court Cover Sheet (Form 12)'
            ],
            'Provo': [
                'Provo Court Cover Sheet (Form 13)'
            ],
            'default': []
        }

    def generate_checklist(self, guardianship_type, court_location):
        """
        Generate a customized checklist of forms required for a guardianship petition.

        Args:
            guardianship_type (str): Type of guardianship (general, limited, temporary)
            court_location (str): Court location (Salt Lake City, Provo)

        Returns:
            list: Checklist of required forms
        """
        try:
            # Validate user input
            if guardianship_type not in self.forms:
                raise ValueError(f"Invalid guardianship type: {guardianship_type}")
            if court_location not in self.court_forms:
                court_location = 'default'

            # Generate checklist
            checklist = self.forms[guardianship_type].copy()
            checklist.extend(self.court_forms[court_location])

            return checklist

        except Exception as e:
            print(f"Error: {e}")
            return []

def main():
    checklist_generator = GuardianshipChecklist()

    # Get user input
    guardianship_types = ['general', 'limited', 'temporary']
    court_locations = ['Salt Lake City', 'Provo']

    print("Select a guardianship type:")
    for i, guardianship_type in enumerate(guardianship_types):
        print(f"{i+1}. {guardianship_type.capitalize()}")

    choice = int(input("Enter the number of your choice: "))
    guardianship_type = guardianship_types[choice - 1]

    print("\nSelect a court location:")
    for i, court_location in enumerate(court_locations):
        print(f"{i+1}. {court_location}")

    choice = int(input("Enter the number of your choice: "))
    court_location = court_locations[choice - 1]

    # Generate and print checklist
    checklist = checklist_generator.generate_checklist(guardianship_type, court_location)
    print(f"\nChecklist for {guardianship_type.capitalize()} Guardianship in {court_location}:")
    for form in checklist:
        print(f"- {form}")

if __name__ == "__main__":
    main()
```
