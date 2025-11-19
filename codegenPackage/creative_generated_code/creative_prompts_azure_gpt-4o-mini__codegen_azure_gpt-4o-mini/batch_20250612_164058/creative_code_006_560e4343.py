"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mercanza.es
Prompt: What tools and libraries does Mercanza suggest for ensuring data quality and management in a business environment?
Generated: DETERMINISTIC_560e4343c964c367
Batch ID: 20250612_164058
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
from pandas.errors import EmptyDataError

class DataQualityManager:
    """
    A class to manage and ensure data quality in a business environment.

    Attributes
    ----------
    data : pd.DataFrame
        The input dataset as a pandas DataFrame.

    Methods
    -------
    load_data(filepath: str) -> None
        Loads data from a CSV file into the DataFrame.
    
    check_missing_values() -> pd.Series
        Returns a Series with the count of missing values per column.
    
    check_duplicates() -> pd.DataFrame
        Returns a DataFrame containing duplicate rows.
    
    clean_data() -> pd.DataFrame
        Cleans the DataFrame by handling missing values and duplicates.
    """

    def __init__(self):
        self.data = pd.DataFrame()

    def load_data(self, filepath: str) -> None:
        """
        Loads data from a CSV file into the DataFrame.

        Parameters
        ----------
        filepath : str
            The path to the CSV file to be loaded.

        Raises
        ------
        FileNotFoundError
            If the specified file does not exist.
        EmptyDataError
            If the provided file is empty.
        """
        try:
            self.data = pd.read_csv(filepath)
            print(f"Data loaded successfully from {filepath}")
        except FileNotFoundError:
            print(f"Error: The file {filepath} was not found.")
        except EmptyDataError:
            print("Error: The file is empty.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def check_missing_values(self) -> pd.Series:
        """
        Returns a Series with the count of missing values per column.

        Returns
        -------
        pd.Series
            A Series with column names as index and missing value counts as values.
        """
        return self.data.isnull().sum()

    def check_duplicates(self) -> pd.DataFrame:
        """
        Returns a DataFrame containing duplicate rows.

        Returns
        -------
        pd.DataFrame
            A DataFrame containing the duplicate rows from the dataset.
        """
        return self.data[self.data.duplicated()]

    def clean_data(self) -> pd.DataFrame:
        """
        Cleans the DataFrame by handling missing values and duplicates.

        Returns
        -------
        pd.DataFrame
            A cleaned DataFrame with missing values filled and duplicates removed.
        """
        # Fill missing values with the mean of each column for numerical data
        self.data.fillna(self.data.mean(), inplace=True)
        print("Missing values filled with column means.")
        
        # Remove duplicates
        initial_count = len(self.data)
        self.data.drop_duplicates(inplace=True)
        final_count = len(self.data)
        print(f"Removed {initial_count - final_count} duplicate rows.")
        
        return self.data

# Example usage (Uncomment to use):
# if __name__ == "__main__":
#     manager = DataQualityManager()
#     manager.load_data('data.csv')
#     print(manager.check_missing_values())
#     print(manager.check_duplicates())
#     cleaned_data = manager.clean_data()
#     print(cleaned_data)
```
