"""
Generated Code Metadata:
========================
Original URL: https://efeitoharmonie.com.br
Prompt: Write Python code to calculate the average number of hair follicles per unit based on the FUE technique described on the Efeito Harmonie website, assuming 01 to 06 hairs per follicle with an average of 2.5 hairs per follicle.
Generated: DETERMINISTIC_4da89591ad28fa11
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_average_hair_follicles(unit_area, min_hairs_per_follicle=1, max_hairs_per_follicle=6, average_hairs_per_follicle=2.5):
    """
    Calculate the average number of hair follicles per unit based on the FUE technique.

    Args:
        unit_area (float): The area of the unit.
        min_hairs_per_follicle (int, optional): The minimum number of hairs per follicle. Defaults to 1.
        max_hairs_per_follicle (int, optional): The maximum number of hairs per follicle. Defaults to 6.
        average_hairs_per_follicle (float, optional): The average number of hairs per follicle. Defaults to 2.5.

    Returns:
        float: The average number of hair follicles per unit.

    Raises:
        ValueError: If unit_area is not a positive number.
        ValueError: If min_hairs_per_follicle, max_hairs_per_follicle or average_hairs_per_follicle is not a positive number.
    """

    # Validate input parameters
    if unit_area <= 0:
        raise ValueError("Unit area must be a positive number.")

    if min_hairs_per_follicle <= 0 or max_hairs_per_follicle <= 0 or average_hairs_per_follicle <= 0:
        raise ValueError("Hairs per follicle must be a positive number.")

    if min_hairs_per_follicle > max_hairs_per_follicle:
        raise ValueError("Minimum hairs per follicle cannot be greater than maximum hairs per follicle.")

    # Assuming a linear distribution for simplicity, in reality this may vary
    average_follicles_per_unit = unit_area * (average_hairs_per_follicle / (min_hairs_per_follicle + max_hairs_per_follicle) * 2)

    return average_follicles_per_unit


def main():
    try:
        unit_area = 1.0  # example unit area
        average_follicles = calculate_average_hair_follicles(unit_area)
        print(f"The average number of hair follicles per unit is: {average_follicles}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
