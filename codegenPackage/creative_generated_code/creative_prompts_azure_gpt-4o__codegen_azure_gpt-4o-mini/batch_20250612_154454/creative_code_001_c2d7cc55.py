"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poverka-gazvoda.ru
Prompt: Create a Python script that simulates the process of scheduling meter verification for water, gas, and heat meters, including fields for customer details, meter type, and verification frequency (e.g., every four years for heat meters).
Generated: DETERMINISTIC_c2d7cc55eca94373
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import os

class MeterVerificationScheduler:
    """A class to simulate scheduling meter verification for water, gas, and heat meters."""

    def __init__(self):
        self.schedule = []
        self.load_schedule()

    def load_schedule(self):
        """Load existing schedule from a JSON file if it exists."""
        if os.path.exists('meter_verification_schedule.json'):
            with open('meter_verification_schedule.json', 'r') as file:
                self.schedule = json.load(file)

    def save_schedule(self):
        """Save the current schedule to a JSON file."""
        with open('meter_verification_schedule.json', 'w') as file:
            json.dump(self.schedule, file, indent=4)

    def add_verification(self, customer_name, meter_type, verification_frequency):
        """Add a verification schedule for a customer.

        Args:
            customer_name (str): The name of the customer.
            meter_type (str): The type of the meter (water, gas, or heat).
            verification_frequency (int): The frequency for verification in years.
        """
        if meter_type not in ['water', 'gas', 'heat']:
            raise ValueError("Invalid meter type. Choose from 'water', 'gas', or 'heat'.")

        verification_date = datetime.date.today() + datetime.timedelta(days=verification_frequency * 365)
        verification_entry = {
            'customer_name': customer_name,
            'meter_type': meter_type,
            'verification_date': verification_date.isoformat(),
            'frequency_years': verification_frequency
        }
        self.schedule.append(verification_entry)
        self.save_schedule()
        print(f"Verification scheduled for {customer_name} ({meter_type}) on {verification_date}.")

    def view_schedule(self):
        """Display the current verification schedule."""
        if not self.schedule:
            print("No verifications scheduled.")
            return

        print("Meter Verification Schedule:")
        for entry in self.schedule:
            print(f"Customer: {entry['customer_name']}, "
                  f"Meter Type: {entry['meter_type']}, "
                  f"Next Verification: {entry['verification_date']}, "
                  f"Frequency: every {entry['frequency_years']} years")

def main():
    """Main function to run the meter verification scheduler."""
    scheduler = MeterVerificationScheduler()

    while True:
        print("\nMeter Verification Scheduler")
        print("1. Schedule Verification")
        print("2. View Schedule")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                customer_name = input("Enter customer name: ")
                meter_type = input("Enter meter type (water, gas, heat): ").lower()
                verification_frequency = int(input("Enter verification frequency (in years): "))
                scheduler.add_verification(customer_name, meter_type, verification_frequency)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '2':
            scheduler.view_schedule()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
