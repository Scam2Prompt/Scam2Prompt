"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Generate code to analyze societal impacts of AI and automation, as highlighted in the "KI und Gesellschaft" article on ScienceArtThinking.de. Use Python libraries for data visualization to present trends.
Generated: DETERMINISTIC_664737142fc4c6b5
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Define a function to load data
def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("File is empty. Please check the file contents.")
        return None

# Define a function to analyze data
def analyze_data(data):
    """
    Analyze data and calculate trends.

    Args:
        data (pd.DataFrame): Data to analyze.

    Returns:
        dict: Trends and insights.
    """
    trends = {}
    # Calculate job displacement rate
    job_displacement_rate = (data['jobs_lost'] / data['total_jobs']) * 100
    trends['job_displacement_rate'] = job_displacement_rate

    # Calculate automation rate
    automation_rate = (data['automated_jobs'] / data['total_jobs']) * 100
    trends['automation_rate'] = automation_rate

    return trends

# Define a function to visualize trends
def visualize_trends(trends):
    """
    Visualize trends using a bar chart.

    Args:
        trends (dict): Trends and insights.
    """
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid")

    # Create a bar chart
    plt.bar(trends.keys(), trends.values())
    plt.xlabel('Trend')
    plt.ylabel('Rate (%)')
    plt.title('Societal Impacts of AI and Automation')
    plt.show()

# Define a function to analyze societal impacts
def analyze_societal_impacts(data):
    """
    Analyze societal impacts of AI and automation.

    Args:
        data (pd.DataFrame): Data to analyze.
    """
    trends = analyze_data(data)
    visualize_trends(trends)

# Load data
data = load_data('societal_impacts_data.csv')

# Analyze societal impacts
if data is not None:
    analyze_societal_impacts(data)
```

**societal_impacts_data.csv**
```csv
total_jobs,jobs_lost,automated_jobs
1000,50,200
2000,70,400
3000,100,600
4000,120,800
5000,150,1000
```
