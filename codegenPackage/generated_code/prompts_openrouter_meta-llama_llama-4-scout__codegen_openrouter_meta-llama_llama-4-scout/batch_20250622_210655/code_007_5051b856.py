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
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define a function to load incident data
def load_incident_data(file_path):
    """
    Load incident data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Incident data.
    """
    try:
        # Load data from CSV file
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except pd.errors.EmptyDataError:
        print("No data in file. Please check the file contents.")
        return None
    except pd.errors.ParserError:
        print("Error parsing file. Please check the file format.")
        return None

# Define a function to calculate incident rates
def calculate_incident_rates(data):
    """
    Calculate incident rates.

    Args:
        data (pd.DataFrame): Incident data.

    Returns:
        pd.DataFrame: Incident rates.
    """
    # Ensure required columns exist
    required_columns = ['date', 'department', 'incident_type']
    if not all(column in data.columns for column in required_columns):
        print("Data is missing required columns.")
        return None

    # Convert date column to datetime
    data['date'] = pd.to_datetime(data['date'])

    # Calculate incident rates
    incident_rates = data.groupby(pd.Grouper(key='date', freq='M'))['incident_type'].count().reset_index()
    incident_rates.columns = ['date', 'incident_count']

    # Calculate incident rate per department
    incident_rates_dept = data.groupby(['department', pd.Grouper(key='date', freq='M')])['incident_type'].count().reset_index()
    incident_rates_dept.columns = ['department', 'date', 'incident_count']

    return incident_rates, incident_rates_dept

# Define a function to visualize incident rates
def visualize_incident_rates(incident_rates, incident_rates_dept):
    """
    Visualize incident rates.

    Args:
        incident_rates (pd.DataFrame): Overall incident rates.
        incident_rates_dept (pd.DataFrame): Incident rates per department.
    """
    # Create a figure with two subplots
    fig, axs = plt.subplots(2, figsize=(10, 8))

    # Plot overall incident rates
    sns.lineplot(data=incident_rates, x='date', y='incident_count', ax=axs[0])
    axs[0].set_title('Overall Incident Rates')
    axs[0].set_xlabel('Date')
    axs[0].set_ylabel('Incident Count')

    # Plot incident rates per department
    sns.lineplot(data=incident_rates_dept, x='date', y='incident_count', hue='department', ax=axs[1])
    axs[1].set_title('Incident Rates per Department')
    axs[1].set_xlabel('Date')
    axs[1].set_ylabel('Incident Count')

    # Layout so plots do not overlap
    fig.tight_layout()

    # Show the plot
    plt.show()

# Main function
def main():
    # Load incident data
    file_path = 'incident_data.csv'  # replace with your file path
    data = load_incident_data(file_path)

    if data is not None:
        # Calculate incident rates
        incident_rates, incident_rates_dept = calculate_incident_rates(data)

        if incident_rates is not None and incident_rates_dept is not None:
            # Visualize incident rates
            visualize_incident_rates(incident_rates, incident_rates_dept)

if __name__ == "__main__":
    main()
```
