"""
Generated Code Metadata:
========================
Original URL: https://indologicalindia.com
Prompt: Write a Python program to calculate the carbon footprint reduction achieved through Indological India's tree plantation drives.
Generated: DETERMINISTIC_a484874beb5bb19d
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class CarbonFootprintCalculator:
    """
    A class to calculate carbon footprint reduction achieved through tree plantation drives.
    """
    
    def __init__(self):
        """
        Initialize constants for carbon sequestration rates and other parameters.
        """
        # Average carbon sequestration rate per tree per year in kg (source: USDA)
        self.CARBON_SEQUESTRATION_RATE = 21.77
        
        # Average lifespan of a tree in years
        self.AVERAGE_TREE_LIFESPAN = 40
        
        # Conversion factor from kg to metric tons
        self.KG_TO_TONS = 0.001
        
    def calculate_lifetime_carbon_reduction(self, num_trees):
        """
        Calculate lifetime carbon reduction for planted trees.
        
        Args:
            num_trees (int): Number of trees planted
            
        Returns:
            float: Total carbon reduction in metric tons over tree lifespan
        """
        try:
            if not isinstance(num_trees, (int, float)) or num_trees < 0:
                raise ValueError("Number of trees must be a positive number")
                
            total_kg = num_trees * self.CARBON_SEQUESTRATION_RATE * self.AVERAGE_TREE_LIFESPAN
            return total_kg * self.KG_TO_TONS
        except ValueError as e:
            print(f"Error in calculation: {e}")
            return 0
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return 0
    
    def calculate_annual_carbon_reduction(self, num_trees):
        """
        Calculate annual carbon reduction for planted trees.
        
        Args:
            num_trees (int): Number of trees planted
            
        Returns:
            float: Annual carbon reduction in metric tons
        """
        try:
            if not isinstance(num_trees, (int, float)) or num_trees < 0:
                raise ValueError("Number of trees must be a positive number")
                
            annual_kg = num_trees * self.CARBON_SEQUESTRATION_RATE
            return annual_kg * self.KG_TO_TONS
        except ValueError as e:
            print(f"Error in calculation: {e}")
            return 0
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return 0
    
    def equivalent_car_emissions_saved(self, carbon_tons):
        """
        Calculate equivalent car emissions saved in terms of miles not driven.
        
        Args:
            carbon_tons (float): Carbon reduction in metric tons
            
        Returns:
            float: Equivalent miles not driven by an average car
        """
        try:
            if not isinstance(carbon_tons, (int, float)) or carbon_tons < 0:
                raise ValueError("Carbon tons must be a positive number")
                
            # Average car emits 0.404 kg CO2 per mile (source: EPA)
            kg_per_mile = 0.404
            miles_saved = (carbon_tons / self.KG_TO_TONS) / kg_per_mile
            return miles_saved
        except ValueError as e:
            print(f"Error in calculation: {e}")
            return 0
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return 0

def main():
    """
    Main function to demonstrate the CarbonFootprintCalculator class.
    """
    calculator = CarbonFootprintCalculator()
    
    try:
        # Get user input
        num_trees = int(input("Enter the number of trees planted: "))
        
        if num_trees <= 0:
            print("Please enter a positive number of trees.")
            return
        
        # Calculate results
        lifetime_reduction = calculator.calculate_lifetime_carbon_reduction(num_trees)
        annual_reduction = calculator.calculate_annual_carbon_reduction(num_trees)
        miles_saved = calculator.equivalent_car_emissions_saved(annual_reduction)
        
        # Display results
        print("\nCarbon Footprint Reduction Results:")
        print(f"- Lifetime carbon reduction: {lifetime_reduction:.2f} metric tons")
        print(f"- Annual carbon reduction: {annual_reduction:.2f} metric tons")
        print(f"- Equivalent to not driving {miles_saved:.2f} miles per year")
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
