"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlconsortium.com
Prompt: Write a script to visualize ENL Consortium's warehouse space utilization and cargo stacking areas using data from their port operations system.
Generated: DETERMINISTIC_3a457f9fc0e53bc8
Batch ID: 20250612_151232
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
import seaborn as sns

# Set the style for the plots
sns.set(style="whitegrid")

def load_data(file_path):
    """
    Load warehouse space utilization data from a CSV file.

    Parameters:
        file_path (str): The path to the CSV file containing warehouse data.

    Returns:
        pd.DataFrame: A DataFrame containing the warehouse data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()

def visualize_space_utilization(data):
    """
    Visualize space utilization in the warehouse.

    Parameters:
        data (pd.DataFrame): The DataFrame containing warehouse data with columns for 
                             'Area', 'Used Space', and 'Total Space'.
    """
    if data.empty:
        print("No data to visualize.")
        return

    # Calculate the utilization percentage
    data['Utilization (%)'] = (data['Used Space'] / data['Total Space']) * 100

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Area', y='Utilization (%)', data=data)
    plt.title('Warehouse Space Utilization')
    plt.xlabel('Warehouse Area')
    plt.ylabel('Utilization (%)')
    plt.xticks(rotation=45)
    plt.axhline(y=100, color='r', linestyle='--', label='Maximum Utilization (100%)')
    plt.legend()
    plt.tight_layout()
    plt.show()

def visualize_cargo_stacking(data):
    """
    Visualize cargo stacking areas in the warehouse.

    Parameters:
        data (pd.DataFrame): The DataFrame containing warehouse data with the 'Stack Height' column.
    """
    if data.empty:
        print("No data to visualize.")
        return

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Area', y='Stack Height', data=data)
    plt.title('Cargo Stacking Heights by Area')
    plt.xlabel('Warehouse Area')
    plt.ylabel('Stack Height (in meters)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the data loading and visualization.
    """
    # Path to the CSV file (update this path as needed)
    file_path = 'warehouse_data.csv'

    # Load the data
    warehouse_data = load_data(file_path)

    # Visualize space utilization and cargo stacking areas
    visualize_space_utilization(warehouse_data)
    visualize_cargo_stacking(warehouse_data)

if __name__ == "__main__":
    main()
```
