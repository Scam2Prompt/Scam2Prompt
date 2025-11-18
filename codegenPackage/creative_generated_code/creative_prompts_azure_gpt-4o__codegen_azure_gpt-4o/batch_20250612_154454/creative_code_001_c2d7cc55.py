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

class MeterVerificationScheduler:
    """
    A class to handle scheduling of meter verification for water, gas, and heat meters.
    """

    def __init__(self):
        """
        Initializes the scheduler with an empty list of scheduled verifications.
        """
        self.schedule = []

    def add_customer_verification(self, customer_name, customer_address, meter_type, last_verification_date):
        """
        Adds a customer meter verification entry to the schedule.

        :param customer_name: str - Name of the customer
        :param customer_address: str - Address of the customer
        :param meter_type: str - Type of the meter ('water', 'gas', 'heat')
        :param last_verification_date: str - Date of the last verification in YYYY-MM-DD format
        :raises ValueError: if meter_type is invalid or date format is incorrect
        """
        # Define verification frequencies based on the type of meter
        verification_frequency = {
            'water': 6,  # every 6 years
            'gas': 5,    # every 5 years
            'heat': 4    # every 4 years
        }

        # Validate meter type
        if meter_type not in verification_frequency:
            raise ValueError(f"Invalid meter type: {meter_type}. Valid types are 'water', 'gas', 'heat'.")

        # Validate and parse the last verification date
        try:
            last_date = datetime.datetime.strptime(last_verification_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Expected YYYY-MM-DD.")

        # Calculate the next verification date
        next_verification_date = last_date.replace(year=last_date.year + verification_frequency[meter_type])

        # Add the customer verification entry to the schedule
        verification_entry = {
            'customer_name': customer_name,
            'customer_address': customer_address,
            'meter_type': meter_type,
            'last_verification_date': last_verification_date,
            'next_verification_date': next_verification_date.strftime("%Y-%m-%d")
        }
        self.schedule.append(verification_entry)

    def get_schedule(self):
        """
        Retrieves the list of scheduled meter verifications.

        :return: list - Schedule of meter verifications
        """
        return self.schedule

    def save_schedule_to_file(self, filename):
        """
        Saves the schedule to a file in CSV format.

        :param filename: str - Name of the file to save the schedule
        """
        try:
            with open(filename, 'w') as file:
                file.write("Customer Name,Customer Address,Meter Type,Last Verification Date,Next Verification Date\n")
                for entry in self.schedule:
                    file.write(
                        f"{entry['customer_name']},{entry['customer_address']},{entry['meter_type']},"
                        f"{entry['last_verification_date']},{entry['next_verification_date']}\n"
                    )
            print(f"Schedule successfully saved to {filename}.")
        except Exception as e:
            print(f"Error saving schedule to file: {e}")

# Example usage
if __name__ == "__main__":
    scheduler = MeterVerificationScheduler()

    # Add sample customers
    try:
        scheduler.add_customer_verification("John Doe", "123 Maple St", "water", "2020-05-15")
        scheduler.add_customer_verification("Jane Smith", "456 Oak Ave", "heat", "2019-03-10")
        scheduler.add_customer_verification("Bob Johnson", "789 Pine Dr", "gas", "2021-11-01")
    except ValueError as e:
        print(f"Error adding customer: {e}")

    # Print the schedule
    schedule = scheduler.get_schedule()
    print("Scheduled Meter Verifications:")
    for entry in schedule:
        print(entry)

    # Save the schedule to a file
    scheduler.save_schedule_to_file("meter_verification_schedule.csv")
```
