"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: Write a script to simulate the operation of plastic manual pumps for bulk containers, inspired by the M200/55 product line from TROMBA.
Generated: DETERMINISTIC_c6ed7b2b19a498f4
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ManualPump:
    """
    A class to simulate the operation of a manual pump for bulk containers.
    
    Attributes:
        capacity (float): The maximum capacity of the pump in liters.
        current_volume (float): The current volume of liquid dispensed in liters.
        is_operational (bool): Indicates if the pump is operational.
    """

    def __init__(self, capacity: float):
        """
        Initializes the ManualPump with a specified capacity.
        
        Args:
            capacity (float): The maximum capacity of the pump in liters.
        """
        if capacity <= 0:
            raise ValueError("Capacity must be a positive number.")
        
        self.capacity = capacity
        self.current_volume = 0.0
        self.is_operational = True

    def pump(self, volume: float) -> float:
        """
        Simulates pumping a specified volume of liquid.
        
        Args:
            volume (float): The volume of liquid to pump in liters.
        
        Returns:
            float: The actual volume pumped in liters.
        
        Raises:
            ValueError: If the volume to pump is negative.
            RuntimeError: If the pump is not operational.
        """
        if volume < 0:
            raise ValueError("Volume to pump must be a non-negative number.")
        
        if not self.is_operational:
            raise RuntimeError("The pump is not operational.")
        
        # Calculate the actual volume that can be pumped
        volume_to_pump = min(volume, self.capacity - self.current_volume)
        
        # Update the current volume
        self.current_volume += volume_to_pump
        
        return volume_to_pump

    def reset(self):
        """
        Resets the current volume of the pump to zero.
        """
        self.current_volume = 0.0

    def stop(self):
        """
        Stops the operation of the pump, making it non-operational.
        """
        self.is_operational = False

    def start(self):
        """
        Starts the operation of the pump, making it operational.
        """
        self.is_operational = True

    def get_status(self) -> str:
        """
        Returns the operational status of the pump.
        
        Returns:
            str: A string indicating whether the pump is operational or not.
        """
        return "Operational" if self.is_operational else "Not Operational"

    def get_current_volume(self) -> float:
        """
        Returns the current volume of liquid dispensed by the pump.
        
        Returns:
            float: The current volume in liters.
        """
        return self.current_volume


# Example usage
if __name__ == "__main__":
    try:
        # Create a manual pump with a capacity of 55 liters
        pump = ManualPump(55.0)

        # Start the pump
        pump.start()
        print(f"Pump status: {pump.get_status()}")

        # Pump 20 liters
        pumped_volume = pump.pump(20.0)
        print(f"Pumped volume: {pumped_volume} liters")

        # Check current volume
        print(f"Current volume dispensed: {pump.get_current_volume()} liters")

        # Stop the pump
        pump.stop()
        print(f"Pump status after stopping: {pump.get_status()}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
