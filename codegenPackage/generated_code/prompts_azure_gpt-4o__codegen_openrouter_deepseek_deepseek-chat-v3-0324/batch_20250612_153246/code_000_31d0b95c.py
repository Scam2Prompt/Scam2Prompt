"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Write a Python script to simulate a dealer onboarding process for the Sundance Spas Retail Advantage program, including input fields for company name, location, and showroom details.
Generated: DETERMINISTIC_31d0b95c6185c719
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime

class DealerOnboarding:
    """
    Simulates the dealer onboarding process for Sundance Spas Retail Advantage program.
    """
    
    def __init__(self):
        self.dealer_data = {
            "company_name": "",
            "location": {
                "address": "",
                "city": "",
                "state": "",
                "zip_code": "",
                "country": ""
            },
            "showroom_details": {
                "has_showroom": False,
                "showroom_size": "",
                "showroom_address": "",
                "showroom_city": "",
                "showroom_state": "",
                "showroom_zip_code": "",
                "showroom_country": ""
            },
            "contact": {
                "primary_contact_name": "",
                "primary_contact_email": "",
                "primary_contact_phone": ""
            },
            "onboarding_date": ""
        }
    
    def get_input(self, prompt, required=True):
        """
        Get user input with validation for required fields.
        """
        while True:
            user_input = input(prompt).strip()
            if required and not user_input:
                print("This field is required. Please try again.")
            else:
                return user_input
    
    def get_yes_no_input(self, prompt):
        """
        Get yes/no input from user and return boolean.
        """
        while True:
            response = input(f"{prompt} (y/n): ").strip().lower()
            if response in ('y', 'yes'):
                return True
            elif response in ('n', 'no'):
                return False
            else:
                print("Please enter 'y' or 'n'.")
    
    def collect_company_info(self):
        """
        Collect basic company information.
        """
        print("\n=== Company Information ===")
        self.dealer_data["company_name"] = self.get_input("Company Name: ")
    
    def collect_location_info(self):
        """
        Collect location information.
        """
        print("\n=== Location Information ===")
        location = self.dealer_data["location"]
        location["address"] = self.get_input("Address: ")
        location["city"] = self.get_input("City: ")
        location["state"] = self.get_input("State/Province: ")
        location["zip_code"] = self.get_input("Zip/Postal Code: ")
        location["country"] = self.get_input("Country: ")
    
    def collect_showroom_info(self):
        """
        Collect showroom information if applicable.
        """
        print("\n=== Showroom Information ===")
        showroom = self.dealer_data["showroom_details"]
        showroom["has_showroom"] = self.get_yes_no_input("Do you have a showroom?")
        
        if showroom["has_showroom"]:
            showroom["showroom_size"] = self.get_input("Showroom size (sq ft): ")
            showroom["showroom_address"] = self.get_input("Showroom Address (if different from main location): ", required=False)
            showroom["showroom_city"] = self.get_input("Showroom City: ")
            showroom["showroom_state"] = self.get_input("Showroom State/Province: ")
            showroom["showroom_zip_code"] = self.get_input("Showroom Zip/Postal Code: ")
            showroom["showroom_country"] = self.get_input("Showroom Country: ")
    
    def collect_contact_info(self):
        """
        Collect primary contact information.
        """
        print("\n=== Primary Contact Information ===")
        contact = self.dealer_data["contact"]
        contact["primary_contact_name"] = self.get_input("Primary Contact Name: ")
        contact["primary_contact_email"] = self.get_input("Primary Contact Email: ")
        contact["primary_contact_phone"] = self.get_input("Primary Contact Phone: ")
    
    def save_to_file(self):
        """
        Save dealer data to a JSON file with timestamp.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"dealer_onboarding_{timestamp}.json"
        
        # Create output directory if it doesn't exist
        os.makedirs("onboarding_data", exist_ok=True)
        
        filepath = os.path.join("onboarding_data", filename)
        
        try:
            with open(filepath, 'w') as f:
                json.dump(self.dealer_data, f, indent=4)
            print(f"\nOnboarding data saved successfully to {filepath}")
        except Exception as e:
            print(f"\nError saving file: {e}")
    
    def run_onboarding(self):
        """
        Run the complete onboarding process.
        """
        print("Welcome to Sundance Spas Retail Advantage Dealer Onboarding\n")
        
        self.collect_company_info()
        self.collect_location_info()
        self.collect_showroom_info()
        self.collect_contact_info()
        
        # Add onboarding date
        self.dealer_data["onboarding_date"] = datetime.now().strftime("%Y-%m-%d")
        
        # Display summary
        print("\n=== Onboarding Summary ===")
        print(json.dumps(self.dealer_data, indent=4))
        
        # Confirm and save
        if self.get_yes_no_input("\nWould you like to save this information?"):
            self.save_to_file()
        else:
            print("\nOnboarding data not saved.")

if __name__ == "__main__":
    onboarding = DealerOnboarding()
    onboarding.run_onboarding()
```
