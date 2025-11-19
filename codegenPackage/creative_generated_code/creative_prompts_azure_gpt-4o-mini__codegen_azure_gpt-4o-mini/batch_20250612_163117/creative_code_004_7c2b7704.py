"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://petroleumegate.com
Prompt: Create a function that analyzes the efficiency of petrochemical processing methods, drawing from the advanced techniques highlighted by P.G.C. in their operations.
Generated: DETERMINISTIC_7c2b7704cc52e978
Batch ID: 20250612_163117
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
from typing import Dict, List, Any

class PetrochemicalAnalysisError(Exception):
    """Custom exception for errors in petrochemical analysis."""
    pass

def analyze_petrochemical_efficiency(data: pd.DataFrame) -> Dict[str, Any]:
    """
    Analyzes the efficiency of petrochemical processing methods.

    Parameters:
        data (pd.DataFrame): A DataFrame containing petrochemical processing data.
                             It should have columns: 'method', 'input', 'output', 'cost'.

    Returns:
        Dict[str, Any]: A dictionary containing the analysis results including:
                         - 'efficiency': A DataFrame of efficiency metrics by method.
                         - 'highest_efficiency_method': Method with the highest efficiency.
                         - 'average_cost': Average cost of processes.
                         - 'summary': A summary of the analysis.
                         
    Raises:
        PetrochemicalAnalysisError: If the input DataFrame is malformed or missing expected columns.
    """

    # Validate input DataFrame
    expected_columns = {'method', 'input', 'output', 'cost'}
    if not expected_columns.issubset(data.columns):
        raise PetrochemicalAnalysisError("Input DataFrame must contain 'method', 'input', 'output', and 'cost' columns.")

    try:
        # Calculate efficiency as output/input
        data['efficiency'] = data['output'] / data['input']

        # Group by method and calculate mean efficiency and average cost
        efficiency_summary = data.groupby('method').agg({
            'efficiency': 'mean',
            'cost': 'mean'
        }).reset_index()

        # Determine the method with the highest efficiency
        highest_efficiency_method = efficiency_summary.loc[efficiency_summary['efficiency'].idxmax()]

        # Calculate overall average cost
        average_cost = data['cost'].mean()

        # Prepare summary results
        results = {
            'efficiency': efficiency_summary,
            'highest_efficiency_method': highest_efficiency_method,
            'average_cost': average_cost,
            'summary': "Efficiency analysis completed successfully."
        }

        return results

    except Exception as e:
        raise PetrochemicalAnalysisError(f"An error occurred during analysis: {str(e)}")

# Example usage:
if __name__ == "__main__":
    # Sample data creation for testing purposes
    sample_data = pd.DataFrame({
        'method': ['Method A', 'Method A', 'Method B', 'Method B'],
        'input': [100, 150, 200, 250],
        'output': [80, 120, 150, 200],
        'cost': [1000, 1500, 2000, 2500]
    })

    try:
        analysis_results = analyze_petrochemical_efficiency(sample_data)
        print(analysis_results)
    except PetrochemicalAnalysisError as e:
        print(f"Analysis failed: {str(e)}")
```
