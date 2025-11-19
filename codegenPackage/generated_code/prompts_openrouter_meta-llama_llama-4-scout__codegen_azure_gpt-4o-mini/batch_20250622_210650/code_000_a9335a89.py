"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Design a bioethanol fireplace with Planika BEV Technology™, including its features and benefits.
Generated: DETERMINISTIC_a9335a898d8da5a9
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BioethanolFireplace:
    """
    A class to represent a bioethanol fireplace using Planika BEV Technology™.
    
    Attributes:
        model (str): The model name of the fireplace.
        fuel_capacity (float): The maximum fuel capacity in liters.
        current_fuel_level (float): The current fuel level in liters.
        is_on (bool): The state of the fireplace (on/off).
    """

    def __init__(self, model: str, fuel_capacity: float):
        """
        Initializes the BioethanolFireplace with a model and fuel capacity.
        
        Args:
            model (str): The model name of the fireplace.
            fuel_capacity (float): The maximum fuel capacity in liters.
        """
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.current_fuel_level = 0.0
        self.is_on = False

    def fill_fuel(self, amount: float):
        """
        Fills the fireplace with bioethanol fuel.
        
        Args:
            amount (float): The amount of fuel to add in liters.
        
        Raises:
            ValueError: If the amount is negative or exceeds the available capacity.
        """
        if amount < 0:
            raise ValueError("Amount of fuel to fill must be non-negative.")
        
        if self.current_fuel_level + amount > self.fuel_capacity:
            raise ValueError("Cannot exceed fuel capacity.")
        
        self.current_fuel_level += amount
        print(f"Filled {amount} liters of fuel. Current fuel level: {self.current_fuel_level} liters.")

    def ignite(self):
        """
        Ignites the fireplace if there is enough fuel.
        
        Raises:
            RuntimeError: If the fireplace is already on or if there is not enough fuel.
        """
        if self.is_on:
            raise RuntimeError("The fireplace is already on.")
        
        if self.current_fuel_level <= 0:
            raise RuntimeError("Not enough fuel to ignite the fireplace.")
        
        self.is_on = True
        print(f"{self.model} is now ignited.")

    def extinguish(self):
        """
        Extinguishes the fireplace if it is currently on.
        
        Raises:
            RuntimeError: If the fireplace is already off.
        """
        if not self.is_on:
            raise RuntimeError("The fireplace is already off.")
        
        self.is_on = False
        print(f"{self.model} has been extinguished.")

    def burn_fuel(self, duration: float):
        """
        Simulates burning fuel for a specified duration.
        
        Args:
            duration (float): The duration in hours for which the fuel will burn.
        
        Raises:
            ValueError: If the duration is negative.
            RuntimeError: If the fireplace is off or not enough fuel is available.
        """
        if duration < 0:
            raise ValueError("Duration must be non-negative.")
        
        if not self.is_on:
            raise RuntimeError("The fireplace must be on to burn fuel.")
        
        fuel_needed = duration * 0.5  # Assume 0.5 liters of fuel is consumed per hour
        if self.current_fuel_level < fuel_needed:
            raise RuntimeError("Not enough fuel to burn for the specified duration.")
        
        self.current_fuel_level -= fuel_needed
        print(f"Burned {fuel_needed} liters of fuel for {duration} hours. Remaining fuel: {self.current_fuel_level} liters.")

    def get_status(self):
        """
        Returns the current status of the fireplace.
        
        Returns:
            str: A string describing the current state of the fireplace.
        """
        status = "on" if self.is_on else "off"
        return (f"Model: {self.model}, "
                f"Current Fuel Level: {self.current_fuel_level} liters, "
                f"Status: {status}")

# Example usage
if __name__ == "__main__":
    try:
        fireplace = BioethanolFireplace("Planika BEV", 5.0)
        fireplace.fill_fuel(3.0)
        fireplace.ignite()
        fireplace.burn_fuel(2.0)
        print(fireplace.get_status())
        fireplace.extinguish()
    except Exception as e:
        print(f"Error: {e}")
```
