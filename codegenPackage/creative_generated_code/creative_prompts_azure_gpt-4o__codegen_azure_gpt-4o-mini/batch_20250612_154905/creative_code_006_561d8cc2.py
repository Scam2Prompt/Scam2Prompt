"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.crediblebd.net
Prompt: Develop a program to calculate the total cost and energy efficiency of installing LED Explosion Proof Flood Lights in a factory setting, using the specifications from Credible BD.
Generated: DETERMINISTIC_561d8cc21c95bf5b
Batch ID: 20250612_154905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LEDFloodLight:
    """
    Class representing an LED Explosion Proof Flood Light.
    
    Attributes:
        wattage (float): The power consumption of the flood light in watts.
        quantity (int): The number of flood lights to be installed.
        cost_per_unit (float): The cost of one flood light in currency units.
    """

    def __init__(self, wattage: float, quantity: int, cost_per_unit: float):
        """
        Initializes the LEDFloodLight instance.

        Args:
            wattage (float): The power consumption of the flood light in watts.
            quantity (int): The number of flood lights to be installed.
            cost_per_unit (float): The cost of one flood light in currency units.
        """
        if wattage <= 0:
            raise ValueError("Wattage must be greater than zero.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if cost_per_unit < 0:
            raise ValueError("Cost per unit cannot be negative.")
        
        self.wattage = wattage
        self.quantity = quantity
        self.cost_per_unit = cost_per_unit

    def total_cost(self) -> float:
        """
        Calculates the total installation cost of the flood lights.

        Returns:
            float: The total cost of the flood lights.
        """
        return self.quantity * self.cost_per_unit

    def total_power_consumption(self) -> float:
        """
        Calculates the total power consumption of the installed flood lights.

        Returns:
            float: The total power consumption in kilowatts (kW).
        """
        return (self.wattage * self.quantity) / 1000  # Convert watts to kilowatts

    def energy_efficiency(self) -> float:
        """
        Calculates energy efficiency as cost per watt.

        Returns:
            float: The energy efficiency in currency units per watt.
        """
        total_cost = self.total_cost()
        total_power = self.total_power_consumption()
        
        if total_power == 0:
            raise ValueError("Total power consumption cannot be zero.")
        
        return total_cost / total_power


def main():
    """
    Main function to execute the LED flood light cost and efficiency calculations.
    """
    try:
        # Example specifications for the LED flood lights
        wattage = 150.0  # watts
        quantity = 10  # number of flood lights
        cost_per_unit = 120.0  # cost per unit in currency

        # Create an instance of LEDFloodLight
        led_flood_light = LEDFloodLight(wattage, quantity, cost_per_unit)

        # Calculate total cost and energy efficiency
        total_cost = led_flood_light.total_cost()
        total_power = led_flood_light.total_power_consumption()
        efficiency = led_flood_light.energy_efficiency()

        # Display the results
        print(f"Total Cost: {total_cost:.2f} currency units")
        print(f"Total Power Consumption: {total_power:.2f} kW")
        print(f"Energy Efficiency: {efficiency:.2f} currency units per watt")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
