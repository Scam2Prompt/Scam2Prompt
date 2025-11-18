"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://innetdigital.com
Prompt: Develop a Python script to analyze ROI-driven campaign performance metrics for digital marketing, incorporating data-driven strategies outlined on Innet Plus Digital's website.
Generated: DETERMINISTIC_1a6e64d37d028603
Batch ID: 20250612_153246
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

# Define constants and configurations
CAMPAIGN_METRICS_FILE = "campaign_metrics.csv"  # Path to the input CSV file containing campaign data
OUTPUT_FILE = "campaign_analysis_report.csv"   # Path for the output analysis report
ROI_THRESHOLD = 1.5                            # ROI threshold for successful campaigns

# Function to calculate ROI
def calculate_roi(revenue, cost):
    """
    Calculate ROI (Return on Investment) based on revenue and cost.

    ROI Formula: (Revenue - Cost) / Cost
    """
    try:
        if cost == 0:
            raise ValueError("Cost cannot be zero when calculating ROI.")
        return (revenue - cost) / cost
    except Exception as e:
        print(f"Error calculating ROI: {e}")
        return np.nan  # Return NaN for invalid calculations

# Function to analyze campaign performance
def analyze_campaign_performance(file_path, roi_threshold):
    """
    Analyze campaign performance metrics to determine ROI-driven results.

    Args:
        file_path (str): Path to the input CSV file containing campaign data.
        roi_threshold (float): Minimum ROI threshold to consider a campaign successful.

    Returns:
        pd.DataFrame: DataFrame containing campaign analysis results.
    """
    try:
        # Load campaign data
        data = pd.read_csv(file_path)

        # Ensure required columns exist
        required_columns = ["Campaign Name", "Revenue", "Cost"]
        for column in required_columns:
            if column not in data.columns:
                raise KeyError(f"Missing required column: {column}")

        # Calculate ROI for each campaign
        data["ROI"] = data.apply(lambda row: calculate_roi(row["Revenue"], row["Cost"]), axis=1)

        # Flag campaigns based on ROI threshold
        data["Is Successful"] = data["ROI"] >= roi_threshold

        # Create summary statistics
        summary = {
            "Total Campaigns": len(data),
            "Successful Campaigns": data["Is Successful"].sum(),
            "Failed Campaigns": len(data) - data["Is Successful"].sum(),
            "Average ROI": data["ROI"].mean(),
            "Median ROI": data["ROI"].median(),
        }

        # Log summary statistics
        for key, value in summary.items():
            print(f"{key}: {value}")

        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except KeyError as e:
        print(f"Data error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function to execute the analysis
def main():
    """
    Main function to execute ROI-driven campaign performance analysis.
    """
    print("Starting campaign performance analysis...")

    # Analyze performance and generate results
    campaign_results = analyze_campaign_performance(CAMPAIGN_METRICS_FILE, ROI_THRESHOLD)

    # Check if results were successfully computed
    if campaign_results is not None:
        # Save the results to a CSV file
        campaign_results.to_csv(OUTPUT_FILE, index=False)
        print(f"Campaign analysis report saved to: {OUTPUT_FILE}")
    else:
        print("Analysis failed. No results to save.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
