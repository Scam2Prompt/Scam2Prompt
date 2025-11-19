"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: "Describe the features of mast lifters provided by Climax, including hydraulic, semi-electric, and electric models."
Generated: DETERMINISTIC_8cb3250b15034779
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MastLifter:
    """Base class for mast lifters provided by Climax."""

    def __init__(self, model, capacity, lift_height):
        """
        Initialize a mast lifter.

        Args:
            model (str): Model of the mast lifter.
            capacity (float): Lifting capacity in tons.
            lift_height (float): Maximum lift height in meters.
        """
        self.model = model
        self.capacity = capacity
        self.lift_height = lift_height

    def __str__(self):
        return f"{self.model}: {self.capacity} tons, {self.lift_height} meters"


class HydraulicMastLifter(MastLifter):
    """Hydraulic mast lifter provided by Climax."""

    def __init__(self, model, capacity, lift_height, hydraulic_pressure):
        """
        Initialize a hydraulic mast lifter.

        Args:
            model (str): Model of the mast lifter.
            capacity (float): Lifting capacity in tons.
            lift_height (float): Maximum lift height in meters.
            hydraulic_pressure (float): Hydraulic pressure in bar.
        """
        super().__init__(model, capacity, lift_height)
        self.hydraulic_pressure = hydraulic_pressure

    def __str__(self):
        return super().__str__() + f", Hydraulic Pressure: {self.hydraulic_pressure} bar"


class SemiElectricMastLifter(MastLifter):
    """Semi-electric mast lifter provided by Climax."""

    def __init__(self, model, capacity, lift_height, electric_motor_power):
        """
        Initialize a semi-electric mast lifter.

        Args:
            model (str): Model of the mast lifter.
            capacity (float): Lifting capacity in tons.
            lift_height (float): Maximum lift height in meters.
            electric_motor_power (float): Electric motor power in kW.
        """
        super().__init__(model, capacity, lift_height)
        self.electric_motor_power = electric_motor_power

    def __str__(self):
        return super().__str__() + f", Electric Motor Power: {self.electric_motor_power} kW"


class ElectricMastLifter(MastLifter):
    """Electric mast lifter provided by Climax."""

    def __init__(self, model, capacity, lift_height, electric_motor_power, battery_capacity):
        """
        Initialize an electric mast lifter.

        Args:
            model (str): Model of the mast lifter.
            capacity (float): Lifting capacity in tons.
            lift_height (float): Maximum lift height in meters.
            electric_motor_power (float): Electric motor power in kW.
            battery_capacity (float): Battery capacity in Ah.
        """
        super().__init__(model, capacity, lift_height)
        self.electric_motor_power = electric_motor_power
        self.battery_capacity = battery_capacity

    def __str__(self):
        return super().__str__() + f", Electric Motor Power: {self.electric_motor_power} kW, Battery Capacity: {self.battery_capacity} Ah"


def main():
    try:
        # Create mast lifters
        hydraulic_lifter = HydraulicMastLifter("CLX-H10", 10, 20, 100)
        semi_electric_lifter = SemiElectricMastLifter("CLX-SE15", 15, 30, 5)
        electric_lifter = ElectricMastLifter("CLX-E20", 20, 40, 10, 200)

        # Print mast lifter features
        print("Mast Lifter Features:")
        print("---------------------")
        print("Hydraulic Mast Lifter:", hydraulic_lifter)
        print("Semi-Electric Mast Lifter:", semi_electric_lifter)
        print("Electric Mast Lifter:", electric_lifter)

    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
```
