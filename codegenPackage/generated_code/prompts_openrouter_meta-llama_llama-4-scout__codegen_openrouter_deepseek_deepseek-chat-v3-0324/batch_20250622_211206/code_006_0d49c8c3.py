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
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def load_data(file_path):
    """
    Load data from a CSV file containing community directory listings.
    Expected columns: 'name', 'profession', etc.
    
    Args:
        file_path (str): Path to the CSV file.
    
    Returns:
        pandas.DataFrame: Loaded data.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not a valid CSV or missing required columns.
    """
    try:
        data = pd.read_csv(file_path)
        if 'profession' not in data.columns:
            raise ValueError("CSV file must contain 'profession' column.")
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise ValueError(f"Error loading CSV file: {e}")

def analyze_professions(data):
    """
    Analyze the distribution of professions in the data.
    
    Args:
        data (pandas.DataFrame): Data containing 'profession' column.
    
    Returns:
        dict: Profession counts sorted by frequency.
    """
    profession_counts = Counter(data['profession'].dropna())
    return dict(sorted(profession_counts.items(), key=lambda item: item[1], reverse=True))

def visualize_results(profession_counts, chart_type='bar'):
    """
    Visualize profession distribution using a bar chart or pie chart.
    
    Args:
        profession_counts (dict): Profession counts.
        chart_type (str): Type of chart ('bar' or 'pie').
    
    Raises:
        ValueError: If chart_type is invalid.
    """
    if not profession_counts:
        print("No profession data to visualize.")
        return

    professions = list(profession_counts.keys())
    counts = list(profession_counts.values())

    plt.figure(figsize=(10, 6))
    
    if chart_type == 'bar':
        plt.bar(professions, counts)
        plt.xlabel('Profession')
        plt.ylabel('Count')
        plt.title('Profession Distribution (Bar Chart)')
        plt.xticks(rotation=45, ha='right')
    elif chart_type == 'pie':
        plt.pie(counts, labels=professions, autopct='%1.1f%%')
        plt.title('Profession Distribution (Pie Chart)')
    else:
        raise ValueError("Invalid chart_type. Use 'bar' or 'pie'.")
    
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to load data, analyze professions, and visualize results.
    """
    try:
        # Replace with your file path
        file_path = 'community_directory.csv'
        data = load_data(file_path)
        profession_counts = analyze_professions(data)
        
        print("Profession Distribution:")
        for profession, count in profession_counts.items():
            print(f"{profession}: {count}")
        
        visualize_results(profession_counts, chart_type='bar')
        visualize_results(profession_counts, chart_type='pie')
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
```
