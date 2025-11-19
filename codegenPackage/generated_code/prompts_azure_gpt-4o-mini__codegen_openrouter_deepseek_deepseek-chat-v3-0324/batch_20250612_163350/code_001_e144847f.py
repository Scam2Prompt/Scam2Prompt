"""
Generated Code Metadata:
========================
Original URL: https://junkintheboxatl.com
Prompt: Write a Python function that calculates the appropriate dumpster size needed for various types of waste removal, referencing the 10, 15, and 20 yard options from Junk in The Box ATL.
Generated: DETERMINISTIC_e144847f06fd3f57
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_dumpster_size(waste_type, volume_cubic_yards):
    """
    Calculate the appropriate dumpster size needed for waste removal based on type and volume.
    
    Parameters:
    - waste_type (str): Type of waste (e.g., 'construction', 'household', 'yard')
    - volume_cubic_yards (float): Estimated volume of waste in cubic yards
    
    Returns:
    - str: Recommended dumpster size ('10-yard', '15-yard', '20-yard', or 'Special handling required')
    
    Raises:
    - ValueError: If volume_cubic_yards is negative or waste_type is not recognized
    """
    
    # Validate input
    if volume_cubic_yards < 0:
        raise ValueError("Volume cannot be negative.")
    
    waste_type = waste_type.lower()
    if waste_type not in ['construction', 'household', 'yard']:
        raise ValueError("Unrecognized waste type. Must be 'construction', 'household', or 'yard'.")
    
    # Determine dumpster size based on volume and waste type
    if volume_cubic_yards <= 10:
        return '10-yard'
    elif volume_cubic_yards <= 15:
        return '15-yard'
    elif volume_cubic_yards <= 20:
        return '20-yard'
    else:
        return 'Special handling required'
```
