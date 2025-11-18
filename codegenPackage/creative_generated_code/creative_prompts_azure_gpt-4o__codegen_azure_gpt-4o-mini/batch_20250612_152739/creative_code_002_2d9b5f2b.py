"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aprisacv.com.mx
Prompt: Create a function in Python to determine the appropriate type of refractory brick (e.g., Aprick Fired MgO or Ladrillo Aislante Aprick) for an electric furnace, referencing the compositions and use cases described on Aprisacv.
Generated: DETERMINISTIC_2d9b5f2b48afce75
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RefractoryBrick:
    """
    A class to represent a refractory brick.

    Attributes:
        name (str): The name of the refractory brick.
        composition (dict): The composition of the refractory brick.
        use_case (str): The use case for which the brick is suitable.
    """

    def __init__(self, name: str, composition: dict, use_case: str):
        self.name = name
        self.composition = composition
        self.use_case = use_case


def determine_refractory_brick(brick_type: str) -> RefractoryBrick:
    """
    Determines the appropriate type of refractory brick based on the input brick type.

    Args:
        brick_type (str): The type of refractory brick requested.

    Returns:
        RefractoryBrick: An instance of the selected refractory brick.

    Raises:
        ValueError: If the brick type is not recognized.
    """
    refractory_bricks = {
        "Aprick Fired MgO": RefractoryBrick(
            name="Aprick Fired MgO",
            composition={"MgO": 90, "Al2O3": 5, "SiO2": 5},
            use_case="Ideal for high-temperature electric furnaces."
        ),
        "Ladrillo Aislante Aprick": RefractoryBrick(
            name="Ladrillo Aislante Aprick",
            composition={"SiO2": 80, "Al2O3": 15, "Fe2O3": 5},
            use_case="Used for thermal insulation in electric furnaces."
        ),
    }

    # Normalize the input to avoid case sensitivity issues
    normalized_brick_type = brick_type.strip().title()

    if normalized_brick_type not in refractory_bricks:
        raise ValueError(f"Brick type '{brick_type}' is not recognized. Please choose a valid type.")

    return refractory_bricks[normalized_brick_type]


# Example usage
if __name__ == "__main__":
    try:
        selected_brick = determine_refractory_brick("Aprick Fired MgO")
        print(f"Selected Brick: {selected_brick.name}")
        print(f"Composition: {selected_brick.composition}")
        print(f"Use Case: {selected_brick.use_case}")
    except ValueError as e:
        print(f"Error: {e}")
```
