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
"""
Earth Surface Water Coverage Calculator

Calculates the percentage of water covering the Earth's surface.
"""

def calculate_water_coverage(percentage: float) -> dict:
    """
    Calculates the percentage of water covering the Earth's surface.

    Args:
        percentage (float): The percentage of water covering the Earth's surface.

    Returns:
        dict: A dictionary containing the percentage of water and land covering the Earth's surface.

    Raises:
        ValueError: If the percentage is not between 0 and 100.
    """
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100")

    water_coverage = percentage
    land_coverage = 100 - water_coverage

    return {
        "water": water_coverage,
        "land": land_coverage
    }


def main() -> None:
    try:
        # Given percentage of water covering the Earth's surface
        water_percentage = 70.0

        # Calculate water and land coverage
        coverage = calculate_water_coverage(water_percentage)

        # Print the results
        print(f"Water coverage: {coverage['water']}%")
        print(f"Land coverage: {coverage['land']}%")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
