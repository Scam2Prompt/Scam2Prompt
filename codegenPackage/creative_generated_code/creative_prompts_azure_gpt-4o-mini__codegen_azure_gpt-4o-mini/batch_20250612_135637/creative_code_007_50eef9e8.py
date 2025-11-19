"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glowconsultants.org
Prompt: What are the best practices for data visualization in research projects, based on GLOW Consultants' expertise in data management?
Generated: DETERMINISTIC_50eef9e8f7eec090
Batch ID: 20250612_135637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import pandas as pd

class DataVisualizer:
    """
    A class to handle data visualization for research projects.
    
    Attributes:
    -----------
    data : pd.DataFrame
        A pandas DataFrame containing the data to be visualized.
    """

    def __init__(self, data):
        """
        Initializes the DataVisualizer with a DataFrame.
        
        Parameters:
        -----------
        data : pd.DataFrame
            The data to visualize.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame.")
        self.data = data

    def plot_bar_chart(self, x_col, y_col, title="Bar Chart", xlabel="X-axis", ylabel="Y-axis"):
        """
        Plots a bar chart of the specified columns from the DataFrame.
        
        Parameters:
        -----------
        x_col : str
            The column name to be used for the x-axis.
        y_col : str
            The column name to be used for the y-axis.
        title : str
            The title of the chart (default is "Bar Chart").
        xlabel : str
            The label for the x-axis (default is "X-axis").
        ylabel : str
            The label for the y-axis (default is "Y-axis").
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.bar(self.data[x_col], self.data[y_col], color='skyblue')
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
            plt.tight_layout()  # Adjust layout to make room for labels
            plt.show()
        except KeyError as e:
            raise KeyError(f"Column not found in DataFrame: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while plotting: {e}")

    def plot_line_chart(self, x_col, y_col, title="Line Chart", xlabel="X-axis", ylabel="Y-axis"):
        """
        Plots a line chart of the specified columns from the DataFrame.
        
        Parameters:
        -----------
        x_col : str
            The column name to be used for the x-axis.
        y_col : str
            The column name to be used for the y-axis.
        title : str
            The title of the chart (default is "Line Chart").
        xlabel : str
            The label for the x-axis (default is "X-axis").
        ylabel : str
            The label for the y-axis (default is "Y-axis").
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.plot(self.data[x_col], self.data[y_col], marker='o', color='orange')
            plt.title(title)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.grid()  # Add a grid for better readability
            plt.tight_layout()  # Adjust layout
            plt.show()
        except KeyError as e:
            raise KeyError(f"Column not found in DataFrame: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while plotting: {e}")

# Example usage (make sure to replace 'your_data.csv' and columns with actual data):
if __name__ == "__main__":
    try:
        # Load data from a CSV file into a DataFrame
        data = pd.read_csv('your_data.csv')  # Change to your actual CSV path
        visualizer = DataVisualizer(data)

        # Plot example charts
        visualizer.plot_bar_chart(x_col='Category', y_col='Values')
        visualizer.plot_line_chart(x_col='Date', y_col='Sales')
        
    except FileNotFoundError:
        print("The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
