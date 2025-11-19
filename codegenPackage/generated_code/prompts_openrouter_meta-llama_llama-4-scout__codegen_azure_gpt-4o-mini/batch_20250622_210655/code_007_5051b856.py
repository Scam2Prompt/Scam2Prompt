"""
Generated Code Metadata:
========================
Original URL: https://gesec.com.co
Prompt: "Write a Python script to analyze and visualize incident rates in a workplace, helping to identify areas for improvement in the SG-SST implementation."
Generated: DETERMINISTIC_5051b856320e2607
Batch ID: 20250622_210655
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
    Load incident data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing incident data.

    Returns:
    pd.DataFrame: A DataFrame containing the incident data.
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

def preprocess_data(data):
    """
    Preprocess the incident data.

    Parameters:
    data (pd.DataFrame): The DataFrame containing incident data.

    Returns:
    pd.DataFrame: A cleaned DataFrame ready for analysis.
    """
    # Check for necessary columns
    required_columns = ['Date', 'Incident_Type', 'Location']
    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")

    # Convert 'Date' to datetime
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data.dropna(subset=['Date'], inplace=True)

    return data

def analyze_incidents(data):
    """
    Analyze incident rates by month and location.

    Parameters:
    data (pd.DataFrame): The DataFrame containing incident data.

    Returns:
    pd.DataFrame: A DataFrame summarizing incident counts by month and location.
    """
    # Extract month and year from the date
    data['YearMonth'] = data['Date'].dt.to_period('M')

    # Group by YearMonth and Location, then count incidents
    incident_summary = data.groupby(['YearMonth', 'Location']).size().reset_index(name='Incident_Count')
    return incident_summary

def visualize_incidents(incident_summary):
    """
    Visualize the incident rates using a bar plot.

    Parameters:
    incident_summary (pd.DataFrame): The DataFrame summarizing incident counts.
    """
    plt.figure(figsize=(12, 6))
    sns.barplot(data=incident_summary, x='YearMonth', y='Incident_Count', hue='Location')
    plt.title('Incident Rates by Month and Location')
    plt.xlabel('Month')
    plt.ylabel('Number of Incidents')
    plt.xticks(rotation=45)
    plt.legend(title='Location')
    plt.tight_layout()
    plt.show()

def main(file_path):
    """
    Main function to execute the incident analysis and visualization.

    Parameters:
    file_path (str): The path to the CSV file containing incident data.
    """
    # Load the data
    data = load_data(file_path)
    if data is None:
        return

    # Preprocess the data
    try:
        cleaned_data = preprocess_data(data)
    except ValueError as e:
        print(e)
        return

    # Analyze incidents
    incident_summary = analyze_incidents(cleaned_data)

    # Visualize incidents
    visualize_incidents(incident_summary)

if __name__ == "__main__":
    # Specify the path to the incident data CSV file
    file_path = 'incident_data.csv'
    main(file_path)
```
