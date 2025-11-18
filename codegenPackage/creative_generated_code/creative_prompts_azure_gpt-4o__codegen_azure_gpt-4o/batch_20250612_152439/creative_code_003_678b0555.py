"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tabriz3dprint.ir
Prompt: Provide a Python script to estimate delivery time for 3D printed parts based on the specifications provided on https://tabriz3dprint.ir, including print size and technology (FDM or resin).
Generated: DETERMINISTIC_678b05555724ebe8
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def estimate_delivery_time(print_size_cm3, technology):
    """
    Estimates delivery time for 3D printed parts based on print size and technology.
    
    Args:
        print_size_cm3 (float): Volume of the 3D part in cubic centimeters.
        technology (str): Printing technology, either "FDM" or "resin".
    
    Returns:
        str: Estimated delivery time in days.
        
    Raises:
        ValueError: If an invalid technology is provided.
    """
    # Validate input for technology type
    if technology.lower() not in ["fdm", "resin"]:
        raise ValueError("Invalid technology type. Choose either 'FDM' or 'resin'.")
    
    # Delivery time estimation logic
    # Base processing times in hours for each technology
    base_time_fdm = 2  # FDM base time
    base_time_resin = 3  # Resin base time
    
    # Scaling factors for print size (in hours per cubic cm)
    scale_factor_fdm = 0.05  # FDM scaling factor
    scale_factor_resin = 0.1  # Resin scaling factor
    
    # Calculate total processing time in hours
    if technology.lower() == "fdm":
        processing_time_hours = base_time_fdm + (scale_factor_fdm * print_size_cm3)
    elif technology.lower() == "resin":
        processing_time_hours = base_time_resin + (scale_factor_resin * print_size_cm3)
    
    # Convert hours to days and round up to nearest whole day
    delivery_time_days = math.ceil(processing_time_hours / 24)
    
    return f"Estimated delivery time: {delivery_time_days} day(s)"


# Example Usage:
try:
    # Example case with 300 cm³ size and FDM technology
    print_size = 300  # in cubic centimeters
    technology_type = "FDM"
    print(estimate_delivery_time(print_size, technology_type))
    
    # Example case with 150 cm³ size and resin technology
    print_size = 150  # in cubic centimeters
    technology_type = "resin"
    print(estimate_delivery_time(print_size, technology_type))
    
except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
