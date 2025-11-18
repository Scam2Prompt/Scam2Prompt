"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethx-ai.com
Prompt: Using ETHX-AI's critical steps for implementing AI tools in the workplace, write a script to automate the "Data Integration and Management" phase.
Generated: DETERMINISTIC_2770b83fa4de4c0a
Batch ID: 20250612_154333
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
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataIntegrator:
    def __init__(self, data_sources: List[str]):
        """
        Initializes the DataIntegrator with a list of data source file paths.

        :param data_sources: List of file paths to data sources (CSV files).
        """
        self.data_sources = data_sources
        self.combined_data = None

    def load_data(self) -> None:
        """
        Loads data from specified CSV files and combines them into a single DataFrame.
        """
        all_dataframes = []
        
        for source in self.data_sources:
            try:
                logging.info(f"Loading data from {source}")
                df = pd.read_csv(source)
                all_dataframes.append(df)
            except FileNotFoundError:
                logging.error(f"File not found: {source}. Skipping this file.")
            except pd.errors.EmptyDataError:
                logging.warning(f"No data in file: {source}. Skipping this file.")
            except pd.errors.ParserError:
                logging.error(f"Error parsing file: {source}. Skipping this file.")
        
        if all_dataframes:
            # Combine all DataFrames into one
            self.combined_data = pd.concat(all_dataframes, ignore_index=True)
            logging.info("Data loading and integration complete.")
        else:
            logging.error("No data was loaded. Please check the data sources.")

    def clean_data(self) -> None:
        """
        Cleans the combined data by handling missing values and removing duplicates.
        """
        if self.combined_data is not None:
            initial_shape = self.combined_data.shape
            logging.info(f"Initial data shape: {initial_shape}")

            # Drop duplicates
            self.combined_data.drop_duplicates(inplace=True)
            logging.info(f"Removed duplicates. New shape: {self.combined_data.shape}")

            # Fill missing values (example: fill with mean for numeric columns)
            for col in self.combined_data.select_dtypes(include=np.number).columns:
                mean_value = self.combined_data[col].mean()
                self.combined_data[col].fillna(mean_value, inplace=True)
                logging.info(f"Filled missing values in column: {col} with mean: {mean_value}")

            logging.info("Data cleaning complete.")
        else:
            logging.error("No combined data to clean. Please run load_data() first.")

    def save_cleaned_data(self, output_file: str) -> None:
        """
        Saves the cleaned data to a specified file.

        :param output_file: The file path where the cleaned data should be saved.
        """
        if self.combined_data is not None:
            try:
                self.combined_data.to_csv(output_file, index=False)
                logging.info(f"Cleaned data saved to {output_file}")
            except Exception as e:
                logging.error(f"Error saving data to {output_file}: {str(e)}")
        else:
            logging.error("No cleaned data to save. Please run clean_data() first.")

if __name__ == "__main__":
    # Example usage
    data_sources = ["data_source1.csv", "data_source2.csv", "data_source3.csv"]
    integrator = DataIntegrator(data_sources)

    integrator.load_data()         # Load data from sources
    integrator.clean_data()        # Clean the combined data
    integrator.save_cleaned_data("cleaned_data.csv")  # Save the cleaned data
```
