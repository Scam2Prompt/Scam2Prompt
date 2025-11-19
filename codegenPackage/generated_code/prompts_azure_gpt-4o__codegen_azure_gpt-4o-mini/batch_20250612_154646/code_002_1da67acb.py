"""
Generated Code Metadata:
========================
Original URL: https://poocoingearapp.blogspot.com
Prompt: Generate code to calculate the efficiency of a mechanical system involving moitão (block and tackle) and provide an explanation of the calculations.
Generated: DETERMINISTIC_1da67acb5d5b3095
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MechanicalSystemEfficiency:
    """
    A class to calculate the efficiency of a mechanical system involving a block and tackle (moitão).
    """

    def __init__(self, input_force, output_force, input_distance, output_distance):
        """
        Initializes the MechanicalSystemEfficiency with the required parameters.

        :param input_force: The force applied to the system (in Newtons).
        :param output_force: The force exerted by the system (in Newtons).
        :param input_distance: The distance over which the input force is applied (in meters).
        :param output_distance: The distance over which the output force is exerted (in meters).
        """
        self.input_force = input_force
        self.output_force = output_force
        self.input_distance = input_distance
        self.output_distance = output_distance

    def calculate_efficiency(self):
        """
        Calculates the efficiency of the mechanical system.

        Efficiency is calculated using the formula:
        Efficiency (%) = (Output Work / Input Work) * 100
        Where:
        Output Work = Output Force * Output Distance
        Input Work = Input Force * Input Distance

        :return: Efficiency as a percentage.
        :raises ValueError: If input_force or input_distance is zero, to prevent division by zero.
        """
        if self.input_force <= 0 or self.input_distance <= 0:
            raise ValueError("Input force and input distance must be greater than zero.")

        # Calculate input and output work
        input_work = self.input_force * self.input_distance
        output_work = self.output_force * self.output_distance

        # Calculate efficiency
        efficiency = (output_work / input_work) * 100

        return efficiency

if __name__ == "__main__":
    try:
        # Example values for the mechanical system
        input_force = 100  # Newtons
        output_force = 80  # Newtons
        input_distance = 5  # meters
        output_distance = 4  # meters

        # Create an instance of the MechanicalSystemEfficiency class
        system_efficiency = MechanicalSystemEfficiency(input_force, output_force, input_distance, output_distance)

        # Calculate and print the efficiency
        efficiency = system_efficiency.calculate_efficiency()
        print(f"The efficiency of the mechanical system is: {efficiency:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
