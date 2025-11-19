"""
Generated Code Metadata:
========================
Original URL: https://immediateunity.com
Prompt: Write a Python script to analyze the importance of work-life balance in part-time jobs, considering factors beyond hourly wages.
Generated: DETERMINISTIC_bf0fed45cbf96a6b
Batch ID: 20250622_211310
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
    Load the dataset from a CSV file.

    :param file_path: str - Path to the CSV file
    :return: DataFrame - Loaded data
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
        print("Error: The file could not be parsed.")
        return None

def analyze_work_life_balance(data):
    """
    Analyze the importance of work-life balance in part-time jobs.

    :param data: DataFrame - The dataset containing job information
    """
    if data is None or data.empty:
        print("No data to analyze.")
        return

    # Display basic statistics
    print("Basic Statistics:")
    print(data.describe())

    # Check for missing values
    print("\nMissing Values:")
    print(data.isnull().sum())

    # Visualize the relationship between work-life balance and job satisfaction
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='work_life_balance', y='job_satisfaction', data=data)
    plt.title('Work-Life Balance vs Job Satisfaction')
    plt.xlabel('Work-Life Balance')
    plt.ylabel('Job Satisfaction')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Correlation matrix to see how different factors relate
    correlation = data.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm', square=True)
    plt.title('Correlation Matrix')
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the work-life balance analysis.
    """
    # Path to the dataset
    file_path = 'part_time_jobs.csv'
    
    # Load the data
    data = load_data(file_path)
    
    # Analyze the work-life balance
    analyze_work_life_balance(data)

if __name__ == "__main__":
    main()
```

Make sure to have a CSV file named `part_time_jobs.csv` with appropriate columns such as `work_life_balance` and `job_satisfaction` for the script to run successfully.
