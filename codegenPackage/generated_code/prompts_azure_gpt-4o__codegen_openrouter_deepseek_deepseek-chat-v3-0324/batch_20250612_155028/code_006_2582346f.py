"""
Generated Code Metadata:
========================
Original URL: https://1inch-docs.vercel.app
Prompt: Write a Python script to query Dune Analytics for data related to the 1inch Aggregation Protocol V5 and visualize swap transaction metrics.
Generated: DETERMINISTIC_2582346f107ba8ce
Batch ID: 20250612_155028
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dune.com/api/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Configuration
DUNE_API_KEY = "your_dune_api_key"  # Replace with your Dune Analytics API key
QUERY_ID = "your_query_id"  # Replace with your Dune query ID
BASE_URL = "https://api.dune.com/api/v1"

# Headers for Dune API
headers = {
    "x-dune-api-key": DUNE_API_KEY,
    "Content-Type": "application/json"
}

def execute_dune_query(query_id):
    """
    Execute a Dune Analytics query and return the execution ID.
    
    Args:
        query_id (str): The ID of the query to execute.
        
    Returns:
        str: Execution ID for the query.
    """
    try:
        url = f"{BASE_URL}/query/{query_id}/execute"
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()["execution_id"]
    except requests.exceptions.RequestException as e:
        print(f"Error executing query: {e}")
        return None

def get_query_results(execution_id):
    """
    Retrieve results from a Dune Analytics query execution.
    
    Args:
        execution_id (str): The execution ID of the query.
        
    Returns:
        dict: Query results in JSON format.
    """
    try:
        url = f"{BASE_URL}/execution/{execution_id}/results"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching query results: {e}")
        return None

def process_data(results):
    """
    Process raw query results into a pandas DataFrame.
    
    Args:
        results (dict): Raw query results from Dune API.
        
    Returns:
        pd.DataFrame: Processed data.
    """
    try:
        if not results or "result" not in results or "rows" not in results["result"]:
            raise ValueError("Invalid or empty results data")
            
        df = pd.DataFrame(results["result"]["rows"])
        
        # Convert timestamp to datetime if present
        if "timestamp" in df.columns:
            df["timestamp"] = pd.to_datetime(df["timestamp"])
            
        return df
    except Exception as e:
        print(f"Error processing data: {e}")
        return None

def visualize_swap_metrics(df):
    """
    Generate visualizations for swap transaction metrics.
    
    Args:
        df (pd.DataFrame): Processed data containing swap metrics.
    """
    if df is None or df.empty:
        print("No data available for visualization")
        return
    
    plt.figure(figsize=(15, 10))
    
    # Plot 1: Daily Swap Volume
    plt.subplot(2, 2, 1)
    if "timestamp" in df.columns and "swap_volume_usd" in df.columns:
        daily_volume = df.groupby(pd.Grouper(key="timestamp", freq="D"))["swap_volume_usd"].sum()
        daily_volume.plot(kind="line", title="Daily Swap Volume (USD)")
        plt.ylabel("Volume (USD)")
    else:
        print("Required columns for daily swap volume not found")
    
    # Plot 2: Token Distribution
    plt.subplot(2, 2, 2)
    if "token_symbol" in df.columns and "swap_count" in df.columns:
        token_dist = df.groupby("token_symbol")["swap_count"].sum().nlargest(10)
        token_dist.plot(kind="bar", title="Top 10 Tokens by Swap Count")
        plt.ylabel("Swap Count")
    else:
        print("Required columns for token distribution not found")
    
    # Plot 3: Average Swap Size Over Time
    plt.subplot(2, 2, 3)
    if "timestamp" in df.columns and "swap_volume_usd" in df.columns and "swap_count" in df.columns:
        daily_avg = df.groupby(pd.Grouper(key="timestamp", freq="D")).apply(
            lambda x: x["swap_volume_usd"].sum() / x["swap_count"].sum()
        )
        daily_avg.plot(kind="line", title="Daily Average Swap Size (USD)")
        plt.ylabel("Average Size (USD)")
    else:
        print("Required columns for average swap size not found")
    
    # Plot 4: Unique Users Over Time
    plt.subplot(2, 2, 4)
    if "timestamp" in df.columns and "user_count" in df.columns:
        df.groupby(pd.Grouper(key="timestamp", freq="D"))["user_count"].sum().plot(
            kind="line", title="Daily Unique Users"
        )
        plt.ylabel("User Count")
    else:
        print("Required columns for unique users not found")
    
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the Dune query, process data, and visualize results.
    """
    print("Starting 1inch Aggregation Protocol V5 analysis...")
    
    # Step 1: Execute the query
    print("Executing Dune query...")
    execution_id = execute_dune_query(QUERY_ID)
    if not execution_id:
        print("Failed to execute query")
        return
    
    print(f"Query execution started with ID: {execution_id}")
    
    # Step 2: Get query results (in a real scenario, you might need to poll for completion)
    print("Fetching query results...")
    results = get_query_results(execution_id)
    if not results:
        print("Failed to fetch results")
        return
    
    # Step 3: Process the data
    print("Processing data...")
    df = process_data(results)
    if df is None:
        print("Failed to process data")
        return
    
    print(f"Successfully processed {len(df)} records")
    
    # Step 4: Visualize the metrics
    print("Generating visualizations...")
    visualize_swap_metrics(df)

if __name__ == "__main__":
    main()
```
