"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: Create a Python script that analyzes the effectiveness of promotional campaigns, similar to the services offered by NMKT for small and medium enterprises.
Generated: DETERMINISTIC_04f5ac9017d42679
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
import numpy as np
from datetime import datetime
import logging

# Configure logging for error handling and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_data(file_path):
    """
    Load campaign data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the campaign data.
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully.")
        return data
    except FileNotFoundError:
        logging.error("File not found. Please check the file path.")
        raise
    except pd.errors.EmptyDataError:
        logging.error("File is empty. Please provide a valid CSV file.")
        raise
    except Exception as e:
        logging.error(f"An error occurred while loading the data: {e}")
        raise

def preprocess_data(data):
    """
    Preprocess the campaign data.

    Args:
        data (pd.DataFrame): Raw campaign data.

    Returns:
        pd.DataFrame: Preprocessed campaign data.
    """
    try:
        # Ensure required columns exist
        required_columns = ['CampaignName', 'StartDate', 'EndDate', 'Cost', 'Revenue']
        for col in required_columns:
            if col not in data.columns:
                raise ValueError(f"Missing required column: {col}")

        # Convert date columns to datetime
        data['StartDate'] = pd.to_datetime(data['StartDate'], errors='coerce')
        data['EndDate'] = pd.to_datetime(data['EndDate'], errors='coerce')

        # Drop rows with invalid dates
        data = data.dropna(subset=['StartDate', 'EndDate'])

        # Calculate campaign duration in days
        data['DurationDays'] = (data['EndDate'] - data['StartDate']).dt.days

        # Drop rows with negative or zero duration
        data = data[data['DurationDays'] > 0]

        # Fill missing cost and revenue values with 0
        data['Cost'] = data['Cost'].fillna(0)
        data['Revenue'] = data['Revenue'].fillna(0)

        logging.info("Data preprocessing completed successfully.")
        return data
    except Exception as e:
        logging.error(f"An error occurred during preprocessing: {e}")
        raise

def analyze_campaigns(data):
    """
    Analyze the effectiveness of promotional campaigns.

    Args:
        data (pd.DataFrame): Preprocessed campaign data.

    Returns:
        pd.DataFrame: DataFrame containing analysis results.
    """
    try:
        # Calculate ROI (Return on Investment)
        data['ROI'] = np.where(data['Cost'] > 0, (data['Revenue'] - data['Cost']) / data['Cost'], np.nan)

        # Categorize campaigns based on ROI
        data['Effectiveness'] = pd.cut(
            data['ROI'],
            bins=[-np.inf, 0, 0.5, 1, np.inf],
            labels=['Loss', 'Low', 'Moderate', 'High']
        )

        # Aggregate results
        summary = data.groupby('Effectiveness').agg(
            TotalCampaigns=('CampaignName', 'count'),
            AvgROI=('ROI', 'mean'),
            TotalRevenue=('Revenue', 'sum'),
            TotalCost=('Cost', 'sum')
        ).reset_index()

        logging.info("Campaign analysis completed successfully.")
        return summary
    except Exception as e:
        logging.error(f"An error occurred during analysis: {e}")
        raise

def save_results(summary, output_path):
    """
    Save the analysis results to a CSV file.

    Args:
        summary (pd.DataFrame): DataFrame containing analysis results.
        output_path (str): Path to save the CSV file.

    Returns:
        None
    """
    try:
        summary.to_csv(output_path, index=False)
        logging.info(f"Results saved successfully to {output_path}.")
    except Exception as e:
        logging.error(f"An error occurred while saving the results: {e}")
        raise

def main():
    """
    Main function to execute the campaign analysis workflow.
    """
    try:
        # File paths
        input_file = 'campaign_data.csv'  # Replace with your input file path
        output_file = 'campaign_analysis_results.csv'  # Replace with your output file path

        # Load, preprocess, analyze, and save results
        data = load_data(input_file)
        preprocessed_data = preprocess_data(data)
        analysis_results = analyze_campaigns(preprocessed_data)
        save_results(analysis_results, output_file)

        logging.info("Campaign analysis workflow completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred in the main workflow: {e}")

if __name__ == "__main__":
    main()
```
