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
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define a function to load and prepare data
def load_data(file_path):
    """
    Load screen time usage and PEGI ratings data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        # Load data from CSV file
        data = pd.read_csv(file_path)

        # Validate required columns
        required_columns = ['screen_time', 'PEGI_rating']
        if not all(column in data.columns for column in required_columns):
            raise ValueError("The CSV file is missing required columns.")

        return data
    except FileNotFoundError:
        print("The file was not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty. Please check the file contents.")
        return None
    except pd.errors.ParserError:
        print("Error parsing the file. Please check the file format.")
        return None

# Define a function to analyze data
def analyze_data(data):
    """
    Analyze screen time usage and PEGI ratings data.

    Args:
        data (pd.DataFrame): A DataFrame containing the data.

    Returns:
        dict: A dictionary containing the analysis results.
    """
    # Calculate mean screen time by PEGI rating
    mean_screen_time = data.groupby('PEGI_rating')['screen_time'].mean().reset_index()

    # Calculate total screen time
    total_screen_time = data['screen_time'].sum()

    return {
        'mean_screen_time': mean_screen_time,
        'total_screen_time': total_screen_time
    }

# Define a function to visualize data
def visualize_data(data, analysis_results):
    """
    Visualize screen time usage and PEGI ratings data.

    Args:
        data (pd.DataFrame): A DataFrame containing the data.
        analysis_results (dict): A dictionary containing the analysis results.
    """
    # Create a figure with two subplots
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Plot mean screen time by PEGI rating
    sns.barplot(x='PEGI_rating', y='screen_time', data=analysis_results['mean_screen_time'], ax=axs[0])
    axs[0].set_title('Mean Screen Time by PEGI Rating')
    axs[0].set_xlabel('PEGI Rating')
    axs[0].set_ylabel('Mean Screen Time')

    # Plot distribution of screen time usage
    sns.histplot(data['screen_time'], ax=axs[1])
    axs[1].set_title('Distribution of Screen Time Usage')
    axs[1].set_xlabel('Screen Time')
    axs[1].set_ylabel('Frequency')

    # Layout so plots do not overlap
    fig.tight_layout()

    plt.show()

# Main function
def main():
    # Load data
    file_path = 'screen_time_data.csv'  # Replace with your file path
    data = load_data(file_path)

    if data is not None:
        # Analyze data
        analysis_results = analyze_data(data)

        # Visualize data
        visualize_data(data, analysis_results)

if __name__ == "__main__":
    main()
```
