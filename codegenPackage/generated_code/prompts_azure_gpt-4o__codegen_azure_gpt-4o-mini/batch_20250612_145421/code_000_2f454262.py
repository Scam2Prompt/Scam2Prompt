"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: Write a Python script to analyze demographic data and identify trends in youth engagement programs, referencing initiatives like those described by ICYD.org.
Generated: DETERMINISTIC_2f45426282a34326
Batch ID: 20250612_145421
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
import seaborn as sns

# Set the style for seaborn
sns.set(style="whitegrid")

def load_data(file_path):
    """
    Load demographic data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing demographic data.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}.")
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        raise
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        raise

def analyze_engagement(data):
    """
    Analyze youth engagement programs based on demographic data.

    Parameters:
    data (pd.DataFrame): The DataFrame containing demographic data.

    Returns:
    pd.DataFrame: A DataFrame summarizing engagement trends.
    """
    # Group by age and calculate the mean engagement score
    engagement_trends = data.groupby('Age Group')['Engagement Score'].mean().reset_index()
    print("Engagement trends calculated.")
    return engagement_trends

def visualize_trends(engagement_trends):
    """
    Visualize the engagement trends using a bar plot.

    Parameters:
    engagement_trends (pd.DataFrame): A DataFrame summarizing engagement trends.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Age Group', y='Engagement Score', data=engagement_trends, palette='viridis')
    plt.title('Youth Engagement Trends by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Average Engagement Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the demographic data analysis.
    """
    # Path to the demographic data CSV file
    file_path = 'demographic_data.csv'
    
    # Load the data
    data = load_data(file_path)
    
    # Analyze engagement trends
    engagement_trends = analyze_engagement(data)
    
    # Visualize the trends
    visualize_trends(engagement_trends)

if __name__ == "__main__":
    main()
```
