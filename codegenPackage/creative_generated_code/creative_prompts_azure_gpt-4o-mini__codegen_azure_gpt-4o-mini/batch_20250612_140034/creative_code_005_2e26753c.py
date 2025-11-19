"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foundation.ru
Prompt: Explain how to assess the impact of new construction on existing structures using techniques from the Geotechnical Center's offerings.
Generated: DETERMINISTIC_2e26753cf2dae2e4
Batch ID: 20250612_140034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

class ConstructionImpactAssessment:
    """
    A class to assess the impact of new construction on existing structures
    using geotechnical methodologies.
    """

    def __init__(self, existing_structure_data, new_construction_data):
        """
        Initializes the ConstructionImpactAssessment with existing and new construction data.

        :param existing_structure_data: DataFrame containing data about existing structures
        :param new_construction_data: DataFrame containing data about new constructions
        """
        self.existing_structure_data = existing_structure_data
        self.new_construction_data = new_construction_data

    def simulate_ground_movement(self):
        """
        Simulates ground movement based on new construction and assesses its impact.

        :return: A DataFrame with the impact assessment results
        """
        try:
            # Simulate ground movement due to new construction
            movement = self.new_construction_data['load'] * np.random.normal(1.0, 0.1, len(self.new_construction_data))
            self.existing_structure_data['ground_movement'] = movement
            
            return self.existing_structure_data
            
        except Exception as e:
            print(f"Error during ground movement simulation: {e}")
            return None

    def visualize_impact(self):
        """
        Visualizes the impact of new construction on existing structures.

        :return: A matplotlib figure showing the impact
        """
        try:
            # Check if ground movement data exists
            if 'ground_movement' not in self.existing_structure_data.columns:
                raise ValueError("Ground movement data not calculated. Please run simulate_ground_movement first.")

            plt.figure(figsize=(12, 6))
            plt.scatter(self.existing_structure_data['structure_id'], 
                        self.existing_structure_data['ground_movement'], 
                        color='blue', label='Ground Movement', alpha=0.6)
            plt.title('Impact of New Construction on Existing Structures')
            plt.xlabel('Structure ID')
            plt.ylabel('Ground Movement (mm)')
            plt.axhline(0, color='red', linestyle='--', label='No Movement')
            plt.legend()
            plt.grid()
            plt.show()
            
        except Exception as e:
            print(f"Error during visualization: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for existing structures
    existing_data = {
        'structure_id': [1, 2, 3, 4, 5],
        'location': ['A', 'B', 'C', 'D', 'E'],
        'age': [15, 20, 10, 25, 30]  # in years
    }

    # Sample data for new constructions
    new_construction_data = {
        'construction_id': [101, 102],
        'load': [300, 500]  # in kN
    }

    existing_structure_df = pd.DataFrame(existing_data)
    new_construction_df = pd.DataFrame(new_construction_data)

    assessment = ConstructionImpactAssessment(existing_structure_df, new_construction_df)
    assessment.simulate_ground_movement()
    assessment.visualize_impact()
```
