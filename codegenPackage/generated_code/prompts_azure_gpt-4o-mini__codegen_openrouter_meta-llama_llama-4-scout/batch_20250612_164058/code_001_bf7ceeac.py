"""
Generated Code Metadata:
========================
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: Write a code snippet for a booking system that allows users to schedule windscreen repairs, inspired by the services offered at Cheap Windscreens Melbourne.
Generated: DETERMINISTIC_bf7ceeac45cde606
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum

# Define an Enum for repair status
class RepairStatus(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELLED = 4

# Define a class for Windscreen Repair
class WindscreenRepair:
    def __init__(self, customer_name, vehicle_type, appointment_time, repair_type):
        """
        Initialize a WindscreenRepair object.

        Args:
            customer_name (str): Name of the customer.
            vehicle_type (str): Type of vehicle.
            appointment_time (datetime): Scheduled appointment time.
            repair_type (str): Type of windscreen repair.
        """
        self.customer_name = customer_name
        self.vehicle_type = vehicle_type
        self.appointment_time = appointment_time
        self.repair_type = repair_type
        self.status = RepairStatus.PENDING

    def __str__(self):
        return f"Customer: {self.customer_name}, Vehicle: {self.vehicle_type}, Appointment Time: {self.appointment_time}, Repair Type: {self.repair_type}, Status: {self.status.name}"

# Define a class for Booking System
class BookingSystem:
    def __init__(self):
        """
        Initialize a BookingSystem object.
        """
        self.repairs = []

    def schedule_repair(self, customer_name, vehicle_type, appointment_time, repair_type):
        """
        Schedule a windscreen repair.

        Args:
            customer_name (str): Name of the customer.
            vehicle_type (str): Type of vehicle.
            appointment_time (datetime): Scheduled appointment time.
            repair_type (str): Type of windscreen repair.

        Returns:
            WindscreenRepair: The scheduled repair.
        """
        if appointment_time < datetime.now():
            raise ValueError("Appointment time must be in the future")

        repair = WindscreenRepair(customer_name, vehicle_type, appointment_time, repair_type)
        self.repairs.append(repair)
        return repair

    def cancel_repair(self, repair):
        """
        Cancel a scheduled windscreen repair.

        Args:
            repair (WindscreenRepair): The repair to cancel.

        Raises:
            ValueError: If the repair is not found or has already been cancelled/completed.
        """
        if repair not in self.repairs:
            raise ValueError("Repair not found")
        if repair.status != RepairStatus.PENDING:
            raise ValueError("Repair has already been cancelled or completed")

        repair.status = RepairStatus.CANCELLED

    def update_repair_status(self, repair, status):
        """
        Update the status of a windscreen repair.

        Args:
            repair (WindscreenRepair): The repair to update.
            status (RepairStatus): The new status.

        Raises:
            ValueError: If the repair is not found.
        """
        if repair not in self.repairs:
            raise ValueError("Repair not found")

        repair.status = status

    def get_repairs(self):
        """
        Get all scheduled windscreen repairs.

        Returns:
            list[WindscreenRepair]: A list of all scheduled repairs.
        """
        return self.repairs

def main():
    booking_system = BookingSystem()

    # Schedule a repair
    appointment_time = datetime.now() + timedelta(days=1)
    repair = booking_system.schedule_repair("John Doe", "Toyota Camry", appointment_time, "Windscreen replacement")
    print(repair)

    # Get all repairs
    repairs = booking_system.get_repairs()
    for r in repairs:
        print(r)

    # Cancel a repair
    booking_system.cancel_repair(repair)
    print(repair)

if __name__ == "__main__":
    main()
```
