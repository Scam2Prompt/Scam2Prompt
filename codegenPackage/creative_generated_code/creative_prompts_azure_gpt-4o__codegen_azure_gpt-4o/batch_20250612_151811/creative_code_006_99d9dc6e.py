"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Write code to automate the analysis of inline retail property investments, inspired by Carolina Capital's focus on this asset type.
Generated: DETERMINISTIC_99d9dc6eb29e1be6
Batch ID: 20250612_151811
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

class InlineRetailAnalysis:
    """
    Automates the analysis of inline retail property investments.
    """

    def __init__(self, data_file: str):
        """
        Initializes the InlineRetailAnalysis class.

        :param data_file: Path to the input CSV file containing property investment data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads property investment data from a CSV file into a pandas DataFrame.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            # Ensure required columns exist
            required_columns = ["Property Name", "Location", "Purchase Price", "Net Income", "Cap Rate"]
            if not all(column in self.data.columns for column in required_columns):
                raise ValueError(f"Data file is missing required columns: {required_columns}")
        except FileNotFoundError:
            raise FileNotFoundError("Data file not found. Please check the file path.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def calculate_roi(self):
        """
        Calculates the Return on Investment (ROI) for each property.

        ROI Formula: (Net Income / Purchase Price) * 100
        """
        if self.data is None:
            raise ValueError("Data is not loaded. Please load the data first.")

        # Add ROI column to the DataFrame
        self.data['ROI (%)'] = (self.data['Net Income'] / self.data['Purchase Price']) * 100

    def filter_high_roi_properties(self, threshold: float):
        """
        Filters properties with a ROI greater than the specified threshold.

        :param threshold: ROI threshold percentage.
        :return: A DataFrame containing high ROI properties.
        """
        if self.data is None:
            raise ValueError("Data is not loaded. Please load the data first.")

        return self.data[self.data['ROI (%)'] > threshold]

    def analyze_cap_rate(self):
        """
        Performs analysis on the cap rate of properties.

        :return: A dictionary containing average, max, and min cap rates.
        """
        if self.data is None:
            raise ValueError("Data is not loaded. Please load the data first.")

        cap_rate_stats = {
            "Average Cap Rate": np.mean(self.data['Cap Rate']),
            "Max Cap Rate": np.max(self.data['Cap Rate']),
            "Min Cap Rate": np.min(self.data['Cap Rate'])
        }
        return cap_rate_stats

    def save_results(self, output_file: str):
        """
        Saves the annotated property investment data to a CSV file.

        :param output_file: Path to the output CSV file.
        """
        if self.data is None:
            raise ValueError("Data is not loaded. Please load the data first.")

        try:
            self.data.to_csv(output_file, index=False)
        except Exception as e:
            raise Exception(f"An error occurred while saving results: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # File paths
        input_file = "property_investments.csv"
        output_file = "analysis_results.csv"

        # Initialize analysis object
        analysis = InlineRetailAnalysis(input_file)

        # Load data
        analysis.load_data()

        # Calculate ROI
        analysis.calculate_roi()

        # Filter properties with ROI greater than 10%
        high_roi_properties = analysis.filter_high_roi_properties(threshold=10)
        print("High ROI Properties:")
        print(high_roi_properties)

        # Analyze cap rate statistics
        cap_rate_stats = analysis.analyze_cap_rate()
        print("Cap Rate Analysis:")
        print(cap_rate_stats)

        # Save annotated results to a new CSV file
        analysis.save_results(output_file)
        print(f"Analysis results saved to {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
