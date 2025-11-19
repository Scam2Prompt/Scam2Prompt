"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://login.trezor.com.usmaninterlining.com
Prompt: How can I create a program that helps students navigate the admissions process at a community college like Berkeley City College?
Generated: DETERMINISTIC_81f5db9db0ef81d7
Batch ID: 20250612_135957
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class AdmissionsNavigator:
    """A class to help students navigate the admissions process at a community college."""

    def __init__(self, college_name):
        self.college_name = college_name
        self.steps = []
        self.load_steps()

    def load_steps(self):
        """Load the admissions steps from a JSON file."""
        try:
            with open('admissions_steps.json', 'r') as file:
                self.steps = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file 'admissions_steps.json' was not found.")
        except json.JSONDecodeError:
            print("Error: The JSON file is invalid.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_steps(self):
        """Display the admissions steps to the user."""
        if not self.steps:
            print("No admissions steps available.")
            return
        
        print(f"Admissions Process for {self.college_name}:")
        for index, step in enumerate(self.steps, start=1):
            print(f"{index}. {step}")

    def get_user_input(self):
        """Get input from the user to navigate through the admissions process."""
        while True:
            user_choice = input("Would you like to see the admissions steps? (yes/no): ").strip().lower()
            if user_choice in ('yes', 'y'):
                self.display_steps()
            elif user_choice in ('no', 'n'):
                print("Thank you for using the Admissions Navigator. Good luck!")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    """Main function to run the Admissions Navigator."""
    college_name = "Berkeley City College"
    navigator = AdmissionsNavigator(college_name)
    navigator.get_user_input()

if __name__ == "__main__":
    main()
```

**Note:** The `admissions_steps.json` file should be structured as a JSON array of strings, for example:
```json
[
    "Complete the application form.",
    "Submit necessary documents (transcripts, ID, etc.).",
    "Attend an orientation session.",
    "Register for classes."
]
```
