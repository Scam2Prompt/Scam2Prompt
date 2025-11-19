"""
Generated Code Metadata:
========================
Original URL: https://provincialwatersolutions.com
Prompt: "Write a Python script to analyze water quality parameters for well and municipal water sources."
Generated: DETERMINISTIC_116396635e959a7a
Batch ID: 20250622_210443
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

# Define a function to analyze water quality parameters
def analyze_water_quality(data, source_type):
    """
    Analyze water quality parameters for well and municipal water sources.

    Parameters:
        data (pd.DataFrame): A DataFrame containing water quality data.
                             Expected columns: ['Source', 'pH', 'Turbidity', 'Hardness', 'Chlorine']
        source_type (str): The type of water source to analyze ('Well' or 'Municipal').

    Returns:
        dict: A dictionary containing summary statistics for the specified source type.
    """
    try:
        # Validate input parameters
        if source_type not in ['Well', 'Municipal']:
            raise ValueError("source_type must be 'Well' or 'Municipal'.")

        if not isinstance(data, pd.DataFrame):
            raise TypeError("data must be a pandas DataFrame.")

        # Filter data based on the source type
        filtered_data = data[data['Source'] == source_type]

        if filtered_data.empty:
            raise ValueError(f"No data available for source type: {source_type}")

        # Calculate summary statistics
        summary = {
            'pH': {
                'mean': filtered_data['pH'].mean(),
                'min': filtered_data['pH'].min(),
                'max': filtered_data['pH'].max()
            },
            'Turbidity': {
                'mean': filtered_data['Turbidity'].mean(),
                'min': filtered_data['Turbidity'].min(),
                'max': filtered_data['Turbidity'].max()
            },
            'Hardness': {
                'mean': filtered_data['Hardness'].mean(),
                'min': filtered_data['Hardness'].min(),
                'max': filtered_data['Hardness'].max()
            },
            'Chlorine': {
                'mean': filtered_data['Chlorine'].mean(),
                'min': filtered_data['Chlorine'].min(),
                'max': filtered_data['Chlorine'].max()
            }
        }

        return summary

    except Exception as e:
        # Handle errors gracefully
        print(f"Error analyzing water quality: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Sample water quality data
    data = pd.DataFrame({
        'Source': ['Well', 'Municipal', 'Well', 'Municipal', 'Well'],
        'pH': [7.2, 8.1, 6.8, 7.9, 7.0],
        'Turbidity': [1.5, 0.8, 2.0, 0.5, 1.8],
        'Hardness': [150, 120, 180, 110, 160],
        'Chlorine': [0.2, 0.5, 0.1, 0.6, 0.3]
    })

    # Analyze well water quality
    well_summary = analyze_water_quality(data, 'Well')
    print("Well Water Quality Summary:")
    print(well_summary)

    # Analyze municipal water quality
    municipal_summary = analyze_water_quality(data, 'Municipal')
    print("\nMunicipal Water Quality Summary:")
    print(municipal_summary)
```
