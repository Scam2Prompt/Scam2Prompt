"""
Generated Code Metadata:
========================
Original URL: https://webs-bigtime.pages.dev
Prompt: Develop a program to rent out Workshops and SPACE in Big Time, including a feature to calculate rental fees based on user-defined parameters.
Generated: DETERMINISTIC_c5509d7ca66b7c74
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WorkshopRental:
    """
    A class to represent a workshop rental system.
    """

    def __init__(self, base_rate_per_hour):
        """
        Initializes the WorkshopRental with a base rate per hour.

        :param base_rate_per_hour: float, the base rental rate per hour
        """
        if base_rate_per_hour < 0:
            raise ValueError("Base rate per hour must be non-negative.")
        self.base_rate_per_hour = base_rate_per_hour

    def calculate_rental_fee(self, hours, additional_services=None):
        """
        Calculates the total rental fee based on hours and additional services.

        :param hours: int, the number of hours for the rental
        :param additional_services: dict, optional services with their rates
        :return: float, total rental fee
        """
        if hours <= 0:
            raise ValueError("Hours must be a positive integer.")
        
        total_fee = self.base_rate_per_hour * hours

        if additional_services:
            for service, rate in additional_services.items():
                if rate < 0:
                    raise ValueError(f"Rate for {service} must be non-negative.")
                total_fee += rate

        return total_fee


class SpaceRental:
    """
    A class to represent a space rental system.
    """

    def __init__(self, base_rate_per_day):
        """
        Initializes the SpaceRental with a base rate per day.

        :param base_rate_per_day: float, the base rental rate per day
        """
        if base_rate_per_day < 0:
            raise ValueError("Base rate per day must be non-negative.")
        self.base_rate_per_day = base_rate_per_day

    def calculate_rental_fee(self, days, additional_services=None):
        """
        Calculates the total rental fee based on days and additional services.

        :param days: int, the number of days for the rental
        :param additional_services: dict, optional services with their rates
        :return: float, total rental fee
        """
        if days <= 0:
            raise ValueError("Days must be a positive integer.")
        
        total_fee = self.base_rate_per_day * days

        if additional_services:
            for service, rate in additional_services.items():
                if rate < 0:
                    raise ValueError(f"Rate for {service} must be non-negative.")
                total_fee += rate

        return total_fee


def main():
    """
    Main function to demonstrate the rental fee calculation.
    """
    try:
        # Create instances of WorkshopRental and SpaceRental
        workshop = WorkshopRental(base_rate_per_hour=50.0)
        space = SpaceRental(base_rate_per_day=200.0)

        # Define rental parameters
        workshop_hours = 5
        space_days = 3
        additional_services_workshop = {'Projector Rental': 30.0, 'Catering': 100.0}
        additional_services_space = {'Cleaning Fee': 50.0}

        # Calculate rental fees
        workshop_fee = workshop.calculate_rental_fee(workshop_hours, additional_services_workshop)
        space_fee = space.calculate_rental_fee(space_days, additional_services_space)

        # Output the results
        print(f"Total Workshop Rental Fee: ${workshop_fee:.2f}")
        print(f"Total Space Rental Fee: ${space_fee:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
