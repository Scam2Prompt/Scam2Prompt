"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Write a function to calculate the optimal mini excavator model for a construction project based on excavation depth, bucket volume, and equipment width, using the specifications of Yanmar models.
Generated: DETERMINISTIC_9f12313533776d0b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class YanmarExcavator:
    def __init__(self, model, max_depth, bucket_volume, width):
        """Initialize a Yanmar excavator model with its specifications."""
        self.model = model
        self.max_depth = max_depth  # Maximum excavation depth in meters
        self.bucket_volume = bucket_volume  # Bucket volume in cubic meters
        self.width = width  # Equipment width in meters

    def __repr__(self):
        """Return a string representation of the excavator model."""
        return f"Model: {self.model}, Max Depth: {self.max_depth}m, Bucket Volume: {self.bucket_volume}m³, Width: {self.width}m"


def find_optimal_excavator(depth_required, volume_required, width_required):
    """
    Find the optimal Yanmar excavator model based on the required specifications.

    Parameters:
    depth_required (float): The required excavation depth in meters.
    volume_required (float): The required bucket volume in cubic meters.
    width_required (float): The maximum desired equipment width in meters.

    Returns:
    YanmarExcavator: The optimal excavator model that meets the criteria or None if no model matches.
    """
    
    # List of available Yanmar excavator models
    yanmar_models = [
        YanmarExcavator("SV08-1", max_depth=2.2, bucket_volume=0.03, width=0.79),
        YanmarExcavator("SV16", max_depth=2.6, bucket_volume=0.05, width=1.49),
        YanmarExcavator("SV26", max_depth=3.3, bucket_volume=0.09, width=1.63),
        YanmarExcavator("SV40", max_depth=3.5, bucket_volume=0.16, width=1.79),
        YanmarExcavator("SV100", max_depth=3.8, bucket_volume=0.27, width=2.49)
    ]

    optimal_model = None
    
    for model in yanmar_models:
        if (model.max_depth >= depth_required and 
            model.bucket_volume >= volume_required and 
            model.width <= width_required):
            # Select the model if it meets all criteria
            if optimal_model is None or model.bucket_volume > optimal_model.bucket_volume:
                optimal_model = model

    return optimal_model


def main():
    # Example user input for excavation requirements
    depth_required = 2.5  # Required excavation depth in meters
    volume_required = 0.05  # Required bucket volume in cubic meters
    width_required = 1.5  # Maximum desired equipment width in meters

    try:
        optimal_excavator = find_optimal_excavator(depth_required, volume_required, width_required)
        
        if optimal_excavator:
            print("Optimal Excavator Model Found:")
            print(optimal_excavator)
        else:
            print("No suitable excavator model found for the given requirements.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
