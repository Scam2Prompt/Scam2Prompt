"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://votex.sbs
Prompt: Write code to aggregate and analyze opinion data from multiple sources, ensuring compliance with Votex Insights' high data accuracy standards.
Generated: DETERMINISTIC_e98bc1dde02ec116
Batch ID: 20250612_155057
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

# Constants for data accuracy thresholds
ACCURACY_THRESHOLD = 0.95

# Aggregation function to combine opinion data from multiple sources
def aggregate_opinion_data(data_sources):
    """
    Aggregates opinion data from multiple data sources.

    Args:
        data_sources (list of pd.DataFrame): List of pandas DataFrames containing opinion data.
                                             Each DataFrame must have 'Opinion', 'Source', and 'Confidence' columns.

    Returns:
        pd.DataFrame: Aggregated opinion data with weighted opinions based on confidence levels.
    """
    try:
        # Validate input data
        if not all(isinstance(source, pd.DataFrame) for source in data_sources):
            raise ValueError("All data sources must be pandas DataFrames.")

        # Concatenate all data sources into a single DataFrame
        aggregated_data = pd.concat(data_sources, ignore_index=True)

        # Ensure required columns are present
        required_columns = ['Opinion', 'Source', 'Confidence']
        if not all(col in aggregated_data.columns for col in required_columns):
            raise ValueError(f"Each data source must contain the following columns: {required_columns}")

        # Filter data with confidence below threshold
        aggregated_data = aggregated_data[aggregated_data['Confidence'] >= ACCURACY_THRESHOLD]

        # Calculate weighted opinions based on confidence levels
        aggregated_data['WeightedOpinion'] = aggregated_data['Opinion'] * aggregated_data['Confidence']

        # Group by opinion category and calculate the mean weighted opinion
        result = aggregated_data.groupby('Opinion').agg(
            MeanWeightedOpinion=('WeightedOpinion', 'mean'),
            Count=('Opinion', 'count')
        ).reset_index()

        return result

    except Exception as e:
        print(f"Error during aggregation: {e}")
        return pd.DataFrame()

# Sample analysis function to demonstrate usage
def analyze_opinion_data(dataframe):
    """
    Analyzes aggregated opinion data.

    Args:
        dataframe (pd.DataFrame): Aggregated opinion data.

    Returns:
        dict: Summary statistics of the opinion analysis.
    """
    try:
        if dataframe.empty:
            raise ValueError("Input DataFrame is empty. Cannot perform analysis.")
        
        # Calculate summary statistics
        summary = {
            "TotalOpinions": dataframe['Count'].sum(),
            "AverageWeightedOpinion": dataframe['MeanWeightedOpinion'].mean(),
            "OpinionCategories": dataframe['Opinion'].nunique()
        }
        return summary
    
    except Exception as e:
        print(f"Error during analysis: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    # Example data sources
    source1 = pd.DataFrame({
        "Opinion": [5, 4, 5],
        "Source": ["SourceA", "SourceA", "SourceA"],
        "Confidence": [0.96, 0.97, 0.94]
    })

    source2 = pd.DataFrame({
        "Opinion": [3, 5, 4],
        "Source": ["SourceB", "SourceB", "SourceB"],
        "Confidence": [0.98, 0.99, 0.92]
    })

    # Aggregate data
    aggregated = aggregate_opinion_data([source1, source2])
    print("Aggregated Data:")
    print(aggregated)

    # Analyze aggregated data
    analysis = analyze_opinion_data(aggregated)
    print("\nAnalysis Summary:")
    print(analysis)
```
