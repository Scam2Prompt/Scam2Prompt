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
import json

class DocumentChecklist:
    """
    A class to represent a checklist of required documents for temporary registration in Adygea, Russia.
    """

    def __init__(self):
        """
        Initializes the checklist with required documents.
        """
        self.documents = [
            "Passport (original and copy)",
            "Application form for temporary registration",
            "Proof of residence (rental agreement or property ownership)",
            "Migration card (if applicable)",
            "Photos (size 3x4 cm, usually 2 copies)",
            "Medical insurance (if applicable)",
            "Proof of income (if applicable)"
        ]

    def get_checklist(self):
        """
        Returns the checklist of required documents.
        """
        return self.documents

    def save_checklist_to_file(self, filename):
        """
        Saves the checklist to a JSON file.

        :param filename: The name of the file to save the checklist.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.documents, file, ensure_ascii=False, indent=4)
            print(f"Checklist saved to {filename}")
        except IOError as e:
            print(f"Error saving checklist to file: {e}")

class ApplicationForm:
    """
    A class to represent a sample application form for temporary registration.
    """

    def __init__(self):
        """
        Initializes the application form with default fields.
        """
        self.fields = {
            "Full Name": "",
            "Date of Birth": "",
            "Passport Number": "",
            "Address of Temporary Residence": "",
            "Contact Number": "",
            "Email": ""
        }

    def fill_form(self, **kwargs):
        """
        Fills the application form with provided data.

        :param kwargs: Key-value pairs of form fields and their values.
        """
        for key, value in kwargs.items():
            if key in self.fields:
                self.fields[key] = value
            else:
                print(f"Warning: {key} is not a valid field.")

    def display_form(self):
        """
        Displays the filled application form.
        """
        print("Application Form for Temporary Registration:")
        for field, value in self.fields.items():
            print(f"{field}: {value}")

# Example usage
if __name__ == "__main__":
    # Create a document checklist
    checklist = DocumentChecklist()
    print("Required Documents for Temporary Registration:")
    for doc in checklist.get_checklist():
        print(f"- {doc}")

    # Save the checklist to a file
    checklist.save_checklist_to_file("adygea_registration_checklist.json")

    # Create and fill an application form
    application_form = ApplicationForm()
    application_form.fill_form(
        Full_Name="John Doe",
        Date_of_Birth="1990-01-01",
        Passport_Number="123456789",
        Address_of_Temporary_Residence="123 Main St, Adygea",
        Contact_Number="+7 123 456 7890",
        Email="johndoe@example.com"
    )
    
    # Display the filled application form
    application_form.display_form()
```
