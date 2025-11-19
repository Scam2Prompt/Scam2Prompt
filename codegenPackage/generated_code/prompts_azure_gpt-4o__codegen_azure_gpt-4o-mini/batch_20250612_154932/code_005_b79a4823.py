"""
Generated Code Metadata:
========================
Original URL: https://ropesfirm.com
Prompt: Create a Python program to simulate a client intake form for a law firm specializing in cryptocurrency recovery, including fields for stolen asset details and contact information as outlined by Riesger Law Firm.
Generated: DETERMINISTIC_b79a4823f2fbb131
Batch ID: 20250612_154932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class ClientIntakeForm:
    def __init__(self):
        """Initialize the client intake form with default values."""
        self.client_info = {
            "name": "",
            "email": "",
            "phone": "",
            "stolen_asset_details": {
                "asset_type": "",
                "amount": 0.0,
                "date_of_theft": "",
                "description": ""
            }
        }

    def collect_client_info(self):
        """Collect client information through user input."""
        try:
            self.client_info["name"] = input("Enter your full name: ")
            self.client_info["email"] = input("Enter your email address: ")
            self.client_info["phone"] = input("Enter your phone number: ")

            # Collect stolen asset details
            self.client_info["stolen_asset_details"]["asset_type"] = input("Enter the type of stolen asset (e.g., Bitcoin, Ethereum): ")
            self.client_info["stolen_asset_details"]["amount"] = float(input("Enter the amount of stolen asset: "))
            self.client_info["stolen_asset_details"]["date_of_theft"] = input("Enter the date of theft (YYYY-MM-DD): ")
            self.client_info["stolen_asset_details"]["description"] = input("Provide a brief description of the theft: ")

        except ValueError as e:
            print(f"Error in input: {e}. Please ensure you enter the correct data types.")
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False
        
        return True

    def save_to_file(self, filename='client_intake_form.json'):
        """Save the collected client information to a JSON file."""
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.client_info, json_file, indent=4)
            print(f"Client information saved successfully to {filename}.")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def run(self):
        """Run the client intake form process."""
        print("Welcome to the Cryptocurrency Recovery Client Intake Form.")
        if self.collect_client_info():
            self.save_to_file()

if __name__ == "__main__":
    form = ClientIntakeForm()
    form.run()
```
