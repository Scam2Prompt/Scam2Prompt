"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serveutah.com
Prompt: Can you provide a checklist of forms needed to petition for guardianship of an adult child in Utah?
Generated: DETERMINISTIC_c713e0c2aeb2c606
Batch ID: 20250612_161041
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

class GuardianshipChecklist:
    def __init__(self):
        """Initialize the checklist with required documents for guardianship petition."""
        self.forms = [
            "Petition for Appointment of Guardian (Form 101)",
            "Confidential Information Form (Form 102)",
            "Proposed Order Appointing Guardian (Form 103)",
            "Notice of Hearing (Form 104)",
            "Affidavit of Service (Form 105)",
            "Background Check Authorization (Form 106)",
            "Financial Disclosure Form (Form 107)",
            "Affidavit of Competency (Form 108)"
        ]

    def display_checklist(self):
        """Display the checklist of forms needed to petition for guardianship."""
        print("Checklist for Petitioning Guardianship of an Adult Child in Utah:")
        for index, form in enumerate(self.forms, start=1):
            print(f"{index}. {form}")

    def save_checklist_to_file(self, filename="guardianship_checklist.txt"):
        """Save the checklist to a text file.

        Args:
            filename (str): The name of the file to save the checklist.
        """
        try:
            with open(filename, 'w') as file:
                file.write("Checklist for Petitioning Guardianship of an Adult Child in Utah:\n")
                for form in self.forms:
                    file.write(f"{form}\n")
            print(f"Checklist saved to {filename}.")
        except IOError as e:
            print(f"An error occurred while trying to save the checklist: {e}")

def main():
    """Main function to execute the guardianship checklist program."""
    checklist = GuardianshipChecklist()
    checklist.display_checklist()
    
    # Optional: Save the checklist to a file
    save_to_file = input("Would you like to save the checklist to a file? (yes/no): ").strip().lower()
    if save_to_file == 'yes':
        checklist.save_checklist_to_file()

if __name__ == "__main__":
    main()
```
