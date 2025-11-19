"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeco.pk
Prompt: Develop a code snippet that models the hydraulic control system for a tractor-mounted water bowser, inspired by JECO's product features.
Generated: DETERMINISTIC_b1be3f28dfef10c2
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HydraulicControlSystem:
    """
    A class to model the hydraulic control system for a tractor-mounted water bowser.
    
    Attributes:
        tank_capacity (float): The total capacity of the water tank in liters.
        current_fill_level (float): The current fill level of the tank in liters.
        pump_status (bool): The status of the water pump (True for ON, False for OFF).
    """

    def __init__(self, tank_capacity: float):
        """
        Initializes the hydraulic control system with a specified tank capacity.
        
        Args:
            tank_capacity (float): The capacity of the tank in liters. Must be positive.
        """
        if tank_capacity <= 0:
            raise ValueError("Tank capacity must be a positive value.")
        
        self.tank_capacity = tank_capacity
        self.current_fill_level = 0.0
        self.pump_status = False

    def fill_tank(self, amount: float):
        """
        Fills the water tank by a specified amount, ensuring it does not exceed capacity.

        Args:
            amount (float): The amount of water to fill in liters. Must be positive.
        
        Raises:
            ValueError: If the amount is negative or if it exceeds the remaining capacity.
        """
        if amount <= 0:
            raise ValueError("Fill amount must be a positive value.")
        
        if self.current_fill_level + amount > self.tank_capacity:
            raise ValueError("Filling exceeds tank capacity.")
        
        self.current_fill_level += amount
        print(f"Tank filled by {amount} liters. Current level: {self.current_fill_level} liters.")

    def drain_tank(self, amount: float):
        """
        Drains the water tank by a specified amount, ensuring it does not go below zero.

        Args:
            amount (float): The amount of water to drain in liters. Must be positive.
        
        Raises:
            ValueError: If the amount is negative or if it exceeds the current fill level.
        """
        if amount <= 0:
            raise ValueError("Drain amount must be a positive value.")
        
        if amount > self.current_fill_level:
            raise ValueError("Draining exceeds current fill level.")
        
        self.current_fill_level -= amount
        print(f"Tank drained by {amount} liters. Current level: {self.current_fill_level} liters.")

    def start_pump(self):
        """
        Starts the water pump to distribute water.
        
        Raises:
            RuntimeError: If the pump is already running.
        """
        if self.pump_status:
            raise RuntimeError("Pump is already running.")
        
        self.pump_status = True
        print("Pump started. Water is being distributed.")

    def stop_pump(self):
        """
        Stops the water pump.

        Raises:
            RuntimeError: If the pump is not running.
        """
        if not self.pump_status:
            raise RuntimeError("Pump is not running.")
        
        self.pump_status = False
        print("Pump stopped. Water distribution halted.")

    def get_status(self):
        """
        Returns the current status of the hydraulic control system.

        Returns:
            dict: A dictionary containing the current fill level and pump status.
        """
        return {
            'current_fill_level': self.current_fill_level,
            'pump_status': self.pump_status
        }


# Example usage:
if __name__ == "__main__":
    try:
        water_bowser = HydraulicControlSystem(tank_capacity=1000)

        # Filling the tank
        water_bowser.fill_tank(500)
        # Starting the pump
        water_bowser.start_pump()
        
        # Draining some water
        water_bowser.drain_tank(200)
        
        # Checking status
        status = water_bowser.get_status()
        print("Current Status:", status)

        # Stopping the pump
        water_bowser.stop_pump()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
