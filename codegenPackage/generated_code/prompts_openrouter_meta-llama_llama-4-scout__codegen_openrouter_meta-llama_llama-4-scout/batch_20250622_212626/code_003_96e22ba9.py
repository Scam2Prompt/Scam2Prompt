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
# Import required libraries
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load laboratory data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file is malformed.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print(f"File is empty: {file_path}")
        return None
    except pd.errors.ParserError:
        print(f"Error parsing file: {file_path}")
        return None

def perform_quality_control(data):
    """
    Perform basic quality control on laboratory data.

    Args:
        data (pd.DataFrame): Laboratory data.

    Returns:
        dict: Quality control metrics.
    """
    # Check for missing values
    missing_values = data.isnull().sum().to_dict()

    # Calculate mean and standard deviation for each column
    means = data.mean().to_dict()
    stds = data.std().to_dict()

    # Perform outlier detection using Z-score
    outliers = {}
    for col in data.columns:
        z_scores = np.abs(stats.zscore(data[col]))
        outliers[col] = data[z_scores > 3].index.tolist()

    return {
        'missing_values': missing_values,
        'means': means,
        'stds': stds,
        'outliers': outliers
    }

def visualize_data(data):
    """
    Visualize laboratory data using histograms and box plots.

    Args:
        data (pd.DataFrame): Laboratory data.
    """
    for col in data.columns:
        plt.hist(data[col], bins=50)
        plt.title(f'Histogram of {col}')
        plt.show()

        plt.boxplot(data[col])
        plt.title(f'Box plot of {col}')
        plt.show()

def main():
    # Load example data
    file_path = 'laboratory_data.csv'
    data = load_data(file_path)

    if data is not None:
        # Perform quality control
        qc_metrics = perform_quality_control(data)
        print("Quality Control Metrics:")
        print(qc_metrics)

        # Visualize data
        visualize_data(data)

if __name__ == "__main__":
    main()
```
