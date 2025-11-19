"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terawit.net
Prompt: Write a code snippet that analyzes employee training effectiveness using Returns on Training Investment (ROTI) metrics.
Generated: DETERMINISTIC_5e4be988d939e3a2
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class TrainingEffectivenessAnalyzer:
    """
    A class to analyze employee training effectiveness using Returns on Training Investment (ROTI) metrics.
    """

    def __init__(self, training_data: pd.DataFrame):
        """
        Initializes the TrainingEffectivenessAnalyzer with training data.

        Args:
            training_data (pd.DataFrame): DataFrame containing training data with 'cost', 'revenue_increase', and 'employee_id' columns.
        """
        # Check if the DataFrame has the required columns
        required_columns = {'cost', 'revenue_increase', 'employee_id'}
        if not required_columns.issubset(training_data.columns):
            raise ValueError(f"Input DataFrame must contain the following columns: {required_columns}")

        self.training_data = training_data

    def calculate_roti(self) -> pd.DataFrame:
        """
        Calculates the Returns on Training Investment (ROTI) for each employee.

        Returns:
            pd.DataFrame: A DataFrame containing employee IDs and their corresponding ROTI values.
        """
        try:
            # Calculate ROTI: (Revenue Increase - Cost) / Cost
            self.training_data['roti'] = (self.training_data['revenue_increase'] - self.training_data['cost']) / self.training_data['cost']
            return self.training_data[['employee_id', 'roti']]
        except Exception as e:
            raise RuntimeError("Error calculating ROTI metrics") from e

    def analyze_roti(self) -> str:
        """
        Analyzes the ROTI results and returns a summary of effectiveness.

        Returns:
            str: A summary of the training effectiveness based on ROTI.
        """
        roti_summary = self.calculate_roti()
        average_roti = roti_summary['roti'].mean()
        
        if average_roti > 0:
            return f"Training is effective with an average ROTI of {average_roti:.2f}."
        else:
            return f"Training is not effective with an average ROTI of {average_roti:.2f}."

# Example usage:
if __name__ == "__main__":
    # Sample data frame with training costs and revenue increases
    data = {
        'employee_id': [1, 2, 3],
        'cost': [1000, 1500, 1200],
        'revenue_increase': [3000, 4000, 2500]
    }
    
    training_df = pd.DataFrame(data)

    try:
        analyzer = TrainingEffectivenessAnalyzer(training_df)
        print(analyzer.analyze_roti())
    except Exception as e:
        print(f"An error occurred: {e}")
```
