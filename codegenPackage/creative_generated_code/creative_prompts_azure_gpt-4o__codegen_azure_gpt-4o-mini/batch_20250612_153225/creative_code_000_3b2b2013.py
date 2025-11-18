"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shelterder.com
Prompt: Write code to design a custom fireplace configuration using Planika BEV Technology™ for bioethanol fireplaces, ensuring eco-friendly and odorless operation.
Generated: DETERMINISTIC_3b2b2013c71a8ae6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BioethanolFireplace:
    """
    A class representing a custom bioethanol fireplace configuration using Planika BEV Technology™.
    This class ensures eco-friendly and odorless operation of the fireplace.
    """
    
    def __init__(self, model, capacity, flame_height, is_smart):
        """
        Initializes a new instance of the BioethanolFireplace class.

        Parameters:
        model (str): The model name of the fireplace.
        capacity (float): The fuel capacity in liters.
        flame_height (float): The desired flame height in centimeters.
        is_smart (bool): Indicates if the fireplace supports smart features.
        """
        self.model = model
        self.capacity = capacity
        self.flame_height = flame_height
        self.is_smart = is_smart
        self.current_fuel_level = capacity  # Initial fuel level set to capacity
        self.is_on = False  # Fireplace is off initially

    def ignite(self):
        """Ignites the fireplace if there is sufficient fuel."""
        if self.current_fuel_level > 0:
            self.is_on = True
            print(f"{self.model} is now ignited with a flame height of {self.flame_height} cm.")
        else:
            print("Error: Cannot ignite the fireplace. Fuel level is too low.")

    def extinguish(self):
        """Extinguishes the fireplace."""
        if self.is_on:
            self.is_on = False
            print(f"{self.model} has been extinguished.")
        else:
            print("The fireplace is already off.")

    def refuel(self, amount):
        """
        Refuels the fireplace.

        Parameters:
        amount (float): The amount of fuel to add in liters.
        """
        if amount <= 0:
            print("Error: Fuel amount must be positive.")
            return
        
        if self.current_fuel_level + amount > self.capacity:
            print("Error: Refuel amount exceeds capacity.")
            return
        
        self.current_fuel_level += amount
        print(f"{amount} liters added. Current fuel level: {self.current_fuel_level} liters.")

    def check_status(self):
        """Prints the current status of the fireplace."""
        status = "on" if self.is_on else "off"
        print(f"{self.model} is currently {status}. Fuel level: {self.current_fuel_level} liters.")

# Example of using the BioethanolFireplace class
if __name__ == "__main__":
    try:
        # Create a new fireplace instance
        fireplace = BioethanolFireplace("Planika EcoFire", 5.0, 30.0, True)
        
        # Check initial status
        fireplace.check_status()
        
        # Ignite the fireplace
        fireplace.ignite()
        
        # Refuel the fireplace
        fireplace.refuel(2.0)
        
        # Check status again
        fireplace.check_status()
        
        # Extinguish the fireplace
        fireplace.extinguish()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
