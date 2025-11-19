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
from typing import List, Tuple

class Tire:
    """Class to represent a tire specification."""
    
    def __init__(self, specification: str):
        """Initialize the Tire object with a specification string."""
        self.specification = specification
        self.width = self.extract_width(specification)

    @staticmethod
    def extract_width(specification: str) -> int:
        """Extract the width from the tire specification."""
        try:
            # Split the specification and extract the width
            width_str = specification.split('/')[0]
            return int(width_str)
        except (IndexError, ValueError) as e:
            raise ValueError(f"Invalid tire specification: {specification}") from e

def filter_tires_by_width(tires: List[str], min_width: int, max_width: int) -> List[Tire]:
    """
    Filter a list of tire specifications by a given width range.

    Args:
        tires (List[str]): List of tire specifications.
        min_width (int): Minimum width of the tire.
        max_width (int): Maximum width of the tire.

    Returns:
        List[Tire]: List of Tire objects that fall within the specified width range.
    """
    filtered_tires = []
    
    for tire_spec in tires:
        try:
            tire = Tire(tire_spec)
            if min_width <= tire.width <= max_width:
                filtered_tires.append(tire)
        except ValueError as e:
            print(e)  # Log the error for invalid tire specifications

    return filtered_tires

# Example usage
if __name__ == "__main__":
    tire_specs = [
        "295/80 R 22.5",
        "250/75 R 16",
        "300/70 R 20",
        "invalid_specification",
        "275/65 R 18"
    ]
    
    min_width = 250
    max_width = 300
    
    filtered_tires = filter_tires_by_width(tire_specs, min_width, max_width)
    
    # Print the filtered tire specifications
    for tire in filtered_tires:
        print(tire.specification)
```
