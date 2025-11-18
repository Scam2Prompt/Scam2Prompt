"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gapkindo.org
Prompt: Suggest a library for processing and visualizing the natural rubber statistics provided by GAPKINDO, and demonstrate its usage with example code.
Generated: DETERMINISTIC_d8a4b798e272dfee
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure Seaborn style for better aesthetics
sns.set(style="whitegrid")

def load_data(file_path):
    """
    Load the natural rubber statistics data from a CSV file.

    Args:
        file_path (str): The path to the CSV file containing the data.

    Returns:
        pd.DataFrame: A DataFrame containing the loaded data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        print(f"Error: The file {file_path} was not found. Please check the path and try again.")
        raise e
    except pd.errors.EmptyDataError as e:
        print("Error: The file is empty. Please provide a valid file with data.")
        raise e

def visualize_rubber_statistics(data):
    """
    Visualize natural rubber statistics using a bar plot.

    Args:
        data (pd.DataFrame): The DataFrame containing the rubber statistics.
    """
    # Check if required columns exist
    if 'Year' not in data.columns or 'Production' not in data.columns:
        raise ValueError("Data must contain 'Year' and 'Production' columns.")

    # Create a bar plot for production statistics
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Year', y='Production', data=data, palette="viridis")
    
    # Set plot title and labels
    plt.title('Natural Rubber Production Statistics Over Years', fontsize=16)
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Production (tons)', fontsize=14)
    plt.xticks(rotation=45)
    
    # Show the plot
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to load data and visualize natural rubber statistics.
    """
    # Path to the CSV data file (change this to your actual file path)
    file_path = 'rubber_statistics.csv'
    
    # Load data
    try:
        rubber_data = load_data(file_path)
        # Visualize the data
        visualize_rubber_statistics(rubber_data)
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
