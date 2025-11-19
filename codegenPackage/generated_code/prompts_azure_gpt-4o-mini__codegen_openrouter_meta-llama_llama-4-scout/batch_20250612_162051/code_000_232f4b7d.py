"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Generate code to calculate the excavation volume for a Yanmar ViO25 miniexcavadora using its specifications: bucket volume of 0.08 m³ and excavation depth of 2,950 mm.
Generated: DETERMINISTIC_232f4b7d464d8cc0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# excavation_calculator.py

class Miniexcavator:
    def __init__(self, bucket_volume, excavation_depth):
        """
        Initialize a Miniexcavator object.

        Args:
            bucket_volume (float): The volume of the bucket in cubic meters (m³).
            excavation_depth (float): The maximum excavation depth in millimeters (mm).
        """
        self.bucket_volume = bucket_volume  # m³
        self.excavation_depth = excavation_depth  # mm

    def calculate_excavation_volume(self, excavation_length, excavation_width):
        """
        Calculate the excavation volume.

        Args:
            excavation_length (float): The length of the excavation in meters (m).
            excavation_width (float): The width of the excavation in meters (m).

        Returns:
            float: The excavation volume in cubic meters (m³).

        Raises:
            ValueError: If excavation length or width is negative.
        """
        if excavation_length < 0 or excavation_width < 0:
            raise ValueError("Excavation length and width must be non-negative.")

        # Convert excavation depth from mm to m
        excavation_depth_m = self.excavation_depth / 1000

        # Calculate excavation volume in m³
        excavation_volume = excavation_length * excavation_width * excavation_depth_m

        # Calculate the number of buckets needed
        num_buckets = excavation_volume / self.bucket_volume

        return excavation_volume, num_buckets


def main():
    try:
        # Yanmar ViO25 miniexcavator specifications
        bucket_volume = 0.08  # m³
        excavation_depth = 2950  # mm

        miniexcavator = Miniexcavator(bucket_volume, excavation_depth)

        # Example usage
        excavation_length = 10  # m
        excavation_width = 5  # m

        excavation_volume, num_buckets = miniexcavator.calculate_excavation_volume(excavation_length, excavation_width)

        print(f"Excavation volume: {excavation_volume:.2f} m³")
        print(f"Number of buckets: {num_buckets:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
