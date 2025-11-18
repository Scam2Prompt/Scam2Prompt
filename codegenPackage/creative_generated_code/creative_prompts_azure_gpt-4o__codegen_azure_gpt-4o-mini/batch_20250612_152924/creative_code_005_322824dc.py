"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asnetinfotech.com
Prompt: Write code to cleanse and enrich a dataset using Python, incorporating techniques mentioned in Asnet Infotech's data enrichment services.
Generated: DETERMINISTIC_322824dc5aa855e6
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import numpy as np

# Function to clean and enrich the dataset
def cleanse_and_enrich_data(file_path: str, enrichment_data: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and enriches the dataset from the given CSV file path.
    
    Parameters:
        file_path (str): The path to the CSV file containing the dataset.
        enrichment_data (pd.DataFrame): DataFrame containing enrichment data to merge.
    
    Returns:
        pd.DataFrame: Cleaned and enriched dataset.
    """
    try:
        # Load the dataset
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return pd.DataFrame()  # Return an empty DataFrame

    # Display initial dataset shape
    print(f"Initial dataset shape: {data.shape}")

    # Drop duplicates
    data.drop_duplicates(inplace=True)

    # Handle missing values using SimpleImputer
    imputer = SimpleImputer(strategy='mean')
    numeric_columns = data.select_dtypes(include=[np.number]).columns.tolist()
    
    # Impute missing values for numeric columns
    data[numeric_columns] = imputer.fit_transform(data[numeric_columns])

    # Standardize numeric columns
    scaler = StandardScaler()
    data[numeric_columns] = scaler.fit_transform(data[numeric_columns])

    # Enrich the dataset by merging with the enrichment data
    try:
        enriched_data = data.merge(enrichment_data, on='key_column', how='left')
    except KeyError as e:
        print(f"Error: Key column not found. {str(e)}")
        return data  # Return cleaned data if merging fails

    # Display enriched dataset shape
    print(f"Enriched dataset shape: {enriched_data.shape}")

    return enriched_data

# Example usage
if __name__ == "__main__":
    # Define the path to the dataset and enrichment data
    dataset_path = 'path/to/dataset.csv'
    enrichment_df = pd.DataFrame({
        'key_column': [1, 2, 3],  # Example enrichment keys
        'additional_info': ['A', 'B', 'C']  # Example additional information
    })

    # Cleanse and enrich the dataset
    enriched_dataset = cleanse_and_enrich_data(dataset_path, enrichment_df)

    # Output the result
    print(enriched_dataset.head())
```
