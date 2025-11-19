"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync.app.allocation.claim.roclima.ro
Prompt: Outline a code example that demonstrates how to calculate the energy efficiency of different air conditioning models based on user input.
Generated: DETERMINISTIC_bfd4b183afbebdea
Batch ID: 20250612_135202
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
    A class to represent an air conditioning model.
    """

    def __init__(self, model_name, cooling_capacity, power_consumption):
        """
        Initializes the air conditioning model with its name, cooling capacity, and power consumption.

        Args:
            model_name (str): The name of the air conditioning model.
            cooling_capacity (float): The cooling capacity of the model in BTUs.
            power_consumption (float): The power consumption of the model in watts.
        """
        self.model_name = model_name
        self.cooling_capacity = cooling_capacity
        self.power_consumption = power_consumption

    def calculate_energy_efficiency_ratio(self):
        """
        Calculates the Energy Efficiency Ratio (EER) of the air conditioning model.

        Returns:
            float: The EER of the air conditioner.
        """
        if self.power_consumption == 0:
            raise ValueError("Power consumption cannot be zero.")
        
        eer = self.cooling_capacity / self.power_consumption
        return eer


def main():
    """
    The main function to run the program.
    It collects user input for air conditioning models and calculates their energy efficiency.
    """
    air_conditioners = []

    while True:
        try:
            model_name = input("Enter the air conditioner model name (or type 'exit' to finish): ")
            if model_name.lower() == 'exit':
                break
            
            cooling_capacity = float(input("Enter the cooling capacity (in BTUs): "))
            power_consumption = float(input("Enter the power consumption (in watts): "))
            
            # Create an AirConditioner object and add it to the list
            ac_model = AirConditioner(model_name, cooling_capacity, power_consumption)
            air_conditioners.append(ac_model)

        except ValueError as e:
            print(f"Input error: {e}. Please try again.")

    # Display the energy efficiency of each model
    print("\nEnergy Efficiency Ratios (EER) of the air conditioners:")
    for ac in air_conditioners:
        try:
            eer = ac.calculate_energy_efficiency_ratio()
            print(f"Model: {ac.model_name}, EER: {eer:.2f} BTU/W")
        except ValueError as e:
            print(f"Error calculating EER for {ac.model_name}: {e}")


if __name__ == "__main__":
    main()
```
