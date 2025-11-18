"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Develop a Python script to analyze customer preferences for flip-flop designs based on past orders, focusing on categories like "Ojota Dama Pulsera" and "Suecos Hombre."
Generated: DETERMINISTIC_106d4481079b1021
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from typing import Tuple

# Constants for category filtering
TARGET_CATEGORIES = ["Ojota Dama Pulsera", "Suecos Hombre"]

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load customer order data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing order data.
        
    Returns:
        pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        # Load the data from CSV. Ensure the file exists and is readable.
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at path {file_path} was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError(f"The file at path {file_path} is empty or malformed.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading the file: {e}")

def filter_categories(data: pd.DataFrame, categories: list) -> pd.DataFrame:
    """
    Filter the DataFrame to only include rows matching the target categories.
    
    Args:
        data (pd.DataFrame): Original DataFrame containing order data.
        categories (list): List of categories to filter by.
        
    Returns:
        pd.DataFrame: Filtered DataFrame containing only the target categories.
    """
    if "Category" not in data.columns:
        raise ValueError("The DataFrame does not contain a 'Category' column.")
    
    filtered_data = data[data["Category"].isin(categories)]
    return filtered_data

def analyze_preferences(data: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze customer preferences for flip-flop designs.
    
    Args:
        data (pd.DataFrame): Filtered DataFrame containing order data for target categories.
        
    Returns:
        pd.DataFrame: DataFrame summarizing customer preferences (e.g., counts by design).
    """
    if "Design" not in data.columns:
        raise ValueError("The DataFrame does not contain a 'Design' column.")
    
    # Group data by design and calculate order counts
    preference_summary = data.groupby("Design")["Design"].count().reset_index(name="Order_Count")
    
    # Sort by order count in descending order for better readability
    preference_summary = preference_summary.sort_values(by="Order_Count", ascending=False).reset_index(drop=True)
    
    return preference_summary

def main(file_path: str) -> None:
    """
    Main function to execute the customer preference analysis.
    
    Args:
        file_path (str): Path to the CSV file containing order data.
    """
    print("Loading customer order data...")
    data = load_data(file_path)
    
    print("Filtering data for target categories...")
    filtered_data = filter_categories(data, TARGET_CATEGORIES)
    
    print("Analyzing customer preferences...")
    preference_summary = analyze_preferences(filtered_data)
    
    print("Customer preferences analysis complete:")
    print(preference_summary)

# Entry point for the script
if __name__ == "__main__":
    # Replace 'orders.csv' with the actual path to your orders data file
    file_path = "orders.csv"
    try:
        main(file_path)
    except Exception as e:
        print(f"An error occurred: {e}")
```
