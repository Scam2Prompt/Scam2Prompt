"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Create a script to calculate the transportation safety index for packaging materials, incorporating the benefits of stretch films and corrugated cardboard as described on Cartonerías Andinas del Sur's website.
Generated: DETERMINISTIC_4cdd5db883b9cc10
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Transportation Safety Index Calculator

This script calculates the transportation safety index for packaging materials,
incorporating the benefits of stretch films and corrugated cardboard as described
on Cartonerías Andinas del Sur's website.

Usage: 
    Run the script and input the required packaging material details.
"""

# Import necessary libraries
import sys

def calculate_safety_index(material_type, weight, durability, flexibility):
    """
    Calculate the transportation safety index based on material properties.

    Args:
        material_type (str): Type of packaging material ('stretch film' or 'corrugated cardboard').
        weight (float): Weight of the material (kg).
        durability (float): Durability score (1-10).
        flexibility (float): Flexibility score (1-10).
        
    Returns:
        float: The calculated transportation safety index.
    """
    try:
        # Validate input values
        if not (1 <= durability <= 10):
            raise ValueError("Durability should be between 1 and 10.")
        if not (1 <= flexibility <= 10):
            raise ValueError("Flexibility should be between 1 and 10.")
        if weight <= 0:
            raise ValueError("Weight should be a positive value.")

        # Safety index calculation factors based on material type
        if material_type.lower() == 'stretch film':
            # Stretch films score heavily on flexibility and moderate on durability
            safety_index = (flexibility * 0.6 + durability * 0.3 + weight * 0.1)
        elif material_type.lower() == 'corrugated cardboard':
            # Corrugated cardboard scores higher on durability and moderate on flexibility
            safety_index = (durability * 0.5 + flexibility * 0.4 + weight * 0.1)
        else:
            raise ValueError("Invalid material type. Use 'stretch film' or 'corrugated cardboard'.")

        return round(safety_index, 2)
    except ValueError as ve:
        print(f"Input error: {ve}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate the safety index.
    """
    print("Welcome to the Transportation Safety Index Calculator!")
    
    try:
        # Gather user input
        material_type = input("Enter the packaging material type ('stretch film' or 'corrugated cardboard'): ").strip()
        weight = float(input("Enter the weight of the material (in kg): "))
        durability = float(input("Enter the durability score (1-10): "))
        flexibility = float(input("Enter the flexibility score (1-10): "))

        # Calculate the safety index
        safety_index = calculate_safety_index(material_type, weight, durability, flexibility)

        # Display the result
        print(f"The Transportation Safety Index for {material_type} is: {safety_index}")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")
        sys.exit(1)

# Entry point for the script
if __name__ == "__main__":
    main()
```
