"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: Write code to calculate the cost-effectiveness of periodic maintenance for generators, using insights from Birlik Jeneratör's "Periyodik Bakım" service.
Generated: DETERMINISTIC_8cb65551f1f9cfad
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class GeneratorMaintenanceCostEffectiveness:
    """
    A class to calculate the cost-effectiveness of periodic maintenance for generators.
    """

    def __init__(self, maintenance_data: pd.DataFrame):
        """
        Initializes the class with maintenance data.

        :param maintenance_data: A DataFrame containing maintenance records with columns:
                                 'date', 'cost', 'downtime_hours', 'output_loss'
        """
        self.maintenance_data = maintenance_data

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of maintenance.

        :return: Total maintenance cost as a float.
        """
        try:
            total_cost = self.maintenance_data['cost'].sum()
            return total_cost
        except KeyError as e:
            raise ValueError("DataFrame must contain a 'cost' column.") from e

    def calculate_total_downtime(self) -> float:
        """
        Calculates the total downtime incurred during maintenance.

        :return: Total downtime in hours as a float.
        """
        try:
            total_downtime = self.maintenance_data['downtime_hours'].sum()
            return total_downtime
        except KeyError as e:
            raise ValueError("DataFrame must contain a 'downtime_hours' column.") from e

    def calculate_output_loss(self) -> float:
        """
        Calculates the total output loss due to maintenance.

        :return: Total output loss as a float.
        """
        try:
            total_output_loss = self.maintenance_data['output_loss'].sum()
            return total_output_loss
        except KeyError as e:
            raise ValueError("DataFrame must contain an 'output_loss' column.") from e

    def calculate_cost_effectiveness(self) -> dict:
        """
        Calculates the cost-effectiveness of periodic maintenance.

        :return: A dictionary containing total cost, total downtime, total output loss,
                 and cost-effectiveness ratio.
        """
        total_cost = self.calculate_total_cost()
        total_downtime = self.calculate_total_downtime()
        total_output_loss = self.calculate_output_loss()

        # Avoid division by zero
        if total_cost == 0:
            raise ValueError("Total cost cannot be zero for cost-effectiveness calculation.")

        cost_effectiveness_ratio = (total_output_loss / total_cost) if total_cost > 0 else float('inf')

        return {
            'total_cost': total_cost,
            'total_downtime': total_downtime,
            'total_output_loss': total_output_loss,
            'cost_effectiveness_ratio': cost_effectiveness_ratio
        }

# Example usage:
if __name__ == "__main__":
    # Sample maintenance data
    data = {
        'date': ['2023-01-01', '2023-02-01', '2023-03-01'],
        'cost': [1000, 1500, 1200],
        'downtime_hours': [2, 3, 1.5],
        'output_loss': [200, 300, 250]
    }

    maintenance_df = pd.DataFrame(data)

    # Create an instance of the class
    maintenance_calculator = GeneratorMaintenanceCostEffectiveness(maintenance_df)

    # Calculate cost-effectiveness
    try:
        results = maintenance_calculator.calculate_cost_effectiveness()
        print("Cost-Effectiveness Results:", results)
    except ValueError as e:
        print("Error:", e)
```
