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
def calculate_excavated_volume(bucket_volume: float, excavation_depth: float, passes: int = 1) -> float:
    """
    Calculate the total volume of soil excavated by a Yanmar SV100 mini excavator.
    
    Args:
        bucket_volume: Volume of the excavator's bucket in cubic meters (m³)
        excavation_depth: Depth of excavation in meters (m)
        passes: Number of passes/excavation cycles (default: 1)
        
    Returns:
        Total excavated volume in cubic meters (m³)
        
    Raises:
        ValueError: If any input parameter is negative
    """
    # Validate input parameters
    if bucket_volume < 0 or excavation_depth < 0 or passes < 0:
        raise ValueError("All parameters must be non-negative")
    
    # Calculate total excavated volume
    total_volume = bucket_volume * excavation_depth * passes
    
    return total_volume


# Example usage
if __name__ == "__main__":
    try:
        bucket_vol = 0.05  # Typical bucket volume for SV100 (0.05 m³)
        depth = 1.5       # Excavation depth in meters
        num_passes = 10   # Number of excavation passes
        
        volume = calculate_excavated_volume(bucket_vol, depth, num_passes)
        print(f"Total excavated volume: {volume:.2f} m³")
        
    except ValueError as e:
        print(f"Error: {e}")
```
