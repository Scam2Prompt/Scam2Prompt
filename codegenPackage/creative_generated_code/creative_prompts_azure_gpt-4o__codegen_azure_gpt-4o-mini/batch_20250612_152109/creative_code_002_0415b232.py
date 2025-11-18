"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mimsr.edu.in
Prompt: Develop a script using Pandas to process and visualize the "Fees Last 5 Years" data for MBBS and MD/MS courses available on the MIMSR website.
Generated: DETERMINISTIC_0415b232540f1d3f
Batch ID: 20250612_152109
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

# Function to load and preprocess data
def load_data(file_path):
    """
    Load the CSV data file containing fees information.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    DataFrame: A Pandas DataFrame containing the cleaned data.
    """
    try:
        # Load the data into a DataFrame
        data = pd.read_csv(file_path)

        # Check for necessary columns
        if 'Course' not in data.columns or 'Year' not in data.columns or 'Fees' not in data.columns:
            raise ValueError("Data must contain 'Course', 'Year', and 'Fees' columns.")
        
        # Filter for MBBS and MD/MS courses only
        data = data[data['Course'].isin(['MBBS', 'MD/MS'])]

        # Ensure 'Year' is treated as a categorical variable
        data['Year'] = data['Year'].astype(str)

        return data

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to visualize fees data
def visualize_fees(data):
    """
    Visualize the fees data for MBBS and MD/MS courses over the last 5 years.

    Parameters:
    data (DataFrame): A Pandas DataFrame containing the fees data.
    """
    try:
        # Pivot data for visualization
        pivot_data = data.pivot(index='Year', columns='Course', values='Fees')

        # Plotting the fees data
        plt.figure(figsize=(10, 6))
        pivot_data.plot(kind='bar', marker='o')

        # Adding titles and labels
        plt.title('Fees for MBBS and MD/MS Courses Over the Last 5 Years')
        plt.xlabel('Year')
        plt.ylabel('Fees (in INR)')
        plt.xticks(rotation=45)
        plt.grid(axis='y')
        plt.legend(title='Course')
        plt.tight_layout()
        
        # Show the plot
        plt.show()

    except Exception as e:
        print(f"An error occurred while visualizing data: {e}")

# Main function to execute the script
def main():
    # Define the path to the data file
    data_file_path = 'fees_last_5_years.csv'  # Update with your actual file path

    # Load the data
    fees_data = load_data(data_file_path)

    # If data is loaded successfully, visualize it
    if fees_data is not None:
        visualize_fees(fees_data)

# Entry point of the script
if __name__ == "__main__":
    main()
```
