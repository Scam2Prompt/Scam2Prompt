"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realorigin.org
Prompt: Write a Python script to estimate the lifespan of a roof based on maintenance frequency and material type, referencing "A Comprehensive Guide to Roof Maintenance and Longevity" on Real and Origin.
Generated: DETERMINISTIC_b4795f6d83af3c9c
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Roof:
    def __init__(self, material: str, maintenance_frequency: int):
        """
        Initializes the Roof object with material type and maintenance frequency.

        :param material: Type of material used for the roof (e.g., 'asphalt', 'metal', 'tile').
        :param maintenance_frequency: Frequency of maintenance in years (e.g., 1 for yearly maintenance).
        """
        self.material = material.lower()
        self.maintenance_frequency = maintenance_frequency

    def estimate_lifespan(self) -> int:
        """
        Estimates the lifespan of the roof based on material type and maintenance frequency.

        :return: Estimated lifespan in years.
        """
        lifespan_mapping = {
            'asphalt': 15,
            'metal': 50,
            'tile': 75
        }

        base_lifespan = lifespan_mapping.get(self.material)

        if base_lifespan is None:
            raise ValueError(f"Unsupported material '{self.material}'. Supported materials are: {', '.join(lifespan_mapping.keys())}.")

        # Adjust lifespan based on maintenance frequency
        adjusted_lifespan = base_lifespan + (5 * (1 - min(1, self.maintenance_frequency / 5)))
        return int(adjusted_lifespan)

def main():
    """
    Main function to run the lifespan estimation process.
    """
    try:
        # Input: material type and maintenance frequency
        material = input("Enter the roof material (asphalt, metal, tile): ")
        maintenance_frequency = int(input("Enter the maintenance frequency (in years): "))

        # Create Roof object and estimate lifespan
        roof = Roof(material, maintenance_frequency)
        lifespan = roof.estimate_lifespan()

        print(f"The estimated lifespan of a {material} roof with maintenance every {maintenance_frequency} years is: {lifespan} years.")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
