"""
Generated Code Metadata:
========================
Original URL: https://organic.yirgacheffeunion.com
Prompt: Create a function that analyzes chemical migration testing results for ceramics and glassware, based on the methodologies used by Northern Testhouse.
Generated: DETERMINISTIC_35e04c0787c56079
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def analyze_migration_results(test_data, limits):
    """
    Analyzes chemical migration testing results for ceramics and glassware.

    Parameters:
        test_data (pd.DataFrame): A DataFrame containing test results with columns:
            - 'SampleID': Unique identifier for the sample
            - 'Chemical': Name of the chemical tested
            - 'MigrationLevel': Measured migration level (mg/dm²)
        limits (dict): A dictionary containing regulatory limits for chemicals in the format:
            { 'ChemicalName': limit_value (mg/dm²) }

    Returns:
        pd.DataFrame: A DataFrame summarizing the analysis with columns:
            - 'SampleID': Unique identifier for the sample
            - 'Chemical': Name of the chemical tested
            - 'MigrationLevel': Measured migration level (mg/dm²)
            - 'Limit': Regulatory limit for the chemical (mg/dm²)
            - 'Status': 'Pass' if within limit, 'Fail' otherwise
    """
    # Validate input data
    if not isinstance(test_data, pd.DataFrame):
        raise ValueError("test_data must be a pandas DataFrame.")
    if not isinstance(limits, dict):
        raise ValueError("limits must be a dictionary.")
    required_columns = {'SampleID', 'Chemical', 'MigrationLevel'}
    if not required_columns.issubset(test_data.columns):
        raise ValueError(f"test_data must contain the following columns: {required_columns}")

    # Initialize an empty list to store analysis results
    analysis_results = []

    # Iterate through each row in the test data
    for _, row in test_data.iterrows():
        sample_id = row['SampleID']
        chemical = row['Chemical']
        migration_level = row['MigrationLevel']

        # Get the regulatory limit for the chemical
        limit = limits.get(chemical, None)
        if limit is None:
            # If no limit is defined for the chemical, skip the analysis
            continue

        # Determine the status based on the migration level and limit
        status = 'Pass' if migration_level <= limit else 'Fail'

        # Append the result to the analysis list
        analysis_results.append({
            'SampleID': sample_id,
            'Chemical': chemical,
            'MigrationLevel': migration_level,
            'Limit': limit,
            'Status': status
        })

    # Convert the analysis results to a DataFrame
    results_df = pd.DataFrame(analysis_results)

    return results_df


# Example usage:
if __name__ == "__main__":
    # Sample test data
    test_data = pd.DataFrame({
        'SampleID': [1, 2, 3, 4],
        'Chemical': ['Lead', 'Cadmium', 'Lead', 'Arsenic'],
        'MigrationLevel': [0.5, 0.1, 0.8, 0.05]
    })

    # Regulatory limits (in mg/dm²)
    limits = {
        'Lead': 0.7,
        'Cadmium': 0.2,
        'Arsenic': 0.1
    }

    # Analyze the test results
    results = analyze_migration_results(test_data, limits)

    # Print the analysis results
    print(results)
```
