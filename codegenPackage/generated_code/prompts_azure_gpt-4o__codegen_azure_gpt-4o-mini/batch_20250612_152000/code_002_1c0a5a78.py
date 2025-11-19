"""
Generated Code Metadata:
========================
Original URL: https://aanjaneya-aero.com
Prompt: Generate code that calculates the cost-effectiveness of manufacturing aerospace components in India, factoring in the low-cost manufacturing opportunities highlighted by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_1c0a5a7876cfd89f
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class AerospaceCostEffectiveness:
    """
    A class to calculate the cost-effectiveness of manufacturing aerospace components in India.
    """

    def __init__(self, manufacturing_data):
        """
        Initializes the AerospaceCostEffectiveness with manufacturing data.

        :param manufacturing_data: A DataFrame containing manufacturing costs and other relevant data.
        """
        self.manufacturing_data = manufacturing_data

    def calculate_cost_effectiveness(self):
        """
        Calculates the cost-effectiveness of manufacturing components.

        :return: A DataFrame with cost-effectiveness metrics.
        """
        try:
            # Ensure necessary columns are present
            required_columns = ['component', 'cost', 'quality_score', 'lead_time']
            for column in required_columns:
                if column not in self.manufacturing_data.columns:
                    raise ValueError(f"Missing required column: {column}")

            # Calculate cost-effectiveness metrics
            self.manufacturing_data['cost_effectiveness'] = (
                self.manufacturing_data['quality_score'] / self.manufacturing_data['cost']
            )

            # Sort by cost-effectiveness
            sorted_data = self.manufacturing_data.sort_values(by='cost_effectiveness', ascending=False)

            return sorted_data[['component', 'cost', 'quality_score', 'lead_time', 'cost_effectiveness']]

        except Exception as e:
            print(f"Error calculating cost-effectiveness: {e}")
            return None

def main():
    # Sample manufacturing data
    data = {
        'component': ['Wing', 'Fuselage', 'Tail', 'Engine'],
        'cost': [50000, 120000, 30000, 200000],
        'quality_score': [90, 85, 80, 95],
        'lead_time': [30, 60, 20, 90]  # in days
    }

    # Create a DataFrame
    manufacturing_df = pd.DataFrame(data)

    # Initialize the cost-effectiveness calculator
    cost_effectiveness_calculator = AerospaceCostEffectiveness(manufacturing_df)

    # Calculate and display cost-effectiveness
    result = cost_effectiveness_calculator.calculate_cost_effectiveness()
    if result is not None:
        print(result)

if __name__ == "__main__":
    main()
```
