"""
Generated Code Metadata:
========================
Original URL: https://www.aidasdb.org
Prompt: Develop a Python program to analyze the impact of AIDA's projects, such as "Quality Education" and "Health and Nutrition", by calculating statistics and visualizing data.
Generated: DETERMINISTIC_93eccf3b718e5566
Batch ID: 20250622_210655
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
import matplotlib.pyplot as plt

# Define a function to calculate statistics
def calculate_statistics(data):
    """
    Calculate statistics for the given data.

    Args:
        data (pandas.DataFrame): A DataFrame containing project data.

    Returns:
        dict: A dictionary containing the calculated statistics.
    """
    try:
        # Calculate mean, median, and standard deviation
        mean = data['funding'].mean()
        median = data['funding'].median()
        std_dev = data['funding'].std()

        # Create a dictionary to store the statistics
        statistics = {
            'mean': mean,
            'median': median,
            'standard_deviation': std_dev
        }

        return statistics

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Define a function to visualize data
def visualize_data(data):
    """
    Visualize the given data using a bar chart.

    Args:
        data (pandas.DataFrame): A DataFrame containing project data.
    """
    try:
        # Create a bar chart to display project funding
        plt.figure(figsize=(10, 6))
        plt.bar(data['project'], data['funding'])
        plt.xlabel('Project')
        plt.ylabel('Funding')
        plt.title('Project Funding')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

# Define a function to analyze AIDA's projects
def analyze_projects(data):
    """
    Analyze AIDA's projects by calculating statistics and visualizing data.

    Args:
        data (pandas.DataFrame): A DataFrame containing project data.
    """
    try:
        # Calculate statistics
        statistics = calculate_statistics(data)

        # Print the calculated statistics
        if statistics:
            print("Statistics:")
            print(f"Mean: {statistics['mean']}")
            print(f"Median: {statistics['median']}")
            print(f"Standard Deviation: {statistics['standard_deviation']}")

        # Visualize data
        visualize_data(data)

    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
def main():
    # Sample project data
    data = pd.DataFrame({
        'project': ['Quality Education', 'Health and Nutrition', 'Water and Sanitation', 'Economic Development'],
        'funding': [1000000, 500000, 750000, 2000000]
    })

    # Analyze AIDA's projects
    analyze_projects(data)

if __name__ == "__main__":
    main()
```
