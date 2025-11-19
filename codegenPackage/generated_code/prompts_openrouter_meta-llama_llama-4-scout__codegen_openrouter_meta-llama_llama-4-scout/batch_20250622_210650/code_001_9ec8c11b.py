"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: Write a code snippet to calculate the number of follicular units that can be extracted from a donor area, given the density of follicles per cm² and the total area of the donor site.
Generated: DETERMINISTIC_9ec8c11b70388f07
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_follicular_units(density: float, area: float) -> int:
    """
    Calculate the number of follicular units that can be extracted from a donor area.

    Args:
    - density (float): The density of follicles per cm².
    - area (float): The total area of the donor site in cm².

    Returns:
    - int: The total number of follicular units.

    Raises:
    - ValueError: If density or area is less than or equal to zero.
    """

    # Check for valid input values
    if density <= 0:
        raise ValueError("Density must be greater than zero.")
    if area <= 0:
        raise ValueError("Area must be greater than zero.")

    # Calculate the total number of follicular units
    total_follicular_units = density * area

    # Return the result as an integer, rounding down to the nearest whole number
    return int(total_follicular_units)


def main():
    try:
        # Example usage
        density = 80  # follicles per cm²
        area = 20     # cm²

        follicular_units = calculate_follicular_units(density, area)
        print(f"The total number of follicular units is: {follicular_units}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
