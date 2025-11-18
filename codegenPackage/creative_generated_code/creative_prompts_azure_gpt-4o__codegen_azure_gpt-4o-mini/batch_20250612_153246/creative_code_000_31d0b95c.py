"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sundancespasadvantage.com
Prompt: Write a Python script to simulate a dealer onboarding process for the Sundance Spas Retail Advantage program, including input fields for company name, location, and showroom details.
Generated: DETERMINISTIC_31d0b95c6185c719
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class DealerOnboarding:
    def __init__(self):
        """Initialize the dealer onboarding process."""
        self.dealer_info = {}

    def collect_information(self):
        """Collect dealer information from user input."""
        try:
            self.dealer_info['company_name'] = input("Enter the company name: ").strip()
            self.dealer_info['location'] = input("Enter the location: ").strip()
            self.dealer_info['showroom_details'] = input("Enter showroom details: ").strip()
            
            if not all(self.dealer_info.values()):
                raise ValueError("All fields must be filled.")

        except ValueError as e:
            print(f"Error: {e}")
            self.collect_information()  # Retry collecting information

    def save_information(self):
        """Save the dealer information to a JSON file."""
        try:
            with open('dealer_info.json', 'w') as json_file:
                json.dump(self.dealer_info, json_file, indent=4)
            print("Dealer information saved successfully.")
        except IOError as e:
            print(f"Error saving information to file: {e}")

    def run_onboarding(self):
        """Run the dealer onboarding process."""
        self.collect_information()
        self.save_information()

if __name__ == "__main__":
    onboarding_process = DealerOnboarding()
    onboarding_process.run_onboarding()
```
