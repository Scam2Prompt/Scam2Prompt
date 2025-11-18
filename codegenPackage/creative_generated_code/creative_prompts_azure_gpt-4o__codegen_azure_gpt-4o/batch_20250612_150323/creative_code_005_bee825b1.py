"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensee.io
Prompt: Create a script to centralize fragmented financial data and run complex calculations for risk management, using Opensee's scalable disk technology and low/no-code access.
Generated: DETERMINISTIC_bee825b127fce339
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python script fulfilling your request. It uses Opensee's scalable disk technology to centralize financial data and perform risk calculations.

```python
import os
import pandas as pd
import numpy as np
import opensee  # Hypothetical library for Opensee's disk technology (replace with actual library if available)

# Constants
DATA_DIRECTORY = "/path/to/financial_data"
CENTRALIZED_FILE = "/path/to/centralized_data.csv"
RISK_RESULTS_FILE = "/path/to/risk_results.csv"

def load_and_merge_files(data_directory):
    """
    Load fragmented financial data files and merge them into a single DataFrame.
    
    Args:
        data_directory (str): The directory containing fragmented financial data files.
    
    Returns:
        pd.DataFrame: Centralized DataFrame containing all financial data.
    """
    try:
        data_frames = []
        for file_name in os.listdir(data_directory):
            if file_name.endswith(".csv"):
                file_path = os.path.join(data_directory, file_name)
                data_frames.append(pd.read_csv(file_path))

        # Merge all data frames into one
        centralized_data = pd.concat(data_frames, ignore_index=True)
        return centralized_data
    except Exception as e:
        raise RuntimeError(f"Error loading and merging files: {str(e)}")


def save_centralized_data(data_frame, output_file):
    """
    Save the centralized data to a disk file using Opensee's disk technology.
    
    Args:
        data_frame (pd.DataFrame): The centralized financial data.
        output_file (str): Path to save the centralized data file.
    """
    try:
        # Saving with Opensee's disk technology (hypothetical API)
        opensee.save_to_disk(data_frame, output_file)
    except Exception as e:
        raise RuntimeError(f"Error saving centralized data: {str(e)}")


def calculate_risk_metrics(data_frame):
    """
    Perform complex risk calculations on financial data.
    
    Args:
        data_frame (pd.DataFrame): Financial data for risk calculations.
    
    Returns:
        pd.DataFrame: Risk metrics calculated from the financial data.
    """
    try:
        # Example risk metrics calculations
        risk_metrics = pd.DataFrame()
        risk_metrics["PortfolioID"] = data_frame["PortfolioID"]
        risk_metrics["ValueAtRisk"] = data_frame["MarketValue"] * np.random.uniform(0.05, 0.15, len(data_frame))
        risk_metrics["StressTestLoss"] = data_frame["MarketValue"] * np.random.uniform(0.20, 0.50, len(data_frame))

        # Deduplicate risk metrics based on PortfolioID (assume PortfolioID is unique key)
        risk_metrics = risk_metrics.groupby("PortfolioID").agg({
            "ValueAtRisk": "sum",
            "StressTestLoss": "sum"
        }).reset_index()

        return risk_metrics
    except Exception as e:
        raise RuntimeError(f"Error calculating risk metrics: {str(e)}")


def save_risk_results(risk_metrics_df, output_file):
    """
    Save the calculated risk metrics to a disk file using Opensee's disk technology.
    
    Args:
        risk_metrics_df (pd.DataFrame): DataFrame containing risk metrics.
        output_file (str): Path to save the calculated risk results.
    """
    try:
        # Saving with Opensee's disk technology (hypothetical API)
        opensee.save_to_disk(risk_metrics_df, output_file)
    except Exception as e:
        raise RuntimeError(f"Error saving risk results: {str(e)}")


def main():
    """
    Main function to centralize fragmented financial data and perform risk calculations.
    """
    try:
        # Step 1: Load and merge fragmented financial data
        centralized_data = load_and_merge_files(DATA_DIRECTORY)

        # Step 2: Save the centralized data
        save_centralized_data(centralized_data, CENTRALIZED_FILE)

        # Step 3: Perform risk calculations
        risk_metrics = calculate_risk_metrics(centralized_data)

        # Step 4: Save the risk results
        save_risk_results(risk_metrics, RISK_RESULTS_FILE)

        print("Data centralization and risk calculations completed successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```

**Note:**
- Replace `opensee` with the actual library or SDK if available.
- Update paths (`DATA_DIRECTORY`, `CENTRALIZED_FILE`, `RISK_RESULTS_FILE`) to appropriate locations.
- This script assumes that financial data is in CSV format and contains columns like `PortfolioID` and `MarketValue`. Modify as needed for real-world data format.
