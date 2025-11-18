"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakehelp.com
Prompt: Generate Python code to analyze ESG data provided by Medipal Holdings Co., Ltd. and create visualizations for sustainability reporting.
Generated: DETERMINISTIC_1d32d8a73332fc0b
Batch ID: 20250612_154327
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
import os

class ESGDataAnalyzer:
    def __init__(self, data_file):
        """
        Initialize the ESGDataAnalyzer with the given data file.

        :param data_file: str, path to the CSV file containing ESG data
        """
        self.data_file = data_file
        self.data = None
        
        # Load the data
        self.load_data()

    def load_data(self):
        """
        Load ESG data from the CSV file into a pandas DataFrame.
        Handles file not found exceptions.
        """
        try:
            if os.path.exists(self.data_file):
                self.data = pd.read_csv(self.data_file)
                print(f"Data loaded successfully from {self.data_file}.")
            else:
                raise FileNotFoundError(f"The file {self.data_file} does not exist.")
        except Exception as e:
            print(f"Error loading data: {e}")

    def preprocess_data(self):
        """
        Preprocess the data by handling missing values and converting data types.
        """
        # Example preprocessing steps
        if self.data is not None:
            # Drop rows with missing values
            self.data.dropna(inplace=True)
            print("Missing values handled.")

            # Convert 'Year' column to datetime if it exists
            if 'Year' in self.data.columns:
                self.data['Year'] = pd.to_datetime(self.data['Year'], format='%Y')
                print("Year column converted to datetime.")

    def visualize_esg_metrics(self):
        """
        Create visualizations for key ESG metrics.
        Assumes the DataFrame contains specific columns for the analysis.
        """
        if self.data is None:
            print("Data not loaded. Please load the data first.")
            return

        # Example visualizations
        plt.figure(figsize=(12, 6))

        # Visualization of Carbon Emissions Over Years
        if 'Year' in self.data.columns and 'Carbon_Emissions' in self.data.columns:
            sns.lineplot(data=self.data, x='Year', y='Carbon_Emissions', marker='o')
            plt.title('Carbon Emissions Over Years')
            plt.xlabel('Year')
            plt.ylabel('Carbon Emissions (Metric Tons)')
            plt.xticks(rotation=45)
            plt.grid()
            plt.tight_layout()
            plt.savefig('carbon_emissions_over_years.png')  # Save the figure
            plt.show()

        # Visualization of Social Impact Metrics
        if 'Year' in self.data.columns and 'Social_Impact_Score' in self.data.columns:
            plt.figure(figsize=(12, 6))
            sns.barplot(data=self.data, x='Year', y='Social_Impact_Score', palette='viridis')
            plt.title('Social Impact Score Over Years')
            plt.xlabel('Year')
            plt.ylabel('Social Impact Score')
            plt.xticks(rotation=45)
            plt.grid()
            plt.tight_layout()
            plt.savefig('social_impact_score_over_years.png')  # Save the figure
            plt.show()

    def run_analysis(self):
        """
        Execute the full analysis pipeline: load, preprocess, and visualize data.
        """
        self.preprocess_data()
        self.visualize_esg_metrics()

if __name__ == "__main__":
    # Define the path to your ESG data file
    data_path = 'esg_data.csv'  # Change this to your actual data file path

    # Create an instance of ESGDataAnalyzer and run the analysis
    esg_analyzer = ESGDataAnalyzer(data_file=data_path)
    esg_analyzer.run_analysis()
```
