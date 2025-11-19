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
class MiniExcavator:
    """
    A class to represent a mini excavator and calculate excavation volume.
    
    Attributes:
        bucket_volume (float): Volume of the excavator's bucket in cubic meters (m³).
        max_depth (float): Maximum excavation depth in meters (m).
    """
    
    def __init__(self, bucket_volume: float, max_depth: float):
        """
        Initialize the MiniExcavator with bucket volume and max excavation depth.
        
        Args:
            bucket_volume (float): Bucket volume in m³.
            max_depth (float): Maximum excavation depth in mm (converted to m internally).
        """
        self.bucket_volume = bucket_volume
        self.max_depth = max_depth / 1000  # Convert mm to m
        
    def calculate_volume(self, depth: float) -> float:
        """
        Calculate the excavation volume based on the given depth.
        
        Args:
            depth (float): Desired excavation depth in mm.
            
        Returns:
            float: Total excavation volume in m³.
            
        Raises:
            ValueError: If depth exceeds max_depth or is negative.
        """
        depth_m = depth / 1000  # Convert mm to m
        
        if depth_m > self.max_depth:
            raise ValueError(f"Depth {depth}mm exceeds maximum depth of {self.max_depth * 1000}mm")
        if depth_m < 0:
            raise ValueError("Depth cannot be negative")
            
        # Assuming each bucket load excavates the full bucket volume
        # This is a simplified calculation - real-world factors may affect actual volume
        return self.bucket_volume * (depth_m / self.max_depth)

# Example usage
if __name__ == "__main__":
    try:
        # Create a Yanmar ViO25 mini excavator instance
        yanmar_vio25 = MiniExcavator(bucket_volume=0.08, max_depth=2950)
        
        # Calculate volume for a desired depth (e.g., 2000mm)
        desired_depth = 2000  # in mm
        volume = yanmar_vio25.calculate_volume(desired_depth)
        
        print(f"Excavation volume for {desired_depth}mm depth: {volume:.3f} m³")
        
    except ValueError as e:
        print(f"Error: {e}")
```
