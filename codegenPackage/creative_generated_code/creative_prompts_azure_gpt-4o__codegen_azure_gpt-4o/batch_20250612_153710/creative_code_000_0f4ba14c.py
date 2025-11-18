"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amplatinumconsulting.com
Prompt: Write Python code to analyze business performance data using libraries recommended for management consulting, such as pandas and matplotlib.
Generated: DETERMINISTIC_0f4ba14c9d0cc9dd
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Function to load and validate business performance data
def load_data(file_path):
    """
    Loads business performance data from a CSV file and validates the content.

    Parameters:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Validated DataFrame containing the business performance data.
    """
    try:
        # Load data into DataFrame
        data = pd.read_csv(file_path)
        
        # Validate that necessary columns are present
        required_columns = ["Date", "Revenue", "Expense", "Profit"]
        if not all(column in data.columns for column in required_columns):
            raise ValueError(f"Missing required columns. Expected columns: {required_columns}")
        
        # Ensure Date column is treated as a datetime type
        data['Date'] = pd.to_datetime(data['Date'])
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None

# Function to calculate key performance metrics
def calculate_metrics(data):
    """
    Calculates key performance metrics from the business data.

    Parameters:
        data (pd.DataFrame): DataFrame containing business performance data.

    Returns:
        dict: Dictionary containing calculated metrics.
    """
    metrics = {
        "Total Revenue": data["Revenue"].sum(),
        "Total Expense": data["Expense"].sum(),
        "Total Profit": data["Profit"].sum(),
        "Average Monthly Profit": data["Profit"].mean(),
        "Profit Margin (%)": (data["Profit"].sum() / data["Revenue"].sum()) * 100 if data["Revenue"].sum() != 0 else 0
    }
    return metrics

# Function to visualize business performance over time
def visualize_performance(data):
    """
    Creates a visualization of business performance over time using matplotlib.

    Parameters:
        data (pd.DataFrame): DataFrame containing business performance data.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data["Date"], data["Revenue"], label="Revenue", color="green")
    plt.plot(data["Date"], data["Expense"], label="Expense", color="red")
    plt.plot(data["Date"], data["Profit"], label="Profit", color="blue")
    
    plt.title("Business Performance Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount ($)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Main function to orchestrate analysis
def main():
    """
    Main function to execute business performance analysis and visualization.

    Steps:
        1. Load data.
        2. Calculate performance metrics.
        3. Visualize performance trends.
    """
    # File path to the business performance data CSV
    file_path = "business_performance.csv"
    
    # Load data
    data = load_data(file_path)
    if data is None:
        return
    
    # Calculate key metrics
    metrics = calculate_metrics(data)
    print("Key Performance Metrics:")
    for metric, value in metrics.items():
        print(f"{metric}: {value:.2f}")

    # Visualize trends
    visualize_performance(data)

# Entry point for the script
if __name__ == "__main__":
    main()
```
