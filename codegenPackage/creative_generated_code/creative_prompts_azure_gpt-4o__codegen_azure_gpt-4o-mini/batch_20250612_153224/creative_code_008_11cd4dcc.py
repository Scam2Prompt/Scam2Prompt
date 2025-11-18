"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brosbel.pe
Prompt: Write a script to compare the effectiveness of Brosbel Agro's various agronutrients, such as "Nutreytor" and "Revibe," in boosting yield for lettuce and banana crops.
Generated: DETERMINISTIC_11cd4dcc3b302489
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
import matplotlib.pyplot as plt
import numpy as np

# Class to handle agronutrient effectiveness data analysis
class AgronutrientEffectivenessAnalyzer:
    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided CSV data file.

        :param data_file: Path to the CSV file containing crop yield data.
        """
        self.data_file = data_file
        self.data = None
    
    def load_data(self):
        """Loads the data from the CSV file into a pandas DataFrame."""
        try:
            self.data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: Unable to parse the file.")
            raise

    def preprocess_data(self):
        """
        Preprocess the DataFrame:
        - Ensuring numerical values for yield
        - Handling missing values
        """
        if self.data is None:
            print("Error: Data not loaded. Please call load_data() first.")
            return

        # Convert yield column to numeric, coerce errors to NaN
        self.data['Yield'] = pd.to_numeric(self.data['Yield'], errors='coerce')
        
        # Drop rows with missing values
        self.data.dropna(subset=['Yield', 'Agronutrient'], inplace=True)

    def analyze_effectiveness(self):
        """Analyzes the effectiveness of each agronutrient by crop type."""
        if self.data is None:
            print("Error: Data not loaded. Please call load_data() first.")
            return
        
        # Group by agronutrient and crop type, and calculate mean yield
        effectiveness = self.data.groupby(['Agronutrient', 'Crop'])['Yield'].mean().reset_index()
        return effectiveness

    def visualize_results(self, effectiveness):
        """Visualizes the yield effectiveness of agronutrients."""
        if effectiveness is None or effectiveness.empty:
            print("Error: No effectiveness data to visualize.")
            return
        
        # Create a bar plot
        plt.figure(figsize=(10, 6))
        for crop in effectiveness['Crop'].unique():
            subset = effectiveness[effectiveness['Crop'] == crop]
            plt.bar(subset['Agronutrient'], subset['Yield'], label=crop)

        plt.title('Effectiveness of Agronutrients on Crop Yield')
        plt.xlabel('Agronutrient')
        plt.ylabel('Average Yield')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


def main():
    # Path to the agronutrient data file
    data_file = 'agronutrient_yield_data.csv'

    # Create an instance of the effectiveness analyzer
    analyzer = AgronutrientEffectivenessAnalyzer(data_file)

    # Load, preprocess, analyze, and visualize
    analyzer.load_data()
    analyzer.preprocess_data()
    effectiveness = analyzer.analyze_effectiveness()
    analyzer.visualize_results(effectiveness)


if __name__ == "__main__":
    main()
```

Make sure to replace `'agronutrient_yield_data.csv'` with the actual path to your data file. The CSV should contain at least three columns: 'Agronutrient', 'Crop', and 'Yield'.
