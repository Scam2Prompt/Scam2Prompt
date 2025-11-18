"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mieconline.com
Prompt: Create a Python script to analyze the effectiveness of Certified Financial Analyst Training (CFAT) programs, incorporating metrics for learner progress and outcomes.
Generated: DETERMINISTIC_270ab0b9a1c1dcd6
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define constants for the analysis
DATA_FILE = "cfat_program_data.csv"  # Path to the CSV file containing program data
OUTPUT_FILE = "cfat_analysis_results.csv"  # Output file for summary results
PLOT_FILE = "cfat_performance_plot.png"  # File to save the performance plot

def load_data(file_path):
    """
    Load CFAT program data from a CSV file.

    Parameters:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def calculate_metrics(data):
    """
    Calculate learner progress and effectiveness metrics.

    Parameters:
        data (pd.DataFrame): DataFrame containing CFAT program data.

    Returns:
        dict: Dictionary with calculated metrics.
    """
    try:
        metrics = {}
        metrics["average_pre_score"] = data["Pre_Score"].mean()
        metrics["average_post_score"] = data["Post_Score"].mean()
        metrics["average_progress"] = (data["Post_Score"] - data["Pre_Score"]).mean()
        metrics["completion_rate"] = (data["Completed"] == 1).mean() * 100
        return metrics
    except KeyError as e:
        print(f"Error: Missing column in data - {e}")
        return {}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {}

def save_summary_results(metrics, file_path):
    """
    Save calculated metrics to a CSV file.

    Parameters:
        metrics (dict): Dictionary containing calculated metrics.
        file_path (str): Path to the output CSV file.
    """
    try:
        results_df = pd.DataFrame([metrics])
        results_df.to_csv(file_path, index=False)
        print(f"Summary results saved to {file_path}")
    except Exception as e:
        print(f"Error while saving summary results: {e}")

def visualize_progress(data, plot_path):
    """
    Visualize learner progress with a scatter plot.

    Parameters:
        data (pd.DataFrame): DataFrame containing CFAT program data.
        plot_path (str): Path to save the plot image.
    """
    try:
        plt.figure(figsize=(8, 6))
        plt.scatter(data["Pre_Score"], data["Post_Score"], alpha=0.7, label="Learner Progress")
        plt.plot([0, 100], [0, 100], color="red", linestyle="--", label="No Progress Line")
        plt.title("Learner Progress: Pre-Score vs Post-Score")
        plt.xlabel("Pre-Training Score")
        plt.ylabel("Post-Training Score")
        plt.legend()
        plt.grid(True)
        plt.savefig(plot_path)
        print(f"Performance plot saved to {plot_path}")
    except KeyError as e:
        print(f"Error: Missing column in data - {e}")
    except Exception as e:
        print(f"An unexpected error occurred while visualizing progress: {e}")

def main():
    """
    Main function to orchestrate the analysis of CFAT program effectiveness.
    """
    print("Loading data...")
    data = load_data(DATA_FILE)
    if data is None:  # Exit if data loading failed
        return

    print("Calculating metrics...")
    metrics = calculate_metrics(data)
    if not metrics:  # Exit if calculation failed
        return

    print("Saving summary results...")
    save_summary_results(metrics, OUTPUT_FILE)

    print("Visualizing learner progress...")
    visualize_progress(data, PLOT_FILE)

    print("Analysis completed successfully.")

if __name__ == "__main__":
    main()
```
