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
class Excavator:
    """
    A class to represent a mini excavator and calculate excavation depth and bucket volume.
    """

    def __init__(self, model, max_excavation_depth, bucket_volume):
        """
        Initializes the Excavator instance with model specifications.

        :param model: str - The model name of the excavator
        :param max_excavation_depth: float - The maximum excavation depth in meters
        :param bucket_volume: float - The bucket volume in cubic meters
        """
        self.model = model
        self.max_excavation_depth = max_excavation_depth
        self.bucket_volume = bucket_volume

    def calculate_excavation_depth(self, depth):
        """
        Validates and returns the excavation depth.

        :param depth: float - The desired excavation depth in meters
        :return: float - The validated excavation depth
        :raises ValueError: If the depth exceeds the maximum excavation depth
        """
        if depth < 0:
            raise ValueError("Excavation depth cannot be negative.")
        if depth > self.max_excavation_depth:
            raise ValueError(f"Excavation depth exceeds maximum limit of {self.max_excavation_depth} meters.")
        return depth

    def calculate_bucket_volume(self, quantity):
        """
        Calculates the total volume of soil that can be excavated based on the bucket volume and quantity.

        :param quantity: int - The number of bucket loads
        :return: float - The total volume in cubic meters
        """
        if quantity < 0:
            raise ValueError("Quantity of bucket loads cannot be negative.")
        return self.bucket_volume * quantity


def main():
    """
    Main function to demonstrate the Excavator class functionality.
    """
    # Specifications for Yanmar mini excavators
    excavators = {
        "ViO12": Excavator("ViO12", max_excavation_depth=2.5, bucket_volume=0.03),
        "ViO17": Excavator("ViO17", max_excavation_depth=2.8, bucket_volume=0.04),
        "ViO25": Excavator("ViO25", max_excavation_depth=3.0, bucket_volume=0.05),
        "ViO35": Excavator("ViO35", max_excavation_depth=3.5, bucket_volume=0.06),
        "SV100": Excavator("SV100", max_excavation_depth=4.0, bucket_volume=0.08),
    }

    # Example usage
    try:
        model = "ViO25"
        depth = 2.5  # Desired excavation depth
        quantity = 10  # Number of bucket loads

        excavator = excavators[model]
        validated_depth = excavator.calculate_excavation_depth(depth)
        total_volume = excavator.calculate_bucket_volume(quantity)

        print(f"Model: {excavator.model}")
        print(f"Validated Excavation Depth: {validated_depth} meters")
        print(f"Total Bucket Volume for {quantity} loads: {total_volume} cubic meters")

    except ValueError as e:
        print(f"Error: {e}")
    except KeyError:
        print("Error: Excavator model not found.")


if __name__ == "__main__":
    main()
```
