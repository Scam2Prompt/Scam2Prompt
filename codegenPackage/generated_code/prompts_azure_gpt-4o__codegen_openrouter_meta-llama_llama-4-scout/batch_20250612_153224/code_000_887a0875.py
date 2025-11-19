"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Write Python code to calculate excavation depth and bucket volume for Yanmar mini excavators, using specifications like those of the ViO12, ViO17, ViO25, ViO35, and SV100 models.
Generated: DETERMINISTIC_887a087590e7aa20
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# excavation_calculator.py

class YanmarExcavator:
    def __init__(self, model, max_depth, bucket_capacity, bucket_width):
        """
        Initialize a Yanmar excavator model.

        Args:
            model (str): Model name (e.g., ViO12, ViO17, etc.)
            max_depth (float): Maximum excavation depth in meters
            bucket_capacity (float): Bucket capacity in cubic meters
            bucket_width (float): Bucket width in meters
        """
        self.model = model
        self.max_depth = max_depth
        self.bucket_capacity = bucket_capacity
        self.bucket_width = bucket_width

    def calculate_excavation_depth(self, slope_angle):
        """
        Calculate excavation depth based on slope angle.

        Args:
            slope_angle (float): Slope angle in degrees

        Returns:
            float: Excavation depth in meters
        """
        # Assuming a simple linear relationship for demonstration purposes
        # In practice, this may require a more complex calculation or lookup table
        excavation_depth = self.max_depth * (1 - (slope_angle / 90))
        return excavation_depth

    def calculate_bucket_volume(self, fill_factor=0.8):
        """
        Calculate bucket volume.

        Args:
            fill_factor (float, optional): Bucket fill factor (default: 0.8)

        Returns:
            float: Bucket volume in cubic meters
        """
        bucket_volume = self.bucket_capacity * fill_factor
        return bucket_volume


class ExcavatorDatabase:
    def __init__(self):
        self.excavators = {
            "ViO12": YanmarExcavator("ViO12", 4.5, 0.12, 0.6),
            "ViO17": YanmarExcavator("ViO17", 5.2, 0.17, 0.7),
            "ViO25": YanmarExcavator("ViO25", 6.1, 0.25, 0.8),
            "ViO35": YanmarExcavator("ViO35", 7.0, 0.35, 0.9),
            "SV100": YanmarExcavator("SV100", 8.0, 0.5, 1.0),
        }

    def get_excavator(self, model):
        """
        Get an excavator model from the database.

        Args:
            model (str): Model name

        Returns:
            YanmarExcavator: Excavator model or None if not found
        """
        return self.excavators.get(model)


def main():
    database = ExcavatorDatabase()

    model_name = input("Enter excavator model (e.g., ViO12, ViO17, etc.): ")
    excavator = database.get_excavator(model_name)

    if excavator is None:
        print(f"Error: Excavator model '{model_name}' not found.")
        return

    slope_angle = float(input("Enter slope angle (degrees): "))
    excavation_depth = excavator.calculate_excavation_depth(slope_angle)
    print(f"Excavation depth: {excavation_depth:.2f} meters")

    bucket_volume = excavator.calculate_bucket_volume()
    print(f"Bucket volume: {bucket_volume:.2f} cubic meters")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
```
