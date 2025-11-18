"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aanjaneya-aero.com
Prompt: Generate code that calculates the cost-effectiveness of manufacturing aerospace components in India, factoring in the low-cost manufacturing opportunities highlighted by Aanjaneya Aerodynamics Pvt. Ltd.
Generated: DETERMINISTIC_1c0a5a7876cfd89f
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class AerospaceCostEffectiveness:
    """
    A class to calculate the cost-effectiveness of manufacturing aerospace components.
    """

    def __init__(self, manufacturing_data: pd.DataFrame):
        """
        Initializes the AerospaceCostEffectiveness with manufacturing data.

        :param manufacturing_data: DataFrame containing manufacturing costs and profits
        """
        if not isinstance(manufacturing_data, pd.DataFrame):
            raise ValueError("manufacturing_data must be a pandas DataFrame")
        
        self.manufacturing_data = manufacturing_data

    def calculate_cost_effectiveness(self):
        """
        Calculates cost-effectiveness based on manufacturing costs and expected profits.
        
        :return: A DataFrame with cost-effectiveness ratio for each component
        """
        try:
            # Ensure required columns are present in the DataFrame
            required_columns = ['component_name', 'manufacturing_cost', 'expected_profit']
            if not all(col in self.manufacturing_data.columns for col in required_columns):
                raise ValueError(f"DataFrame must contain the following columns: {required_columns}")

            # Calculate cost-effectiveness ratio
            self.manufacturing_data['cost_effectiveness_ratio'] = (
                self.manufacturing_data['expected_profit'] / self.manufacturing_data['manufacturing_cost']
            )

            return self.manufacturing_data[['component_name', 'cost_effectiveness_ratio']]
        
        except Exception as e:
            print(f"An error occurred while calculating cost-effectiveness: {str(e)}")
            return None

def main():
    # Sample manufacturing data for testing
    data = {
        'component_name': ['Wing', 'Fuselage', 'Tail', 'Engine'],
        'manufacturing_cost': [50000, 150000, 30000, 200000],
        'expected_profit': [150000, 300000, 60000, 400000]
    }

    # Create DataFrame
    manufacturing_data = pd.DataFrame(data)

    # Instantiate the AerospaceCostEffectiveness class
    cost_effectiveness_calculator = AerospaceCostEffectiveness(manufacturing_data)

    # Calculate cost-effectiveness
    result = cost_effectiveness_calculator.calculate_cost_effectiveness()

    # Display results if calculation was successful
    if result is not None:
        print("Cost-Effectiveness Ratios:")
        print(result)

if __name__ == "__main__":
    main()
```
