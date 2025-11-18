"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateflow.co
Prompt: Write a script to analyze the geographic diversification of an investment portfolio, leveraging the strategies for global investments outlined on Petrolio Italiano.
Generated: DETERMINISTIC_4344dac87b5b21cc
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to analyze the geographic diversification of an investment portfolio.
Uses global investment strategies as outlined on Petrolio Italiano's framework.

This script reads portfolio data, calculates diversification metrics, and generates
a report showing geographic exposure of investments.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import pandas as pd
import os

# Constants
INPUT_FILE = 'portfolio_data.csv'  # Path to the portfolio data file
OUTPUT_FILE = 'geo_diversification_report.csv'  # Path to save the diversification report
SUPPORTED_REGIONS = ['North America', 'Europe', 'Asia', 'South America', 'Africa', 'Oceania']  # Predefined global regions

def load_portfolio_data(file_path):
    """
    Loads portfolio data from a CSV file.

    Args:
        file_path (str): Path to the portfolio data file.

    Returns:
        pd.DataFrame: Portfolio data loaded into a Pandas DataFrame.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the data cannot be correctly parsed.
    """
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        portfolio_df = pd.read_csv(file_path)
        if 'Region' not in portfolio_df.columns or 'Investment' not in portfolio_df.columns:
            raise ValueError("File must contain 'Region' and 'Investment' columns.")
        return portfolio_df
    except Exception as e:
        print(f"Error loading portfolio data: {e}")
        raise

def validate_regions(portfolio_df):
    """
    Validates that the portfolio contains only supported regions.

    Args:
        portfolio_df (pd.DataFrame): Portfolio data.

    Returns:
        pd.DataFrame: Portfolio data filtered to contain only supported regions.
    """
    unsupported_regions = set(portfolio_df['Region']) - set(SUPPORTED_REGIONS)
    if unsupported_regions:
        print(f"Warning: Unsupported regions found in portfolio data: {unsupported_regions}")
    return portfolio_df[portfolio_df['Region'].isin(SUPPORTED_REGIONS)]

def calculate_diversification(portfolio_df):
    """
    Calculates geographic diversification for the portfolio.

    Args:
        portfolio_df (pd.DataFrame): Portfolio data.

    Returns:
        pd.DataFrame: Data summarizing diversification by region.
    """
    return portfolio_df.groupby('Region')['Investment'].sum().reset_index()

def save_diversification_report(report_df, output_file):
    """
    Saves the geographic diversification report to a CSV file.

    Args:
        report_df (pd.DataFrame): Report data summarizing diversification by region.
        output_file (str): Path to the output file.

    Raises:
        IOError: If saving fails.
    """
    try:
        report_df.to_csv(output_file, index=False)
        print(f"Report saved successfully to {output_file}")
    except Exception as e:
        print(f"Error saving report: {e}")
        raise

def main():
    """
    Main function to execute the portfolio diversification analysis workflow.
    """
    try:
        # Load portfolio data
        portfolio_data = load_portfolio_data(INPUT_FILE)
        
        # Validate regions
        portfolio_data = validate_regions(portfolio_data)
        
        # Calculate diversification
        diversification_report = calculate_diversification(portfolio_data)
        
        # Save report
        save_diversification_report(diversification_report, OUTPUT_FILE)
    except Exception as e:
        print(f"An error occurred during execution: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
