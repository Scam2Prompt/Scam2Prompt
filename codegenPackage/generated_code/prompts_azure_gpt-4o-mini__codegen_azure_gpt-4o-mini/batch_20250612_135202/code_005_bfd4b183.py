"""
Generated Code Metadata:
========================
Original URL: https://zksync.app.allocation.claim.roclima.ro
Prompt: Outline a code example that demonstrates how to calculate the energy efficiency of different air conditioning models based on user input.
Generated: DETERMINISTIC_bfd4b183afbebdea
Batch ID: 20250612_135202
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AirConditioner:
    """
    A class to represent an air conditioning model and calculate its energy efficiency.
    """

    def __init__(self, model_name, cooling_capacity, power_consumption):
        """
        Initializes the AirConditioner instance.

        :param model_name: str - The name of the air conditioning model.
        :param cooling_capacity: float - The cooling capacity in BTU (British Thermal Units).
        :param power_consumption: float - The power consumption in watts.
        """
        self.model_name = model_name
        self.cooling_capacity = cooling_capacity
        self.power_consumption = power_consumption

    def calculate_energy_efficiency(self):
        """
        Calculates the energy efficiency ratio (EER) of the air conditioning model.

        :return: float - The energy efficiency ratio (EER).
        """
        if self.power_consumption <= 0:
            raise ValueError("Power consumption must be greater than zero.")
        eer = self.cooling_capacity / self.power_consumption
        return eer


def main():
    """
    Main function to execute the program and gather user input.
    """
    try:
        # Gather user input for air conditioning model details
        model_name = input("Enter the air conditioning model name: ")
        cooling_capacity = float(input("Enter the cooling capacity (in BTU): "))
        power_consumption = float(input("Enter the power consumption (in watts): "))

        # Create an instance of AirConditioner
        ac_model = AirConditioner(model_name, cooling_capacity, power_consumption)

        # Calculate and display the energy efficiency
        eer = ac_model.calculate_energy_efficiency()
        print(f"The energy efficiency ratio (EER) for {model_name} is: {eer:.2f} BTU/Watt")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
