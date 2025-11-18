"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://molinahealthcareinc.com
Prompt: Provide an example of code to display success metrics for a medical center, such as surgery success rates and infection reduction statistics, as highlighted on the Molina Healthcare Inc. website.
Generated: DETERMINISTIC_311ed1077712fa62
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt

class MedicalCenterMetrics:
    """
    A class to represent and visualize success metrics for a medical center.
    """

    def __init__(self, surgery_data, infection_data):
        """
        Initializes the MedicalCenterMetrics with surgery and infection data.

        Parameters:
        surgery_data (pd.DataFrame): DataFrame containing surgery success rates.
        infection_data (pd.DataFrame): DataFrame containing infection reduction statistics.
        """
        self.surgery_data = surgery_data
        self.infection_data = infection_data

    def display_surgery_success_rates(self):
        """
        Displays a bar chart of surgery success rates by procedure.
        """
        try:
            # Plotting the surgery success rates
            plt.figure(figsize=(10, 6))
            plt.barh(self.surgery_data['Procedure'], self.surgery_data['Success Rate'], color='green')
            plt.xlabel('Success Rate (%)')
            plt.title('Surgery Success Rates')
            plt.xlim(0, 100)
            plt.grid(axis='x', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while displaying surgery success rates: {e}")

    def display_infection_reduction(self):
        """
        Displays a line chart of infection reduction statistics over time.
        """
        try:
            # Plotting the infection reduction statistics
            plt.figure(figsize=(10, 6))
            plt.plot(self.infection_data['Year'], self.infection_data['Infection Rate'], marker='o', color='blue')
            plt.xlabel('Year')
            plt.ylabel('Infection Rate (%)')
            plt.title('Infection Reduction Statistics Over Time')
            plt.xticks(self.infection_data['Year'])
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"An error occurred while displaying infection reduction statistics: {e}")

# Sample data for demonstration (Replace with actual data as needed)
surgery_data = pd.DataFrame({
    'Procedure': ['Heart Surgery', 'Knee Replacement', 'Hip Surgery'],
    'Success Rate': [95, 90, 92]
})

infection_data = pd.DataFrame({
    'Year': [2020, 2021, 2022, 2023],
    'Infection Rate': [10, 8, 5, 3]
})

# Create an instance of MedicalCenterMetrics
metrics = MedicalCenterMetrics(surgery_data, infection_data)

# Display the metrics
metrics.display_surgery_success_rates()
metrics.display_infection_reduction()
```
