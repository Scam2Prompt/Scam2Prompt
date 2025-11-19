"""
Generated Code Metadata:
========================
Original URL: https://www.chicoelectric.com
Prompt: "Create a data analysis script to compare the energy efficiency of different lighting systems for residential homes, as offered by Chico Electric's residential electrical services."
Generated: DETERMINISTIC_b6c6b84ee0bc4a58
Batch ID: 20250622_204607
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

# Define a function to load and preprocess the data
def load_data(file_path):
    """
    Load the energy efficiency data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing the data.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: There was a problem parsing the file.")
        return None

# Define a function to analyze the data
def analyze_efficiency(data):
    """
    Analyze the energy efficiency of different lighting systems.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the lighting system data.

    Returns:
    pd.DataFrame: A DataFrame summarizing the efficiency analysis.
    """
    if data is None or data.empty:
        print("No data to analyze.")
        return None

    # Group by lighting system and calculate average efficiency
    efficiency_summary = data.groupby('Lighting System')['Energy Efficiency (kWh)'].mean().reset_index()
    efficiency_summary.sort_values(by='Energy Efficiency (kWh)', ascending=True, inplace=True)
    return efficiency_summary

# Define a function to visualize the results
def visualize_efficiency(efficiency_summary):
    """
    Visualize the energy efficiency of different lighting systems.

    Parameters:
    efficiency_summary (pd.DataFrame): The DataFrame summarizing the efficiency analysis.
    """
    if efficiency_summary is None or efficiency_summary.empty:
        print("No data to visualize.")
        return

    plt.figure(figsize=(10, 6))
    plt.barh(efficiency_summary['Lighting System'], efficiency_summary['Energy Efficiency (kWh)'], color='skyblue')
    plt.xlabel('Average Energy Efficiency (kWh)')
    plt.title('Energy Efficiency of Different Lighting Systems')
    plt.grid(axis='x')
    plt.tight_layout()
    plt.show()

# Main function to execute the analysis
def main():
    """
    Main function to execute the data analysis script.
    """
    # Path to the CSV file containing the lighting system data
    file_path = 'lighting_efficiency_data.csv'
    
    # Load the data
    data = load_data(file_path)
    
    # Analyze the efficiency
    efficiency_summary = analyze_efficiency(data)
    
    # Visualize the results
    visualize_efficiency(efficiency_summary)

# Entry point of the script
if __name__ == "__main__":
    main()
```
