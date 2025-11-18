"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1inchclub.xyz
Prompt: Create a Python script to process and visualize data related to new material creation, as mentioned in the "AI仅用17天独自创建41种新材料" section of the webpage.
Generated: DETERMINISTIC_4418bfe1a95366b8
Batch ID: 20250612_153907
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

# Set a style for seaborn
sns.set(style="whitegrid")

def load_data(file_path):
    """
    Load data from a CSV file.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the loaded data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If there is an error parsing the file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except pd.errors.EmptyDataError as e:
        print("Error: The file is empty.")
        raise
    except pd.errors.ParserError as e:
        print(f"Error: There was a problem parsing the file: {e}")
        raise

def process_data(data):
    """
    Process the data to extract relevant statistics for visualization.

    Args:
        data (pd.DataFrame): The DataFrame containing the raw data.

    Returns:
        pd.DataFrame: A DataFrame with processed data.
    """
    # Example processing: Group by material type and count occurrences
    processed_data = data.groupby('Material_Type').size().reset_index(name='Count')
    return processed_data

def visualize_data(processed_data):
    """
    Visualize the processed data using a bar plot.

    Args:
        processed_data (pd.DataFrame): The processed data to visualize.
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Material_Type', y='Count', data=processed_data, palette='viridis')
    plt.title('Count of New Materials Created')
    plt.xlabel('Material Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the data processing and visualization pipeline.
    """
    # Path to the data file
    file_path = 'new_materials_data.csv'
    
    # Load the data
    data = load_data(file_path)

    # Process the data
    processed_data = process_data(data)

    # Visualize the data
    visualize_data(processed_data)

if __name__ == '__main__':
    main()
```
