"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://birlikjenerator.com
Prompt: Write Python code to calculate the optimal power capacity for a diesel generator based on user input for energy consumption, referencing the "Güç ve Yer Tespiti" service described on Birlik Jeneratör's website.
Generated: DETERMINISTIC_5fe18271fc185dc6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GeneratorCapacityCalculator:
    """
    A class to calculate the optimal power capacity for a diesel generator
    based on user input for energy consumption.
    """

    def __init__(self):
        self.power_factor = 0.8  # Typical power factor for diesel generators

    def get_user_input(self):
        """
        Get energy consumption input from the user.
        :return: Energy consumption in watts
        """
        while True:
            try:
                consumption = float(input("Enter your total energy consumption in watts: "))
                if consumption <= 0:
                    raise ValueError("Energy consumption must be a positive number.")
                return consumption
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    def calculate_optimal_capacity(self, energy_consumption):
        """
        Calculate the optimal generator capacity based on energy consumption.
        :param energy_consumption: Total energy consumption in watts
        :return: Optimal generator capacity in watts
        """
        # Apply the formula to calculate the required capacity considering the power factor
        required_capacity = energy_consumption / self.power_factor
        return required_capacity

    def display_result(self, optimal_capacity):
        """
        Display the calculated optimal generator capacity.
        :param optimal_capacity: Calculated generator capacity in watts
        """
        print(f"Optimal Generator Capacity: {optimal_capacity:.2f} watts")

    def run(self):
        """
        Run the generator capacity calculation process.
        """
        print("Welcome to the Diesel Generator Capacity Calculator!")
        energy_consumption = self.get_user_input()
        optimal_capacity = self.calculate_optimal_capacity(energy_consumption)
        self.display_result(optimal_capacity)


if __name__ == "__main__":
    calculator = GeneratorCapacityCalculator()
    calculator.run()
```
