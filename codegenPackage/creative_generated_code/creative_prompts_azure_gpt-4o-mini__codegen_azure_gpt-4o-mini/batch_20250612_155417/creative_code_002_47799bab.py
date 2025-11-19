"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://45ybook.ueh.edu.vn
Prompt: Write a Python script that analyzes data on multi-disciplinary programs in universities, inspired by the themes in the UEH publication.
Generated: DETERMINISTIC_47799bab94aa44db
Batch ID: 20250612_155417
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

class UniversityProgramAnalyzer:
    """
    A class to analyze data on multi-disciplinary programs in universities.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the data file.

        :param data_file: str, path to the CSV file containing university program data.
        """
        self.data_file = data_file
        self.df = self.load_data()

    def load_data(self):
        """
        Loads the data from the specified CSV file.

        :return: DataFrame containing the university program data.
        """
        try:
            df = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return df
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def clean_data(self):
        """
        Cleans the DataFrame by handling missing values and duplicates.
        """
        initial_shape = self.df.shape
        self.df.dropna(inplace=True)  # Remove rows with missing values
        self.df.drop_duplicates(inplace=True)  # Remove duplicate rows
        print(f"Data cleaned: {initial_shape} -> {self.df.shape}")

    def analyze_programs(self):
        """
        Analyzes the multi-disciplinary programs and generates basic statistics.

        :return: DataFrame with analysis results.
        """
        # Grouping by program type and counting number of programs
        program_counts = self.df.groupby('Program Type').size().reset_index(name='Count')
        print("Program analysis complete.")
        return program_counts

    def visualize_data(self, analysis_results):
        """
        Visualizes the analysis results using a bar chart.

        :param analysis_results: DataFrame containing the analysis results to visualize.
        """
        plt.figure(figsize=(10, 6))
        plt.bar(analysis_results['Program Type'], analysis_results['Count'], color='skyblue')
        plt.title('Number of Multi-disciplinary Programs by Program Type')
        plt.xlabel('Program Type')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def main():
    """
    Main function to execute the program analysis.
    """
    data_file = 'university_programs.csv'  # Update with your actual data file path
    analyzer = UniversityProgramAnalyzer(data_file)

    # Clean the data
    analyzer.clean_data()

    # Analyze the programs
    analysis_results = analyzer.analyze_programs()

    # Visualize the analysis results
    analyzer.visualize_data(analysis_results)

if __name__ == "__main__":
    main()
```
