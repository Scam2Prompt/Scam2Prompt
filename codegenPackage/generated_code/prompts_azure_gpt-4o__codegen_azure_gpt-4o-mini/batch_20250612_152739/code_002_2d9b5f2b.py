"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: Create a function in Python to determine the appropriate type of refractory brick (e.g., Aprick Fired MgO or Ladrillo Aislante Aprick) for an electric furnace, referencing the compositions and use cases described on Aprisacv.
Generated: DETERMINISTIC_2d9b5f2b48afce75
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class RefractoryBrick:
    def __init__(self, name, composition, use_case):
        """
        Initialize a RefractoryBrick instance.

        :param name: str - The name of the refractory brick.
        :param composition: dict - The composition of the brick (e.g., materials and their percentages).
        :param use_case: str - The specific use case for the brick.
        """
        self.name = name
        self.composition = composition
        self.use_case = use_case

    def __str__(self):
        return f"{self.name}: {self.composition}, Use Case: {self.use_case}"


def determine_refractory_brick(temperature, application):
    """
    Determine the appropriate type of refractory brick for an electric furnace.

    :param temperature: float - The operating temperature of the electric furnace in Celsius.
    :param application: str - The specific application or use case for the furnace.
    :return: RefractoryBrick - The recommended refractory brick.
    :raises ValueError: If the temperature or application is not valid.
    """
    # Define a list of available refractory bricks
    bricks = [
        RefractoryBrick("Aprick Fired MgO", {"MgO": 90, "SiO2": 5, "Al2O3": 5}, "High-temperature applications"),
        RefractoryBrick("Ladrillo Aislante Aprick", {"Al2O3": 30, "SiO2": 70}, "Insulation for lower temperatures"),
    ]

    # Validate input parameters
    if not isinstance(temperature, (int, float)) or temperature <= 0:
        raise ValueError("Temperature must be a positive number.")
    
    if not isinstance(application, str) or not application:
        raise ValueError("Application must be a non-empty string.")

    # Determine the appropriate brick based on temperature and application
    for brick in bricks:
        if (temperature > 1500 and "high-temperature" in application.lower() and "high-temperature" in brick.use_case.lower()):
            return brick
        elif (temperature <= 1500 and "insulation" in application.lower() and "insulation" in brick.use_case.lower()):
            return brick

    raise ValueError("No suitable refractory brick found for the given temperature and application.")


# Example usage
if __name__ == "__main__":
    try:
        brick = determine_refractory_brick(1600, "high-temperature steel melting")
        print(brick)
    except ValueError as e:
        print(f"Error: {e}")
```
