"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cotirex.com
Prompt: Write a script to compare Cotirex predictions for the next South Korean president with external polling data and generate a report.
Generated: DETERMINISTIC_b34646b929d09fcf
Batch ID: 20250612_153809
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

class ElectionPredictionComparator:
    """
    A class to compare Cotirex predictions with external polling data
    and generate a report.
    """

    def __init__(self, cotirex_data: str, polling_data: str):
        """
        Initializes the comparator with Cotirex and polling data file paths.

        Args:
            cotirex_data (str): Path to the Cotirex predictions CSV file.
            polling_data (str): Path to the external polling data CSV file.
        """
        self.cotirex_data = cotirex_data
        self.polling_data = polling_data
        self.cotirex_df = pd.DataFrame()
        self.polling_df = pd.DataFrame()

    def load_data(self):
        """Loads data from the provided CSV files into DataFrames."""
        try:
            self.cotirex_df = pd.read_csv(self.cotirex_data)
            self.polling_df = pd.read_csv(self.polling_data)
            print("Data loaded successfully.")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            raise
        except pd.errors.EmptyDataError:
            print("Error: One of the files is empty.")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise

    def preprocess_data(self):
        """Preprocesses the data to ensure it is ready for comparison."""
        # Ensure the necessary columns exist
        required_columns = ['candidate', 'predicted_votes']
        for column in required_columns:
            if column not in self.cotirex_df.columns or column not in self.polling_df.columns:
                raise ValueError(f"Missing required column: {column}")

        # Aggregate polling data if necessary
        self.polling_df = self.polling_df.groupby('candidate').agg({'poll_votes': 'mean'}).reset_index()
        print("Data preprocessing completed.")

    def compare_predictions(self):
        """Compares Cotirex predictions with external polling data."""
        comparison_df = pd.merge(self.cotirex_df, self.polling_df, on='candidate', how='outer', suffixes=('_cotirex', '_polling'))
        comparison_df['difference'] = comparison_df['predicted_votes'] - comparison_df['poll_votes']
        print("Comparison completed.")
        return comparison_df

    def generate_report(self, comparison_df: pd.DataFrame):
        """Generates a report based on the comparison results."""
        # Save comparison report to CSV
        report_file = 'comparison_report.csv'
        comparison_df.to_csv(report_file, index=False)
        print(f"Report generated and saved to {report_file}.")
        
        # Visualize the comparison
        plt.figure(figsize=(10, 6))
        x = np.arange(len(comparison_df['candidate']))
        width = 0.35

        plt.bar(x - width/2, comparison_df['predicted_votes'], width, label='Cotirex Predictions', color='blue')
        plt.bar(x + width/2, comparison_df['poll_votes'], width, label='Polling Data', color='orange')

        plt.ylabel('Votes')
        plt.title('Comparison of Cotirex Predictions and Polling Data')
        plt.xticks(x, comparison_df['candidate'], rotation=45)
        plt.legend()
        plt.tight_layout()
        plt.show()

    def run(self):
        """Executes the comparison and report generation process."""
        self.load_data()
        self.preprocess_data()
        comparison_df = self.compare_predictions()
        self.generate_report(comparison_df)

if __name__ == "__main__":
    # Replace with actual file paths for Cotirex and polling data CSVs.
    cotirex_file_path = 'cotirex_predictions.csv'
    polling_file_path = 'polling_data.csv'

    comparator = ElectionPredictionComparator(cotirex_file_path, polling_file_path)
    comparator.run()
```
