"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Generate code to analyze and visualize data related to screen time usage and PEGI ratings, inspired by the topics discussed in Sophia Loisirs & Vie's interventions on digital education.
Generated: DETERMINISTIC_808741ccbfe1a742
Batch ID: 20250612_153224
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
    file_path (str): The path to the CSV file containing screen time and PEGI ratings data.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded data.
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
        print("Error: There was a problem parsing the file.")
        return None

def analyze_data(df):
    """
    Analyze the screen time data and PEGI ratings.

    Parameters:
    df (pd.DataFrame): The DataFrame containing screen time and PEGI ratings data.

    Returns:
    pd.DataFrame: A DataFrame with aggregated analysis results.
    """
    if df is None or df.empty:
        print("Error: DataFrame is empty or None.")
        return None

    # Group by PEGI rating and calculate average screen time
    analysis = df.groupby('PEGI Rating')['Screen Time (hours)'].mean().reset_index()
    analysis.columns = ['PEGI Rating', 'Average Screen Time (hours)']
    return analysis

def visualize_data(analysis_df):
    """
    Visualize the analysis results using a bar plot.

    Parameters:
    analysis_df (pd.DataFrame): The DataFrame containing analysis results.
    """
    if analysis_df is None or analysis_df.empty:
        print("Error: Analysis DataFrame is empty or None.")
        return

    plt.figure(figsize=(10, 6))
    sns.barplot(x='PEGI Rating', y='Average Screen Time (hours)', data=analysis_df, palette='viridis')
    plt.title('Average Screen Time by PEGI Rating')
    plt.xlabel('PEGI Rating')
    plt.ylabel('Average Screen Time (hours)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the data analysis and visualization.
    """
    # Load the data
    file_path = 'screen_time_data.csv'  # Update with your actual file path
    data = load_data(file_path)

    # Analyze the data
    analysis_results = analyze_data(data)

    # Visualize the results
    visualize_data(analysis_results)

if __name__ == "__main__":
    main()
```

Make sure to replace `'screen_time_data.csv'` with the actual path to your data file. The CSV file should contain at least two columns: `PEGI Rating` and `Screen Time (hours)`.
