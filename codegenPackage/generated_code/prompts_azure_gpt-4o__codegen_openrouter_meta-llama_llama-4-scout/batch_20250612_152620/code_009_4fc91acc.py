"""
Generated Code Metadata:
========================
Original URL: https://adygeya.propiski-net.ru
Prompt: Write a script to calculate the total cost of temporary registration for multiple individuals in Adygea, including adjustments for minors and duration of registration, as specified on the website.
Generated: DETERMINISTIC_4fc91acc974b986a
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# temporary_registration_cost_calculator.py

class TemporaryRegistrationCalculator:
    """
    Calculates the total cost of temporary registration for individuals in Adygea.

    The cost is calculated based on the duration of registration and 
    adjustments are made for minors.
    """

    def __init__(self, base_cost_per_year, minor_discount):
        """
        Initializes the calculator with the base cost per year and minor discount.

        Args:
            base_cost_per_year (float): The base cost of temporary registration per year.
            minor_discount (float): The discount for minors as a percentage.
        """
        self.base_cost_per_year = base_cost_per_year
        self.minor_discount = minor_discount / 100  # convert to decimal

    def calculate_cost(self, age, duration_in_days):
        """
        Calculates the total cost of temporary registration for an individual.

        Args:
            age (int): The age of the individual.
            duration_in_days (int): The duration of registration in days.

        Returns:
            float: The total cost of temporary registration.

        Raises:
            ValueError: If age or duration is negative.
        """
        if age < 0 or duration_in_days < 0:
            raise ValueError("Age and duration must be non-negative")

        # calculate the cost per day
        cost_per_day = self.base_cost_per_year / 365

        # calculate the base cost
        base_cost = cost_per_day * duration_in_days

        # apply minor discount if applicable
        if age < 18:
            return base_cost * (1 - self.minor_discount)
        else:
            return base_cost

    def calculate_total_cost(self, individuals):
        """
        Calculates the total cost of temporary registration for multiple individuals.

        Args:
            individuals (list): A list of tuples containing the age and duration 
                of registration for each individual.

        Returns:
            float: The total cost of temporary registration for all individuals.

        Raises:
            ValueError: If the input list is empty.
        """
        if not individuals:
            raise ValueError("List of individuals must not be empty")

        total_cost = 0
        for age, duration_in_days in individuals:
            total_cost += self.calculate_cost(age, duration_in_days)

        return total_cost


def main():
    # example usage
    calculator = TemporaryRegistrationCalculator(base_cost_per_year=1000, minor_discount=10)

    individuals = [
        (25, 90),  # 25-year-old for 3 months
        (15, 180),  # 15-year-old for 6 months
        (30, 365)   # 30-year-old for 1 year
    ]

    try:
        total_cost = calculator.calculate_total_cost(individuals)
        print(f"Total cost: {total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
