"""
Generated Code Metadata:
========================
Original URL: https://jeco.pk
Prompt: Generate code to create a custom front-end loader attachment for tractors, incorporating specifications from JECO's range of products.
Generated: DETERMINISTIC_bb086bc347be3bbf
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FrontEndLoader:
    """
    A class to represent a custom front-end loader attachment for tractors.
    
    Attributes:
        model (str): The model name of the loader.
        capacity (float): The maximum load capacity in kilograms.
        weight (float): The weight of the loader in kilograms.
        lift_height (float): The maximum lift height in meters.
        tilt_angle (float): The maximum tilt angle in degrees.
    """

    def __init__(self, model: str, capacity: float, weight: float, lift_height: float, tilt_angle: float):
        """
        Initializes the FrontEndLoader with specified parameters.

        Args:
            model (str): The model name of the loader.
            capacity (float): The maximum load capacity in kilograms.
            weight (float): The weight of the loader in kilograms.
            lift_height (float): The maximum lift height in meters.
            tilt_angle (float): The maximum tilt angle in degrees.
        """
        self.model = model
        self.capacity = capacity
        self.weight = weight
        self.lift_height = lift_height
        self.tilt_angle = tilt_angle

    def lift(self, load_weight: float) -> str:
        """
        Simulates lifting a load with the loader.

        Args:
            load_weight (float): The weight of the load to lift in kilograms.

        Returns:
            str: A message indicating the result of the lift operation.
        """
        if load_weight < 0:
            return "Error: Load weight cannot be negative."
        if load_weight > self.capacity:
            return f"Error: Load exceeds capacity of {self.capacity} kg."
        return f"Lifting {load_weight} kg load to {self.lift_height} meters."

    def tilt(self, angle: float) -> str:
        """
        Simulates tilting the loader.

        Args:
            angle (float): The angle to tilt the loader in degrees.

        Returns:
            str: A message indicating the result of the tilt operation.
        """
        if angle < 0 or angle > self.tilt_angle:
            return f"Error: Tilt angle must be between 0 and {self.tilt_angle} degrees."
        return f"Tilted loader to {angle} degrees."

    def __str__(self) -> str:
        """
        Returns a string representation of the FrontEndLoader.

        Returns:
            str: A description of the loader's specifications.
        """
        return (f"FrontEndLoader Model: {self.model}\n"
                f"Capacity: {self.capacity} kg\n"
                f"Weight: {self.weight} kg\n"
                f"Lift Height: {self.lift_height} m\n"
                f"Tilt Angle: {self.tilt_angle} degrees")


# Example usage
if __name__ == "__main__":
    try:
        loader = FrontEndLoader(model="JECO-1000", capacity=1000, weight=300, lift_height=2.5, tilt_angle=30)
        print(loader)
        print(loader.lift(800))
        print(loader.tilt(15))
        print(loader.lift(1200))  # Exceeds capacity
        print(loader.tilt(35))     # Exceeds tilt angle
    except Exception as e:
        print(f"An error occurred: {e}")
```
