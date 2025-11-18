"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wufis.com
Prompt: Develop a system to include insurance coverage in pet-sitting reservations, as mentioned in the WUFIS platform.
Generated: DETERMINISTIC_fa4d758c399b6a42
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Optional

class PetSittingReservation:
    def __init__(self, reservation_id: int, pet_owner: str, pet_name: str, dates: List[str], insurance: Optional[Dict[str, float]] = None):
        """
        Initializes a pet-sitting reservation.

        :param reservation_id: Unique identifier for the reservation.
        :param pet_owner: Name of the pet owner.
        :param pet_name: Name of the pet.
        :param dates: List of dates for the pet-sitting service.
        :param insurance: Optional dictionary containing insurance details.
        """
        self.reservation_id = reservation_id
        self.pet_owner = pet_owner
        self.pet_name = pet_name
        self.dates = dates
        self.insurance = insurance if insurance is not None else {}

    def add_insurance(self, insurance_type: str, coverage_amount: float) -> None:
        """
        Adds insurance coverage to the reservation.

        :param insurance_type: Type of insurance (e.g., 'basic', 'premium').
        :param coverage_amount: Coverage amount for the insurance.
        """
        if coverage_amount <= 0:
            raise ValueError("Coverage amount must be greater than zero.")
        self.insurance[insurance_type] = coverage_amount

    def remove_insurance(self, insurance_type: str) -> None:
        """
        Removes insurance coverage from the reservation.

        :param insurance_type: Type of insurance to remove.
        """
        if insurance_type not in self.insurance:
            raise KeyError(f"No insurance of type '{insurance_type}' found.")
        del self.insurance[insurance_type]

    def get_total_cost(self) -> float:
        """
        Calculates the total cost of the reservation, including insurance.

        :return: Total cost of the reservation.
        """
        base_cost_per_day = 30.0
        total_cost = base_cost_per_day * len(self.dates)
        
        # Adding insurance costs
        total_cost += sum(self.insurance.values())
        
        return total_cost

    def __str__(self) -> str:
        """
        Returns a string representation of the reservation.

        :return: Detailed information about the reservation.
        """
        insurance_info = ', '.join([f"{k}: ${v:.2f}" for k, v in self.insurance.items()]) if self.insurance else "No insurance"
        return (f"Reservation ID: {self.reservation_id}\n"
                f"Pet Owner: {self.pet_owner}\n"
                f"Pet Name: {self.pet_name}\n"
                f"Dates: {', '.join(self.dates)}\n"
                f"Insurance: {insurance_info}\n"
                f"Total Cost: ${self.get_total_cost():.2f}")

# Example usage
if __name__ == "__main__":
    try:
        reservation = PetSittingReservation(1, "John Doe", "Fido", ["2023-10-01", "2023-10-02"])
        reservation.add_insurance("basic", 5.0)
        reservation.add_insurance("premium", 10.0)
        print(reservation)
        
        # Remove an insurance
        reservation.remove_insurance("basic")
        print(reservation)
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
