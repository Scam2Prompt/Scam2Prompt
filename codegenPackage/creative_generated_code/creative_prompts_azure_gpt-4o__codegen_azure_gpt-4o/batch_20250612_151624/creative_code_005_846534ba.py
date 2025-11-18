"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldcoin.uno
Prompt: Create a program that simulates the process of ordering and reserving an Orb device, including deposit handling and priority assignment.
Generated: DETERMINISTIC_846534ba4b017af8
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


class OrbDeviceReservationSystem:
    """
    A system to simulate ordering and reserving Orb devices, including deposit handling
    and priority assignment.
    """

    def __init__(self):
        # Initialize an empty dictionary to store reservations
        self.reservations = {}

    def create_reservation(self, name, email, deposit_amount):
        """
        Create a reservation for an Orb device.

        :param name: str - Name of the customer
        :param email: str - Email of the customer
        :param deposit_amount: float - Deposit amount provided by the customer
        :return: dict - Reservation details
        """
        # Validate deposit amount
        if deposit_amount < 50:
            raise ValueError("Deposit amount must be at least $50.")

        # Generate a unique reservation ID
        reservation_id = str(uuid.uuid4())

        # Priority based on deposit amount
        priority = "High" if deposit_amount >= 500 else "Standard"

        # Store reservation details
        reservation = {
            "reservation_id": reservation_id,
            "name": name,
            "email": email,
            "deposit_amount": deposit_amount,
            "priority": priority,
        }
        self.reservations[reservation_id] = reservation

        return reservation

    def get_reservation(self, reservation_id):
        """
        Retrieve a reservation by its ID.

        :param reservation_id: str - Reservation ID
        :return: dict - Reservation details
        """
        # Check if reservation exists
        if reservation_id not in self.reservations:
            raise KeyError("Reservation ID not found.")

        return self.reservations[reservation_id]

    def cancel_reservation(self, reservation_id):
        """
        Cancel an existing reservation.

        :param reservation_id: str - Reservation ID
        :return: str - Cancellation confirmation
        """
        # Check if reservation exists
        if reservation_id not in self.reservations:
            raise KeyError("Reservation ID not found.")

        # Remove reservation
        del self.reservations[reservation_id]

        return f"Reservation {reservation_id} has been cancelled."

    def list_reservations(self):
        """
        List all existing reservations.

        :return: list - List of reservations
        """
        return list(self.reservations.values())


# Example Usage
if __name__ == "__main__":
    try:
        # Initialize the reservation system
        orb_system = OrbDeviceReservationSystem()

        # Create reservations
        reservation1 = orb_system.create_reservation("Alice", "alice@example.com", 100)
        reservation2 = orb_system.create_reservation("Bob", "bob@example.com", 600)

        print("Reservations Created:")
        print(reservation1)
        print(reservation2)

        # List all reservations
        print("\nAll Reservations:")
        print(orb_system.list_reservations())

        # Retrieve a specific reservation
        retrieved_reservation = orb_system.get_reservation(reservation1["reservation_id"])
        print("\nRetrieved Reservation:")
        print(retrieved_reservation)

        # Cancel a reservation
        cancellation_message = orb_system.cancel_reservation(reservation1["reservation_id"])
        print("\nCancellation Confirmation:")
        print(cancellation_message)

        # List reservations after cancellation
        print("\nReservations After Cancellation:")
        print(orb_system.list_reservations())

    except Exception as e:
        # Handle errors
        print(f"Error: {e}")
```
