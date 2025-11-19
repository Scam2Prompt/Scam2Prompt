"""
Generated Code Metadata:
========================
Original URL: https://45ybook.ueh.edu.vn
Prompt: Write a Python script that analyzes data on multi-disciplinary programs in universities, inspired by the themes in the UEH publication.
Generated: DETERMINISTIC_47799bab94aa44db
Batch ID: 20250612_155417
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
    Load data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data.
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

def analyze_programs(data):
    """
    Analyze multi-disciplinary programs in the dataset.

    Parameters:
    data (DataFrame): The DataFrame containing university program data.

    Returns:
    DataFrame: A DataFrame with analysis results.
    """
    if data is None or data.empty:
        print("No data to analyze.")
        return None

    # Group by program type and count the number of occurrences
    program_counts = data['Program Type'].value_counts().reset_index()
    program_counts.columns = ['Program Type', 'Count']
    
    return program_counts

def visualize_data(program_counts):
    """
    Visualize the analysis results using a bar plot.

    Parameters:
    program_counts (DataFrame): The DataFrame containing program counts.
    """
    if program_counts is None or program_counts.empty:
        print("No data to visualize.")
        return

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Count', y='Program Type', data=program_counts, palette='viridis')
    plt.title('Distribution of Multi-Disciplinary Programs in Universities')
    plt.xlabel('Number of Programs')
    plt.ylabel('Program Type')
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the data analysis workflow.
    """
    # Path to the CSV file containing university program data
    file_path = 'university_programs.csv'
    
    # Load the data
    data = load_data(file_path)
    
    # Analyze the data
    program_counts = analyze_programs(data)
    
    # Visualize the results
    visualize_data(program_counts)

if __name__ == "__main__":
    main()
```
