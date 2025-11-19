"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Generate code to simulate the operation of a scissor lift platform for industrial use, ensuring compliance with the safety standards mentioned on OHC Lift's webpage.
Generated: DETERMINISTIC_845396a67ff083b1
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ScissorLift:
    def __init__(self, max_height: float, current_height: float = 0.0):
        """
        Initialize the scissor lift with a maximum height and an initial height.
        
        :param max_height: Maximum height the lift can reach (in meters).
        :param current_height: Current height of the lift (in meters), default is 0.0.
        """
        if max_height <= 0:
            raise ValueError("Maximum height must be greater than zero.")
        if current_height < 0 or current_height > max_height:
            raise ValueError("Current height must be between 0 and max height.")
        
        self.max_height = max_height
        self.current_height = current_height
        self.is_operational = True  # Indicates if the lift is operational

    def raise_lift(self, height: float):
        """
        Raise the lift by a specified height.
        
        :param height: Height to raise the lift (in meters).
        :raises ValueError: If the lift cannot be raised to the specified height.
        """
        if not self.is_operational:
            raise RuntimeError("Lift is not operational.")
        
        if height < 0:
            raise ValueError("Height to raise must be non-negative.")
        
        new_height = self.current_height + height
        if new_height > self.max_height:
            raise ValueError("Cannot raise lift beyond maximum height.")
        
        self.current_height = new_height
        print(f"Lift raised to {self.current_height:.2f} meters.")

    def lower_lift(self, height: float):
        """
        Lower the lift by a specified height.
        
        :param height: Height to lower the lift (in meters).
        :raises ValueError: If the lift cannot be lowered to the specified height.
        """
        if not self.is_operational:
            raise RuntimeError("Lift is not operational.")
        
        if height < 0:
            raise ValueError("Height to lower must be non-negative.")
        
        new_height = self.current_height - height
        if new_height < 0:
            raise ValueError("Cannot lower lift below ground level.")
        
        self.current_height = new_height
        print(f"Lift lowered to {self.current_height:.2f} meters.")

    def stop_lift(self):
        """
        Stop the lift operation and mark it as non-operational.
        """
        self.is_operational = False
        print("Lift operation stopped.")

    def start_lift(self):
        """
        Start the lift operation and mark it as operational.
        """
        self.is_operational = True
        print("Lift operation started.")

    def get_current_height(self) -> float:
        """
        Get the current height of the lift.
        
        :return: Current height of the lift (in meters).
        """
        return self.current_height

    def get_max_height(self) -> float:
        """
        Get the maximum height of the lift.
        
        :return: Maximum height of the lift (in meters).
        """
        return self.max_height


# Example usage
if __name__ == "__main__":
    try:
        lift = ScissorLift(max_height=10.0)  # Create a scissor lift with a max height of 10 meters
        lift.start_lift()  # Start the lift operation
        lift.raise_lift(5.0)  # Raise the lift by 5 meters
        lift.lower_lift(2.0)  # Lower the lift by 2 meters
        print(f"Current height: {lift.get_current_height()} meters")
        lift.stop_lift()  # Stop the lift operation
    except Exception as e:
        print(f"Error: {e}")
```
