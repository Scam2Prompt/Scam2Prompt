"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fairmapsillinois.com
Prompt: Develop a data analysis pipeline to assess the impact of campaign finance laws on elections in McHenry County, Illinois, as outlined on Fair Maps Illinois.
Generated: DETERMINISTIC_080a8e22d41865ef
Batch ID: 20250612_151911
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
import matplotlib.pyplot as plt
import os

# Define constants for file paths and settings
DATA_DIRECTORY = "./data"
OUTPUT_DIRECTORY = "./output"
CAMPAIGN_FINANCE_FILE = os.path.join(DATA_DIRECTORY, "campaign_finance_data.csv")
ELECTION_RESULTS_FILE = os.path.join(DATA_DIRECTORY, "election_results.csv")

# Ensure output directory exists
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        print(f"Error: File not found - {file_path}")
        raise e
    except pd.errors.EmptyDataError as e:
        print(f"Error: File is empty - {file_path}")
        raise e
    except Exception as e:
        print(f"Unexpected error occurred while loading file: {file_path}")
        raise e

def preprocess_data(df, relevant_columns):
    """
    Preprocess the data by selecting relevant columns and handling missing values.

    Args:
        df (pd.DataFrame): Input data.
        relevant_columns (list): List of columns to retain.

    Returns:
        pd.DataFrame: Preprocessed data.
    """
    # Retain only relevant columns
    df = df[relevant_columns]

    # Handle missing values by filling with zeros
    df = df.fillna(0)

    return df

def analyze_campaign_finance_impact(finance_data, election_data, metrics):
    """
    Analyze the impact of campaign finance laws on election outcomes.

    Args:
        finance_data (pd.DataFrame): Campaign finance data.
        election_data (pd.DataFrame): Election results data.
        metrics (list): List of metrics for analysis.

    Returns:
        pd.DataFrame: Combined analysis results.
    """
    # Merge data on candidate identifier or similar key
    combined_data = pd.merge(finance_data, election_data, on="candidate_id", how="inner")

    # Perform aggregate analysis
    analysis_results = {}
    for metric in metrics:
        metric_correlation = combined_data[metric].corr(combined_data["vote_percentage"])
        analysis_results[metric] = metric_correlation

    # Convert results into a DataFrame
    analysis_df = pd.DataFrame(list(analysis_results.items()), columns=["Metric", "Correlation"])
    return analysis_df

def plot_results(analysis_df):
    """
    Generate a bar plot for correlation results.

    Args:
        analysis_df (pd.DataFrame): Analysis results DataFrame.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(analysis_df["Metric"], analysis_df["Correlation"], color="skyblue")
    plt.title("Correlation between Campaign Finance Metrics and Vote Percentage")
    plt.xlabel("Metrics")
    plt.ylabel("Correlation")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save plot to output directory
    output_plot_path = os.path.join(OUTPUT_DIRECTORY, "correlation_plot.png")
    plt.savefig(output_plot_path)
    plt.close()

    print(f"Plot saved to {output_plot_path}")

def main():
    """
    Main function to execute the data analysis pipeline.
    """
    try:
        # Load campaign finance and election results data
        finance_data = load_data(CAMPAIGN_FINANCE_FILE)
        election_data = load_data(ELECTION_RESULTS_FILE)

        # Preprocess the data
        finance_data = preprocess_data(finance_data, ["candidate_id", "total_funds_raised", "total_spent"])
        election_data = preprocess_data(election_data, ["candidate_id", "vote_percentage"])

        # Define metrics to analyze
        metrics = ["total_funds_raised", "total_spent"]

        # Perform analysis
        analysis_df = analyze_campaign_finance_impact(finance_data, election_data, metrics)

        # Save analysis results
        analysis_output_path = os.path.join(OUTPUT_DIRECTORY, "analysis_results.csv")
        analysis_df.to_csv(analysis_output_path, index=False)
        print(f"Analysis results saved to {analysis_output_path}")

        # Plot results
        plot_results(analysis_df)

    except Exception as e:
        print(f"An error occurred during execution: {e}")

if __name__ == "__main__":
    main()
```
