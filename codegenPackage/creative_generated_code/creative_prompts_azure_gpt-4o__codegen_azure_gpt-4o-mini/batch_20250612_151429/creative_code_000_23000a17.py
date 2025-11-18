"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somcivil.com
Prompt: Write Python code to estimate the cost of structural repairs for a building based on parameters like square footage, age, and type of damage, referencing SOM Civil Engineers' expertise in structural audits and repairs.
Generated: DETERMINISTIC_23000a173459fe33
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StructuralRepairEstimator:
    """
    A class to estimate the cost of structural repairs for a building based on its parameters.
    This estimation is based on the expertise of SOM Civil Engineers in structural audits and repairs.
    """

    def __init__(self, square_footage: float, building_age: int, damage_type: str):
        """
        Initializes the estimator with the building's parameters.

        :param square_footage: The total square footage of the building.
        :param building_age: The age of the building in years.
        :param damage_type: The type of damage (e.g., 'minor', 'moderate', 'severe').
        """
        self.square_footage = square_footage
        self.building_age = building_age
        self.damage_type = damage_type.lower()
        self.cost_per_square_foot = self._get_cost_per_sqft()

    def _get_cost_per_sqft(self) -> float:
        """
        Retrieves the cost per square foot based on the damage type.

        :return: Cost per square foot as a float.
        :raises ValueError: If the damage type is not recognized.
        """
        cost_mapping = {
            'minor': 50.0,
            'moderate': 100.0,
            'severe': 200.0
        }
        
        if self.damage_type not in cost_mapping:
            raise ValueError(f"Unrecognized damage type: {self.damage_type}. "
                             f"Expected one of {list(cost_mapping.keys())}.")

        return cost_mapping[self.damage_type]

    def estimate_repair_cost(self) -> float:
        """
        Estimates the total cost of repairs based on the building's parameters.

        :return: Estimated repair cost as a float.
        """
        # Calculate total cost based on square footage and cost per square foot
        total_cost = self.square_footage * self.cost_per_square_foot
        
        # Apply an age factor, assuming older buildings may have additional costs
        if self.building_age > 50:
            age_factor = 1.2  # 20% increase for buildings older than 50 years
            total_cost *= age_factor
        
        return total_cost

def main():
    """
    Main function to run the estimator based on user input.
    """
    try:
        # Example input parameters for estimation
        square_footage = float(input("Enter square footage of the building: "))
        building_age = int(input("Enter age of the building (in years): "))
        damage_type = input("Enter type of damage (minor, moderate, severe): ")

        # Create an instance of the estimator
        estimator = StructuralRepairEstimator(square_footage, building_age, damage_type)
        
        # Calculate the estimated repair cost
        estimated_cost = estimator.estimate_repair_cost()
        
        print(f"The estimated cost of structural repairs is: ${estimated_cost:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

if __name__ == "__main__":
    main()
```
