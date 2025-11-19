"""
Generated Code Metadata:
========================
Original URL: https://get-link.io
Prompt: How does the study on U.S. universities driving regional innovation, as conducted by MIT, highlight the importance of universities in attracting inventors and contributing to the economy?
Generated: DETERMINISTIC_bb4a70a62dc185bd
Batch ID: 20250622_212137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np

# Define a function to analyze the impact of universities on regional innovation
def analyze_university_impact(university_data, inventor_data):
    """
    Analyze the impact of universities on regional innovation.

    Parameters:
    university_data (pd.DataFrame): Data containing information about universities.
    inventor_data (pd.DataFrame): Data containing information about inventors.

    Returns:
    pd.DataFrame: A DataFrame containing the analysis results.
    """

    # Check if input data is valid
    if not isinstance(university_data, pd.DataFrame) or not isinstance(inventor_data, pd.DataFrame):
        raise ValueError("Invalid input data. Both university_data and inventor_data must be DataFrames.")

    # Merge university and inventor data based on location
    try:
        merged_data = pd.merge(university_data, inventor_data, on='location')
    except KeyError:
        raise ValueError("Invalid input data. Both DataFrames must have a 'location' column.")

    # Calculate the number of inventors attracted to each university
    inventors_per_university = merged_data.groupby('university_id')['inventor_id'].count().reset_index()
    inventors_per_university.columns = ['university_id', 'num_inventors']

    # Calculate the economic impact of each university
    economic_impact = merged_data.groupby('university_id')['economic_contribution'].sum().reset_index()

    # Merge the number of inventors and economic impact data
    university_impact = pd.merge(inventors_per_university, economic_impact, on='university_id')

    return university_impact

# Example usage
if __name__ == "__main__":
    # Sample university data
    university_data = pd.DataFrame({
        'university_id': [1, 2, 3],
        'location': ['New York', 'Los Angeles', 'Chicago'],
        'economic_contribution': [1000000, 2000000, 3000000]
    })

    # Sample inventor data
    inventor_data = pd.DataFrame({
        'inventor_id': [101, 102, 103, 104, 105],
        'location': ['New York', 'New York', 'Los Angeles', 'Chicago', 'Chicago'],
        'university_id': [1, 1, 2, 3, 3]
    })

    try:
        # Analyze the impact of universities on regional innovation
        university_impact = analyze_university_impact(university_data, inventor_data)
        print(university_impact)
    except Exception as e:
        print(f"An error occurred: {e}")
```
