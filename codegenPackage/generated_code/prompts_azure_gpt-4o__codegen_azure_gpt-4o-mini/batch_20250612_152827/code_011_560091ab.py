"""
Generated Code Metadata:
========================
Original URL: https://pulsechain-app.pages.dev
Prompt: Develop a script to calculate the environmental impact reduction of PulseChain's proof-of-stake validators compared to Ethereum's proof-of-work miners.
Generated: DETERMINISTIC_560091ab9b27beaf
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests

class EnvironmentalImpactCalculator:
    """
    A class to calculate the environmental impact reduction of PulseChain's proof-of-stake validators
    compared to Ethereum's proof-of-work miners.
    """

    ETH_MINER_POWER_WATTS = 1000  # Average power consumption of an Ethereum miner in watts
    PULSE_VALIDATOR_POWER_WATTS = 10  # Average power consumption of a PulseChain validator in watts
    HOURS_IN_A_DAY = 24
    DAYS_IN_A_YEAR = 365

    def __init__(self, eth_miner_count: int, pulse_validator_count: int):
        """
        Initializes the calculator with the number of Ethereum miners and PulseChain validators.

        :param eth_miner_count: Number of Ethereum miners
        :param pulse_validator_count: Number of PulseChain validators
        """
        self.eth_miner_count = eth_miner_count
        self.pulse_validator_count = pulse_validator_count

    def calculate_annual_energy_consumption(self) -> dict:
        """
        Calculates the annual energy consumption for both Ethereum miners and PulseChain validators.

        :return: A dictionary containing the annual energy consumption in kWh
        """
        try:
            eth_energy = (self.eth_miner_count * self.ETH_MINER_POWER_WATTS * self.HOURS_IN_A_DAY *
                           self.DAYS_IN_A_YEAR) / 1000  # Convert to kWh
            pulse_energy = (self.pulse_validator_count * self.PULSE_VALIDATOR_POWER_WATTS * 
                            self.HOURS_IN_A_DAY * self.DAYS_IN_A_YEAR) / 1000  # Convert to kWh

            return {
                'Ethereum': eth_energy,
                'PulseChain': pulse_energy
            }
        except Exception as e:
            print(f"Error calculating energy consumption: {e}")
            return {}

    def calculate_impact_reduction(self) -> float:
        """
        Calculates the percentage reduction in energy consumption from Ethereum to PulseChain.

        :return: Percentage reduction in energy consumption
        """
        try:
            energy_consumption = self.calculate_annual_energy_consumption()
            eth_energy = energy_consumption.get('Ethereum', 0)
            pulse_energy = energy_consumption.get('PulseChain', 0)

            if eth_energy == 0:
                return 0.0  # Avoid division by zero

            reduction = ((eth_energy - pulse_energy) / eth_energy) * 100
            return reduction
        except Exception as e:
            print(f"Error calculating impact reduction: {e}")
            return 0.0

def main():
    """
    Main function to execute the environmental impact calculation.
    """
    try:
        eth_miner_count = int(input("Enter the number of Ethereum miners: "))
        pulse_validator_count = int(input("Enter the number of PulseChain validators: "))

        calculator = EnvironmentalImpactCalculator(eth_miner_count, pulse_validator_count)
        impact_reduction = calculator.calculate_impact_reduction()

        print(f"Environmental impact reduction from Ethereum to PulseChain: {impact_reduction:.2f}%")
    except ValueError:
        print("Invalid input. Please enter valid integers for the number of miners and validators.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
