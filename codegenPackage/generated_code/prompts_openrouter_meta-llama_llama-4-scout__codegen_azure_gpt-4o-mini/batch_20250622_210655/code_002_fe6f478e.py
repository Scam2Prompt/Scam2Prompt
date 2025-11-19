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
class Excavator:
    def __init__(self, bucket_volume: float):
        """
        Initializes the Excavator with a given bucket volume.

        :param bucket_volume: Volume of the excavator's bucket in cubic meters.
        """
        if bucket_volume <= 0:
            raise ValueError("Bucket volume must be a positive number.")
        self.bucket_volume = bucket_volume

    def calculate_excavated_volume(self, depth: float, width: float, length: float) -> float:
        """
        Calculates the total volume of soil excavated based on the depth, width, and length of the excavation.

        :param depth: Depth of the excavation in meters.
        :param width: Width of the excavation in meters.
        :param length: Length of the excavation in meters.
        :return: Total volume of soil excavated in cubic meters.
        """
        if depth <= 0 or width <= 0 or length <= 0:
            raise ValueError("Depth, width, and length must be positive numbers.")

        # Calculate the volume of the excavation
        excavated_volume = depth * width * length
        return excavated_volume

    def calculate_buckets_needed(self, depth: float, width: float, length: float) -> int:
        """
        Calculates the number of buckets needed to excavate the specified volume.

        :param depth: Depth of the excavation in meters.
        :param width: Width of the excavation in meters.
        :param length: Length of the excavation in meters.
        :return: Number of buckets needed to complete the excavation.
        """
        excavated_volume = self.calculate_excavated_volume(depth, width, length)
        buckets_needed = excavated_volume / self.bucket_volume
        return int(buckets_needed) + (1 if buckets_needed % 1 > 0 else 0)  # Round up to the next whole bucket


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the Excavator with a bucket volume of 0.3 cubic meters
        excavator = Excavator(bucket_volume=0.3)

        # Define excavation dimensions
        excavation_depth = 2.0  # in meters
        excavation_width = 1.5   # in meters
        excavation_length = 3.0  # in meters

        # Calculate the number of buckets needed
        buckets_needed = excavator.calculate_buckets_needed(excavation_depth, excavation_width, excavation_length)

        print(f"Number of buckets needed for excavation: {buckets_needed}")

    except ValueError as e:
        print(f"Error: {e}")
```
