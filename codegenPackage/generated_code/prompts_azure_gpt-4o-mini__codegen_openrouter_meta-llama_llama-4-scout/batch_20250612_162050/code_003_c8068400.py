"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: Develop a library function that estimates the number of grafts needed for a hair transplant based on the area of baldness, referencing Efeito Harmonie's methodology.
Generated: DETERMINISTIC_c8068400f9a2ddb9
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
hair_transplant_calculator.py

Calculates the number of grafts needed for a hair transplant based on the area of baldness,
following Efeito Harmonie's methodology.

Author: [Your Name]
Date: [Today's Date]
"""

class HairTransplantCalculator:
    """
    Estimates the number of grafts needed for a hair transplant.

    Attributes:
        follicular_units_per_cm2 (float): Average number of follicular units per cm^2.
    """

    def __init__(self, follicular_units_per_cm2=70):
        """
        Initializes the calculator with the average number of follicular units per cm^2.

        Args:
            follicular_units_per_cm2 (float, optional): Average number of follicular units per cm^2. Defaults to 70.
        """
        self.follicular_units_per_cm2 = follicular_units_per_cm2

    def calculate_grafts(self, baldness_area_cm2, donor_area_cm2, graft_harvest_rate=0.7):
        """
        Estimates the number of grafts needed for a hair transplant.

        Args:
            baldness_area_cm2 (float): Area of baldness in cm^2.
            donor_area_cm2 (float): Area of donor site in cm^2.
            graft_harvest_rate (float, optional): Rate of successful graft harvesting. Defaults to 0.7.

        Returns:
            int: Estimated number of grafts needed.

        Raises:
            ValueError: If any input value is negative.
        """
        if baldness_area_cm2 < 0 or donor_area_cm2 < 0 or graft_harvest_rate < 0:
            raise ValueError("Input values cannot be negative")

        # Calculate the total number of follicular units needed
        total_follicular_units_needed = baldness_area_cm2 * self.follicular_units_per_cm2

        # Calculate the total number of grafts available from the donor site
        total_grafts_available = donor_area_cm2 * self.follicular_units_per_cm2 * graft_harvest_rate

        # Calculate the estimated number of grafts needed
        estimated_grafts_needed = max(total_follicular_units_needed / self.follicular_units_per_cm2, 1)

        # Ensure the estimated number of grafts does not exceed the available grafts
        estimated_grafts_needed = min(estimated_grafts_needed, total_grafts_available / self.follicular_units_per_cm2)

        return round(estimated_grafts_needed)


def main():
    calculator = HairTransplantCalculator()

    try:
        baldness_area_cm2 = float(input("Enter the area of baldness in cm^2: "))
        donor_area_cm2 = float(input("Enter the area of donor site in cm^2: "))

        estimated_grafts_needed = calculator.calculate_grafts(baldness_area_cm2, donor_area_cm2)

        print(f"Estimated number of grafts needed: {estimated_grafts_needed}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
