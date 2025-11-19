"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Design a hydraulic vehicle lift system for a parking garage with a capacity of 5 tons, considering the dimensions and safety features discussed on ohclift.com.
Generated: DETERMINISTIC_ea4675cd6dd91775
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HydraulicLift:
    """
    A class to represent a hydraulic vehicle lift system for a parking garage.
    
    Attributes:
        capacity (float): The maximum weight capacity of the lift in tons.
        current_weight (float): The current weight on the lift in tons.
        is_operational (bool): Status of the lift's operational state.
    """

    def __init__(self, capacity: float):
        """
        Initializes the hydraulic lift with a specified capacity.
        
        Args:
            capacity (float): The maximum weight capacity of the lift in tons.
        """
        self.capacity = capacity
        self.current_weight = 0.0
        self.is_operational = True

    def add_vehicle(self, weight: float) -> None:
        """
        Adds a vehicle to the lift.
        
        Args:
            weight (float): The weight of the vehicle in tons.
        
        Raises:
            ValueError: If the weight exceeds the lift's capacity.
            RuntimeError: If the lift is not operational.
        """
        if not self.is_operational:
            raise RuntimeError("Lift is not operational.")
        
        if self.current_weight + weight > self.capacity:
            raise ValueError("Exceeds lift capacity.")
        
        self.current_weight += weight
        print(f"Vehicle added. Current weight: {self.current_weight} tons.")

    def remove_vehicle(self, weight: float) -> None:
        """
        Removes a vehicle from the lift.
        
        Args:
            weight (float): The weight of the vehicle in tons.
        
        Raises:
            ValueError: If the weight to remove exceeds the current weight.
            RuntimeError: If the lift is not operational.
        """
        if not self.is_operational:
            raise RuntimeError("Lift is not operational.")
        
        if weight > self.current_weight:
            raise ValueError("Cannot remove more weight than currently on the lift.")
        
        self.current_weight -= weight
        print(f"Vehicle removed. Current weight: {self.current_weight} tons.")

    def lift_vehicle(self) -> None:
        """
        Lifts the vehicle to the designated height.
        
        Raises:
            RuntimeError: If the lift is not operational or if no weight is on the lift.
        """
        if not self.is_operational:
            raise RuntimeError("Lift is not operational.")
        
        if self.current_weight == 0:
            raise RuntimeError("No vehicle on the lift to raise.")
        
        print(f"Lifting vehicle weighing {self.current_weight} tons... Lifted!")

    def lower_vehicle(self) -> None:
        """
        Lowers the vehicle back to the ground.
        
        Raises:
            RuntimeError: If the lift is not operational or if no weight is on the lift.
        """
        if not self.is_operational:
            raise RuntimeError("Lift is not operational.")
        
        if self.current_weight == 0:
            raise RuntimeError("No vehicle on the lift to lower.")
        
        print(f"Lowering vehicle weighing {self.current_weight} tons... Lowered!")

    def shutdown(self) -> None:
        """
        Shuts down the lift, marking it as non-operational.
        """
        self.is_operational = False
        print("Lift has been shut down.")

    def restart(self) -> None:
        """
        Restarts the lift, marking it as operational.
        """
        self.is_operational = True
        print("Lift is operational again.")

# Example usage
if __name__ == "__main__":
    try:
        lift = HydraulicLift(capacity=5.0)  # 5 tons capacity
        lift.add_vehicle(2.0)  # Adding a vehicle of 2 tons
        lift.lift_vehicle()  # Lifting the vehicle
        lift.lower_vehicle()  # Lowering the vehicle
        lift.remove_vehicle(2.0)  # Removing the vehicle
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
