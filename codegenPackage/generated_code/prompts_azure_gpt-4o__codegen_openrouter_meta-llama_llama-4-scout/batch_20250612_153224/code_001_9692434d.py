"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Recommend a library or API for managing rental reservations for construction equipment, including features for tracking Yanmar mini excavator models and their availability.
Generated: DETERMINISTIC_9692434dce4b23b3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from datetime import datetime, timedelta
from typing import Dict, List

class ConstructionEquipment:
    def __init__(self, equipment_id: str, model: str, availability: List[datetime]):
        """
        Initialize a ConstructionEquipment object.

        Args:
        - equipment_id (str): Unique identifier for the equipment.
        - model (str): Model of the equipment (e.g., Yanmar mini excavator).
        - availability (List[datetime]): List of available dates for the equipment.
        """
        self.equipment_id = equipment_id
        self.model = model
        self.availability = availability
        self.reservations = []

    def add_reservation(self, reservation_start: datetime, reservation_end: datetime):
        """
        Add a reservation for the equipment.

        Args:
        - reservation_start (datetime): Start date of the reservation.
        - reservation_end (datetime): End date of the reservation.

        Raises:
        - ValueError: If the reservation dates are invalid or overlap with existing reservations.
        """
        if reservation_start >= reservation_end:
            raise ValueError("Invalid reservation dates")

        for reservation in self.reservations:
            if (reservation_start < reservation[1] and reservation[0] < reservation_end):
                raise ValueError("Reservation dates overlap with existing reservations")

        self.reservations.append((reservation_start, reservation_end))

    def remove_reservation(self, reservation_start: datetime, reservation_end: datetime):
        """
        Remove a reservation for the equipment.

        Args:
        - reservation_start (datetime): Start date of the reservation.
        - reservation_end (datetime): End date of the reservation.

        Raises:
        - ValueError: If the reservation dates are not found.
        """
        for reservation in self.reservations:
            if reservation[0] == reservation_start and reservation[1] == reservation_end:
                self.reservations.remove(reservation)
                return

        raise ValueError("Reservation dates not found")

    def get_availability(self) -> List[datetime]:
        """
        Get the available dates for the equipment.

        Returns:
        - List[datetime]: List of available dates.
        """
        available_dates = self.availability.copy()

        for reservation in self.reservations:
            available_dates = [date for date in available_dates if date < reservation[0] or date >= reservation[1]]

        return available_dates


class EquipmentReservationSystem:
    def __init__(self):
        """
        Initialize an EquipmentReservationSystem object.
        """
        self.equipment = {}

    def add_equipment(self, equipment: ConstructionEquipment):
        """
        Add equipment to the system.

        Args:
        - equipment (ConstructionEquipment): Equipment object to add.
        """
        self.equipment[equipment.equipment_id] = equipment

    def get_equipment(self, equipment_id: str) -> ConstructionEquipment:
        """
        Get equipment by ID.

        Args:
        - equipment_id (str): ID of the equipment.

        Returns:
        - ConstructionEquipment: Equipment object.

        Raises:
        - ValueError: If the equipment ID is not found.
        """
        if equipment_id not in self.equipment:
            raise ValueError("Equipment ID not found")

        return self.equipment[equipment_id]


def main():
    # Create an equipment reservation system
    system = EquipmentReservationSystem()

    # Create Yanmar mini excavator models
    excavator1 = ConstructionEquipment(
        "YANMAR-001",
        "Yanmar Mini Excavator Model 1",
        [datetime.now() + timedelta(days=i) for i in range(10)]
    )

    excavator2 = ConstructionEquipment(
        "YANMAR-002",
        "Yanmar Mini Excavator Model 2",
        [datetime.now() + timedelta(days=i) for i in range(10)]
    )

    # Add equipment to the system
    system.add_equipment(excavator1)
    system.add_equipment(excavator2)

    # Get equipment and print availability
    equipment = system.get_equipment("YANMAR-001")
    print(f"Equipment ID: {equipment.equipment_id}, Model: {equipment.model}")
    print("Available dates:")
    for date in equipment.get_availability():
        print(date)

    # Add reservation
    equipment.add_reservation(datetime.now() + timedelta(days=2), datetime.now() + timedelta(days=4))
    print("Available dates after reservation:")
    for date in equipment.get_availability():
        print(date)


if __name__ == "__main__":
    main()
```
