"""
Generated Code Metadata:
========================
Original URL: https://adygeya.propiski-net.ru
Prompt: Generate a checklist of required documents for temporary registration in Adygea, Russia, and provide a sample application form.
Generated: DETERMINISTIC_241d7da00549c784
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

def generate_checklist():
    """
    Generates a checklist of required documents for temporary registration in Adygea, Russia.
    Returns the checklist as a list of strings.
    """
    try:
        checklist = [
            "Passport (original and copy)",
            "Migration card (original and copy)",
            "Temporary residence permit or visa (if applicable)",
            "Proof of address (e.g., rental agreement or property ownership document)",
            "Application form for temporary registration",
            "Receipt of state fee payment (if required)"
        ]
        return checklist
    except Exception as e:
        print(f"Error generating checklist: {e}")
        return []

def generate_sample_application_form():
    """
    Generates a sample application form for temporary registration in Adygea, Russia.
    Returns the form as a dictionary.
    """
    try:
        application_form = {
            "title": "Application for Temporary Registration",
            "fields": {
                "Full Name": "Enter your full name",
                "Date of Birth": "Enter your date of birth (DD/MM/YYYY)",
                "Passport Number": "Enter your passport number",
                "Migration Card Number": "Enter your migration card number",
                "Address of Temporary Residence": "Enter the address where you will reside temporarily",
                "Contact Information": "Enter your phone number and/or email address",
                "Duration of Stay": "Enter the intended duration of your stay (e.g., 3 months)"
            },
            "instructions": "Please fill out all fields accurately and legibly. Attach required documents."
        }
        return application_form
    except Exception as e:
        print(f"Error generating application form: {e}")
        return {}

def save_to_file(data, filename):
    """
    Saves the given data to a file in JSON format.
    :param data: The data to save (list or dictionary).
    :param filename: The name of the file to save the data to.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving data to file: {e}")

if __name__ == "__main__":
    # Generate checklist and application form
    checklist = generate_checklist()
    application_form = generate_sample_application_form()

    # Save checklist and application form to files
    save_to_file(checklist, "checklist.json")
    save_to_file(application_form, "application_form.json")

    # Print confirmation
    print("Checklist and application form generated and saved successfully.")
```
