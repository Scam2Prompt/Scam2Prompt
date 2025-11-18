"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Generate a Python script to analyze sales data for Meta+, identifying trends in demand for stainless steel, aluminum, and other metals across different regions in Mexico.
Generated: DETERMINISTIC_e25fbe29bcd5d3b0
Batch ID: 20250612_151659
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
import os

def load_sales_data(file_path):
    """
    Load sales data from a CSV file.
    
    Parameters:
        file_path (str): Path to the sales data CSV file.
        
    Returns:
        pd.DataFrame: Dataframe containing the sales data.
    """
    try:
        sales_data = pd.read_csv(file_path)
        return sales_data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        return None
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return None

def preprocess_data(data):
    """
    Preprocess sales data for analysis.
    
    Parameters:
        data (pd.DataFrame): Raw sales data.
        
    Returns:
        pd.DataFrame: Preprocessed sales data.
    """
    # Check if necessary columns exist
    required_columns = ['Region', 'Metal', 'Sales', 'Month']
    for col in required_columns:
        if col not in data.columns:
            raise ValueError(f"Missing required column: {col}")

    # Handle missing values
    data = data.dropna(subset=required_columns)
    
    # Ensure 'Sales' column is numeric
    data['Sales'] = pd.to_numeric(data['Sales'], errors='coerce')
    
    # Remove rows where 'Sales' could not be converted to numeric
    data = data.dropna(subset=['Sales'])
    
    return data

def analyze_trends(data):
    """
    Analyze trends in demand for different metals across regions.
    
    Parameters:
        data (pd.DataFrame): Preprocessed sales data.
        
    Returns:
        dict: Analysis results with trends per metal and region.
    """
    trends = {}
    
    # Group by Region and Metal, and calculate monthly averages
    grouped_data = data.groupby(['Region', 'Metal', 'Month']).agg({'Sales': 'sum'}).reset_index()
    
    # Identify trends for each metal in each region
    for region in grouped_data['Region'].unique():
        trends[region] = {}
        region_data = grouped_data[grouped_data['Region'] == region]
        
        for metal in region_data['Metal'].unique():
            metal_data = region_data[region_data['Metal'] == metal]
            
            avg_sales = metal_data.groupby('Month')['Sales'].mean()
            trends[region][metal] = avg_sales
    
    return trends

def plot_trends(trends, output_dir):
    """
    Plot sales trends for each metal and region, and save plots.
    
    Parameters:
        trends (dict): Sales trends data.
        output_dir (str): Directory to save plots.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for region, metals in trends.items():
        for metal, monthly_sales in metals.items():
            plt.figure(figsize=(10, 6))
            monthly_sales.plot(kind='bar', color='steelblue')
            plt.title(f'{metal} Sales Trends in {region}')
            plt.xlabel('Month')
            plt.ylabel('Average Sales')
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            
            plot_path = os.path.join(output_dir, f'{region}_{metal}_trends.png')
            plt.savefig(plot_path)
            plt.close()

def main():
    """
    Main function to execute the sales data analysis script.
    """
    # Configuration
    input_file = 'sales_data_mexico.csv'
    output_dir = 'sales_trends_plots'
    
    # Load data
    sales_data = load_sales_data(input_file)
    if sales_data is None:
        return
    
    # Preprocess data
    try:
        sales_data = preprocess_data(sales_data)
    except ValueError as e:
        print(f"Error during preprocessing: {e}")
        return
    
    # Analyze trends
    trends = analyze_trends(sales_data)
    
    # Plot trends
    plot_trends(trends, output_dir)
    
    print(f"Analysis completed. Plots saved to {output_dir}.")

if __name__ == '__main__':
    main()
```
