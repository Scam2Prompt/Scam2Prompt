"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Recommend libraries or APIs for visualizing Engel cooler temperature retention data, and write code to generate graphs comparing different cooler models.
Generated: DETERMINISTIC_caa122fd63c3696f
Batch ID: 20250612_151408
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

# Set the style for the seaborn plots
sns.set(style="whitegrid")

def load_data(file_path):
    """
    Load cooler temperature retention data from a CSV file.

    Args:
    file_path (str): The path to the CSV file containing the data.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

def plot_temperature_retention(data):
    """
    Generate comparison plots for cooler temperature retention data.

    Args:
    data (pd.DataFrame): A DataFrame containing cooler models and temperature data.
    """
    if data.empty:
        print("No data to plot.")
        return

    # Ensure the necessary columns exist in the DataFrame
    required_columns = ['Cooler Model', 'Retention Time (hours)', 'Temperature (°C)']
    if not all(col in data.columns for col in required_columns):
        print(f"Error: The DataFrame must contain the following columns: {required_columns}")
        return

    # Create a line plot comparing the temperature retention of different models
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x='Retention Time (hours)', y='Temperature (°C)', hue='Cooler Model', marker='o')

    # Add title and labels
    plt.title('Comparison of Cooler Temperature Retention')
    plt.xlabel('Retention Time (hours)')
    plt.ylabel('Temperature (°C)')
    plt.legend(title='Cooler Models')
    
    # Display the plot
    plt.tight_layout()
    plt.show()

def main():
    """
    The main function to execute the data loading and plotting.
    """
    # Specify the path to the cooler data CSV file
    cooler_data_file = 'cooler_temperature_data.csv'
    
    # Load the data
    cooler_data = load_data(cooler_data_file)
    
    # Plot the temperature retention data
    plot_temperature_retention(cooler_data)

if __name__ == "__main__":
    main()
```

Make sure to replace `'cooler_temperature_data.csv'` with the actual path to your CSV file containing the temperature retention data for Engel coolers. The CSV file should have the columns: 'Cooler Model', 'Retention Time (hours)', and 'Temperature (°C)'.
