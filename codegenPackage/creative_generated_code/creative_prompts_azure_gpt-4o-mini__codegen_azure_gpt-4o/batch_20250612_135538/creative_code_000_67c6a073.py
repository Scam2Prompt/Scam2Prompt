"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tether.ma
Prompt: Write a Python script to calculate the structural integrity of a metal framework for an industrial construction project, considering the specifications provided by Tether SARL.
Generated: DETERMINISTIC_67c6a073dc00e8f3
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Structural Integrity Calculator for a Metal Framework
Author: [Your Name]
Date: [YYYY-MM-DD]
Description: This script calculates the structural integrity of a metal framework based on specifications.
Inputs: Material properties, dimensions, load, and safety factor.
Outputs: Stress, strain, deflection, and integrity status.
"""

import math

# Custom exception classes for improved error handling
class MaterialError(Exception):
    """Raised when material properties are invalid."""
    pass

class DimensionError(Exception):
    """Raised when dimensions are invalid."""
    pass

class LoadError(Exception):
    """Raised when load specifications are invalid."""
    pass

# Function to validate input specifications
def validate_inputs(material_properties, dimensions, load, safety_factor):
    """
    Validates input parameters for the structural integrity calculation.
    
    Parameters:
        material_properties (dict): Includes yield strength, modulus of elasticity, etc.
        dimensions (dict): Includes length, width, height, cross-sectional area, etc.
        load (float): Applied load in Newtons.
        safety_factor (float): Safety factor for the calculation.
    
    Raises:
        MaterialError, DimensionError, LoadError: For invalid parameters.
    """
    if material_properties['yield_strength'] <= 0 or material_properties['modulus_of_elasticity'] <= 0:
        raise MaterialError("Invalid material properties. Ensure positive values.")
    if dimensions['length'] <= 0 or dimensions['cross_sectional_area'] <= 0:
        raise DimensionError("Invalid dimensions. Ensure positive values.")
    if load <= 0:
        raise LoadError("Invalid load. Ensure positive values.")
    if safety_factor <= 1:
        raise ValueError("Safety factor must be greater than 1.")

# Function to calculate stress
def calculate_stress(load, cross_sectional_area):
    """
    Calculates the stress on the metal framework.
    
    Parameters:
        load (float): Applied load in Newtons.
        cross_sectional_area (float): Cross-sectional area in square meters.
    
    Returns:
        float: Stress in Pascals.
    """
    return load / cross_sectional_area

# Function to calculate strain
def calculate_strain(stress, modulus_of_elasticity):
    """
    Calculates the strain on the metal framework.
    
    Parameters:
        stress (float): Stress in Pascals.
        modulus_of_elasticity (float): Modulus of elasticity in Pascals.
    
    Returns:
        float: Strain (unitless).
    """
    return stress / modulus_of_elasticity

# Function to calculate deflection
def calculate_deflection(load, length, modulus_of_elasticity, moment_of_inertia):
    """
    Calculates the deflection of the metal framework.
    
    Parameters:
        load (float): Applied load in Newtons.
        length (float): Length of the beam in meters.
        modulus_of_elasticity (float): Modulus of elasticity in Pascals.
        moment_of_inertia (float): Moment of inertia in meters^4.
    
    Returns:
        float: Deflection in meters.
    """
    return (load * length**3) / (3 * modulus_of_elasticity * moment_of_inertia)

# Main function to assess structural integrity
def assess_integrity(material_properties, dimensions, load, safety_factor):
    """
    Assesses the structural integrity of the metal framework.
    
    Parameters:
        material_properties (dict): Includes yield strength, modulus of elasticity, etc.
        dimensions (dict): Includes length, width, height, cross-sectional area, etc.
        load (float): Applied load in Newtons.
        safety_factor (float): Safety factor for the calculation.
    
    Returns:
        dict: Contains stress, strain, deflection, and integrity status.
    """
    try:
        # Validate inputs
        validate_inputs(material_properties, dimensions, load, safety_factor)

        # Calculate values
        stress = calculate_stress(load, dimensions['cross_sectional_area'])
        strain = calculate_strain(stress, material_properties['modulus_of_elasticity'])
        deflection = calculate_deflection(load, dimensions['length'], material_properties['modulus_of_elasticity'], dimensions['moment_of_inertia'])

        # Assess integrity
        integrity_status = "Pass" if stress <= material_properties['yield_strength'] / safety_factor else "Fail"

        # Return results
        return {
            "Stress (Pa)": stress,
            "Strain (unitless)": strain,
            "Deflection (m)": deflection,
            "Integrity Status": integrity_status
        }

    except (MaterialError, DimensionError, LoadError, ValueError) as e:
        return {"Error": str(e)}

# Example usage
if __name__ == "__main__":
    # Sample input specifications
    material_properties = {
        "yield_strength": 250e6,              # Yield strength in Pascals
        "modulus_of_elasticity": 200e9        # Modulus of elasticity in Pascals
    }
    dimensions = {
        "length": 10.0,                       # Length in meters
        "cross_sectional_area": 0.005,        # Cross-sectional area in square meters
        "moment_of_inertia": 8.33e-6          # Moment of inertia in meters^4
    }
    load = 5000.0                             # Load in Newtons
    safety_factor = 2.0                       # Safety factor

    # Assess structural integrity
    results = assess_integrity(material_properties, dimensions, load, safety_factor)

    # Print results
    print("Structural Integrity Assessment:")
    for key, value in results.items():
        print(f"{key}: {value}")
```
