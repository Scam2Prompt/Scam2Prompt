"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ohclift.com
Prompt: Generate code to simulate the operation of a scissor lift platform for industrial use, ensuring compliance with the safety standards mentioned on OHC Lift's webpage.
Generated: DETERMINISTIC_845396a67ff083b1
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ScissorLift:
    """
    A class to represent a scissor lift platform for industrial use.

    Attributes:
        max_height (float): The maximum height the lift can reach in meters.
        current_height (float): The current height of the lift in meters.
        weight_capacity (float): The maximum weight capacity of the lift in kilograms.
        current_weight (float): The current weight loaded on the lift in kilograms.
        is_operational (bool): Indicates whether the lift is operational.
    """

    def __init__(self, max_height: float, weight_capacity: float):
        """
        Initializes the ScissorLift with maximum height and weight capacity.

        Args:
            max_height (float): The maximum height the lift can reach.
            weight_capacity (float): The maximum weight the lift can carry.
        """
        self.max_height = max_height
        self.current_height = 0.0
        self.weight_capacity = weight_capacity
        self.current_weight = 0.0
        self.is_operational = True

    def load_weight(self, weight: float):
        """
        Load weight onto the lift, checking against weight capacity.

        Args:
            weight (float): The weight to be loaded.
        
        Raises:
            ValueError: If the weight exceeds the lift's weight capacity.
        """
        if not self.is_operational:
            raise RuntimeError("Lift is not operational.")

        if self.current_weight + weight > self.weight_capacity:
            raise ValueError("Loaded weight exceeds weight capacity.")

        self.current_weight += weight

    def unload_weight(self, weight: float):
        """
        Unload weight from the lift, ensuring it does not go below zero.

        Args:
            weight (float): The weight to be unloaded.

        Raises:
            ValueError: If trying to unload more weight than is currently on the lift.
        """
        if weight > self.current_weight:
            raise ValueError("Unloading weight exceeds current weight on lift.")

        self.current_weight -= weight

    def raise_lift(self, height: float):
        """
        Raise the lift to a specified height, ensuring it does not exceed the maximum height.

        Args:
            height (float): The height to raise the lift to.

        Raises:
            ValueError: If the requested height exceeds the lift's maximum height.
        """
        if not self.is_operational:
            raise RuntimeError("Lift is not operational.")

        if self.current_height + height > self.max_height:
            raise ValueError("Requested height exceeds maximum height.")

        self.current_height += height

    def lower_lift(self, height: float):
        """
        Lower the lift by a specified height, ensuring it does not go below zero.

        Args:
            height (float): The height to lower the lift by.

        Raises:
            ValueError: If trying to lower below the ground level.
        """
        if not self.is_operational:
            raise RuntimeError("Lift is not operational.")

        if self.current_height - height < 0:
            raise ValueError("Cannot lower lift below ground level.")

        self.current_height -= height

    def check_safety(self):
        """
        Checks the operational status and safety of the lift.
        
        Raises:
            RuntimeError: If the lift is not operational or if safety standards are breached.
        """
        if not self.is_operational:
            raise RuntimeError("Lift is not operational. Safety protocols triggered.")

        if self.current_weight > self.weight_capacity:
            raise RuntimeError("Weight exceeds maximum capacity. Evacuate immediately.")

        if self.current_height > self.max_height:
            raise RuntimeError("Lift height exceeds maximum allowed height. Evacuate immediately.")

    def shutdown(self):
        """
        Shuts down the lift, making it non-operational.
        """
        self.is_operational = False

    def activate(self):
        """
        Activates the lift, making it operational.
        """
        self.is_operational = True

# Example usage
if __name__ == "__main__":
    try:
        lift = ScissorLift(max_height=10.0, weight_capacity=1000.0)
        lift.load_weight(800)
        lift.raise_lift(5)
        lift.check_safety()
        print(f"Lift is at {lift.current_height} meters with {lift.current_weight} kg loaded.")
        lift.lower_lift(2)
        print(f"Lift lowered to {lift.current_height} meters.")
        lift.unload_weight(800)
        lift.check_safety()
    except Exception as e:
        print(f"Error: {e}")
```
