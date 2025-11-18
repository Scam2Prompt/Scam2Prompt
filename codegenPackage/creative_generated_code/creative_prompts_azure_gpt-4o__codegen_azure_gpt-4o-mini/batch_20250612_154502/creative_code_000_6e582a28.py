"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loghouses-woodcraft.com
Prompt: Write Python code to calculate the flow rate for a QS15-52 water pump based on specifications provided by industrial equipment manufacturers.
Generated: DETERMINISTIC_6e582a28a4b0f2bd
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WaterPump:
    def __init__(self, flow_rate_spec, pressure_spec):
        """
        Initialize the WaterPump with specified flow rate and pressure.

        :param flow_rate_spec: The flow rate specification of the pump in liters per minute (L/min).
        :param pressure_spec: The pressure specification of the pump in bar.
        """
        self.flow_rate_spec = flow_rate_spec
        self.pressure_spec = pressure_spec

    def calculate_flow_rate(self, desired_pressure):
        """
        Calculate the flow rate of the pump based on the desired pressure.

        :param desired_pressure: The pressure at which to calculate the flow rate in bar.
        :return: The calculated flow rate in liters per minute (L/min) or None if input is invalid.
        """
        try:
            # Validate that the pressure is within the allowable range
            if desired_pressure < 0 or desired_pressure > self.pressure_spec:
                raise ValueError("Desired pressure must be between 0 and the maximum pump pressure.")

            # Calculate flow rate using a linear approximation (for demonstration purposes)
            # This is a simplified model; actual calculations may vary based on specific pump curves.
            flow_rate = self.flow_rate_spec * (1 - (desired_pressure / self.pressure_spec))
            return max(flow_rate, 0)  # Ensure flow rate is not negative

        except ValueError as e:
            print(f"Error: {e}")
            return None  # Return None to indicate an error occurred

    def get_specifications(self):
        """
        Retrieve the specifications of the pump.

        :return: A dictionary containing the flow rate and pressure specifications.
        """
        return {
            "flow_rate_spec": self.flow_rate_spec,
            "pressure_spec": self.pressure_spec
        }


def main():
    # Initialize the QS15-52 water pump specifications
    qs15_52 = WaterPump(flow_rate_spec=52, pressure_spec=4.5)  # Flow rate in L/min, pressure in bar

    # Display the pump specifications
    specs = qs15_52.get_specifications()
    print("Pump Specifications:")
    print(f"Flow Rate Spec: {specs['flow_rate_spec']} L/min")
    print(f"Pressure Spec: {specs['pressure_spec']} bar")

    # Example usage: Calculate flow rate at a specific desired pressure
    desired_pressure = 2.0  # Example desired pressure in bar
    flow_rate = qs15_52.calculate_flow_rate(desired_pressure)

    if flow_rate is not None:
        print(f"Calculated Flow Rate at {desired_pressure} bar: {flow_rate:.2f} L/min")


if __name__ == "__main__":
    main()
```
