"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duct-split.com
Prompt: Write Python code to calculate the energy efficiency ratio (EER) for a Gree duct split air conditioner based on its cooling capacity and power consumption. Use the specifications for the "Gree GU36T/AK(E)" model as an example.
Generated: DETERMINISTIC_33fbf4182ccf8e45
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AirConditioner:
    """
    Represents an air conditioner with a specified cooling capacity and power consumption.
    
    Attributes:
        cooling_capacity (float): Cooling capacity in BTU/hr.
        power_consumption (float): Power consumption in watts.
    """

    def __init__(self, cooling_capacity: float, power_consumption: float):
        """
        Initializes the AirConditioner with cooling capacity and power consumption.

        Args:
            cooling_capacity (float): The cooling capacity in BTU/hr.
            power_consumption (float): The power consumption in watts.
        
        Raises:
            ValueError: If cooling_capacity or power_consumption is negative.
        """
        if cooling_capacity <= 0:
            raise ValueError("Cooling capacity must be greater than zero.")
        if power_consumption <= 0:
            raise ValueError("Power consumption must be greater than zero.")
        
        self.cooling_capacity = cooling_capacity
        self.power_consumption = power_consumption

    def calculate_eer(self) -> float:
        """
        Calculates the Energy Efficiency Ratio (EER).

        Returns:
            float: The calculated EER.

        EER is calculated using the formula:
            EER = Cooling Capacity (BTU/hr) / Power Consumption (Watts)
        """
        eer = self.cooling_capacity / self.power_consumption
        return eer


def main():
    """
    Main function to create an air conditioner instance and calculate its EER.
    """
    try:
        # Specifications for the Gree GU36T/AK(E) model
        cooling_capacity_btu = 36000  # Cooling capacity in BTU/hr
        power_consumption_watts = 3800  # Power consumption in watts

        # Create an instance of the AirConditioner
        ac = AirConditioner(cooling_capacity_btu, power_consumption_watts)

        # Calculate EER
        eer = ac.calculate_eer()
        print(f"The Energy Efficiency Ratio (EER) for the Gree GU36T/AK(E) is: {eer:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
