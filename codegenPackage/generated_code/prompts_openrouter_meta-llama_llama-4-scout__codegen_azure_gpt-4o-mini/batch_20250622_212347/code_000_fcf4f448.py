"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: "Design a paddy dryer system with heat exchanger and blower for rice mill."
Generated: DETERMINISTIC_fcf4f4486241aa63
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PaddyDryerSystem:
    """
    A class to represent a paddy dryer system with a heat exchanger and blower for a rice mill.
    """

    def __init__(self, max_capacity, heat_exchanger_efficiency, blower_power):
        """
        Initializes the PaddyDryerSystem with specified parameters.

        :param max_capacity: Maximum capacity of the dryer in kg
        :param heat_exchanger_efficiency: Efficiency of the heat exchanger (0 to 1)
        :param blower_power: Power of the blower in watts
        """
        self.max_capacity = max_capacity
        self.heat_exchanger_efficiency = heat_exchanger_efficiency
        self.blower_power = blower_power
        self.current_load = 0

    def load_paddy(self, amount):
        """
        Loads paddy into the dryer.

        :param amount: Amount of paddy to load in kg
        :raises ValueError: If the amount exceeds the maximum capacity
        """
        if amount + self.current_load > self.max_capacity:
            raise ValueError("Exceeds maximum capacity of the dryer.")
        self.current_load += amount
        print(f"Loaded {amount} kg of paddy. Current load: {self.current_load} kg.")

    def unload_paddy(self, amount):
        """
        Unloads paddy from the dryer.

        :param amount: Amount of paddy to unload in kg
        :raises ValueError: If the amount to unload exceeds the current load
        """
        if amount > self.current_load:
            raise ValueError("Cannot unload more paddy than currently loaded.")
        self.current_load -= amount
        print(f"Unloaded {amount} kg of paddy. Current load: {self.current_load} kg.")

    def dry_paddy(self, drying_time):
        """
        Simulates the drying process of the paddy.

        :param drying_time: Time in hours for which the paddy will be dried
        :raises ValueError: If there is no paddy loaded
        """
        if self.current_load == 0:
            raise ValueError("No paddy loaded to dry.")
        
        # Simulate drying process
        heat_generated = self.blower_power * self.heat_exchanger_efficiency * drying_time
        moisture_reduction = heat_generated / (self.current_load * 2)  # Simplified model
        print(f"Drying paddy for {drying_time} hours. Heat generated: {heat_generated} J.")
        print(f"Moisture reduced by: {moisture_reduction:.2f} kg.")

    def reset_system(self):
        """
        Resets the dryer system to its initial state.
        """
        self.current_load = 0
        print("Paddy dryer system has been reset.")

# Example usage
if __name__ == "__main__":
    try:
        # Create a paddy dryer system with a maximum capacity of 1000 kg, 
        # heat exchanger efficiency of 0.85, and blower power of 1500 watts
        dryer = PaddyDryerSystem(max_capacity=1000, heat_exchanger_efficiency=0.85, blower_power=1500)

        # Load paddy
        dryer.load_paddy(500)

        # Dry paddy for 2 hours
        dryer.dry_paddy(drying_time=2)

        # Unload paddy
        dryer.unload_paddy(200)

        # Reset the system
        dryer.reset_system()

    except ValueError as e:
        print(f"Error: {e}")
```
