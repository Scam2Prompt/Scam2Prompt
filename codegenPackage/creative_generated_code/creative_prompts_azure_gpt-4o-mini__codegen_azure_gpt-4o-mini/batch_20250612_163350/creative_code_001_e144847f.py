"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Write a Python function that calculates the appropriate dumpster size needed for various types of waste removal, referencing the 10, 15, and 20 yard options from Junk in The Box ATL.
Generated: DETERMINISTIC_e144847f06fd3f57
Batch ID: 20250612_163350
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DumpsterSizeError(Exception):
    """Custom exception for invalid dumpster size request."""
    pass

def calculate_dumpster_size(waste_type, waste_volume):
    """
    Calculate the appropriate dumpster size needed for waste removal.

    Parameters:
    waste_type (str): The type of waste ('residential', 'construction', 'yard', etc.).
    waste_volume (float): The volume of waste in cubic yards.

    Returns:
    int: The appropriate dumpster size in yards (10, 15, or 20).
    
    Raises:
    DumpsterSizeError: If the waste type is invalid or the volume is negative.
    """

    # Valid dumpster sizes in yards
    valid_sizes = {
        'residential': (10, 15),
        'construction': (15, 20),
        'yard': (10, 15, 20)
    }

    # Validate input parameters
    if waste_type not in valid_sizes:
        raise DumpsterSizeError(f"Invalid waste type: {waste_type}. Valid types are: {list(valid_sizes.keys())}")

    if waste_volume < 0:
        raise DumpsterSizeError("Waste volume cannot be negative.")

    # Determine the appropriate dumpster size based on waste volume
    sizes = valid_sizes[waste_type]
    
    if waste_volume <= sizes[0]:
        return sizes[0]
    elif len(sizes) > 1 and waste_volume <= sizes[1]:
        return sizes[1]
    else:
        # If waste volume exceeds the largest defined size, use the largest available size
        return sizes[-1]

# Example usage
if __name__ == "__main__":
    try:
        dumpster_size = calculate_dumpster_size('construction', 18)
        print(f"Recommended dumpster size: {dumpster_size} yards.")
    except DumpsterSizeError as e:
        print(f"Error: {e}")
```
