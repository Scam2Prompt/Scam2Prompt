"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Write Python code to calculate excavation depth and bucket volume for Yanmar mini excavators, using specifications like those of the ViO12, ViO17, ViO25, ViO35, and SV100 models.
Generated: DETERMINISTIC_887a087590e7aa20
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Excavator:
    """A class to represent a mini excavator and calculate excavation specifications."""
    
    def __init__(self, model, bucket_capacity, max_excavation_depth):
        """
        Initializes an instance of the Excavator class.
        
        Args:
            model (str): The model name of the excavator.
            bucket_capacity (float): The bucket capacity in cubic meters.
            max_excavation_depth (float): The maximum excavation depth in meters.
        """
        self.model = model
        self.bucket_capacity = bucket_capacity
        self.max_excavation_depth = max_excavation_depth

    def calculate_bucket_volume(self, depth, width, length):
        """
        Calculates the volume of the bucket based on given dimensions.
        
        Args:
            depth (float): Depth of the bucket in meters.
            width (float): Width of the bucket in meters.
            length (float): Length of the bucket in meters.
        
        Returns:
            float: Volume of the bucket in cubic meters.
        """
        try:
            volume = depth * width * length
            return volume
        except Exception as e:
            print(f"Error calculating bucket volume: {e}")
            return None

    def is_excavation_depth_valid(self, depth):
        """
        Checks if the requested excavation depth is within the excavator's limits.
        
        Args:
            depth (float): The requested excavation depth in meters.
        
        Returns:
            bool: True if depth is valid, otherwise False.
        """
        return depth <= self.max_excavation_depth


# Example usage
if __name__ == "__main__":
    # Specifications for Yanmar mini excavators based on user request
    excavators = [
        Excavator("ViO12", bucket_capacity=0.03, max_excavation_depth=2.4),
        Excavator("ViO17", bucket_capacity=0.04, max_excavation_depth=2.8),
        Excavator("ViO25", bucket_capacity=0.06, max_excavation_depth=3.2),
        Excavator("ViO35", bucket_capacity=0.09, max_excavation_depth=3.5),
        Excavator("SV100", bucket_capacity=0.1, max_excavation_depth=3.85),
    ]

    # Sample calculations
    for excavator in excavators:
        print(f"Model: {excavator.model}")
        
        # Calculate volume of a bucket with dimensions (depth, width, length)
        width = 0.5  # in meters
        length = 1.0  # in meters
        depth = 0.6  # in meters
        
        bucket_volume = excavator.calculate_bucket_volume(depth, width, length)
        print(f"Calculated Bucket Volume: {bucket_volume} m³")

        # Validate excavation depth
        requested_depth = 3.0  # in meters
        if excavator.is_excavation_depth_valid(requested_depth):
            print(f"Requested excavation depth {requested_depth}m is valid.")
        else:
            print(f"Requested excavation depth {requested_depth}m exceeds maximum limit of {excavator.max_excavation_depth}m.")
        
        print("-" * 40)
```
