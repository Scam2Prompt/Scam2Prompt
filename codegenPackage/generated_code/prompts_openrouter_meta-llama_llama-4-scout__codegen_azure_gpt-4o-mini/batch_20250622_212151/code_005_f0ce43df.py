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
import json

class GuardianshipChecklist:
    def __init__(self):
        # Define the forms required for different types of guardianship
        self.forms = {
            "minor": {
                "Salt Lake": ["Form A", "Form B", "Form C"],
                "Utah County": ["Form D", "Form E"],
            },
            "adult": {
                "Salt Lake": ["Form F", "Form G"],
                "Utah County": ["Form H", "Form I", "Form J"],
            },
            "temporary": {
                "Salt Lake": ["Form K"],
                "Utah County": ["Form L", "Form M"],
            }
        }

    def get_checklist(self, guardianship_type, court_location):
        """
        Generate a checklist of forms based on the type of guardianship and court location.

        :param guardianship_type: Type of guardianship (e.g., 'minor', 'adult', 'temporary')
        :param court_location: Location of the court (e.g., 'Salt Lake', 'Utah County')
        :return: List of required forms or an error message
        """
        try:
            # Validate input
            if guardianship_type not in self.forms:
                raise ValueError(f"Invalid guardianship type: {guardianship_type}. Valid options are: {list(self.forms.keys())}.")
            if court_location not in self.forms[guardianship_type]:
                raise ValueError(f"Invalid court location: {court_location}. Valid options for '{guardianship_type}' are: {list(self.forms[guardianship_type].keys())}.")

            # Return the checklist of forms
            return self.forms[guardianship_type][court_location]
        
        except ValueError as e:
            return str(e)
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

def main():
    # Create an instance of the GuardianshipChecklist
    checklist_generator = GuardianshipChecklist()

    # User input for guardianship type and court location
    guardianship_type = input("Enter the type of guardianship (minor/adult/temporary): ").strip().lower()
    court_location = input("Enter the court location (Salt Lake/Utah County): ").strip().title()

    # Generate and display the checklist
    checklist = checklist_generator.get_checklist(guardianship_type, court_location)
    print("Required forms for your guardianship petition:")
    print(json.dumps(checklist, indent=2) if isinstance(checklist, list) else checklist)

if __name__ == "__main__":
    main()
```
