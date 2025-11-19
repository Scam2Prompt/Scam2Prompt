"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamass.de
Prompt: Create a prototype for a brand concept that incorporates data visualization techniques highlighted in the portfolio section of metamass.de.
Generated: DETERMINISTIC_ebfabc73c1882f09
Batch ID: 20250612_162508
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
import seaborn as sns

# Set the style for the visualizations
sns.set(style="whitegrid")

class DataVisualizer:
    """
    A class used to visualize data using various techniques.
    
    Attributes
    ----------
    data : pd.DataFrame
        a pandas DataFrame containing the data to visualize
        
    Methods
    -------
    load_data(file_path)
        Loads data from a CSV file into the data attribute.
        
    plot_summary_statistics()
        Plots summary statistics of the dataset.
        
    plot_correlation_matrix()
        Plots a heatmap of the correlation matrix of the dataset.
        
    plot_distribution(column_name)
        Plots the distribution of a specified column in the dataset.
    """

    def __init__(self):
        """
        Initializes the DataVisualizer with an empty DataFrame.
        """
        self.data = pd.DataFrame()

    def load_data(self, file_path):
        """
        Loads data from a CSV file into the data attribute.
        
        Parameters
        ----------
        file_path : str
            The path to the CSV file to be loaded.
        
        Raises
        ------
        FileNotFoundError
            If the specified file does not exist.
        pd.errors.EmptyDataError
            If the file is empty.
        pd.errors.ParserError
            If the file contains malformed data.
        """
        try:
            self.data = pd.read_csv(file_path)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise
        except pd.errors.EmptyDataError as e:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError as e:
            print("Error: There is a parsing error in the file.")
            raise

    def plot_summary_statistics(self):
        """
        Plots summary statistics of the dataset.
        
        This method generates a box plot for each numerical column in the dataset
        to visualize the summary statistics (like median, quartiles, etc.).
        """
        # Check if data is loaded
        if self.data.empty:
            print("Error: No data loaded. Please load data before plotting.")
            return

        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.data)
        plt.title("Summary Statistics Box Plot")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_correlation_matrix(self):
        """
        Plots a heatmap of the correlation matrix of the dataset.
        
        This method visualizes the correlation between all numerical features,
        helping to identify patterns and relationships in the data.
        """
        # Check if data is loaded
        if self.data.empty:
            print("Error: No data loaded. Please load data before plotting.")
            return

        plt.figure(figsize=(12, 8))
        correlation_matrix = self.data.corr()
        sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
        plt.title("Correlation Matrix Heatmap")
        plt.tight_layout()
        plt.show()

    def plot_distribution(self, column_name):
        """
        Plots the distribution of a specified column in the dataset.
        
        Parameters
        ----------
        column_name : str
            The name of the column to visualize the distribution.
        
        Raises
        ------
        ValueError
            If the specified column does not exist in the DataFrame.
        """
        # Check if data is loaded
        if self.data.empty:
            print("Error: No data loaded. Please load data before plotting.")
            return

        if column_name not in self.data.columns:
            raise ValueError(f"Error: Column '{column_name}' does not exist in the dataset.")

        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column_name], bins=30, kde=True)
        plt.title(f"Distribution of {column_name}")
        plt.xlabel(column_name)
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.show()


# Example usage (replace 'your_data_file.csv' with your actual data file path)
if __name__ == "__main__":
    visualizer = DataVisualizer()
    visualizer.load_data('your_data_file.csv')
    visualizer.plot_summary_statistics()
    visualizer.plot_correlation_matrix()
    visualizer.plot_distribution('your_column_name')  # Replace 'your_column_name' with actual column name
```
