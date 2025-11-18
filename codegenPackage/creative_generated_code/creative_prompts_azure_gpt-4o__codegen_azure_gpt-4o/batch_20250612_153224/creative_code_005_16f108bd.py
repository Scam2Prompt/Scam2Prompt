"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karenfixing.com
Prompt: Write a function to calculate the optimal spacing for "پیچ بوکسی سر مته 30 * 6 (1.25 * 14)" in the installation of dry facade systems, referencing Karen Fixing's guidelines.
Generated: DETERMINISTIC_16f108bdfde92fee
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import math

def calculate_optimal_spacing(diameter, length, thread_pitch, load_capacity, facade_weight, safety_factor=1.5):
    """
    Calculate the optimal spacing for "پیچ بوکسی سر مته 30 * 6 (1.25 * 14)" 
    based on installation guidelines for dry facade systems.
    
    Parameters:
        diameter (float): Diameter of the screw in mm.
        length (float): Length of the screw in mm.
        thread_pitch (float): Thread pitch of the screw in mm.
        load_capacity (float): Load capacity of the screw in Newtons.
        facade_weight (float): Total weight of the facade in Newtons.
        safety_factor (float): Safety factor to ensure reliable installation (default is 1.5).

    Returns:
        float: Optimal spacing between screws in mm.
        
    Raises:
        ValueError: If any input parameter is invalid.
    """
    # Validate input parameters
    if diameter <= 0 or length <= 0 or thread_pitch <= 0 or load_capacity <= 0 or facade_weight <= 0:
        raise ValueError("All input parameters must be positive numbers.")

    if safety_factor <= 1.0:
        raise ValueError("Safety factor must be greater than 1.0.")

    # Calculate the required number of screws based on load capacity and facade weight
    required_screws = math.ceil((facade_weight * safety_factor) / load_capacity)
    
    # Calculate the optimal spacing
    # Assuming a standard installation area size (e.g., 1000 mm width and height)
    installation_area = 1000  # mm (example width/height of a facade panel)
    optimal_spacing = installation_area / required_screws

    return optimal_spacing


# Example Usage:
try:
    # Example parameters based on Karen Fixing guidelines
    screw_diameter = 6.0   # mm
    screw_length = 30.0    # mm
    screw_thread_pitch = 1.25  # mm
    screw_load_capacity = 500.0  # N (example capacity)
    facade_total_weight = 5000.0  # N (example weight of facade)
    
    spacing = calculate_optimal_spacing(screw_diameter, screw_length, screw_thread_pitch, screw_load_capacity, facade_total_weight)
    print(f"Optimal Spacing Between Screws: {spacing:.2f} mm")
except ValueError as e:
    print(f"Error: {e}")
```
