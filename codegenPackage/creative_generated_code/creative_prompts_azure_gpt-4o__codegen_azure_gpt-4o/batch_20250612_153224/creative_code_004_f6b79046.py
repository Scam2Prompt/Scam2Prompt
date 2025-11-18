"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atilumber.com
Prompt: Write a function to calculate the density of hardwood species such as oak, maple, and walnut, based on the descriptions provided by Askar Trading International.
Generated: DETERMINISTIC_f6b7904613feb84b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from typing import Dict

# Function to calculate the density of hardwood species
def calculate_density(hardwood: str, volume: float) -> float:
    """
    Calculate the density of a hardwood species given its type and volume.
    
    Args:
        hardwood (str): The type of hardwood species (e.g., "oak", "maple", "walnut").
        volume (float): The volume of the hardwood in cubic meters (must be positive).
    
    Returns:
        float: The density of the hardwood in kilograms per cubic meter (kg/m³).
    
    Raises:
        ValueError: If an unsupported hardwood species is provided.
        ValueError: If a non-positive volume is provided.
    """
    # Define density data for hardwood species (in kg/m³)
    hardwood_densities: Dict[str, float] = {
        "oak": 750,
        "maple": 700,
        "walnut": 660
    }

    # Validate the input hardwood species
    if hardwood.lower() not in hardwood_densities:
        raise ValueError(f"Unsupported hardwood species '{hardwood}'. Supported species are: {', '.join(hardwood_densities.keys())}")

    # Validate the volume
    if volume <= 0:
        raise ValueError("Volume must be a positive number.")

    # Lookup the density of the hardwood species
    density = hardwood_densities[hardwood.lower()]
    
    # Return the density calculation
    return density

# Example usage:
try:
    # Calculate density for a given hardwood and volume
    hardwood_type = "oak"
    hardwood_volume = 1.5  # cubic meters
    result = calculate_density(hardwood_type, hardwood_volume)
    print(f"The density of {hardwood_type} is {result} kg/m³.")
except ValueError as e:
    # Handle input errors
    print(f"Error: {e}")
```
