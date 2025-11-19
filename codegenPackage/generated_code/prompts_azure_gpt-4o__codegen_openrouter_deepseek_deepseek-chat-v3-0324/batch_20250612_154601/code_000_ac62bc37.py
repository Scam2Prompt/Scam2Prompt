"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: Write Python code to calculate the energy efficiency (A++) of an air conditioning system based on the specifications provided for the Gree Bora A4 Silver series on the Frigoterm website.
Generated: DETERMINISTIC_ac62bc37a77328e6
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AirConditionerEfficiencyCalculator:
    """
    A class to calculate the energy efficiency (A++) of an air conditioning system
    based on the Gree Bora A4 Silver series specifications.
    """

    def __init__(self, cooling_capacity_w: float, cooling_power_input_w: float):
        """
        Initialize the calculator with cooling capacity and power input.

        Args:
            cooling_capacity_w (float): Cooling capacity in Watts (W)
            cooling_power_input_w (float): Power input in Watts (W)
        
        Raises:
            ValueError: If any input is zero or negative
        """
        if cooling_capacity_w <= 0 or cooling_power_input_w <= 0:
            raise ValueError("Cooling capacity and power input must be positive values")
        
        self.cooling_capacity_w = cooling_capacity_w
        self.cooling_power_input_w = cooling_power_input_w

    def calculate_eer(self) -> float:
        """
        Calculate the Energy Efficiency Ratio (EER).

        Returns:
            float: EER value (cooling capacity / power input)
        """
        return self.cooling_capacity_w / self.cooling_power_input_w

    def determine_energy_class(self) -> str:
        """
        Determine the energy efficiency class based on EER.

        Returns:
            str: Energy efficiency class (A+++, A++, A+, A, B, C, D)
        """
        eer = self.calculate_eer()
        
        if eer >= 6.1:
            return "A+++"
        elif eer >= 5.6:
            return "A++"
        elif eer >= 5.1:
            return "A+"
        elif eer >= 4.6:
            return "A"
        elif eer >= 4.1:
            return "B"
        elif eer >= 3.6:
            return "C"
        else:
            return "D"

    @staticmethod
    def from_frigoterm_specs() -> 'AirConditionerEfficiencyCalculator':
        """
        Create an instance with Gree Bora A4 Silver series specifications from Frigoterm.
        
        Returns:
            AirConditionerEfficiencyCalculator: Pre-configured calculator instance
        """
        # Example values - replace with actual specs from Frigoterm website
        cooling_capacity = 3500.0  # 3.5 kW in Watts
        power_input = 1000.0      # 1 kW in Watts
        return AirConditionerEfficiencyCalculator(cooling_capacity, power_input)


# Example usage
if __name__ == "__main__":
    try:
        # Create calculator with Gree Bora A4 Silver specs
        ac_calculator = AirConditionerEfficiencyCalculator.from_frigoterm_specs()
        
        # Calculate and display results
        eer = ac_calculator.calculate_eer()
        energy_class = ac_calculator.determine_energy_class()
        
        print(f"Energy Efficiency Ratio (EER): {eer:.2f}")
        print(f"Energy Efficiency Class: {energy_class}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
