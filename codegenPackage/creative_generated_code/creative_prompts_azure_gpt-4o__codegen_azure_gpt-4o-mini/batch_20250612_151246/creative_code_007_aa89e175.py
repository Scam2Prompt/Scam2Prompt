"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getgrass-claim.pages.dev
Prompt: Write a Python program to clean and prepare structured datasets collected through a Grass-like network for AI model training purposes.
Generated: DETERMINISTIC_aa89e1751b185722
Batch ID: 20250612_151246
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

class DatasetCleaner:
    """
    A class to clean and prepare structured datasets collected from a Grass-like network.
    This class provides methods to handle missing values, remove duplicates, 
    and normalize data for AI model training purposes.
    """

    def __init__(self, dataset: pd.DataFrame):
        """
        Initializes the DatasetCleaner with a pandas DataFrame.

        Args:
            dataset (pd.DataFrame): The dataset to be cleaned.
        """
        self.dataset = dataset

    def remove_duplicates(self):
        """Removes duplicate rows from the dataset."""
        initial_shape = self.dataset.shape
        self.dataset.drop_duplicates(inplace=True)
        new_shape = self.dataset.shape
        print(f"Removed duplicates: {initial_shape[0] - new_shape[0]} rows dropped.")

    def handle_missing_values(self, strategy='mean'):
        """
        Handles missing values in the dataset.

        Args:
            strategy (str): The strategy to handle missing values - 'mean', 'median', or 'drop'.
        """
        if strategy not in ['mean', 'median', 'drop']:
            raise ValueError("Invalid strategy. Use 'mean', 'median', or 'drop'.")

        if strategy == 'drop':
            initial_shape = self.dataset.shape
            self.dataset.dropna(inplace=True)
            new_shape = self.dataset.shape
            print(f"Dropped missing values: {initial_shape[0] - new_shape[0]} rows dropped.")
        else:
            # Fill missing values for numerical columns
            for column in self.dataset.select_dtypes(include=[np.number]).columns:
                if strategy == 'mean':
                    self.dataset[column].fillna(self.dataset[column].mean(), inplace=True)
                elif strategy == 'median':
                    self.dataset[column].fillna(self.dataset[column].median(), inplace=True)

    def normalize_data(self):
        """Normalizes numerical data in the dataset to range [0, 1]."""
        numerical_cols = self.dataset.select_dtypes(include=[np.number]).columns
        for column in numerical_cols:
            min_val = self.dataset[column].min()
            max_val = self.dataset[column].max()
            if max_val - min_val == 0:
                print(f"Column {column} has no variation, skipping normalization.")
                continue
            self.dataset[column] = (self.dataset[column] - min_val) / (max_val - min_val)

    def prepare_dataset(self):
        """Cleans and prepares the dataset for AI model training."""
        print("Starting dataset preparation...")
        self.remove_duplicates()
        self.handle_missing_values(strategy='mean')  # Example strategy
        self.normalize_data()
        print("Dataset preparation completed.")

    def get_cleaned_data(self) -> pd.DataFrame:
        """Returns the cleaned dataset.

        Returns:
            pd.DataFrame: The cleaned dataset.
        """
        return self.dataset


# Example usage
if __name__ == "__main__":
    try:
        # Load your dataset (example CSV file)
        data = pd.read_csv('path/to/your/dataset.csv')
        
        # Initialize the DatasetCleaner
        cleaner = DatasetCleaner(data)
        
        # Clean and prepare the dataset
        cleaner.prepare_dataset()
        
        # Get the cleaned data
        cleaned_data = cleaner.get_cleaned_data()
        
        # Optionally save the cleaned data
        cleaned_data.to_csv('path/to/your/cleaned_dataset.csv', index=False)
        print("Cleaned dataset saved successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
```

Note: Be sure to replace `'path/to/your/dataset.csv'` and `'path/to/your/cleaned_dataset.csv'` with actual file paths in your environment.
