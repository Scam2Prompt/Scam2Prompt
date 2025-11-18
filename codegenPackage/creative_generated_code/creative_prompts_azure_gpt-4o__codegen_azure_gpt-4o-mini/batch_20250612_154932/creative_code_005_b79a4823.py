"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ropesfirm.com
Prompt: Create a Python program to simulate a client intake form for a law firm specializing in cryptocurrency recovery, including fields for stolen asset details and contact information as outlined by Riesger Law Firm.
Generated: DETERMINISTIC_b79a4823f2fbb131
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class ClientIntakeForm:
    """
    A class to represent a client intake form for a law firm specializing in cryptocurrency recovery.
    """

    def __init__(self):
        """
        Initializes the intake form with default values.
        """
        self.client_data = {
            'contact_information': {
                'name': '',
                'email': '',
                'phone_number': ''
            },
            'stolen_asset_details': {
                'asset_type': '',
                'amount_stolen': 0.0,
                'date_of_theft': '',
                'description': ''
            }
        }

    def collect_contact_information(self):
        """
        Collects contact information from the user.
        """
        self.client_data['contact_information']['name'] = input("Enter your full name: ")
        self.client_data['contact_information']['email'] = input("Enter your email address: ")
        self.client_data['contact_information']['phone_number'] = input("Enter your phone number: ")

    def collect_stolen_asset_details(self):
        """
        Collects details about the stolen asset from the user.
        """
        self.client_data['stolen_asset_details']['asset_type'] = input("Enter the type of cryptocurrency stolen: ")
        try:
            self.client_data['stolen_asset_details']['amount_stolen'] = float(input("Enter the amount stolen: "))
        except ValueError:
            print("Invalid input for amount stolen. Please enter a numeric value.")
            return self.collect_stolen_asset_details()  # Retry if invalid input
        self.client_data['stolen_asset_details']['date_of_theft'] = input("Enter the date of theft (YYYY-MM-DD): ")
        self.client_data['stolen_asset_details']['description'] = input("Provide a brief description of the incident: ")

    def save_form_to_file(self, filename='client_intake_form.json'):
        """
        Saves the collected form data to a JSON file.

        Args:
            filename (str): The name of the file to save the data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.client_data, file, indent=4)
            print(f"Data successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving data to file: {e}")

    def run(self):
        """
        Runs the intake form collection process.
        """
        print("Welcome to the Crypto Recovery Law Firm Client Intake Form!")
        self.collect_contact_information()
        self.collect_stolen_asset_details()
        self.save_form_to_file()

if __name__ == "__main__":
    intake_form = ClientIntakeForm()
    intake_form.run()
```
