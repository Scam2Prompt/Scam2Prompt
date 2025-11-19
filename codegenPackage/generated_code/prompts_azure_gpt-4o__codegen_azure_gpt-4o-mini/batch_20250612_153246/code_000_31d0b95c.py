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

class DealerOnboarding:
    def __init__(self):
        """Initialize the dealer onboarding process with default values."""
        self.dealer_info = {
            "company_name": "",
            "location": "",
            "showroom_details": ""
        }

    def collect_input(self):
        """Collect dealer information from user input."""
        try:
            self.dealer_info["company_name"] = input("Enter the company name: ").strip()
            self.dealer_info["location"] = input("Enter the location: ").strip()
            self.dealer_info["showroom_details"] = input("Enter showroom details: ").strip()

            # Validate inputs
            self.validate_input()
        except Exception as e:
            print(f"An error occurred while collecting input: {e}")

    def validate_input(self):
        """Validate the collected input to ensure all fields are filled."""
        for key, value in self.dealer_info.items():
            if not value:
                raise ValueError(f"{key.replace('_', ' ').title()} cannot be empty.")

    def save_to_file(self, filename='dealer_info.json'):
        """Save the dealer information to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.dealer_info, file, indent=4)
            print(f"Dealer information saved to {filename}.")
        except IOError as e:
            print(f"An error occurred while saving to file: {e}")

    def run_onboarding(self):
        """Run the dealer onboarding process."""
        print("Welcome to the Sundance Spas Retail Advantage Dealer Onboarding Process.")
        self.collect_input()
        self.save_to_file()

if __name__ == "__main__":
    onboarding_process = DealerOnboarding()
    onboarding_process.run_onboarding()
```
