"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Create a Python script that simulates the process of scheduling meter verification for water, gas, and heat meters, including fields for customer details, meter type, and verification frequency (e.g., every four years for heat meters).
Generated: DETERMINISTIC_c2d7cc55eca94373
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class MeterVerificationScheduler:
    def __init__(self):
        """Initialize the scheduler with an empty list of verifications."""
        self.verifications = []

    def add_verification(self, customer_name, customer_address, meter_type, verification_frequency):
        """
        Add a new meter verification to the schedule.

        :param customer_name: Name of the customer
        :param customer_address: Address of the customer
        :param meter_type: Type of meter (water, gas, heat)
        :param verification_frequency: Frequency of verification in years
        """
        try:
            # Validate input parameters
            if not isinstance(customer_name, str) or not customer_name:
                raise ValueError("Customer name must be a non-empty string.")
            if not isinstance(customer_address, str) or not customer_address:
                raise ValueError("Customer address must be a non-empty string.")
            if meter_type not in ['water', 'gas', 'heat']:
                raise ValueError("Meter type must be one of: 'water', 'gas', 'heat'.")
            if not isinstance(verification_frequency, int) or verification_frequency <= 0:
                raise ValueError("Verification frequency must be a positive integer.")

            # Calculate the next verification date
            next_verification_date = datetime.datetime.now() + datetime.timedelta(days=verification_frequency * 365)

            # Create a verification record
            verification_record = {
                'customer_name': customer_name,
                'customer_address': customer_address,
                'meter_type': meter_type,
                'verification_frequency': verification_frequency,
                'next_verification_date': next_verification_date.strftime('%Y-%m-%d')
            }

            # Add the record to the list
            self.verifications.append(verification_record)
            print(f"Added verification for {customer_name}.")

        except Exception as e:
            print(f"Error adding verification: {e}")

    def save_schedule(self, filename):
        """
        Save the current verification schedule to a JSON file.

        :param filename: Name of the file to save the schedule
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.verifications, file, indent=4)
            print(f"Verification schedule saved to {filename}.")
        except IOError as e:
            print(f"Error saving schedule to file: {e}")

    def load_schedule(self, filename):
        """
        Load a verification schedule from a JSON file.

        :param filename: Name of the file to load the schedule from
        """
        try:
            with open(filename, 'r') as file:
                self.verifications = json.load(file)
            print(f"Verification schedule loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading schedule from file: {e}")

    def display_schedule(self):
        """Display the current verification schedule."""
        if not self.verifications:
            print("No verifications scheduled.")
            return

        print("Current Meter Verification Schedule:")
        for verification in self.verifications:
            print(f"Customer: {verification['customer_name']}, "
                  f"Address: {verification['customer_address']}, "
                  f"Meter Type: {verification['meter_type']}, "
                  f"Next Verification: {verification['next_verification_date']}")

if __name__ == "__main__":
    scheduler = MeterVerificationScheduler()
    
    # Example usage
    scheduler.add_verification("John Doe", "123 Elm St", "water", 4)
    scheduler.add_verification("Jane Smith", "456 Oak St", "heat", 4)
    scheduler.display_schedule()
    scheduler.save_schedule("verification_schedule.json")
    scheduler.load_schedule("verification_schedule.json")
    scheduler.display_schedule()
```
