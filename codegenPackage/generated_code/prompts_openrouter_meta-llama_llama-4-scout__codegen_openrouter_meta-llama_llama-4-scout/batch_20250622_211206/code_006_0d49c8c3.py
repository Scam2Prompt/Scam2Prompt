"""
Generated Code Metadata:
========================
Original URL: https://thefacesofsedonaandtheverdevalley.com
Prompt: "Write a Python script to analyze the distribution of professions among community directory listings and visualize the results using a bar chart or pie chart."
Generated: DETERMINISTIC_0d49c8c3b415bfa0
Batch ID: 20250622_211206
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_directory_listings(file_path):
    """
    Load community directory listings from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the directory listings.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file is malformed.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except pd.errors.EmptyDataError:
        logging.error(f"File is empty: {file_path}")
        raise
    except pd.errors.ParserError as e:
        logging.error(f"Error parsing file: {file_path} - {e}")
        raise

def extract_professions(directory_listings, profession_column):
    """
    Extract professions from the directory listings.

    Args:
        directory_listings (pd.DataFrame): A DataFrame containing the directory listings.
        profession_column (str): The column name containing the professions.

    Returns:
        list: A list of professions.

    Raises:
        ValueError: If the profession column does not exist.
    """
    if profession_column not in directory_listings.columns:
        logging.error(f"Profession column not found: {profession_column}")
        raise ValueError(f"Profession column not found: {profession_column}")
    return directory_listings[profession_column].tolist()

def count_professions(professions):
    """
    Count the occurrences of each profession.

    Args:
        professions (list): A list of professions.

    Returns:
        Counter: A Counter object containing the profession counts.
    """
    return Counter(professions)

def visualize_profession_distribution(profession_counts, chart_type='bar'):
    """
    Visualize the profession distribution using a bar chart or pie chart.

    Args:
        profession_counts (Counter): A Counter object containing the profession counts.
        chart_type (str, optional): The type of chart to use. Defaults to 'bar'.

    Raises:
        ValueError: If the chart type is not supported.
    """
    if chart_type not in ['bar', 'pie']:
        logging.error(f"Unsupported chart type: {chart_type}")
        raise ValueError(f"Unsupported chart type: {chart_type}")

    if chart_type == 'bar':
        plt.bar(profession_counts.keys(), profession_counts.values())
        plt.xlabel('Profession')
        plt.ylabel('Count')
        plt.title('Profession Distribution (Bar Chart)')
        plt.xticks(rotation=90)
    elif chart_type == 'pie':
        plt.pie(profession_counts.values(), labels=profession_counts.keys(), autopct='%1.1f%%')
        plt.title('Profession Distribution (Pie Chart)')

    plt.tight_layout()
    plt.show()

def main():
    file_path = 'directory_listings.csv'  # Replace with your file path
    profession_column = 'profession'  # Replace with your profession column name

    try:
        directory_listings = load_directory_listings(file_path)
        professions = extract_professions(directory_listings, profession_column)
        profession_counts = count_professions(professions)
        visualize_profession_distribution(profession_counts, chart_type='bar')
        visualize_profession_distribution(profession_counts, chart_type='pie')
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```
