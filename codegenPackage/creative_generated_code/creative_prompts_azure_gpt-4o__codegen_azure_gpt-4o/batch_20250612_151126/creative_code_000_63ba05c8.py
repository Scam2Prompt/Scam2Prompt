"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alps.foundation
Prompt: Write Python code to analyze and visualize data from research studies on psychedelics, focusing on the evidence-based findings discussed by the ALPS Foundation.
Generated: DETERMINISTIC_63ba05c86e3904aa
Batch ID: 20250612_151126
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

def load_data(file_path):
    """
    Load the research study data from a CSV file.
    
    :param file_path: str, path to the CSV file
    :return: pd.DataFrame, loaded data
    """
    try:
        # Load the data into a pandas DataFrame
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("Error: File is empty or corrupted.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def preprocess_data(data):
    """
    Preprocess the data by handling missing values and renaming columns.
    
    :param data: pd.DataFrame, raw data
    :return: pd.DataFrame, cleaned data
    """
    # Drop rows with missing values in critical columns
    critical_columns = ['Study_ID', 'Psychedelic_Type', 'Evidence_Level', 'Effect_Size']
    data = data.dropna(subset=critical_columns)
    
    # Standardize column names
    data.columns = [col.strip().replace(' ', '_').lower() for col in data.columns]
    
    return data


def visualize_evidence_levels(data):
    """
    Create a bar chart to visualize the distribution of evidence levels across studies.
    
    :param data: pd.DataFrame, preprocessed data
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='evidence_level', palette='viridis')
    plt.title('Distribution of Evidence Levels Across Studies', fontsize=16)
    plt.xlabel('Evidence Level', fontsize=12)
    plt.ylabel('Number of Studies', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def visualize_effect_size(data):
    """
    Create a box plot to visualize the effect size distribution by psychedelic type.
    
    :param data: pd.DataFrame, preprocessed data
    """
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=data, x='psychedelic_type', y='effect_size', palette='coolwarm')
    plt.title('Effect Size Distribution by Psychedelic Type', fontsize=16)
    plt.xlabel('Psychedelic Type', fontsize=12)
    plt.ylabel('Effect Size', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    """
    Main function to load, preprocess, analyze, and visualize the data.
    """
    # Path to the research study dataset
    data_file_path = 'research_studies_psychedelics.csv'
    
    # Load the data
    data = load_data(data_file_path)
    if data is None:
        print("Failed to load data. Exiting.")
        return
    
    # Preprocess the data
    data = preprocess_data(data)
    
    # Analyze and visualize the data
    visualize_evidence_levels(data)
    visualize_effect_size(data)


if __name__ == "__main__":
    # Execute the main function
    main()
```
