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
# Import necessary modules
from datetime import datetime
from typing import Optional

class InsuranceCoverage:
    """
    Class to represent insurance coverage for pet-sitting reservations.
    """
    def __init__(self, coverage_amount: float, cost: float):
        """
        Initializes the insurance coverage with coverage amount and cost.

        :param coverage_amount: The amount covered by insurance (in USD).
        :param cost: The cost of the insurance (in USD).
        """
        self.coverage_amount = coverage_amount
        self.cost = cost

    def __repr__(self):
        return f"InsuranceCoverage(coverage_amount=${self.coverage_amount:.2f}, cost=${self.cost:.2f})"


class PetSittingReservation:
    """
    Class to represent a pet-sitting reservation with optional insurance coverage.
    """
    def __init__(self, pet_owner_name: str, pet_type: str, start_date: datetime, end_date: datetime, daily_rate: float):
        """
        Initializes the reservation details.

        :param pet_owner_name: Name of the pet owner.
        :param pet_type: Type of pet (e.g., Dog, Cat).
        :param start_date: Start date of the reservation.
        :param end_date: End date of the reservation.
        :param daily_rate: Daily rate for pet sitting (in USD).
        """
        self.pet_owner_name = pet_owner_name
        self.pet_type = pet_type
        self.start_date = start_date
        self.end_date = end_date
        self.daily_rate = daily_rate
        self.insurance_coverage: Optional[InsuranceCoverage] = None

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the reservation including insurance (if added).

        :return: Total cost (in USD).
        """
        total_days = (self.end_date - self.start_date).days
        if total_days <= 0:
            raise ValueError("End date must be after start date.")
        total_cost = total_days * self.daily_rate
        if self.insurance_coverage:
            total_cost += self.insurance_coverage.cost
        return total_cost

    def add_insurance(self, coverage_amount: float, cost: float):
        """
        Adds insurance coverage to the reservation.

        :param coverage_amount: Insurance coverage amount (in USD).
        :param cost: Cost of the insurance (in USD).
        """
        self.insurance_coverage = InsuranceCoverage(coverage_amount, cost)

    def __repr__(self):
        return (f"PetSittingReservation(pet_owner_name={self.pet_owner_name}, "
                f"pet_type={self.pet_type}, start_date={self.start_date.date()}, "
                f"end_date={self.end_date.date()}, daily_rate=${self.daily_rate:.2f}, "
                f"insurance_coverage={self.insurance_coverage})")


# Example usage
if __name__ == "__main__":
    # Create a new reservation
    try:
        reservation = PetSittingReservation(
            pet_owner_name="John Doe",
            pet_type="Dog",
            start_date=datetime(2023, 10, 1),
            end_date=datetime(2023, 10, 5),
            daily_rate=50.0,
        )

        # Add insurance to the reservation
        reservation.add_insurance(coverage_amount=1000.0, cost=15.0)

        # Print reservation details
        print(reservation)

        # Calculate total cost and print it
        total_cost = reservation.calculate_total_cost()
        print(f"Total cost: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
