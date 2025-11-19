"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Write a Python code snippet to calculate the volume of soil excavated by a Yanmar SV100 mini excavator given its bucket volume and excavation depth.
Generated: DETERMINISTIC_fe6f478e0b88c0f8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sys

def calculate_excavated_soil_volume(bucket_volume, excavation_depth):
    """
    Calculate the volume of soil excavated by a mini excavator.

    Parameters:
        bucket_volume (float): The volume of the excavator's bucket in cubic meters.
        excavation_depth (float): The depth of excavation in meters.

    Returns:
        float: The total volume of soil excavated in cubic meters.
    """
    try:
        # Validate inputs
        if bucket_volume <= 0:
            raise ValueError("Bucket volume must be greater than zero.")
        if excavation_depth <= 0:
            raise ValueError("Excavation depth must be greater than zero.")
        
        # Calculate the total volume of soil excavated
        total_volume = bucket_volume * excavation_depth
        return total_volume

    except ValueError as ve:
        # Handle invalid input values
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None

# Example usage
if __name__ == "__main__":
    try:
        # Input values
        bucket_volume = float(input("Enter the bucket volume in cubic meters: "))
        excavation_depth = float(input("Enter the excavation depth in meters: "))
        
        # Calculate and display the result
        excavated_volume = calculate_excavated_soil_volume(bucket_volume, excavation_depth)
        if excavated_volume is not None:
            print(f"The total volume of soil excavated is: {excavated_volume:.2f} cubic meters.")
    except ValueError:
        print("Please enter valid numeric values for bucket volume and excavation depth.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
