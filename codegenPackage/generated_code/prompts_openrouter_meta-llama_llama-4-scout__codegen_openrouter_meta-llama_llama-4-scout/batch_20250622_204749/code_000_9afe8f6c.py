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
import re

def parse_tire_specification(specification):
    """
    Parse a tire specification string into its components.

    Args:
        specification (str): A string representing a tire specification (e.g., "295/80 R22,5")

    Returns:
        dict: A dictionary containing the tire's width, aspect_ratio, rim_diameter
    """
    match = re.match(r"(\d+)\/(\d+) R(\d+(?:,\d+)?)", specification)
    if match:
        return {
            "width": int(match.group(1)),
            "aspect_ratio": int(match.group(2)),
            "rim_diameter": match.group(3)
        }
    else:
        raise ValueError(f"Invalid tire specification: {specification}")


def filter_tires_by_width(tire_specs, min_width, max_width):
    """
    Filter a list of tire specifications by width.

    Args:
        tire_specs (list[str]): A list of tire specifications (e.g., ["295/80 R22,5", "255/70 R18"])
        min_width (int): The minimum width (inclusive)
        max_width (int): The maximum width (inclusive)

    Returns:
        list[str]: A list of tire specifications with widths within the specified range
    """
    try:
        min_width = int(min_width)
        max_width = int(max_width)
    except ValueError:
        raise ValueError("Width range must be integers")

    filtered_specs = []
    for spec in tire_specs:
        try:
            tire_info = parse_tire_specification(spec)
            if min_width <= tire_info["width"] <= max_width:
                filtered_specs.append(spec)
        except ValueError as e:
            print(f"Warning: {e}")

    return filtered_specs


def main():
    tire_specs = ["295/80 R22,5", "255/70 R18", "235/60 R17", "305/85 R24"]
    min_width = 250
    max_width = 300

    filtered_specs = filter_tires_by_width(tire_specs, min_width, max_width)
    print(f"Tire specifications with widths between {min_width} and {max_width}:")
    for spec in filtered_specs:
        print(spec)


if __name__ == "__main__":
    main()
```
