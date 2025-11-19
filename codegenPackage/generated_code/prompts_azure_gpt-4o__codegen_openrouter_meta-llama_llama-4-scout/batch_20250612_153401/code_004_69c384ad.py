"""
Generated Code Metadata:
========================
Original URL: https://inaro.com.co
Prompt: Write a script to visualize the progress of construction projects using Python and a data visualization library (e.g., `Matplotlib` or `Plotly`), incorporating metrics like apartments constructed, hours worked, and jobs generated, inspired by INARO S.A.S.'s statistics.
Generated: DETERMINISTIC_69c384ad23a23e49
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

# Define a class to visualize construction project progress
class ConstructionProjectVisualizer:
    def __init__(self, data):
        """
        Initialize the visualizer with project data.

        Args:
        - data (dict or pandas.DataFrame): A dictionary or DataFrame containing project metrics.
            Expected keys/columns:
                - 'Month'
                - 'Apartments Constructed'
                - 'Hours Worked'
                - 'Jobs Generated'
        """
        if isinstance(data, dict):
            self.data = pd.DataFrame(data)
        elif isinstance(data, pd.DataFrame):
            self.data = data
        else:
            raise ValueError("Invalid data type. Expected dict or pandas.DataFrame.")

    def validate_data(self):
        """
        Validate the project data.

        Raises:
        - ValueError: If required columns are missing.
        """
        required_columns = ['Month', 'Apartments Constructed', 'Hours Worked', 'Jobs Generated']
        if not all(column in self.data.columns for column in required_columns):
            raise ValueError("Missing required columns.")

    def plot_progress_matplotlib(self):
        """
        Plot project progress using Matplotlib.
        """
        self.validate_data()

        # Create a figure with subplots
        fig, axs = plt.subplots(3, figsize=(10, 12))

        # Plot apartments constructed
        axs[0].plot(self.data['Month'], self.data['Apartments Constructed'], marker='o')
        axs[0].set_title('Apartments Constructed')
        axs[0].set_xlabel('Month')
        axs[0].set_ylabel('Apartments')

        # Plot hours worked
        axs[1].plot(self.data['Month'], self.data['Hours Worked'], marker='o')
        axs[1].set_title('Hours Worked')
        axs[1].set_xlabel('Month')
        axs[1].set_ylabel('Hours')

        # Plot jobs generated
        axs[2].plot(self.data['Month'], self.data['Jobs Generated'], marker='o')
        axs[2].set_title('Jobs Generated')
        axs[2].set_xlabel('Month')
        axs[2].set_ylabel('Jobs')

        # Layout so plots do not overlap
        fig.tight_layout()

        plt.show()

    def plot_progress_plotly(self):
        """
        Plot project progress using Plotly.
        """
        self.validate_data()

        # Melt the DataFrame for Plotly express
        df_melted = pd.melt(self.data, id_vars='Month', var_name='Metric', value_name='Value')

        # Create a line figure
        fig = px.line(df_melted, x='Month', y='Value', color='Metric', title='Construction Project Progress')

        # Update layout for better readability
        fig.update_layout(xaxis_title='Month', yaxis_title='Value')

        fig.show()


# Example usage
if __name__ == "__main__":
    # Sample project data
    data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'Apartments Constructed': [10, 15, 12, 18, 20],
        'Hours Worked': [1000, 1200, 1100, 1300, 1400],
        'Jobs Generated': [50, 60, 55, 65, 70]
    }

    visualizer = ConstructionProjectVisualizer(data)
    visualizer.plot_progress_matplotlib()
    visualizer.plot_progress_plotly()
```
