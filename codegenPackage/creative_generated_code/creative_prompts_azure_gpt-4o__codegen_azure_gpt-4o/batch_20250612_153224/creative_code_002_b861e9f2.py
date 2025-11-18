"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sardiniameetsazores.eu
Prompt: Generate a script to calculate the throughput of a "كسارة الإمباكيت بالسلسلة CI5X" based on input material properties and crusher specifications provided on the Sardinia Meets Azores site.
Generated: DETERMINISTIC_b861e9f255b066d7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the throughput of a CI5X Impact Crusher based on input material properties
# and crusher specifications. 

# Import necessary modules
import math

def calculate_throughput(material_density, feed_size, rotor_speed, crushing_ratio, efficiency_factor):
    """
    Calculate the throughput of the CI5X Impact Crusher.

    Parameters:
    material_density (float): Density of the input material in kg/m^3.
    feed_size (float): Average feed size of the material in mm.
    rotor_speed (float): Rotor speed in revolutions per minute (RPM).
    crushing_ratio (float): Crusher's crushing ratio.
    efficiency_factor (float): Efficiency factor of the crusher (value between 0 and 1).

    Returns:
    float: Throughput of the crusher in tons/hour.
    """
    try:
        # Validate inputs
        if not (0 < efficiency_factor <= 1):
            raise ValueError("Efficiency factor must be between 0 and 1.")
        if material_density <= 0 or feed_size <= 0 or rotor_speed <= 0 or crushing_ratio <= 0:
            raise ValueError("All inputs must be positive values.")

        # Convert feed size from mm to meters
        feed_size_m = feed_size / 1000.0

        # Calculate throughput using a simplified formula
        # Throughput (tons/hour) = Material Density * Feed Size * Rotor Speed * Crushing Ratio * Efficiency Factor
        throughput = (
            material_density * feed_size_m * rotor_speed * crushing_ratio * efficiency_factor
        ) / 1000.0  # Convert to tons
      
        return throughput

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Crusher specifications and material properties
    material_density = 2400  # kg/m^3 (example: granite)
    feed_size = 100  # mm
    rotor_speed = 1500  # RPM
    crushing_ratio = 10  # Typical value
    efficiency_factor = 0.85  # 85% efficiency

    # Calculate and display the throughput
    throughput = calculate_throughput(
        material_density, feed_size, rotor_speed, crushing_ratio, efficiency_factor
    )

    if throughput is not None:
        print(f"The calculated throughput of the CI5X Impact Crusher is {throughput:.2f} tons/hour.")
```
