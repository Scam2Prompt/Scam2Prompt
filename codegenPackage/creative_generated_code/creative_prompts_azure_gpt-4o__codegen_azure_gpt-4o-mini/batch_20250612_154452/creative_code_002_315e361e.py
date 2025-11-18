"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omegaenergy.co
Prompt: Generate code to model the specialized lifting systems used in the Bloque Cóndor for maximizing production efficiency, as outlined in Omega Energy's operations.
Generated: DETERMINISTIC_315e361ecddb5ede
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LiftSystem:
    """
    A class to represent a specialized lifting system for optimizing production efficiency.
    This class models key attributes and methods associated with the lifting system.

    Attributes:
        lift_capacity (float): The maximum weight the lift can handle (in kg).
        current_load (float): The current weight being lifted (in kg).
        operational_status (bool): Indicates whether the lift is operational.
    """

    def __init__(self, lift_capacity):
        """
        Initializes the lift system with a specified lift capacity.
        
        Args:
            lift_capacity (float): The maximum weight the lift can handle.
        """
        if lift_capacity <= 0:
            raise ValueError("Lift capacity must be a positive number.")
        self.lift_capacity = lift_capacity
        self.current_load = 0.0
        self.operational_status = True  # Lift starts as operational

    def load(self, weight):
        """
        Loads a specified weight onto the lift.
        
        Args:
            weight (float): The weight to be loaded onto the lift.
        
        Raises:
            ValueError: If the weight exceeds the lift's capacity.
            Exception: If the lift is not operational.
        """
        if not self.operational_status:
            raise Exception("Lift is not operational. Cannot load weight.")
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")
        if self.current_load + weight > self.lift_capacity:
            raise ValueError("Loading this weight exceeds lift capacity.")
        
        self.current_load += weight
        print(f"Loaded {weight} kg. Current load is now {self.current_load} kg.")

    def unload(self, weight):
        """
        Unloads a specified weight from the lift.
        
        Args:
            weight (float): The weight to be unloaded from the lift.
        
        Raises:
            ValueError: If the weight to unload is greater than the current load.
            Exception: If the lift is not operational.
        """
        if not self.operational_status:
            raise Exception("Lift is not operational. Cannot unload weight.")
        if weight <= 0:
            raise ValueError("Weight must be a positive number.")
        if weight > self.current_load:
            raise ValueError("Cannot unload more weight than is currently loaded.")
        
        self.current_load -= weight
        print(f"Unloaded {weight} kg. Current load is now {self.current_load} kg.")

    def set_operational_status(self, status):
        """
        Sets the operational status of the lift.
        
        Args:
            status (bool): True to make the lift operational, False otherwise.
        """
        self.operational_status = status
        status_str = "operational" if status else "non-operational"
        print(f"The lift is now {status_str}.")

    def get_status(self):
        """
        Returns the current status of the lift.
        
        Returns:
            dict: A dictionary with the lift's current load and operational status.
        """
        return {
            "current_load": self.current_load,
            "operational_status": self.operational_status
        }


# Example usage:
if __name__ == "__main__":
    try:
        lift = LiftSystem(lift_capacity=1000.0)  # Create a lift system with a capacity of 1000 kg
        lift.load(200.0)  # Load 200 kg
        lift.load(300.0)  # Load 300 kg
        lift.unload(100.0)  # Unload 100 kg
        lift.set_operational_status(False)  # Set lift to non-operational
        # lift.load(150.0)  # This will raise an exception
    except Exception as e:
        print(f"Error: {e}")
```
