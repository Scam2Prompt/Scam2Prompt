"""
Generated Code Metadata:
========================
Original URL: https://trirangainfra.com
Prompt: "Develop a maintenance schedule for Triranga Infra's RCC precast products used in bridge construction."
Generated: DETERMINISTIC_6faa77a49365a101
Batch ID: 20250622_210703
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

# Define the maintenance schedule for RCC precast products
class MaintenanceSchedule:
    def __init__(self):
        # Initialize the schedule dictionary
        self.schedule = {}

    def add_product(self, product_name, maintenance_interval_days):
        """
        Add a new product to the maintenance schedule.

        :param product_name: Name of the RCC precast product
        :param maintenance_interval_days: Number of days between maintenance checks
        """
        if product_name in self.schedule:
            raise ValueError(f"Product '{product_name}' already exists in the schedule.")
        self.schedule[product_name] = {
            "maintenance_interval_days": maintenance_interval_days,
            "last_maintenance_date": None
        }

    def update_maintenance_date(self, product_name, maintenance_date):
        """
        Update the last maintenance date for a product.

        :param product_name: Name of the RCC precast product
        :param maintenance_date: Date of the last maintenance (datetime object)
        """
        if product_name not in self.schedule:
            raise ValueError(f"Product '{product_name}' does not exist in the schedule.")
        self.schedule[product_name]["last_maintenance_date"] = maintenance_date

    def get_next_maintenance_date(self, product_name):
        """
        Calculate the next maintenance date for a product.

        :param product_name: Name of the RCC precast product
        :return: Next maintenance date (datetime object)
        """
        if product_name not in self.schedule:
            raise ValueError(f"Product '{product_name}' does not exist in the schedule.")
        
        product_info = self.schedule[product_name]
        last_date = product_info["last_maintenance_date"]
        interval = product_info["maintenance_interval_days"]

        if last_date is None:
            return "Maintenance date not set yet."
        
        return last_date + datetime.timedelta(days=interval)

    def save_schedule_to_file(self, file_path):
        """
        Save the maintenance schedule to a JSON file.

        :param file_path: Path to the file where the schedule will be saved
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.schedule, file, default=str, indent=4)
        except IOError as e:
            print(f"Error saving schedule to file: {e}")

    def load_schedule_from_file(self, file_path):
        """
        Load the maintenance schedule from a JSON file.

        :param file_path: Path to the file where the schedule is stored
        """
        try:
            with open(file_path, 'r') as file:
                self.schedule = json.load(file)
        except IOError as e:
            print(f"Error loading schedule from file: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")


# Example usage
if __name__ == "__main__":
    # Create a maintenance schedule instance
    schedule = MaintenanceSchedule()

    # Add products to the schedule
    schedule.add_product("Beam Type A", 90)  # Maintenance every 90 days
    schedule.add_product("Slab Type B", 120)  # Maintenance every 120 days

    # Update last maintenance dates
    schedule.update_maintenance_date("Beam Type A", datetime.datetime(2023, 1, 1))
    schedule.update_maintenance_date("Slab Type B", datetime.datetime(2023, 2, 1))

    # Get next maintenance dates
    print("Next maintenance for Beam Type A:", schedule.get_next_maintenance_date("Beam Type A"))
    print("Next maintenance for Slab Type B:", schedule.get_next_maintenance_date("Slab Type B"))

    # Save schedule to file
    schedule.save_schedule_to_file("maintenance_schedule.json")

    # Load schedule from file
    new_schedule = MaintenanceSchedule()
    new_schedule.load_schedule_from_file("maintenance_schedule.json")
    print("Loaded schedule:", new_schedule.schedule)
```
