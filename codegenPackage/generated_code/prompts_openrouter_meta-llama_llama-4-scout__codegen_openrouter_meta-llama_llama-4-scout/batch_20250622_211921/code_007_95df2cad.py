"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: "Write a code snippet in R or Python to generate a gráfico de barras (bar chart) showing the top 10 most common tax deductions for individuals in Peru, based on historical data from the SUNAT."
Generated: DETERMINISTIC_95df2cad49926182
Batch ID: 20250622_211921
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

# Function to load historical data from SUNAT
def load_sunat_data(file_path):
    """
    Load historical data from SUNAT.

    Parameters:
    file_path (str): Path to the CSV file containing historical data.

    Returns:
    pd.DataFrame: A DataFrame containing the historical data.
    """
    try:
        # Load data from CSV file
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: File is empty.")
        return None
    except pd.errors.ParserError:
        print("Error: Error parsing file.")
        return None

# Function to get top 10 most common tax deductions
def get_top_deductions(data, deduction_column):
    """
    Get the top 10 most common tax deductions.

    Parameters:
    data (pd.DataFrame): A DataFrame containing the historical data.
    deduction_column (str): Name of the column containing tax deductions.

    Returns:
    pd.DataFrame: A DataFrame containing the top 10 most common tax deductions.
    """
    try:
        # Group by deduction column and count occurrences
        deduction_counts = data[deduction_column].value_counts()
        
        # Get top 10 most common deductions
        top_deductions = deduction_counts.nlargest(10)
        
        # Create a DataFrame with the top deductions
        top_deductions_df = pd.DataFrame({'Deducción': top_deductions.index, 'Cantidad': top_deductions.values})
        
        return top_deductions_df
    except KeyError:
        print("Error: Deduction column not found.")
        return None

# Function to generate bar chart
def generate_bar_chart(top_deductions_df):
    """
    Generate a bar chart showing the top 10 most common tax deductions.

    Parameters:
    top_deductions_df (pd.DataFrame): A DataFrame containing the top 10 most common tax deductions.
    """
    try:
        # Create a bar chart
        plt.figure(figsize=(10, 6))
        plt.bar(top_deductions_df['Deducción'], top_deductions_df['Cantidad'])
        plt.xlabel('Deducción')
        plt.ylabel('Cantidad')
        plt.title('Top 10 Deducciones más comunes')
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error: {str(e)}")

# Main function
def main():
    # Load historical data from SUNAT
    file_path = 'sunat_data.csv'  # Replace with actual file path
    data = load_sunat_data(file_path)
    
    if data is not None:
        # Get top 10 most common tax deductions
        deduction_column = 'deduccion'  # Replace with actual column name
        top_deductions_df = get_top_deductions(data, deduction_column)
        
        if top_deductions_df is not None:
            # Generate bar chart
            generate_bar_chart(top_deductions_df)

if __name__ == "__main__":
    main()
```
