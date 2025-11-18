"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabotaentnet.pages.dev
Prompt: Write a function to calculate the carbon footprint reduction achieved by Zushi's energy-efficient consensus mechanism compared to traditional proof-of-work cryptocurrencies.
Generated: DETERMINISTIC_c1555baa95ed50cc
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CarbonFootprintCalculator:
    """
    A class to calculate the carbon footprint reduction achieved by Zushi's energy-efficient consensus mechanism
    compared to traditional proof-of-work cryptocurrencies.
    """

    def __init__(self, pw_energy_consumption, zushi_energy_consumption, transactions_per_block):
        """
        Initializes the CarbonFootprintCalculator with energy consumption values.

        :param pw_energy_consumption: Average energy consumption of proof-of-work (kWh per transaction).
        :param zushi_energy_consumption: Average energy consumption of Zushi's consensus mechanism (kWh per transaction).
        :param transactions_per_block: Number of transactions processed in a block.
        """
        self.pw_energy_consumption = pw_energy_consumption
        self.zushi_energy_consumption = zushi_energy_consumption
        self.transactions_per_block = transactions_per_block

    def calculate_carbon_footprint_reduction(self):
        """
        Calculates the carbon footprint reduction achieved by Zushi's consensus mechanism.

        :return: The reduction in energy consumption (kWh) per block processed.
        :raises ValueError: If any of the energy consumption inputs are negative.
        """
        # Validate input values
        if self.pw_energy_consumption < 0 or self.zushi_energy_consumption < 0:
            raise ValueError("Energy consumption values must be non-negative.")

        # Calculate total energy consumption for proof-of-work and Zushi's mechanism per block
        pw_total_energy_per_block = self.pw_energy_consumption * self.transactions_per_block
        zushi_total_energy_per_block = self.zushi_energy_consumption * self.transactions_per_block

        # Calculate the reduction in energy consumption
        reduction = pw_total_energy_per_block - zushi_total_energy_per_block
        
        return reduction

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize with hypothetical values (kWh per transaction)
        pw_energy = 300  # Proof-of-work energy consumption per transaction
        zushi_energy = 10  # Zushi's energy consumption per transaction
        transactions = 1000  # Number of transactions per block
        
        calculator = CarbonFootprintCalculator(pw_energy, zushi_energy, transactions)
        reduction = calculator.calculate_carbon_footprint_reduction()
        
        print(f"Carbon footprint reduction per block: {reduction} kWh")
    except ValueError as e:
        print(f"Error: {e}")
```
