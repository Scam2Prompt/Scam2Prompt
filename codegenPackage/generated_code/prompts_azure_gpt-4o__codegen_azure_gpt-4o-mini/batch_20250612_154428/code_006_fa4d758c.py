"""
Generated Code Metadata:
========================
Original URL: https://wufis.com
Prompt: Develop a system to include insurance coverage in pet-sitting reservations, as mentioned in the WUFIS platform.
Generated: DETERMINISTIC_fa4d758c399b6a42
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pet_sitting.py

class PetSittingReservation:
    """
    A class to represent a pet-sitting reservation with insurance coverage.
    """

    def __init__(self, pet_owner, pet_type, reservation_date, insurance_coverage=False):
        """
        Initializes a new pet-sitting reservation.

        :param pet_owner: str - Name of the pet owner
        :param pet_type: str - Type of pet (e.g., dog, cat)
        :param reservation_date: str - Date of the reservation in 'YYYY-MM-DD' format
        :param insurance_coverage: bool - Indicates if insurance coverage is included
        """
        self.pet_owner = pet_owner
        self.pet_type = pet_type
        self.reservation_date = reservation_date
        self.insurance_coverage = insurance_coverage

    def toggle_insurance(self):
        """
        Toggles the insurance coverage for the reservation.
        """
        self.insurance_coverage = not self.insurance_coverage

    def get_reservation_details(self):
        """
        Returns the details of the reservation.

        :return: dict - A dictionary containing reservation details
        """
        return {
            "pet_owner": self.pet_owner,
            "pet_type": self.pet_type,
            "reservation_date": self.reservation_date,
            "insurance_coverage": self.insurance_coverage
        }

    def validate_reservation(self):
        """
        Validates the reservation details.

        :raises ValueError: If any of the reservation details are invalid
        """
        if not self.pet_owner:
            raise ValueError("Pet owner name cannot be empty.")
        if not self.pet_type:
            raise ValueError("Pet type cannot be empty.")
        if not self.is_valid_date(self.reservation_date):
            raise ValueError("Invalid reservation date format. Use 'YYYY-MM-DD'.")

    @staticmethod
    def is_valid_date(date_str):
        """
        Validates the date format.

        :param date_str: str - Date string to validate
        :return: bool - True if valid, False otherwise
        """
        from datetime import datetime
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False


def main():
    """
    Main function to demonstrate the pet-sitting reservation system.
    """
    try:
        # Create a new reservation
        reservation = PetSittingReservation("John Doe", "Dog", "2023-10-15", True)

        # Validate the reservation
        reservation.validate_reservation()

        # Get and print reservation details
        details = reservation.get_reservation_details()
        print("Reservation Details:", details)

        # Toggle insurance coverage
        reservation.toggle_insurance()
        print("Updated Reservation Details:", reservation.get_reservation_details())

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
