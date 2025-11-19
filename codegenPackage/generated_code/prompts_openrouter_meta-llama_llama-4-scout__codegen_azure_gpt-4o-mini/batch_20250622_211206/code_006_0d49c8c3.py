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

def load_data(file_path):
    """
    Load community directory data from a CSV file.

    Args:
        file_path (str): The path to the CSV file containing directory listings.

    Returns:
        pd.DataFrame: A DataFrame containing the directory data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return pd.DataFrame()
    except pd.errors.ParserError:
        print("Error: The file could not be parsed.")
        return pd.DataFrame()

def analyze_professions(data):
    """
    Analyze the distribution of professions in the directory listings.

    Args:
        data (pd.DataFrame): The DataFrame containing directory data.

    Returns:
        pd.Series: A Series containing the count of each profession.
    """
    if 'profession' not in data.columns:
        print("Error: 'profession' column not found in the data.")
        return pd.Series()  # Return an empty Series on error

    profession_counts = data['profession'].value_counts()
    return profession_counts

def visualize_distribution(profession_counts):
    """
    Visualize the distribution of professions using a bar chart.

    Args:
        profession_counts (pd.Series): A Series containing the count of each profession.
    """
    if profession_counts.empty:
        print("No profession data to visualize.")
        return

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    profession_counts.plot(kind='bar', color='skyblue')
    plt.title('Distribution of Professions in Community Directory')
    plt.xlabel('Professions')
    plt.ylabel('Number of Listings')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
    plt.show()

def main():
    """
    Main function to execute the script.
    """
    file_path = 'community_directory.csv'  # Path to the CSV file
    data = load_data(file_path)  # Load the data
    profession_counts = analyze_professions(data)  # Analyze professions
    visualize_distribution(profession_counts)  # Visualize the results

if __name__ == "__main__":
    main()
```
