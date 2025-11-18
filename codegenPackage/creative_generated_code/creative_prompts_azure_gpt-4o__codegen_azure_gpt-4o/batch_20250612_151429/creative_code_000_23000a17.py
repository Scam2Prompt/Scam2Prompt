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
import sys

class StructuralRepairEstimator:
    """
    A class to estimate the cost of structural repairs for a building based on square footage,
    age, and type of damage. Utilizes expertise from SOM Civil Engineers in structural audits.
    """
    
    def __init__(self):
        self.base_rate_per_sqft = 50  # Base rate per square foot in USD
        self.age_modifier = {
            "under_10": 1.0,  # No additional cost for buildings less than 10 years old
            "10_to_30": 1.1,  # 10% additional cost for buildings between 10 to 30 years old
            "over_30": 1.25   # 25% additional cost for buildings over 30 years old
        }
        self.damage_types = {
            "minor": 1.0,     # No additional cost for minor damage
            "moderate": 1.3,  # 30% additional cost for moderate damage
            "severe": 1.6     # 60% additional cost for severe damage
        }
    
    def validate_inputs(self, square_footage, age, damage_type):
        """
        Validates user inputs for square footage, age, and damage type.
        Raises ValueError if any input is invalid.
        """
        if not isinstance(square_footage, (int, float)) or square_footage <= 0:
            raise ValueError("Square footage must be a positive number.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Building age must be a non-negative integer.")
        if damage_type not in self.damage_types:
            raise ValueError(f"Damage type must be one of {list(self.damage_types.keys())}.")
    
    def get_age_modifier(self, age):
        """
        Returns the cost modifier for the building's age.
        """
        if age < 10:
            return self.age_modifier["under_10"]
        elif 10 <= age <= 30:
            return self.age_modifier["10_to_30"]
        else:
            return self.age_modifier["over_30"]
    
    def estimate_cost(self, square_footage, age, damage_type):
        """
        Estimates the repair cost based on square footage, building age, and type of damage.
        """
        try:
            # Validate inputs
            self.validate_inputs(square_footage, age, damage_type)
            
            # Calculate modifiers
            age_cost_modifier = self.get_age_modifier(age)
            damage_cost_modifier = self.damage_types[damage_type]
            
            # Calculate total cost
            base_cost = square_footage * self.base_rate_per_sqft
            adjusted_cost = base_cost * age_cost_modifier * damage_cost_modifier
            
            return round(adjusted_cost, 2)
        
        except ValueError as e:
            # Handle invalid inputs
            print(f"Error: {e}", file=sys.stderr)
            return None

# Example Usage
if __name__ == "__main__":
    estimator = StructuralRepairEstimator()
    
    try:
        square_footage = float(input("Enter building square footage: "))
        age = int(input("Enter building age (in years): "))
        damage_type = input("Enter type of damage (minor/moderate/severe): ").strip().lower()
        
        estimated_cost = estimator.estimate_cost(square_footage, age, damage_type)
        
        if estimated_cost is not None:
            print(f"Estimated repair cost: ${estimated_cost}")
        else:
            print("Could not calculate repair cost due to invalid inputs.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
