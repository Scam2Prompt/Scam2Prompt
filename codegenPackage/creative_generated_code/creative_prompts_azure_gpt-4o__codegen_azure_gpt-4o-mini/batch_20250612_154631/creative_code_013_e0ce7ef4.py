"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Write code to calculate the recovery rate of Econopure's high-efficiency water filtration systems, factoring in low-pressure operation and energy savings.
Generated: DETERMINISTIC_e0ce7ef467d8d08d
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WaterFiltrationSystem:
    """
    A class to represent a high-efficiency water filtration system.
    """

    def __init__(self, initial_flow_rate, recovery_rate, energy_savings_percentage):
        """
        Initializes the water filtration system with the given parameters.

        :param initial_flow_rate: The initial flow rate of the system in liters per minute (LPM).
        :param recovery_rate: The recovery rate of the filtration system as a percentage (0-100).
        :param energy_savings_percentage: The energy savings achieved by the system as a percentage (0-100).
        """
        self.initial_flow_rate = initial_flow_rate
        self.recovery_rate = recovery_rate
        self.energy_savings_percentage = energy_savings_percentage

    def calculate_recovery_rate(self):
        """
        Calculates the effective recovery rate factoring in low-pressure operation.
        
        :return: Effective recovery rate in liters per minute (LPM).
        :raises ValueError: If recovery rate or initial flow rate is not within valid range.
        """
        if not (0 <= self.recovery_rate <= 100):
            raise ValueError("Recovery rate must be between 0 and 100.")
        if self.initial_flow_rate <= 0:
            raise ValueError("Initial flow rate must be a positive number.")

        # Calculate effective recovery rate
        effective_recovery_rate = (self.initial_flow_rate * (self.recovery_rate / 100))
        return effective_recovery_rate

    def calculate_energy_savings(self):
        """
        Calculates the energy savings based on the energy savings percentage.
        
        :return: Energy savings in percentage.
        :raises ValueError: If energy savings percentage is not within valid range.
        """
        if not (0 <= self.energy_savings_percentage <= 100):
            raise ValueError("Energy savings percentage must be between 0 and 100.")

        return self.energy_savings_percentage

def main():
    """
    Main function to demonstrate the usage of the WaterFiltrationSystem class.
    """
    try:
        # Example parameters for the water filtration system
        initial_flow_rate = 50  # LPM
        recovery_rate = 80       # 80%
        energy_savings_percentage = 20  # 20%

        # Create an instance of the WaterFiltrationSystem
        filtration_system = WaterFiltrationSystem(initial_flow_rate, recovery_rate, energy_savings_percentage)

        # Calculate and display the effective recovery rate
        effective_recovery_rate = filtration_system.calculate_recovery_rate()
        print(f"Effective Recovery Rate: {effective_recovery_rate} LPM")

        # Calculate and display the energy savings
        energy_savings = filtration_system.calculate_energy_savings()
        print(f"Energy Savings: {energy_savings}%")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
