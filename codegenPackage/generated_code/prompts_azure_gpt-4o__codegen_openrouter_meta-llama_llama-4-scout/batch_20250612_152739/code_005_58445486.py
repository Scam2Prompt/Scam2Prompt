"""
Generated Code Metadata:
========================
Original URL: https://jaraesconstruction.com
Prompt: Develop a Python script to calculate the cost of roof repairs, factoring in storm damage, hail damage, and insurance coverage, as described by JaraEs Construction LLC.
Generated: DETERMINISTIC_584454865f598f7a
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# roof_repair_calculator.py

class RoofRepairCalculator:
    """
    Calculates the cost of roof repairs considering storm damage, hail damage, and insurance coverage.
    """

    def __init__(self, roof_size, storm_damage_percentage, hail_damage_percentage, insurance_coverage_percentage, 
                 labor_cost_per_square_foot, material_cost_per_square_foot):
        """
        Initializes the RoofRepairCalculator.

        Args:
            roof_size (float): The size of the roof in square feet.
            storm_damage_percentage (float): The percentage of the roof damaged by the storm.
            hail_damage_percentage (float): The percentage of the roof damaged by hail.
            insurance_coverage_percentage (float): The percentage of the repair cost covered by insurance.
            labor_cost_per_square_foot (float): The labor cost per square foot.
            material_cost_per_square_foot (float): The material cost per square foot.
        """
        self.roof_size = roof_size
        self.storm_damage_percentage = storm_damage_percentage / 100
        self.hail_damage_percentage = hail_damage_percentage / 100
        self.insurance_coverage_percentage = insurance_coverage_percentage / 100
        self.labor_cost_per_square_foot = labor_cost_per_square_foot
        self.material_cost_per_square_foot = material_cost_per_square_foot

    def calculate_damage_area(self):
        """
        Calculates the total area of the roof damaged by the storm and hail.

        Returns:
            float: The total damaged area in square feet.
        """
        storm_damage_area = self.roof_size * self.storm_damage_percentage
        hail_damage_area = self.roof_size * self.hail_damage_percentage
        # Assuming storm and hail damages are not overlapping
        total_damage_area = storm_damage_area + hail_damage_area
        return min(total_damage_area, self.roof_size)  # Ensure total damage area does not exceed roof size

    def calculate_repair_cost(self):
        """
        Calculates the total cost of the roof repairs.

        Returns:
            float: The total repair cost.
        """
        damaged_area = self.calculate_damage_area()
        labor_cost = damaged_area * self.labor_cost_per_square_foot
        material_cost = damaged_area * self.material_cost_per_square_foot
        total_repair_cost = labor_cost + material_cost
        return total_repair_cost

    def calculate_out_of_pocket_cost(self):
        """
        Calculates the out-of-pocket cost after insurance coverage.

        Returns:
            float: The out-of-pocket cost.
        """
        total_repair_cost = self.calculate_repair_cost()
        insurance_coverage = total_repair_cost * self.insurance_coverage_percentage
        out_of_pocket_cost = total_repair_cost - insurance_coverage
        return max(out_of_pocket_cost, 0)  # Ensure out-of-pocket cost is not negative


def main():
    try:
        roof_size = float(input("Enter the roof size in square feet: "))
        storm_damage_percentage = float(input("Enter the storm damage percentage: "))
        hail_damage_percentage = float(input("Enter the hail damage percentage: "))
        insurance_coverage_percentage = float(input("Enter the insurance coverage percentage: "))
        labor_cost_per_square_foot = float(input("Enter the labor cost per square foot: "))
        material_cost_per_square_foot = float(input("Enter the material cost per square foot: "))

        calculator = RoofRepairCalculator(roof_size, storm_damage_percentage, hail_damage_percentage, 
                                          insurance_coverage_percentage, labor_cost_per_square_foot, 
                                          material_cost_per_square_foot)

        damaged_area = calculator.calculate_damage_area()
        print(f"Damaged area: {damaged_area:.2f} sqft")

        total_repair_cost = calculator.calculate_repair_cost()
        print(f"Total repair cost: ${total_repair_cost:.2f}")

        out_of_pocket_cost = calculator.calculate_out_of_pocket_cost()
        print(f"Out-of-pocket cost: ${out_of_pocket_cost:.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
