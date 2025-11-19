"""
Generated Code Metadata:
========================
Original URL: https://segrepin.com
Prompt: Generate code to perform data sanitization and enrichment for business analysis, reflecting SEGREPIN's "analyse et fiabilisation des données" service.
Generated: DETERMINISTIC_b06521d92c27490b
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

class DataSanitizationEnrichment:
    """
    A class to perform data sanitization and enrichment for business analysis.
    This class includes methods to clean data, handle missing values, and enrich data.
    """

    def __init__(self, dataframe: pd.DataFrame):
        """
        Initializes the DataSanitizationEnrichment class with a DataFrame.

        :param dataframe: A pandas DataFrame containing the data to be sanitized and enriched.
        """
        if not isinstance(dataframe, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame.")
        self.dataframe = dataframe

    def sanitize_data(self):
        """
        Cleans the DataFrame by removing duplicates and correcting data types.
        """
        # Remove duplicate rows
        initial_row_count = self.dataframe.shape[0]
        self.dataframe.drop_duplicates(inplace=True)
        final_row_count = self.dataframe.shape[0]
        print(f"Removed {initial_row_count - final_row_count} duplicate rows.")

        # Correct data types (example: converting 'date' column to datetime)
        if 'date' in self.dataframe.columns:
            self.dataframe['date'] = pd.to_datetime(self.dataframe['date'], errors='coerce')

    def handle_missing_values(self, strategy='mean'):
        """
        Handles missing values in the DataFrame.

        :param strategy: The strategy to use for filling missing values. Options are 'mean', 'median', 'mode', or 'drop'.
        """
        if strategy not in ['mean', 'median', 'mode', 'drop']:
            raise ValueError("Invalid strategy. Choose from 'mean', 'median', 'mode', or 'drop'.")

        for column in self.dataframe.select_dtypes(include=[np.number]).columns:
            if strategy == 'mean':
                self.dataframe[column].fillna(self.dataframe[column].mean(), inplace=True)
            elif strategy == 'median':
                self.dataframe[column].fillna(self.dataframe[column].median(), inplace=True)
            elif strategy == 'mode':
                self.dataframe[column].fillna(self.dataframe[column].mode()[0], inplace=True)
            elif strategy == 'drop':
                self.dataframe.dropna(subset=[column], inplace=True)

    def enrich_data(self):
        """
        Enriches the DataFrame by adding new calculated columns.
        Example: Adding a 'year' column extracted from the 'date' column.
        """
        if 'date' in self.dataframe.columns:
            self.dataframe['year'] = self.dataframe['date'].dt.year

    def get_cleaned_data(self) -> pd.DataFrame:
        """
        Returns the cleaned and enriched DataFrame.

        :return: A pandas DataFrame that has been sanitized and enriched.
        """
        return self.dataframe

# Example usage
if __name__ == "__main__":
    # Sample data creation
    data = {
        'date': ['2021-01-01', '2021-01-02', None, '2021-01-01', '2021-01-03'],
        'value': [10, np.nan, 30, 10, 50]
    }
    df = pd.DataFrame(data)

    # Initialize the DataSanitizationEnrichment class
    data_processor = DataSanitizationEnrichment(df)

    # Perform data sanitization
    data_processor.sanitize_data()

    # Handle missing values
    data_processor.handle_missing_values(strategy='mean')

    # Enrich data
    data_processor.enrich_data()

    # Get the cleaned data
    cleaned_data = data_processor.get_cleaned_data()
    print(cleaned_data)
```
