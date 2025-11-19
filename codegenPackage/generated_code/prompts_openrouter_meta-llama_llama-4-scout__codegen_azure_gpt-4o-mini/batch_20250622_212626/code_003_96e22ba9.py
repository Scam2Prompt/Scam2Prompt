"""
Generated Code Metadata:
========================
Original URL: https://labiqc.com
Prompt: What libraries are available for data analysis in laboratory settings, and how can they be used for quality control?
Generated: DETERMINISTIC_96e22ba9adfebd41
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries for data analysis and visualization
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Function to load data from a CSV file
def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to perform quality control checks
def quality_control(data, threshold=3):
    """
    Perform quality control checks on the data using Z-scores.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data to be checked.
    threshold (float): The Z-score threshold for identifying outliers.

    Returns:
    pd.DataFrame: DataFrame containing the outliers.
    """
    # Calculate Z-scores for each column
    z_scores = np.abs(stats.zscore(data.select_dtypes(include=[np.number])))
    outliers = (z_scores > threshold)

    # Identify outlier rows
    outlier_rows = data[outliers.any(axis=1)]
    print(f"Identified {len(outlier_rows)} outlier rows based on Z-score threshold of {threshold}.")
    return outlier_rows

# Function to visualize data distribution
def visualize_data(data):
    """
    Visualize the distribution of the data using histograms and boxplots.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the data to be visualized.
    """
    # Set the aesthetic style of the plots
    sns.set(style="whitegrid")

    # Create histograms for each numeric column
    data.hist(bins=30, figsize=(15, 10), layout=(3, 3))
    plt.suptitle('Histograms of Numeric Columns')
    plt.show()

    # Create boxplots for each numeric column
    plt.figure(figsize=(15, 10))
    sns.boxplot(data=data.select_dtypes(include=[np.number]))
    plt.title('Boxplots of Numeric Columns')
    plt.xticks(rotation=45)
    plt.show()

# Main function to execute the data analysis workflow
def main(file_path):
    """
    Main function to execute the data analysis workflow.

    Parameters:
    file_path (str): The path to the CSV file containing the laboratory data.
    """
    # Load the data
    data = load_data(file_path)
    if data is not None:
        # Perform quality control
        outliers = quality_control(data)
        
        # Visualize the data
        visualize_data(data)

# Example usage
if __name__ == "__main__":
    # Replace 'your_data_file.csv' with the path to your data file
    main('your_data_file.csv')
```
