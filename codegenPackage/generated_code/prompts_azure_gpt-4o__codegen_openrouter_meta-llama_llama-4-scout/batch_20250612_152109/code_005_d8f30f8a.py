"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Create a program that tracks car repair progress through the 3-step process described on Mechanics.ae (Service Inquiry, Car Pick-Up, Repair & Final Testing).
Generated: DETERMINISTIC_d8f30f8afde93d01
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from datetime import datetime

class RepairStatus(Enum):
    """Enum for tracking repair status"""
    SERVICE_INQUIRY = 1
    CAR_PICK_UP = 2
    REPAIR_AND_TESTING = 3
    COMPLETED = 4

class CarRepairTracker:
    """Class for tracking car repair progress"""

    def __init__(self):
        """Initialize an empty dictionary to store repair status"""
        self.repairs = {}

    def add_repair(self, vehicle_id):
        """Add a new repair entry"""
        if vehicle_id in self.repairs:
            print(f"Repair for vehicle {vehicle_id} already exists.")
            return

        self.repairs[vehicle_id] = {
            "status": RepairStatus.SERVICE_INQUIRY,
            "service_inquiry_date": None,
            "car_pick_up_date": None,
            "repair_start_date": None,
            "repair_end_date": None
        }
        print(f"Repair for vehicle {vehicle_id} added.")

    def update_status(self, vehicle_id, status):
        """Update the status of a repair"""
        if vehicle_id not in self.repairs:
            print(f"Repair for vehicle {vehicle_id} does not exist.")
            return

        if status == RepairStatus.SERVICE_INQUIRY:
            self.repairs[vehicle_id]["service_inquiry_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elif status == RepairStatus.CAR_PICK_UP:
            if self.repairs[vehicle_id]["status"] != RepairStatus.SERVICE_INQUIRY:
                print("Invalid status transition.")
                return
            self.repairs[vehicle_id]["car_pick_up_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elif status == RepairStatus.REPAIR_AND_TESTING:
            if self.repairs[vehicle_id]["status"] != RepairStatus.CAR_PICK_UP:
                print("Invalid status transition.")
                return
            self.repairs[vehicle_id]["repair_start_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elif status == RepairStatus.COMPLETED:
            if self.repairs[vehicle_id]["status"] != RepairStatus.REPAIR_AND_TESTING:
                print("Invalid status transition.")
                return
            self.repairs[vehicle_id]["repair_end_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.repairs[vehicle_id]["status"] = status
        print(f"Status of vehicle {vehicle_id} updated to {status.name}.")

    def get_repair_status(self, vehicle_id):
        """Get the current status of a repair"""
        if vehicle_id not in self.repairs:
            print(f"Repair for vehicle {vehicle_id} does not exist.")
            return

        status = self.repairs[vehicle_id]["status"]
        dates = {
            "Service Inquiry": self.repairs[vehicle_id]["service_inquiry_date"],
            "Car Pick-Up": self.repairs[vehicle_id]["car_pick_up_date"],
            "Repair Start": self.repairs[vehicle_id]["repair_start_date"],
            "Repair End": self.repairs[vehicle_id]["repair_end_date"]
        }

        print(f"Current status of vehicle {vehicle_id}: {status.name}")
        for event, date in dates.items():
            if date:
                print(f"{event}: {date}")

def main():
    tracker = CarRepairTracker()

    while True:
        print("\n1. Add repair")
        print("2. Update status")
        print("3. Get repair status")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            vehicle_id = input("Enter vehicle ID: ")
            tracker.add_repair(vehicle_id)
        elif choice == "2":
            vehicle_id = input("Enter vehicle ID: ")
            print("\n1. Service Inquiry")
            print("2. Car Pick-Up")
            print("3. Repair & Final Testing")
            print("4. Completed")

            status_choice = input("Choose a status: ")
            if status_choice == "1":
                tracker.update_status(vehicle_id, RepairStatus.SERVICE_INQUIRY)
            elif status_choice == "2":
                tracker.update_status(vehicle_id, RepairStatus.CAR_PICK_UP)
            elif status_choice == "3":
                tracker.update_status(vehicle_id, RepairStatus.REPAIR_AND_TESTING)
            elif status_choice == "4":
                tracker.update_status(vehicle_id, RepairStatus.COMPLETED)
        elif choice == "3":
            vehicle_id = input("Enter vehicle ID: ")
            tracker.get_repair_status(vehicle_id)
        elif choice == "4":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
```
