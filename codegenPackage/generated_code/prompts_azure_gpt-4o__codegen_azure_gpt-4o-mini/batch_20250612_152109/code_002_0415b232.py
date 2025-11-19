"""
Generated Code Metadata:
========================
Original URL: https://mimsr.edu.in
Prompt: Develop a script using Pandas to process and visualize the "Fees Last 5 Years" data for MBBS and MD/MS courses available on the MIMSR website.
Generated: DETERMINISTIC_0415b232540f1d3f
Batch ID: 20250612_152109
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

# Function to load and process the fees data
def load_and_process_data(file_path):
    """
    Load the fees data from a CSV file and process it for visualization.

    Parameters:
    file_path (str): The path to the CSV file containing the fees data.

    Returns:
    pd.DataFrame: A DataFrame containing the processed fees data.
    """
    try:
        # Load the data into a DataFrame
        data = pd.read_csv(file_path)

        # Check if required columns are present
        required_columns = ['Year', 'Course', 'Fees']
        if not all(col in data.columns for col in required_columns):
            raise ValueError("CSV file must contain 'Year', 'Course', and 'Fees' columns.")

        # Filter data for MBBS and MD/MS courses
        filtered_data = data[data['Course'].isin(['MBBS', 'MD/MS'])]

        return filtered_data

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error

# Function to visualize the fees data
def visualize_fees(data):
    """
    Visualize the fees data for MBBS and MD/MS courses.

    Parameters:
    data (pd.DataFrame): The DataFrame containing the fees data.
    """
    if data.empty:
        print("No data available for visualization.")
        return

    # Pivot the data for better visualization
    pivot_data = data.pivot(index='Year', columns='Course', values='Fees')

    # Plotting the fees data
    plt.figure(figsize=(10, 6))
    pivot_data.plot(kind='bar', marker='o')
    plt.title('Fees for MBBS and MD/MS Courses Over the Last 5 Years')
    plt.xlabel('Year')
    plt.ylabel('Fees (in INR)')
    plt.xticks(rotation=45)
    plt.legend(title='Course')
    plt.grid(axis='y')
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()

# Main function to execute the script
def main():
    """
    Main function to execute the data loading and visualization.
    """
    # Path to the CSV file (update this path as necessary)
    file_path = 'fees_last_5_years.csv'

    # Load and process the data
    fees_data = load_and_process_data(file_path)

    # Visualize the fees data
    visualize_fees(fees_data)

# Entry point of the script
if __name__ == "__main__":
    main()
```
