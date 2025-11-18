"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.hu
Prompt: Create a program that uses Initia Capital's investment criteria to filter a dataset of companies based on organic growth capability, leadership talent, and market expansion potential.
Generated: DETERMINISTIC_a87d7c5da5c2b6c5
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Define the investment criteria as constants
ORGANIC_GROWTH_THRESHOLD = 75  # e.g., percentage score for organic growth capability
LEADERSHIP_TALENT_THRESHOLD = 80  # e.g., percentage score for leadership talent
MARKET_EXPANSION_THRESHOLD = 70  # e.g., percentage score for market expansion potential

def filter_companies(dataset_path, output_path):
    """
    Filters a dataset of companies based on Initia Capital's investment criteria.

    Args:
        dataset_path (str): Path to the input CSV file containing the dataset.
        output_path (str): Path to save the filtered dataset as a CSV file.

    Returns:
        None
    """
    try:
        # Load the dataset
        companies = pd.read_csv(dataset_path)

        # Ensure required columns are present in the dataset
        required_columns = ['Company Name', 'Organic Growth Score', 'Leadership Talent Score', 'Market Expansion Score']
        for column in required_columns:
            if column not in companies.columns:
                raise ValueError(f"Missing required column: {column}")

        # Apply filters based on investment criteria
        filtered_companies = companies[
            (companies['Organic Growth Score'] >= ORGANIC_GROWTH_THRESHOLD) &
            (companies['Leadership Talent Score'] >= LEADERSHIP_TALENT_THRESHOLD) &
            (companies['Market Expansion Score'] >= MARKET_EXPANSION_THRESHOLD)
        ]

        # Save the filtered dataset to a new CSV file
        filtered_companies.to_csv(output_path, index=False)
        print(f"Filtered dataset saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: File not found at path '{dataset_path}'")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# Provide the path to the dataset and the path for the output file
input_file = "companies_dataset.csv"  # Replace with actual dataset path
output_file = "filtered_companies.csv"  # Replace with actual output file path
filter_companies(input_file, output_file)
```
