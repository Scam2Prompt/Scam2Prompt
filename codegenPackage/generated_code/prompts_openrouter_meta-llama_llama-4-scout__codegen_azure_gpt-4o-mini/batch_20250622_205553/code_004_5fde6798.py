"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Develop a technical specification for an hydraulic disabled platform with a lifting capacity of 500 kg, incorporating the design and safety considerations highlighted in the OHC Lift product catalog.
Generated: DETERMINISTIC_5fde67988cb144bf
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HydraulicPlatform:
    """
    A class to represent a hydraulic disabled platform.

    Attributes:
        capacity (float): The maximum lifting capacity of the platform in kg.
        height (float): The current height of the platform in meters.
        is_operational (bool): Status of the platform's operational state.
    """

    def __init__(self, capacity: float):
        """
        Initializes the hydraulic platform with a specified lifting capacity.

        Args:
            capacity (float): The lifting capacity of the platform in kg.

        Raises:
            ValueError: If the capacity is less than or equal to zero.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")
        self.capacity = capacity
        self.height = 0.0  # Initial height
        self.is_operational = True  # Platform is operational by default

    def lift(self, weight: float, height_increase: float):
        """
        Lifts the platform by a specified height if within capacity limits.

        Args:
            weight (float): The weight to lift in kg.
            height_increase (float): The height to lift the platform in meters.

        Raises:
            ValueError: If the weight exceeds the platform's capacity.
            RuntimeError: If the platform is not operational.
        """
        if not self.is_operational:
            raise RuntimeError("The platform is not operational.")
        if weight > self.capacity:
            raise ValueError("Weight exceeds platform capacity.")
        
        self.height += height_increase
        print(f"Platform lifted to {self.height} meters.")

    def lower(self, height_decrease: float):
        """
        Lowers the platform by a specified height.

        Args:
            height_decrease (float): The height to lower the platform in meters.

        Raises:
            ValueError: If the height decrease is greater than the current height.
        """
        if height_decrease > self.height:
            raise ValueError("Cannot lower below ground level.")
        
        self.height -= height_decrease
        print(f"Platform lowered to {self.height} meters.")

    def disable(self):
        """
        Disables the platform, making it non-operational.
        """
        self.is_operational = False
        print("Platform has been disabled.")

    def enable(self):
        """
        Enables the platform, making it operational again.
        """
        self.is_operational = True
        print("Platform is now operational.")

    def get_status(self):
        """
        Returns the current status of the platform.

        Returns:
            dict: A dictionary containing the current height, capacity, and operational status.
        """
        return {
            "current_height": self.height,
            "capacity": self.capacity,
            "is_operational": self.is_operational
        }


# Example usage
if __name__ == "__main__":
    try:
        platform = HydraulicPlatform(capacity=500)  # Create a platform with 500 kg capacity
        platform.lift(weight=300, height_increase=2)  # Lift with 300 kg
        platform.lower(height_decrease=1)  # Lower by 1 meter
        print(platform.get_status())  # Get current status
        platform.disable()  # Disable the platform
    except Exception as e:
        print(f"An error occurred: {e}")
```
