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
import matplotlib.pyplot as plt
import pandas as pd

# Sample data for construction projects
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Apartments_Constructed': [10, 20, 30, 25, 40, 50],
    'Hours_Worked': [200, 400, 600, 500, 800, 1000],
    'Jobs_Generated': [5, 10, 15, 12, 20, 25]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Function to visualize construction project metrics
def visualize_construction_progress(df):
    """
    Visualizes the progress of construction projects using Matplotlib.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing construction metrics.
    """
    try:
        # Set the figure size
        plt.figure(figsize=(12, 6))

        # Plotting Apartments Constructed
        plt.subplot(3, 1, 1)
        plt.plot(df['Month'], df['Apartments_Constructed'], marker='o', color='b', label='Apartments Constructed')
        plt.title('Apartments Constructed Over Time')
        plt.xlabel('Month')
        plt.ylabel('Number of Apartments')
        plt.grid()
        plt.legend()

        # Plotting Hours Worked
        plt.subplot(3, 1, 2)
        plt.plot(df['Month'], df['Hours_Worked'], marker='o', color='g', label='Hours Worked')
        plt.title('Hours Worked Over Time')
        plt.xlabel('Month')
        plt.ylabel('Hours')
        plt.grid()
        plt.legend()

        # Plotting Jobs Generated
        plt.subplot(3, 1, 3)
        plt.plot(df['Month'], df['Jobs_Generated'], marker='o', color='r', label='Jobs Generated')
        plt.title('Jobs Generated Over Time')
        plt.xlabel('Month')
        plt.ylabel('Number of Jobs')
        plt.grid()
        plt.legend()

        # Adjust layout to prevent overlap
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred while visualizing the data: {e}")

# Call the function to visualize the construction progress
if __name__ == "__main__":
    visualize_construction_progress(df)
```
