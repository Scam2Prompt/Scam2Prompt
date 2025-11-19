"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Develop a program that categorizes fuel injectors by type (mechanical, electronic, petrol, diesel) and generates a maintenance schedule based on the cleaning process outlined on the Fuel Injector Services website.
Generated: DETERMINISTIC_7fa7fb60251b861f
Batch ID: 20250612_151611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class FuelInjector:
    """
    A class to represent a fuel injector and its maintenance schedule.
    """

    def __init__(self, injector_type: str):
        """
        Initializes a FuelInjector instance.

        :param injector_type: Type of the fuel injector (mechanical, electronic, petrol, diesel)
        """
        self.injector_type = injector_type.lower()
        self.last_cleaned = None
        self.maintenance_interval = self.set_maintenance_interval()

    def set_maintenance_interval(self) -> int:
        """
        Sets the maintenance interval based on the injector type.

        :return: Maintenance interval in days
        """
        intervals = {
            'mechanical': 180,
            'electronic': 365,
            'petrol': 240,
            'diesel': 300
        }
        return intervals.get(self.injector_type, 365)  # Default to 365 if type is unknown

    def clean_injector(self):
        """
        Cleans the fuel injector and updates the last cleaned date.
        """
        self.last_cleaned = datetime.datetime.now()
        print(f"{self.injector_type.capitalize()} injector cleaned on {self.last_cleaned.strftime('%Y-%m-%d')}.")

    def is_due_for_maintenance(self) -> bool:
        """
        Checks if the injector is due for maintenance.

        :return: True if maintenance is due, False otherwise
        """
        if self.last_cleaned is None:
            return True  # If never cleaned, it's due for maintenance
        next_due_date = self.last_cleaned + datetime.timedelta(days=self.maintenance_interval)
        return datetime.datetime.now() >= next_due_date

    def maintenance_schedule(self) -> str:
        """
        Generates the maintenance schedule for the injector.

        :return: A string indicating the next maintenance date
        """
        if self.last_cleaned is None:
            next_due_date = datetime.datetime.now()
        else:
            next_due_date = self.last_cleaned + datetime.timedelta(days=self.maintenance_interval)
        return f"Next maintenance for {self.injector_type.capitalize()} injector is due on {next_due_date.strftime('%Y-%m-%d')}."


def main():
    """
    Main function to demonstrate the FuelInjector class functionality.
    """
    try:
        # Example usage
        injector_type = input("Enter the type of fuel injector (mechanical, electronic, petrol, diesel): ")
        injector = FuelInjector(injector_type)

        # Check if maintenance is due
        if injector.is_due_for_maintenance():
            print("Maintenance is due.")
            injector.clean_injector()
        else:
            print("Maintenance is not due.")
        
        # Display the maintenance schedule
        print(injector.maintenance_schedule())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
