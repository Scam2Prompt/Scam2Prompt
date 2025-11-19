"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Write a function to calculate the optimal mini excavator model for a construction project based on excavation depth, bucket volume, and equipment width, using the specifications of Yanmar models.
Generated: DETERMINISTIC_9f12313533776d0b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MiniExcavator:
    """
    Represents a mini excavator model with its specifications.
    """
    def __init__(self, model_name, max_depth, bucket_volume, width):
        self.model_name = model_name
        self.max_depth = max_depth  # in meters
        self.bucket_volume = bucket_volume  # in cubic meters
        self.width = width  # in meters


class ExcavatorSelector:
    """
    Selects the optimal mini excavator model based on project requirements.
    """
    def __init__(self):
        # Initialize with Yanmar mini excavator specifications
        self.excavators = [
            MiniExcavator("Yanmar SV08", 1.94, 0.02, 0.98),
            MiniExcavator("Yanmar SV17", 2.64, 0.04, 1.49),
            MiniExcavator("Yanmar SV26", 3.05, 0.06, 1.79),
            MiniExcavator("Yanmar SV40", 3.81, 0.08, 2.09),
            MiniExcavator("Yanmar SV60", 4.11, 0.12, 2.49),
            MiniExcavator("Yanmar SV75", 4.42, 0.15, 2.59),
        ]

    def find_optimal_excavator(self, required_depth, required_bucket_volume, max_width=None):
        """
        Finds the optimal excavator model based on project requirements.
        
        Args:
            required_depth (float): Minimum required excavation depth in meters.
            required_bucket_volume (float): Minimum required bucket volume in cubic meters.
            max_width (float, optional): Maximum allowed equipment width in meters. Defaults to None.
        
        Returns:
            MiniExcavator: The optimal excavator model, or None if no suitable model is found.
        """
        if required_depth <= 0 or required_bucket_volume <= 0:
            raise ValueError("Depth and bucket volume must be positive values.")
        
        if max_width is not None and max_width <= 0:
            raise ValueError("Maximum width must be a positive value if specified.")

        suitable_excavators = []
        
        for excavator in self.excavators:
            # Check if excavator meets all requirements
            if (excavator.max_depth >= required_depth and
                excavator.bucket_volume >= required_bucket_volume and
                (max_width is None or excavator.width <= max_width)):
                
                suitable_excavators.append(excavator)
        
        if not suitable_excavators:
            return None
        
        # Select the smallest suitable excavator (by width)
        return min(suitable_excavators, key=lambda x: x.width)


# Example usage
if __name__ == "__main__":
    selector = ExcavatorSelector()
    
    try:
        # Test case 1: Standard requirements
        optimal_excavator = selector.find_optimal_excavator(
            required_depth=3.0,
            required_bucket_volume=0.05,
            max_width=2.0
        )
        print(f"Optimal excavator: {optimal_excavator.model_name if optimal_excavator else 'None found'}")

        # Test case 2: No width restriction
        optimal_excavator = selector.find_optimal_excavator(
            required_depth=4.0,
            required_bucket_volume=0.1
        )
        print(f"Optimal excavator: {optimal_excavator.model_name if optimal_excavator else 'None found'}")

        # Test case 3: No suitable excavator
        optimal_excavator = selector.find_optimal_excavator(
            required_depth=5.0,
            required_bucket_volume=0.2
        )
        print(f"Optimal excavator: {optimal_excavator.model_name if optimal_excavator else 'None found'}")

    except ValueError as e:
        print(f"Error: {e}")
```
