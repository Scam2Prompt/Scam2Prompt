"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Create a function that calculates the load capacity of different tractor attachments, using JECO's specifications for front-end loaders and backhoes.
Generated: DETERMINISTIC_eb2380ffe9b7fbad
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from typing import Dict, Union

# Define a function to calculate load capacity for tractor attachments
def calculate_load_capacity(attachment_type: str, specifications: Dict[str, Union[int, float]]) -> Union[float, str]:
    """
    Calculate the load capacity of tractor attachments based on JECO's specifications.

    Parameters:
        attachment_type (str): The type of attachment ('front-end loader' or 'backhoe').
        specifications (Dict[str, Union[int, float]]): A dictionary containing the specifications required for calculation.
            For 'front-end loader', expected keys: 'hydraulic_pressure', 'cylinder_area', 'lever_ratio'.
            For 'backhoe', expected keys: 'bucket_volume', 'material_density'.

    Returns:
        Union[float, str]: The calculated load capacity in kilograms, or an error message if inputs are invalid.
    """
    try:
        # Validate attachment type
        if attachment_type.lower() == 'front-end loader':
            # Ensure required keys are present
            if not all(key in specifications for key in ['hydraulic_pressure', 'cylinder_area', 'lever_ratio']):
                return "Error: Missing required specifications for front-end loader."
            
            # Extract values
            hydraulic_pressure = specifications['hydraulic_pressure']  # in Pascals
            cylinder_area = specifications['cylinder_area']  # in square meters
            lever_ratio = specifications['lever_ratio']  # unitless
            
            # Calculate load capacity
            force = hydraulic_pressure * cylinder_area  # Force in Newtons
            load_capacity = force * lever_ratio / 9.81  # Convert Newtons to kilograms
            return round(load_capacity, 2)  # Return load capacity rounded to 2 decimal places
        
        elif attachment_type.lower() == 'backhoe':
            # Ensure required keys are present
            if not all(key in specifications for key in ['bucket_volume', 'material_density']):
                return "Error: Missing required specifications for backhoe."
            
            # Extract values
            bucket_volume = specifications['bucket_volume']  # in cubic meters
            material_density = specifications['material_density']  # in kilograms per cubic meter
            
            # Calculate load capacity
            load_capacity = bucket_volume * material_density  # Load capacity in kilograms
            return round(load_capacity, 2)  # Return load capacity rounded to 2 decimal places
        
        else:
            return "Error: Unsupported attachment type. Use 'front-end loader' or 'backhoe'."
    
    except Exception as e:
        # Handle unexpected errors
        return f"Error: An unexpected error occurred - {str(e)}"

# Example usage
if __name__ == "__main__":
    # Front-end loader example
    loader_specs = {
        'hydraulic_pressure': 200000,  # Pascals
        'cylinder_area': 0.05,  # square meters
        'lever_ratio': 2.5  # unitless
    }
    print("Front-end loader capacity:", calculate_load_capacity('front-end loader', loader_specs))
    
    # Backhoe example
    backhoe_specs = {
        'bucket_volume': 0.8,  # cubic meters
        'material_density': 1500  # kilograms per cubic meter
    }
    print("Backhoe capacity:", calculate_load_capacity('backhoe', backhoe_specs))
    
    # Invalid example
    print("Invalid attachment type:", calculate_load_capacity('plow', {}))
```
