"""
Generated Code Metadata:
========================
Original URL: https://tpcontact.co.za
Prompt: Write code to generate a checklist for South Africans applying for UK visas, incorporating the 5-step process outlined on the ContactTP.co.za website.
Generated: DETERMINISTIC_891a0c40d4c94390
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class VisaChecklist:
    def __init__(self):
        """Initialize the checklist with the 5-step process for UK visa applications."""
        self.steps = [
            {
                "step": 1,
                "title": "Determine the Type of Visa",
                "description": "Identify the specific visa type you need based on your purpose of travel."
            },
            {
                "step": 2,
                "title": "Gather Required Documents",
                "description": "Collect all necessary documents such as passport, financial statements, and proof of accommodation."
            },
            {
                "step": 3,
                "title": "Complete the Visa Application Form",
                "description": "Fill out the appropriate visa application form accurately and completely."
            },
            {
                "step": 4,
                "title": "Pay the Visa Fee",
                "description": "Make the required payment for the visa application fee."
            },
            {
                "step": 5,
                "title": "Book an Appointment",
                "description": "Schedule an appointment at the nearest visa application center for submission."
            }
        ]

    def generate_checklist(self):
        """Generate a checklist in a readable format."""
        checklist = []
        for step in self.steps:
            checklist.append(f"Step {step['step']}: {step['title']}\nDescription: {step['description']}\n")
        return ''.join(checklist)

    def save_checklist_to_file(self, filename):
        """Save the checklist to a JSON file.

        Args:
            filename (str): The name of the file to save the checklist.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.steps, file, indent=4)
            print(f"Checklist successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving checklist to file: {e}")

if __name__ == "__main__":
    visa_checklist = VisaChecklist()
    
    # Generate and print the checklist
    print("UK Visa Application Checklist:\n")
    print(visa_checklist.generate_checklist())
    
    # Save the checklist to a file
    visa_checklist.save_checklist_to_file("uk_visa_checklist.json")
```
