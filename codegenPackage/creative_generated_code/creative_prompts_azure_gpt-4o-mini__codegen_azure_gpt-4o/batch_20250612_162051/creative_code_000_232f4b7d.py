"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Generate code to calculate the excavation volume for a Yanmar ViO25 miniexcavadora using its specifications: bucket volume of 0.08 m³ and excavation depth of 2,950 mm.
Generated: DETERMINISTIC_232f4b7d464d8cc0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Excavation Volume Calculator for Yanmar ViO25 Mini Excavator

# Constants for the specifications of the Yanmar ViO25 mini excavator
BUCKET_VOLUME_M3 = 0.08  # Bucket volume in cubic meters
EXCAVATION_DEPTH_MM = 2950  # Excavation depth in millimeters

# Conversion factor from millimeters to meters
MM_TO_M_CONVERSION = 0.001

def calculate_excavation_volume(bucket_volume, excavation_depth_mm):
    """
    Calculate the total excavation volume based on bucket volume and excavation depth.

    Args:
        bucket_volume (float): The volume of the excavator bucket in cubic meters.
        excavation_depth_mm (int): The maximum excavation depth in millimeters.

    Returns:
        float: The total excavation volume in cubic meters.
    """
    try:
        # Convert excavation depth from millimeters to meters
        excavation_depth_m = excavation_depth_mm * MM_TO_M_CONVERSION

        # Calculate total excavation volume
        excavation_volume = bucket_volume * excavation_depth_m
        return excavation_volume
    except TypeError as e:
        # Handle incorrect argument types
        raise ValueError("Invalid input type. Please ensure bucket_volume is a float and excavation_depth_mm is an integer.") from e

if __name__ == "__main__":
    try:
        # Calculate excavation volume
        excavation_volume_m3 = calculate_excavation_volume(BUCKET_VOLUME_M3, EXCAVATION_DEPTH_MM)

        # Print the result
        print(f"Total Excavation Volume: {excavation_volume_m3:.3f} m³")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
```
