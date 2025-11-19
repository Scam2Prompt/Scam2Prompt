"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Write a Python script to analyze marketing campaign data and generate performance reports, similar to the analytics services offered by IDEX Marketing.
Generated: DETERMINISTIC_d66292d1b8083315
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import os

# Define constants for file paths
DATA_FILE = "marketing_campaign_data.csv"
REPORT_FOLDER = "reports"

# Ensure the reports folder exists
os.makedirs(REPORT_FOLDER, exist_ok=True)

def load_data(file_path):
    """
    Load marketing campaign data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded data as a Pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred while loading data: {e}")
        return None

def analyze_data(data):
    """
    Analyze marketing campaign data and generate key performance metrics.
    
    Args:
        data (pd.DataFrame): Marketing campaign data.
    
    Returns:
        dict: Dictionary containing performance metrics.
    """
    try:
        metrics = {}
        metrics['total_campaigns'] = len(data)
        metrics['total_revenue'] = data['Revenue'].sum()
        metrics['average_revenue_per_campaign'] = data['Revenue'].mean()
        metrics['successful_campaigns'] = len(data[data['Success'] == True])
        metrics['success_rate'] = (metrics['successful_campaigns'] / metrics['total_campaigns']) * 100
        return metrics
    except KeyError as e:
        print(f"Error: Missing expected column in data: {e}")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred during analysis: {e}")
        return None

def generate_report(metrics, output_folder):
    """
    Generate a performance report based on the analyzed metrics.
    
    Args:
        metrics (dict): Dictionary containing performance metrics.
        output_folder (str): Folder to save the report.
    """
    try:
        report_file = os.path.join(output_folder, "performance_report.txt")
        with open(report_file, "w") as file:
            file.write("Marketing Campaign Performance Report\n")
            file.write("=" * 40 + "\n")
            file.write(f"Total Campaigns: {metrics['total_campaigns']}\n")
            file.write(f"Total Revenue: ${metrics['total_revenue']:.2f}\n")
            file.write(f"Average Revenue per Campaign: ${metrics['average_revenue_per_campaign']:.2f}\n")
            file.write(f"Successful Campaigns: {metrics['successful_campaigns']}\n")
            file.write(f"Success Rate: {metrics['success_rate']:.2f}%\n")
        print(f"Report generated successfully: {report_file}")
    except Exception as e:
        print(f"Error: Failed to generate report: {e}")

def plot_data(data, output_folder):
    """
    Generate a bar chart for campaign revenue and save it as an image.
    
    Args:
        data (pd.DataFrame): Marketing campaign data.
        output_folder (str): Folder to save the plot.
    """
    try:
        plt.figure(figsize=(10, 6))
        plt.bar(data['Campaign'], data['Revenue'], color='skyblue')
        plt.title("Campaign Revenue")
        plt.xlabel("Campaign")
        plt.ylabel("Revenue ($)")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plot_file = os.path.join(output_folder, "campaign_revenue.png")
        plt.savefig(plot_file)
        plt.close()
        print(f"Plot saved successfully: {plot_file}")
    except KeyError as e:
        print(f"Error: Missing expected column in data: {e}")
    except Exception as e:
        print(f"Error: Failed to generate plot: {e}")

def main():
    """
    Main function to execute the script workflow.
    """
    print("Loading data...")
    data = load_data(DATA_FILE)
    if data is None:
        return
    
    print("Analyzing data...")
    metrics = analyze_data(data)
    if metrics is None:
        return
    
    print("Generating report...")
    generate_report(metrics, REPORT_FOLDER)
    
    print("Generating plot...")
    plot_data(data, REPORT_FOLDER)

if __name__ == "__main__":
    main()
```
