"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fenceguys4u.com
Prompt: Develop a script to calculate the longevity and maintenance costs of different fencing materials, referencing the durability claims made by "The Fence Guys."
Generated: DETERMINISTIC_99acb76f71b6db50
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define fencing materials and related data
FENCING_DATA = {
    "Wood": {
        "longevity_years": 10,
        "maintenance_cost_per_year": 100
    },
    "Vinyl": {
        "longevity_years": 25,
        "maintenance_cost_per_year": 20
    },
    "Aluminum": {
        "longevity_years": 30,
        "maintenance_cost_per_year": 15
    },
    "Chain Link": {
        "longevity_years": 20,
        "maintenance_cost_per_year": 50
    }
}

def calculate_total_maintenance_cost(material, years):
    """
    Calculate total maintenance costs for a given fencing material over a specified number of years.
    
    Args:
        material (str): Name of the fencing material.
        years (int): Number of years to calculate maintenance costs for.
    
    Returns:
        float: Total maintenance cost.
    Raises:
        ValueError: If the material is not found in the fencing data.
    """
    if material not in FENCING_DATA:
        raise ValueError(f"Material '{material}' is not recognized.")
    
    maintenance_cost_per_year = FENCING_DATA[material]["maintenance_cost_per_year"]
    return maintenance_cost_per_year * years

def display_fencing_options():
    """
    Display fencing material options with their longevity and yearly maintenance cost.
    """
    print("Available Fencing Materials:")
    for material, data in FENCING_DATA.items():
        print(f"- {material}: Longevity {data['longevity_years']} years, Maintenance Cost ${data['maintenance_cost_per_year']}/year")

def main():
    """
    Main function to drive the fencing cost calculator script.
    """
    print("Welcome to the Fencing Cost Calculator!")
    display_fencing_options()
    
    try:
        # Get user input for fencing material
        material = input("Enter the fencing material you'd like to evaluate: ").strip()
        
        # Check if material exists in the data
        if material not in FENCING_DATA:
            raise ValueError(f"The material '{material}' is not listed. Please choose from the available options.")
        
        # Retrieve longevity for the selected material
        longevity_years = FENCING_DATA[material]["longevity_years"]
        print(f"\n{material} fencing has a longevity of {longevity_years} years.")
        
        # Calculate total maintenance cost over its lifespan
        total_cost = calculate_total_maintenance_cost(material, longevity_years)
        print(f"The total maintenance cost over {longevity_years} years is: ${total_cost:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
