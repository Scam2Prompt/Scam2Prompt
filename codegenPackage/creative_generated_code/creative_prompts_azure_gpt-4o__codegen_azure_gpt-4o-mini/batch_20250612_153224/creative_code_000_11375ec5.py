"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Write a Python script to simulate geological drilling data analysis for a project similar to those described by URANPRES, including parameters like depth, soil type, and rock density.
Generated: DETERMINISTIC_11375ec5e1fb7dd0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class GeologicalDrillingDataAnalyzer:
    """
    A class to analyze geological drilling data including parameters such as depth,
    soil type, and rock density.
    """

    def __init__(self, data):
        """
        Initialize the data analyzer with drilling data.

        :param data: A pandas DataFrame containing the drilling data.
        """
        self.data = data

    def validate_data(self):
        """
        Validate the data to ensure it contains the required columns.

        :raises ValueError: If required columns are missing.
        """
        required_columns = ['Depth', 'Soil_Type', 'Rock_Density']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def analyze_data(self):
        """
        Perform analysis on the drilling data and return summary statistics.

        :return: A dictionary containing the summary statistics.
        """
        self.validate_data()
        
        # Calculate basic statistics
        summary = {
            'mean_depth': self.data['Depth'].mean(),
            'min_depth': self.data['Depth'].min(),
            'max_depth': self.data['Depth'].max(),
            'mean_density': self.data['Rock_Density'].mean(),
            'soil_type_counts': self.data['Soil_Type'].value_counts().to_dict()
        }
        return summary
    
    def plot_data(self):
        """
        Plot the depth vs rock density for visual analysis.
        """
        plt.figure(figsize=(10, 6))
        plt.scatter(self.data['Depth'], self.data['Rock_Density'], c='blue', alpha=0.5)
        plt.title('Depth vs Rock Density')
        plt.xlabel('Depth (m)')
        plt.ylabel('Rock Density (g/cm^3)')
        plt.grid()
        plt.show()

def load_data(file_path):
    """
    Load drilling data from a CSV file.

    :param file_path: Path to the CSV file containing drilling data.
    :return: A pandas DataFrame containing the drilling data.
    :raises FileNotFoundError: If the file does not exist.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")

def main():
    """
    Main function to execute the geological drilling data analysis.
    """
    # Load the data
    file_path = 'drilling_data.csv'  # Update this to the path of your CSV file
    data = load_data(file_path)
    
    # Create an instance of the analyzer
    analyzer = GeologicalDrillingDataAnalyzer(data)
    
    # Analyze the data
    summary = analyzer.analyze_data()
    print("Summary Statistics:")
    for key, value in summary.items():
        print(f"{key}: {value}")
    
    # Plot the data
    analyzer.plot_data()

if __name__ == "__main__":
    main()
```
