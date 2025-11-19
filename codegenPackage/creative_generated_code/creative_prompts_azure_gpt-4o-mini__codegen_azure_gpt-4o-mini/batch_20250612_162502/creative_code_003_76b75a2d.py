"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mining-equipment.vercel.app
Prompt: Generate a script that calculates the cost of mining equipment based on the minting of machines for Bitcoin on SOL.
Generated: DETERMINISTIC_76b75a2d866f6539
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MiningEquipmentCostCalculator:
    def __init__(self, equipment_cost_per_machine: float, number_of_machines: int):
        """
        Initialize the calculator with cost per machine and number of machines.

        :param equipment_cost_per_machine: Cost of a single mining machine
        :param number_of_machines: Number of machines to mint
        """
        self.equipment_cost_per_machine = equipment_cost_per_machine
        self.number_of_machines = number_of_machines

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost of mining equipment.

        :return: Total cost of mining equipment
        """
        if self.equipment_cost_per_machine < 0 or self.number_of_machines < 0:
            logging.error("Cost per machine and number of machines must be non-negative.")
            raise ValueError("Cost per machine and number of machines must be non-negative.")

        total_cost = self.equipment_cost_per_machine * self.number_of_machines
        logging.info(f"Calculated total cost: {total_cost}")
        return total_cost


def main():
    try:
        # Example values for equipment cost and number of machines
        equipment_cost_per_machine = 1500.00  # Cost of one mining machine in dollars
        number_of_machines = 10  # Number of machines to mint

        # Create an instance of the calculator
        calculator = MiningEquipmentCostCalculator(equipment_cost_per_machine, number_of_machines)

        # Calculate and print the total cost
        total_cost = calculator.calculate_total_cost()
        print(f"The total cost of mining equipment for {number_of_machines} machines is: ${total_cost:.2f}")

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
