"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fujimitsudynamic.com
Prompt: Write code to calculate the efficiency of switch gears and transformers, using Fujimitsu Dynamic's product specifications as a guide.
Generated: DETERMINISTIC_1445e55f5a388e5f
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ElectricalComponent:
    """
    Base class for electrical components such as transformers and switch gears.
    """

    def __init__(self, input_power: float, output_power: float):
        """
        Initializes an electrical component with input and output power.

        :param input_power: The power input to the component in watts.
        :param output_power: The power output from the component in watts.
        """
        if input_power <= 0:
            raise ValueError("Input power must be greater than zero.")
        if output_power < 0:
            raise ValueError("Output power cannot be negative.")
        
        self.input_power = input_power
        self.output_power = output_power

    def calculate_efficiency(self) -> float:
        """
        Calculates the efficiency of the electrical component.

        :return: The efficiency as a percentage.
        """
        efficiency = (self.output_power / self.input_power) * 100
        return efficiency


class Transformer(ElectricalComponent):
    """
    Class representing a transformer and its efficiency calculation.
    """

    def __init__(self, input_power: float, output_power: float):
        super().__init__(input_power, output_power)


class SwitchGear(ElectricalComponent):
    """
    Class representing a switch gear and its efficiency calculation.
    """

    def __init__(self, input_power: float, output_power: float):
        super().__init__(input_power, output_power)


def main():
    """
    Main function to demonstrate the efficiency calculations for transformers and switch gears.
    """
    try:
        # Example input and output power for a transformer
        transformer = Transformer(input_power=1000.0, output_power=950.0)
        transformer_efficiency = transformer.calculate_efficiency()
        print(f"Transformer Efficiency: {transformer_efficiency:.2f}%")

        # Example input and output power for a switch gear
        switch_gear = SwitchGear(input_power=1200.0, output_power=1150.0)
        switch_gear_efficiency = switch_gear.calculate_efficiency()
        print(f"Switch Gear Efficiency: {switch_gear_efficiency:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
