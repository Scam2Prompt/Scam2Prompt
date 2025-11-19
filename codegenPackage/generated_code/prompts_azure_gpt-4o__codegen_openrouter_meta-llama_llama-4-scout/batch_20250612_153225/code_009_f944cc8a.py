"""
Generated Code Metadata:
========================
Original URL: https://innovarenting.com
Prompt: Write a program to generate personalized renting plans for businesses based on their fleet size, operational needs, and budget, inspired by Innova Renting's tailored solutions.
Generated: DETERMINISTIC_f944cc8a9b7c85a0
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict

class RentalDuration(Enum):
    """Rental duration options"""
    MONTHLY = 1
    QUARTERLY = 3
    YEARLY = 12

class VehicleType(Enum):
    """Vehicle type options"""
    SEDAN = 1
    SUV = 2
    TRUCK = 3

class RentalPlan:
    """Represents a personalized rental plan"""
    def __init__(self, fleet_size: int, vehicle_type: VehicleType, rental_duration: RentalDuration, budget: float):
        self.fleet_size = fleet_size
        self.vehicle_type = vehicle_type
        self.rental_duration = rental_duration
        self.budget = budget
        self.plan_details = self.generate_plan()

    def generate_plan(self) -> Dict:
        """Generates the rental plan details"""
        base_rates = {
            VehicleType.SEDAN: 500,
            VehicleType.SUV: 750,
            VehicleType.TRUCK: 1000
        }

        discounts = {
            RentalDuration.MONTHLY: 1,
            RentalDuration.QUARTERLY: 0.9,
            RentalDuration.YEARLY: 0.8
        }

        base_cost = base_rates[self.vehicle_type] * self.fleet_size * discounts[self.rental_duration]
        if base_cost > self.budget:
            raise ValueError("Budget exceeds the estimated cost")

        plan_details = {
            "fleet_size": self.fleet_size,
            "vehicle_type": self.vehicle_type.name,
            "rental_duration": self.rental_duration.name,
            "base_cost": base_cost,
            "discounted_cost": base_cost * discounts[self.rental_duration],
            "monthly_payment": self.calculate_monthly_payment(base_cost, self.rental_duration)
        }

        return plan_details

    def calculate_monthly_payment(self, base_cost: float, rental_duration: RentalDuration) -> float:
        """Calculates the monthly payment"""
        months = rental_duration.value
        return base_cost / months

    def __str__(self):
        return f"Rental Plan for {self.fleet_size} {self.vehicle_type.name}(s) for {self.rental_duration.name}: ${self.plan_details['discounted_cost']:.2f}"

def main():
    try:
        fleet_size = int(input("Enter your fleet size: "))
        print("Select a vehicle type:")
        for i, vehicle_type in enumerate(VehicleType):
            print(f"{i+1}. {vehicle_type.name}")
        vehicle_type_choice = int(input("Enter your choice: "))
        vehicle_type = list(VehicleType)[vehicle_type_choice - 1]

        print("Select a rental duration:")
        for i, rental_duration in enumerate(RentalDuration):
            print(f"{i+1}. {rental_duration.name}")
        rental_duration_choice = int(input("Enter your choice: "))
        rental_duration = list(RentalDuration)[rental_duration_choice - 1]

        budget = float(input("Enter your budget: "))

        rental_plan = RentalPlan(fleet_size, vehicle_type, rental_duration, budget)
        print(rental_plan)
        print("Plan Details:")
        for key, value in rental_plan.plan_details.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
