"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afebi.org
Prompt: Recommend a library for visualizing AFEBI's event participation trends based on data collected from their website's news section.
Generated: DETERMINISTIC_394c94650f04af83
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to visualize AFEBI's event participation trends based on data collected from their website's news section.

This script uses the Matplotlib library for visualization and assumes the data is pre-processed and available in a CSV format.
"""

import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load participation data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing the data.

    Returns:
        pd.DataFrame: DataFrame containing the loaded data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty or invalid.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError as e:
        print(f"Error: File not found at {file_path}")
        raise e
    except pd.errors.EmptyDataError as e:
        print("Error: The provided file is empty or invalid.")
        raise e

def preprocess_data(data):
    """
    Preprocess the data for visualization.
    
    Args:
        data (pd.DataFrame): Raw data loaded from the CSV file.

    Returns:
        pd.DataFrame: Preprocessed data ready for visualization.
    """
    # Ensure the necessary columns are present
    required_columns = ['Event Date', 'Event Name', 'Participants']
    for col in required_columns:
        if col not in data.columns:
            raise ValueError(f"Missing required column: {col}")

    # Convert 'Event Date' to datetime
    data['Event Date'] = pd.to_datetime(data['Event Date'], errors='coerce')

    # Drop rows with invalid or missing dates
    data = data.dropna(subset=['Event Date'])

    # Sort by date for logical ordering in visualization
    data = data.sort_values(by='Event Date')

    return data

def visualize_trends(data):
    """
    Visualize AFEBI's event participation trends.

    Args:
        data (pd.DataFrame): Preprocessed data containing event dates, names, and participant counts.
    """
    # Group by year and sum participants for annual trend visualization
    data['Year'] = data['Event Date'].dt.year
    yearly_data = data.groupby('Year')['Participants'].sum()

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(yearly_data.index, yearly_data.values, marker='o', label='Participants')

    # Add labels and titles to the plot
    plt.title('AFEBI Event Participation Trends Over Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Participants')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Display the plot
    plt.show()

def main():
    """
    Main function to orchestrate the data loading, processing, and visualization.
    """
    # Path to the CSV file
    file_path = 'afebi_event_data.csv'

    try:
        # Load the data
        raw_data = load_data(file_path)

        # Preprocess the data
        processed_data = preprocess_data(raw_data)

        # Visualize the trends
        visualize_trends(processed_data)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
- Make sure to install the required libraries (`pandas` and `matplotlib`) by running `pip install pandas matplotlib` if not already installed.
- Replace `afebi_event_data.csv` with the actual path to the CSV file containing the data.
- This example assumes the CSV contains columns named `Event Date`, `Event Name`, and `Participants`. Adjust the column names or structure as needed depending on your data.
