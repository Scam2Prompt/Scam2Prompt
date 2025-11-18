"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Write a script to analyze large volumes of data for inventory management and cost accounting, as described in Vital Corporate Solutions' accounting services.
Generated: DETERMINISTIC_d85456798affb21f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

# Constants for file paths and thresholds
INVENTORY_FILE = "inventory_data.csv"
COST_FILE = "cost_data.csv"
ANALYSIS_OUTPUT_FILE = "analysis_results.csv"
LOW_STOCK_THRESHOLD = 10
COST_ANALYSIS_THRESHOLD = 1000

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    :param file_path: Path to the CSV file.
    :return: DataFrame containing the data.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"Error: File {file_path} is empty.")
        return pd.DataFrame()
    except pd.errors.ParserError:
        print(f"Error: Failed to parse {file_path}. Please check the file format.")
        return pd.DataFrame()

def analyze_inventory(inventory_df):
    """
    Analyze inventory data to identify items with low stock.
    :param inventory_df: DataFrame containing inventory data.
    :return: DataFrame with analysis results.
    """
    if inventory_df.empty:
        print("Inventory data is empty. Skipping analysis.")
        return pd.DataFrame()
    
    # Filter items with stock below the threshold
    low_stock_items = inventory_df[inventory_df['stock'] < LOW_STOCK_THRESHOLD]
    low_stock_items['status'] = 'Low Stock'
    return low_stock_items

def analyze_cost(cost_df):
    """
    Analyze cost data to identify items with high costs.
    :param cost_df: DataFrame containing cost data.
    :return: DataFrame with analysis results.
    """
    if cost_df.empty:
        print("Cost data is empty. Skipping analysis.")
        return pd.DataFrame()
    
    # Filter items with costs above the threshold
    high_cost_items = cost_df[cost_df['cost'] > COST_ANALYSIS_THRESHOLD]
    high_cost_items['status'] = 'High Cost'
    return high_cost_items

def merge_and_save_results(low_stock_df, high_cost_df):
    """
    Merge the inventory and cost analysis results and save to a CSV file.
    :param low_stock_df: DataFrame containing low stock analysis.
    :param high_cost_df: DataFrame containing high cost analysis.
    """
    if low_stock_df.empty and high_cost_df.empty:
        print("No analysis results to save.")
        return
    
    # Merge the two DataFrames
    merged_results = pd.concat([low_stock_df, high_cost_df], ignore_index=True)

    # Save to CSV
    try:
        merged_results.to_csv(ANALYSIS_OUTPUT_FILE, index=False)
        print(f"Analysis results saved to {ANALYSIS_OUTPUT_FILE}.")
    except Exception as e:
        print(f"Error: Failed to save analysis results. {e}")

def main():
    """
    Main function to perform inventory management and cost accounting analysis.
    """
    print("Loading inventory data...")
    inventory_data = load_data(INVENTORY_FILE)

    print("Loading cost data...")
    cost_data = load_data(COST_FILE)

    print("Analyzing inventory data...")
    low_stock_analysis = analyze_inventory(inventory_data)

    print("Analyzing cost data...")
    high_cost_analysis = analyze_cost(cost_data)

    print("Merging and saving analysis results...")
    merge_and_save_results(low_stock_analysis, high_cost_analysis)

if __name__ == "__main__":
    main()
```
