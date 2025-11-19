"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Write a Python code snippet to filter tire products by size, given a list of tire specifications (e.g., 295/80 R 22,5) and a desired width range (e.g., 250-300).
Generated: DETERMINISTIC_9afe8f6c7ddbd4d4
Batch ID: 20250622_204749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def filter_tires_by_width(tire_specs, min_width, max_width):
    """
    Filters a list of tire specifications by width range.
    
    Args:
        tire_specs (list): List of tire specification strings (e.g., "295/80 R 22,5")
        min_width (int): Minimum width in millimeters
        max_width (int): Maximum width in millimeters
    
    Returns:
        list: Filtered list of tire specifications that fall within the width range
    """
    filtered_tires = []
    
    for spec in tire_specs:
        try:
            # Extract the width part (first part before '/')
            width_part = spec.split('/')[0]
            width = int(width_part)
            
            if min_width <= width <= max_width:
                filtered_tires.append(spec)
        except (IndexError, ValueError):
            # Skip malformed specifications
            continue
    
    return filtered_tires


# Example usage:
if __name__ == "__main__":
    tire_list = [
        "295/80 R 22,5",
        "245/75 R 16",
        "315/70 R 17,5",
        "285/65 R 20",
        "invalid_spec",
        "300/55 R 18"
    ]
    
    min_w = 250
    max_w = 300
    
    filtered = filter_tires_by_width(tire_list, min_w, max_w)
    print("Filtered tires:", filtered)
```
