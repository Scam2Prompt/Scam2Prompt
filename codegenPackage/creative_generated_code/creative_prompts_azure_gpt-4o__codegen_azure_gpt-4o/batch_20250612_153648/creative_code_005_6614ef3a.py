"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remas.ae
Prompt: Write code to analyze and visualize data for completed projects, including metrics like service quality and client satisfaction, as described in the Remas Engineering Consultants portfolio.
Generated: DETERMINISTIC_6614ef3a58f60dad
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a Python script for analyzing and visualizing project data using `pandas`, `matplotlib`, and `seaborn`. The script assumes you have a CSV file containing project data.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess data
def load_data(file_path):
    """
    Loads project data from a CSV file.
    :param file_path: str - Path to the CSV file
    :return: pd.DataFrame - DataFrame containing the project data
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("Error: File is empty or invalid.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def preprocess_data(data):
    """
    Preprocesses the project data.
    :param data: pd.DataFrame - Raw project data
    :return: pd.DataFrame - Processed project data
    """
    # Drop rows with missing values
    data_cleaned = data.dropna()

    # Ensure proper data types
    data_cleaned['ServiceQuality'] = pd.to_numeric(data_cleaned['ServiceQuality'], errors='coerce')
    data_cleaned['ClientSatisfaction'] = pd.to_numeric(data_cleaned['ClientSatisfaction'], errors='coerce')

    # Drop rows with invalid numeric conversion
    data_cleaned = data_cleaned.dropna(subset=['ServiceQuality', 'ClientSatisfaction'])

    return data_cleaned

def visualize_data(data):
    """
    Visualizes the project data using Seaborn and Matplotlib.
    :param data: pd.DataFrame - Processed project data
    """
    # Define the plot style
    sns.set(style="whitegrid")

    # Service Quality distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(data['ServiceQuality'], kde=True, color='blue', bins=20)
    plt.title("Distribution of Service Quality")
    plt.xlabel("Service Quality")
    plt.ylabel("Count")
    plt.show()

    # Client Satisfaction distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(data['ClientSatisfaction'], kde=True, color='green', bins=20)
    plt.title("Distribution of Client Satisfaction")
    plt.xlabel("Client Satisfaction")
    plt.ylabel("Count")
    plt.show()

    # Scatter plot of Service Quality vs Client Satisfaction
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='ServiceQuality', y='ClientSatisfaction', data=data, color='purple')
    plt.title("Service Quality vs Client Satisfaction")
    plt.xlabel("Service Quality")
    plt.ylabel("Client Satisfaction")
    plt.show()

    # Correlation heatmap
    plt.figure(figsize=(8, 6))
    correlation_matrix = data[['ServiceQuality', 'ClientSatisfaction']].corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()

# Main function
def main():
    """
    Main function to run the data analysis and visualization.
    """
    file_path = "projects_data.csv"  # Replace with the path to your CSV file

    # Load the data
    data = load_data(file_path)
    if data is None:
        return

    # Preprocess the data
    data_cleaned = preprocess_data(data)

    # Visualize the data
    visualize_data(data_cleaned)

if __name__ == "__main__":
    main()
```

### Notes:
1. Replace `"projects_data.csv"` with the path to your data file.
2. Ensure the CSV file contains columns `ServiceQuality` and `ClientSatisfaction` with numeric values for analysis.
3. Install required libraries using `pip install pandas matplotlib seaborn` before running the script.
