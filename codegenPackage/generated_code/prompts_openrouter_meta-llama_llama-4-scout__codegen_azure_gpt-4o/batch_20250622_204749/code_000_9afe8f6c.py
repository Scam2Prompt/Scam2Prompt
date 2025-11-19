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
# Import necessary modules
from typing import List, Tuple

def filter_tires_by_size(tire_specs: List[str], width_range: Tuple[int, int]) -> List[str]:
    """
    Filters tire products by size based on the given width range.

    Args:
        tire_specs (List[str]): A list of tire specifications in the format "width/ratio R diameter".
        width_range (Tuple[int, int]): A tuple specifying the desired width range (min_width, max_width).

    Returns:
        List[str]: A list of tire specifications that fall within the desired width range.
    """
    # Unpack the width range
    min_width, max_width = width_range

    # Validate width range
    if min_width > max_width:
        raise ValueError("Invalid width range: min_width cannot be greater than max_width.")

    # Initialize the filtered list
    filtered_tires = []

    # Iterate through the tire specifications
    for spec in tire_specs:
        try:
            # Split the specification to extract the width
            width = int(spec.split('/')[0])

            # Check if the width falls within the desired range
            if min_width <= width <= max_width:
                filtered_tires.append(spec)
        except (ValueError, IndexError):
            # Handle invalid tire specification format
            print(f"Warning: Skipping invalid tire specification '{spec}'.")

    return filtered_tires


# Example usage
if __name__ == "__main__":
    # List of tire specifications
    tires = ["295/80 R 22.5", "250/70 R 20", "305/75 R 24", "invalid_spec", "275/65 R 18"]

    # Desired width range
    width_range = (250, 300)

    # Filter tires by size
    filtered_tires = filter_tires_by_size(tires, width_range)

    # Output the filtered list
    print("Filtered Tires:", filtered_tires)
```
