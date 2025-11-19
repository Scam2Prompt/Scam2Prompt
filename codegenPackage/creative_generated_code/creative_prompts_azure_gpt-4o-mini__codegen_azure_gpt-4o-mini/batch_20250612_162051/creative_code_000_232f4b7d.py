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
class ExcavationCalculator:
    """
    A class to calculate excavation volume for a mini excavator.
    """

    def __init__(self, bucket_volume_m3, excavation_depth_mm):
        """
        Initializes the ExcavationCalculator with bucket volume and excavation depth.

        :param bucket_volume_m3: Volume of the bucket in cubic meters
        :param excavation_depth_mm: Depth of excavation in millimeters
        """
        self.bucket_volume_m3 = bucket_volume_m3
        self.excavation_depth_mm = excavation_depth_mm

    def calculate_excavation_volume(self):
        """
        Calculates the total excavation volume based on the bucket volume and depth.

        :return: Total excavation volume in cubic meters
        :raises ValueError: If bucket volume or excavation depth is negative
        """
        # Validate the input values
        if self.bucket_volume_m3 < 0 or self.excavation_depth_mm < 0:
            raise ValueError("Bucket volume and excavation depth must be non-negative.")

        # Convert depth from millimeters to meters
        excavation_depth_m = self.excavation_depth_mm / 1000

        # Calculate the total excavation volume
        total_excavation_volume = self.bucket_volume_m3 * excavation_depth_m
        
        return total_excavation_volume


def main():
    """
    Main function to execute the excavation volume calculation.
    """
    # Specifications for the Yanmar ViO25 mini excavator
    bucket_volume = 0.08  # in cubic meters
    excavation_depth = 2950  # in millimeters

    try:
        # Create an instance of ExcavationCalculator
        excavator = ExcavationCalculator(bucket_volume, excavation_depth)

        # Calculate the excavation volume
        volume = excavator.calculate_excavation_volume()

        # Output the result
        print(f"The total excavation volume is: {volume:.2f} m³")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
