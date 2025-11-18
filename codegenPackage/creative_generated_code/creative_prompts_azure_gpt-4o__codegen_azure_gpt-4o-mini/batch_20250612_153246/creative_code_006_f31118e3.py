"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://accutrolsystems.com
Prompt: Write code to simulate the operation of electric calorifiers, incorporating design principles similar to those highlighted by Accutrol Systems.
Generated: DETERMINISTIC_f31118e3c94cc139
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Calorifier:
    """
    A class to simulate the operation of an electric calorifier.
    
    Attributes:
        capacity (float): The total capacity of the calorifier in liters.
        current_temp (float): The current temperature of the water in Celsius.
        heating_power (float): The heating power of the element in watts.
        efficiency (float): Efficiency of the heating element (0 < efficiency <= 1).
        heated_water (float): The amount of heated water in liters.
    """

    def __init__(self, capacity, heating_power, efficiency=0.9):
        """
        Initializes the Calorifier with specified parameters.
        
        Args:
            capacity (float): Total capacity of the calorifier in liters.
            heating_power (float): Heating power in watts.
            efficiency (float): Efficiency of the heater, default is 0.9.
        
        Raises:
            ValueError: If any parameter is not positive or efficiency is not in (0, 1].
        """
        if capacity <= 0 or heating_power <= 0 or not (0 < efficiency <= 1):
            raise ValueError("Capacity and heating power must be positive, and efficiency must be in (0, 1].")

        self.capacity = capacity
        self.current_temp = 20.0  # Initial water temperature in Celsius
        self.heating_power = heating_power
        self.efficiency = efficiency
        self.heated_water = 0.0

    def heat(self, duration):
        """
        Heats the water for a specified duration.
        
        Args:
            duration (float): Duration to heat the water in seconds.
        
        Raises:
            ValueError: If duration is not positive.
        """
        if duration <= 0:
            raise ValueError("Duration must be positive.")

        # Calculate energy used in joules
        energy_used = self.heating_power * self.efficiency * duration
        
        # Convert energy to temperature rise (specific heat of water = 4.186 J/g°C)
        # 1 liter of water = 1000 grams
        temperature_rise = energy_used / (self.capacity * 1000 * 4.186)

        # Update the current temperature
        self.current_temp += temperature_rise

        # Ensure the temperature does not exceed 100°C
        if self.current_temp > 100.0:
            self.current_temp = 100.0

    def use_water(self, amount):
        """
        Simulates using a specified amount of water from the calorifier.
        
        Args:
            amount (float): Amount of water to use in liters.
        
        Raises:
            ValueError: If the amount is not positive or exceeds available heated water.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount > self.heated_water:
            raise ValueError(f"Not enough heated water available. Current heated water: {self.heated_water} liters.")
        
        self.heated_water -= amount

    def fill(self, amount):
        """
        Fills the calorifier with a specified amount of water.
        
        Args:
            amount (float): Amount of water to fill in liters.
        
        Raises:
            ValueError: If the amount is not positive or exceeds capacity.
        """
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        if amount + self.heated_water > self.capacity:
            raise ValueError(f"Cannot fill above capacity. Current: {self.heated_water}, Attempted fill: {amount}")

        self.heated_water += amount

    def get_status(self):
        """
        Returns the current status of the calorifier.
        
        Returns:
            dict: A dictionary containing the current state of the calorifier.
        """
        return {
            "Current Temperature (°C)": self.current_temp,
            "Heated Water (liters)": self.heated_water,
            "Capacity (liters)": self.capacity,
            "Heating Power (watts)": self.heating_power,
            "Efficiency": self.efficiency
        }

# Example usage:
if __name__ == "__main__":
    try:
        # Create a calorifier with a capacity of 100 liters and 3000 watts heating power
        calorifier = Calorifier(capacity=100.0, heating_power=3000.0)

        # Fill the calorifier with 50 liters of water
        calorifier.fill(50.0)

        # Heat the water for 600 seconds (10 minutes)
        calorifier.heat(600.0)

        # Get the current status
        status = calorifier.get_status()
        print(status)

        # Use 20 liters of heated water
        calorifier.use_water(20.0)

        # Get the updated status
        updated_status = calorifier.get_status()
        print(updated_status)

    except ValueError as e:
        print(f"Error: {e}")
```
