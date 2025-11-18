"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Develop a data analysis pipeline in Python using techniques from PDMA's Data Analysis training, including data cleaning and visualization.
Generated: DETERMINISTIC_3ed63e00b87d54be
Batch ID: 20250612_145730
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
import seaborn as sns

# Set visualization style
sns.set(style="whitegrid")

class DataAnalysisPipeline:
    def __init__(self, file_path: str):
        """
        Initializes the DataAnalysisPipeline with the given file path.

        :param file_path: Path to the dataset CSV file.
        """
        self.file_path = file_path
        self.data = None

    def load_data(self) -> pd.DataFrame:
        """
        Loads data from a CSV file into a pandas DataFrame.

        :return: Loaded DataFrame
        """
        try:
            self.data = pd.read_csv(self.file_path)
            print("Data loaded successfully.")
            return self.data
        except FileNotFoundError as e:
            print(f"Error: File not found - {e}")
            raise
        except pd.errors.EmptyDataError as e:
            print(f"Error: No data - {e}")
            raise
        except pd.errors.ParserError as e:
            print(f"Error: Parsing error - {e}")
            raise

    def clean_data(self) -> pd.DataFrame:
        """
        Cleans the dataset by handling missing values and removing duplicates.

        :return: Cleaned DataFrame
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        # Handle missing values
        print("Cleaning data...")
        initial_shape = self.data.shape
        self.data.dropna(inplace=True)  # Drop rows with missing values
        self.data.drop_duplicates(inplace=True)  # Remove duplicate rows

        cleaned_shape = self.data.shape
        print(f"Data cleaned: {initial_shape} -> {cleaned_shape}")
        return self.data

    def visualize_data(self):
        """
        Visualizes the data using histograms and pair plots.

        :return: None
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        # Histogram of each numerical column
        numerical_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()
        self.data[numerical_cols].hist(bins=15, figsize=(15, 6), layout=(2, len(numerical_cols)//2), color='lightblue')
        plt.suptitle('Histograms of Numerical Features')
        plt.show()

        # Pair plot for numerical features
        sns.pairplot(self.data[numerical_cols])
        plt.suptitle('Pair Plot of Numerical Features', y=1.02)
        plt.show()

if __name__ == "__main__":
    # Example usage of DataAnalysisPipeline
    try:
        pipeline = DataAnalysisPipeline(file_path='data.csv')  # Replace with your file path
        pipeline.load_data()
        pipeline.clean_data()
        pipeline.visualize_data()
    except Exception as e:
        print(f"An error occurred: {e}")
```
