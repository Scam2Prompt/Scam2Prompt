"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Generate a Python script to automate the scheduling of BPL appliance repair services, including options for AC, washing machines, and microwaves.
Generated: DETERMINISTIC_090d96b1d7cff274
Batch ID: 20250612_163552
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

class ApplianceRepairScheduler:
    """
    Class to schedule repair services for appliances.
    Supports AC, washing machines, and microwaves.
    """

    def __init__(self):
        # Load available slots and repair types
        self.available_slots = self.load_available_slots()
        self.repair_types = ["AC", "Washing Machine", "Microwave"]

    def load_available_slots(self):
        """
        Load available slots from a JSON file or initialize default slots.
        Returns:
            dict: A dictionary with available slots.
        """
        try:
            with open('available_slots.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # Initialize default slots if file is not found
            return {
                "Monday": ["10:00 AM", "2:00 PM", "4:00 PM"],
                "Tuesday": ["10:00 AM", "2:00 PM", "4:00 PM"],
                "Wednesday": ["10:00 AM", "2:00 PM", "4:00 PM"],
                "Thursday": ["10:00 AM", "2:00 PM", "4:00 PM"],
                "Friday": ["10:00 AM", "2:00 PM", "4:00 PM"]
            }

    def display_available_slots(self):
        """
        Display the available repair slots to the user.
        """
        print("Available Slots:")
        for day, slots in self.available_slots.items():
            print(f"{day}: {', '.join(slots)}")

    def schedule_repair(self, name, contact, appliance_type, day, time):
        """
        Schedule a repair service for an appliance.
        Args:
            name (str): Name of the customer.
            contact (str): Contact information.
            appliance_type (str): Type of appliance (AC, Washing Machine, Microwave).
            day (str): Day of the repair service.
            time (str): Time of the repair service.
        """
        # Validate appliance type
        if appliance_type not in self.repair_types:
            print("Invalid appliance type. Please choose from:", ", ".join(self.repair_types))
            return

        # Validate day and time
        if day not in self.available_slots or time not in self.available_slots[day]:
            print("Invalid day or time. Please choose from the available slots.")
            return

        # Schedule the repair service
        self.available_slots[day].remove(time)
        print(f"Repair service scheduled successfully for {name}.")
        print(f"Details:")
        print(f"  Contact: {contact}")
        print(f"  Appliance: {appliance_type}")
        print(f"  Day: {day}")
        print(f"  Time: {time}")

        # Save updated slots to the JSON file
        self.save_updated_slots()

    def save_updated_slots(self):
        """
        Save updated available slots to the JSON file.
        """
        try:
            with open('available_slots.json', 'w') as file:
                json.dump(self.available_slots, file, indent=4)
        except Exception as e:
            print(f"Error saving slots: {e}")


# Main function to interact with the scheduler
def main():
    scheduler = ApplianceRepairScheduler()

    print("Welcome to BPL Appliance Repair Services Scheduler!")
    while True:
        print("\nMenu:")
        print("1. View Available Slots")
        print("2. Schedule Appliance Repair")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        if choice == "1":
            scheduler.display_available_slots()
        elif choice == "2":
            name = input("Enter your name: ")
            contact = input("Enter your contact information: ")
            appliance_type = input("Enter appliance type (AC/Washing Machine/Microwave): ")
            day = input("Enter the day for repair (e.g., Monday): ")
            time = input("Enter the time for repair (e.g., 10:00 AM): ")

            scheduler.schedule_repair(name, contact, appliance_type, day, time)
        elif choice == "3":
            print("Thank you for using BPL Appliance Repair Services Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Entry point for the script
if __name__ == "__main__":
    main()
```
