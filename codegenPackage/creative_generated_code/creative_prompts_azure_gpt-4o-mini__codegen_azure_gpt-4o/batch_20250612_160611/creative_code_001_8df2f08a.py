"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrium.sk
Prompt: Generate a Python script that automates the creation of a ready-made company registration process, similar to the corporate services offered by Arbitrium iustitia s.r.o.
Generated: DETERMINISTIC_8df2f08a6f86844f
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime
import os

class CompanyRegistration:
    """
    Automates the creation of a ready-made company registration process.
    """

    def __init__(self):
        self.company_details = {}

    def input_company_details(self):
        """
        Collects company details from the user.
        """
        # Collect necessary details for company registration
        self.company_details['company_name'] = input("Enter the company name: ").strip()
        self.company_details['registration_number'] = input("Enter the company registration number: ").strip()
        self.company_details['tax_id'] = input("Enter the Tax ID: ").strip()
        self.company_details['address'] = input("Enter the company address: ").strip()
        self.company_details['director_name'] = input("Enter the director's name: ").strip()
        self.company_details['incorporation_date'] = datetime.datetime.now().strftime('%Y-%m-%d')

    def validate_details(self):
        """
        Validates the company details provided by the user.
        """
        # Check for missing details
        for key, value in self.company_details.items():
            if not value:
                raise ValueError(f"Missing value for {key}. Please provide all required details.")

        # Validate Registration Number format (example: at least 8 alphanumeric characters)
        if len(self.company_details['registration_number']) < 8 or not self.company_details['registration_number'].isalnum():
            raise ValueError("Invalid Registration Number. It must be at least 8 alphanumeric characters.")

        # Validate Tax ID format (example: numeric only, 10 digits)
        if not self.company_details['tax_id'].isdigit() or len(self.company_details['tax_id']) != 10:
            raise ValueError("Invalid Tax ID. It must be numeric and 10 digits long.")

    def save_registration(self):
        """
        Saves company registration details to a JSON file.
        """
        # Generate a file name based on the company name
        file_name = f"{self.company_details['company_name'].replace(' ', '_').lower()}_registration.json"
        file_path = os.path.join(os.getcwd(), file_name)

        # Write the details to a JSON file
        try:
            with open(file_path, 'w') as file:
                json.dump(self.company_details, file, indent=4)
            print(f"Company registration details successfully saved to {file_path}")
        except Exception as e:
            print(f"An error occurred while saving registration details: {e}")

    def run(self):
        """
        Executes the company registration process.
        """
        try:
            self.input_company_details()
            self.validate_details()
            self.save_registration()
            print("Company registration process completed successfully.")
        except ValueError as ve:
            print(f"Validation Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Run the registration process
    registration_process = CompanyRegistration()
    registration_process.run()
```
