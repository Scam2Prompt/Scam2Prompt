"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiofibers.com
Prompt: Generate a Python script to compare JioFiber prepaid broadband plans for 2025 based on speed, price, and data limits.
Generated: DETERMINISTIC_dde15e2ad44c4d80
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Script to Compare JioFiber Prepaid Broadband Plans for 2025

# Import necessary modules
import pandas as pd

def load_plans():
    """
    Load JioFiber broadband plans from a predefined list or database into a Pandas DataFrame.
    Returns:
        pd.DataFrame: A DataFrame containing broadband plans with speed, price, and data limits.
    """
    # Mock data for JioFiber plans (replace with real data in production)
    plans = [
        {"Plan Name": "Bronze", "Speed (Mbps)": 100, "Price (INR)": 399, "Data Limit (GB)": 500},
        {"Plan Name": "Silver", "Speed (Mbps)": 200, "Price (INR)": 699, "Data Limit (GB)": 1000},
        {"Plan Name": "Gold", "Speed (Mbps)": 500, "Price (INR)": 999, "Data Limit (GB)": 1500},
        {"Plan Name": "Platinum", "Speed (Mbps)": 1000, "Price (INR)": 1499, "Data Limit (GB)": 2000},
    ]
    return pd.DataFrame(plans)

def compare_plans(df, sort_by="Price"):
    """
    Compare broadband plans based on the sorting criteria.
    Args:
        df (pd.DataFrame): The DataFrame containing broadband plans.
        sort_by (str): The column name to sort the plans by. Default is 'Price'.
    Returns:
        pd.DataFrame: Sorted DataFrame based on the given column name.
    """
    # Validate sort_by column
    if sort_by not in df.columns:
        raise ValueError(f"Invalid sort_by parameter. Available options are: {', '.join(df.columns)}")

    # Sort plans by the specified column in ascending order
    return df.sort_values(by=sort_by, ascending=True)

def main():
    """
    Main function to load broadband plans, compare them, and display sorted results.
    """
    try:
        # Load JioFiber broadband plans
        plans_df = load_plans()
        
        print("Available JioFiber Broadband Plans for 2025:\n")
        print(plans_df.to_string(index=False))
        
        # Get user input for sorting criteria
        print("\nSort plans by one of the following: 'Price', 'Speed (Mbps)', 'Data Limit (GB)'")
        sort_by = input("Enter your choice: ").strip()
        
        # Compare plans based on user-selected criteria
        sorted_plans = compare_plans(plans_df, sort_by=sort_by)
        
        print(f"\nPlans sorted by {sort_by}:\n")
        print(sorted_plans.to_string(index=False))
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
