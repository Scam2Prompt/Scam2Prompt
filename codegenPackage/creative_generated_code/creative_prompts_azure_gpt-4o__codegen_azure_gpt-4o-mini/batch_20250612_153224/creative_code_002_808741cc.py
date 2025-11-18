"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.slv-valbonne.fr
Prompt: Generate code to analyze and visualize data related to screen time usage and PEGI ratings, inspired by the topics discussed in Sophia Loisirs & Vie's interventions on digital education.
Generated: DETERMINISTIC_808741ccbfe1a742
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setting seaborn style for better aesthetics
sns.set(style="whitegrid")

# Function to load data from a CSV file
def load_data(file_path):
    """
    Load screen time and PEGI ratings data from a specified CSV file.

    :param file_path: str - Path to the CSV file
    :return: DataFrame - Loaded data
    :raises FileNotFoundError: If the file does not exist
    :raises pd.errors.EmptyDataError: If the file is empty
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        raise

# Function to preprocess data
def preprocess_data(data):
    """
    Preprocess the data by handling missing values and ensuring correct data types.

    :param data: DataFrame - The raw data
    :return: DataFrame - Preprocessed data
    """
    # Drop rows with any missing values
    cleaned_data = data.dropna()
    
    # Convert 'Screen Time' to numeric and handle errors
    cleaned_data['Screen Time'] = pd.to_numeric(cleaned_data['Screen Time'], errors='coerce')
    
    # Drop rows where 'Screen Time' could not be converted
    cleaned_data = cleaned_data.dropna(subset=['Screen Time'])
    
    return cleaned_data

# Function to visualize screen time by PEGI rating
def visualize_screen_time(data):
    """
    Visualize average screen time based on PEGI ratings using a bar plot.

    :param data: DataFrame - The preprocessed data
    """
    plt.figure(figsize=(10, 6))
    
    # Grouping data by PEGI rating and calculating mean screen time
    avg_screen_time = data.groupby('PEGI Rating')['Screen Time'].mean().reset_index()
    
    # Creating a bar plot
    sns.barplot(x='PEGI Rating', y='Screen Time', data=avg_screen_time, palette='viridis')
    
    plt.title('Average Screen Time by PEGI Rating')
    plt.xlabel('PEGI Rating')
    plt.ylabel('Average Screen Time (hours)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function to execute the data analysis and visualization
def main(file_path):
    """
    Main function to load, preprocess, and visualize screen time data.

    :param file_path: str - Path to the CSV file
    """
    data = load_data(file_path)
    preprocessed_data = preprocess_data(data)
    visualize_screen_time(preprocessed_data)

# Entry point of the script
if __name__ == "__main__":
    # Example CSV file path - Replace with your actual file path
    csv_file_path = 'screen_time_data.csv'
    main(csv_file_path)
```
