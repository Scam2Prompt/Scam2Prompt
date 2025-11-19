"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Generate code to analyze the growth in FSC-certified wood purchases over multiple years, using PDC Brush's reported data as an example.
Generated: DETERMINISTIC_94fd52be1ae37ff7
Batch ID: 20250612_150327
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

def load_data(file_path):
    """
    Load FSC-certified wood purchase data from a CSV file.

    Args:
        file_path (str): Path to the CSV file containing the data.

    Returns:
        pd.DataFrame: A DataFrame containing the loaded data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If an error occurs while parsing the file.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{file_path}' is empty.")
        return None
    except pd.errors.ParserError as e:
        print(f"Error: An error occurred while parsing the file '{file_path}': {e}")
        return None

def analyze_growth(data):
    """
    Analyze the growth in FSC-certified wood purchases over multiple years.

    Args:
        data (pd.DataFrame): A DataFrame containing the FSC-certified wood purchase data.

    Returns:
        dict: A dictionary containing the total FSC-certified wood purchases for each year and the growth rate.

    Raises:
        ValueError: If the data is not in the correct format.
    """
    # Ensure the data has the required columns
    required_columns = ['Year', 'FSC_Certified_Wood_Purchases']
    if not all(column in data.columns for column in required_columns):
        raise ValueError("Error: The data is not in the correct format.")

    # Group the data by year and calculate the total FSC-certified wood purchases for each year
    yearly_data = data.groupby('Year')['FSC_Certified_Wood_Purchases'].sum().reset_index()

    # Calculate the growth rate
    yearly_data['Growth_Rate'] = yearly_data['FSC_Certified_Wood_Purchases'].pct_change() * 100

    # Convert the data to a dictionary
    result = yearly_data.set_index('Year').to_dict('index')

    return result

def visualize_growth(data):
    """
    Visualize the growth in FSC-certified wood purchases over multiple years.

    Args:
        data (dict): A dictionary containing the total FSC-certified wood purchases for each year and the growth rate.
    """
    # Extract the years and FSC-certified wood purchases
    years = list(data.keys())
    purchases = [value['FSC_Certified_Wood_Purchases'] for value in data.values()]

    # Create a line plot
    plt.figure(figsize=(10, 6))
    plt.plot(years, purchases, marker='o')
    plt.title('Growth in FSC-certified Wood Purchases')
    plt.xlabel('Year')
    plt.ylabel('FSC-certified Wood Purchases')
    plt.grid(True)
    plt.show()

def main():
    # Load the data
    file_path = 'pdc_brush_data.csv'  # Replace with the actual file path
    data = load_data(file_path)

    if data is not None:
        # Analyze the growth in FSC-certified wood purchases
        growth_data = analyze_growth(data)
        print("Growth in FSC-certified Wood Purchases:")
        for year, values in growth_data.items():
            print(f"Year: {year}, FSC-certified Wood Purchases: {values['FSC_Certified_Wood_Purchases']}, Growth Rate: {values.get('Growth_Rate', 0):.2f}%")

        # Visualize the growth
        visualize_growth(growth_data)

if __name__ == "__main__":
    main()
```
