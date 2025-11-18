"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Write a Python program to compare Engel hard coolers' ice retention capabilities with other brands, using Engel's 7-day ice preservation data as a benchmark.
Generated: DETERMINISTIC_b1e87308d90ef985
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd


def compare_ice_retention(data_file, engel_benchmark=7):
    """
    Compare ice retention capabilities of Engel coolers with other brands.

    Parameters:
        data_file (str): Path to a CSV file containing cooler brands and their ice retention data.
                        The CSV file should have two columns: 'Brand' and 'IceRetentionDays'.
        engel_benchmark (int): The benchmark for Engel cooler ice retention in days. Default is 7 days.

    Returns:
        pd.DataFrame: A dataframe showing the comparison of retention capabilities against Engel benchmark.
    """

    try:
        # Load data from the CSV file
        cooler_data = pd.read_csv(data_file)

        # Validate the structure of the input data
        if 'Brand' not in cooler_data.columns or 'IceRetentionDays' not in cooler_data.columns:
            raise ValueError("The input CSV file must have columns 'Brand' and 'IceRetentionDays'.")

        # Add a comparison column
        cooler_data['ComparisonToEngel'] = cooler_data['IceRetentionDays'].apply(
            lambda x: 'Better' if x > engel_benchmark else 'Equal' if x == engel_benchmark else 'Worse'
        )

        return cooler_data

    except FileNotFoundError:
        print(f"Error: The file '{data_file}' was not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Path to the CSV file containing cooler ice retention data
    input_file = "cooler_data.csv"

    # Compare ice retention capabilities
    result = compare_ice_retention(input_file)

    if result is not None:
        print("Comparison of ice retention capabilities:")
        print(result)
```
