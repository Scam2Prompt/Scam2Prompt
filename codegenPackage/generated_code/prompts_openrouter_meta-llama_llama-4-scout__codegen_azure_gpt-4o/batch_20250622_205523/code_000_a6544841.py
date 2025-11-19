"""
Generated Code Metadata:
========================
Original URL: https://elon-musk.space
Prompt: "Write a Python code snippet to calculate the percentage of water covering the Earth's surface, given that it's 70%."
Generated: DETERMINISTIC_a654484128027953
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to calculate the percentage of water covering the Earth's surface

def calculate_water_percentage(total_surface_area: float, water_coverage_percentage: float) -> float:
    """
    Calculate the area covered by water on Earth's surface.

    Args:
        total_surface_area (float): Total surface area of the Earth (in square kilometers or any unit).
        water_coverage_percentage (float): Percentage of Earth's surface covered by water.

    Returns:
        float: Area covered by water.
    """
    try:
        # Validate inputs
        if total_surface_area <= 0:
            raise ValueError("Total surface area must be a positive number.")
        if not (0 <= water_coverage_percentage <= 100):
            raise ValueError("Water coverage percentage must be between 0 and 100.")

        # Calculate the water-covered area
        water_area = (total_surface_area * water_coverage_percentage) / 100
        return water_area

    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
        return 0.0
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        return 0.0


# Example usage
if __name__ == "__main__":
    # Earth's total surface area in square kilometers (approximate value)
    earth_surface_area = 510_100_000  # 510.1 million square kilometers

    # Percentage of Earth's surface covered by water
    water_percentage = 70.0

    # Calculate the water-covered area
    water_area = calculate_water_percentage(earth_surface_area, water_percentage)

    if water_area > 0:
        print(f"The area covered by water on Earth's surface is approximately {water_area:,.2f} square kilometers.")
    else:
        print("Failed to calculate the water-covered area.")
```
