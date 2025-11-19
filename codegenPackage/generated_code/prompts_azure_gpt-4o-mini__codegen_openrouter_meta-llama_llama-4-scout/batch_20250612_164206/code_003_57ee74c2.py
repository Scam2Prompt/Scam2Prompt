"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Provide a sample code to log and track the verification dates of water and heat meters, ensuring compliance with the regulations highlighted on the webpage.
Generated: DETERMINISTIC_57ee74c293733c6e
Batch ID: 20250612_164206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(filename='meter_verification.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Meter:
    def __init__(self, meter_type, verification_date):
        """
        Initialize a Meter object.

        Args:
            meter_type (str): Type of meter (water or heat).
            verification_date (str): Verification date in YYYY-MM-DD format.
        """
        self.meter_type = meter_type
        self.verification_date = datetime.strptime(verification_date, '%Y-%m-%d')

    def __str__(self):
        return f"{self.meter_type.capitalize()} meter verified on {self.verification_date.strftime('%Y-%m-%d')}"

class MeterTracker:
    def __init__(self):
        """
        Initialize a MeterTracker object.
        """
        self.meters = {}

    def add_meter(self, meter):
        """
        Add a meter to the tracker.

        Args:
            meter (Meter): Meter object to add.

        Raises:
            ValueError: If a meter of the same type already exists.
        """
        if meter.meter_type in self.meters:
            raise ValueError(f"A {meter.meter_type} meter already exists.")
        self.meters[meter.meter_type] = meter
        logging.info(f"Added {meter}")

    def update_verification_date(self, meter_type, new_verification_date):
        """
        Update the verification date of a meter.

        Args:
            meter_type (str): Type of meter to update.
            new_verification_date (str): New verification date in YYYY-MM-DD format.

        Raises:
            ValueError: If the meter type does not exist or the new verification date is invalid.
        """
        if meter_type not in self.meters:
            raise ValueError(f"No {meter_type} meter found.")
        try:
            new_date = datetime.strptime(new_verification_date, '%Y-%m-%d')
            self.meters[meter_type].verification_date = new_date
            logging.info(f"Updated {meter_type} meter verification date to {new_verification_date}")
        except ValueError:
            raise ValueError("Invalid verification date format. Use YYYY-MM-DD.")

    def get_verification_date(self, meter_type):
        """
        Get the verification date of a meter.

        Args:
            meter_type (str): Type of meter.

        Returns:
            str: Verification date in YYYY-MM-DD format.

        Raises:
            ValueError: If the meter type does not exist.
        """
        if meter_type not in self.meters:
            raise ValueError(f"No {meter_type} meter found.")
        return self.meters[meter_type].verification_date.strftime('%Y-%m-%d')

def main():
    tracker = MeterTracker()

    while True:
        print("\n1. Add water meter")
        print("2. Add heat meter")
        print("3. Update water meter verification date")
        print("4. Update heat meter verification date")
        print("5. Get water meter verification date")
        print("6. Get heat meter verification date")
        print("7. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                verification_date = input("Enter water meter verification date (YYYY-MM-DD): ")
                tracker.add_meter(Meter('water', verification_date))
            elif choice == "2":
                verification_date = input("Enter heat meter verification date (YYYY-MM-DD): ")
                tracker.add_meter(Meter('heat', verification_date))
            elif choice == "3":
                new_verification_date = input("Enter new water meter verification date (YYYY-MM-DD): ")
                tracker.update_verification_date('water', new_verification_date)
            elif choice == "4":
                new_verification_date = input("Enter new heat meter verification date (YYYY-MM-DD): ")
                tracker.update_verification_date('heat', new_verification_date)
            elif choice == "5":
                print(tracker.get_verification_date('water'))
            elif choice == "6":
                print(tracker.get_verification_date('heat'))
            elif choice == "7":
                break
            else:
                print("Invalid option. Please choose a valid option.")
        except ValueError as e:
            logging.error(f"Error: {e}")
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
