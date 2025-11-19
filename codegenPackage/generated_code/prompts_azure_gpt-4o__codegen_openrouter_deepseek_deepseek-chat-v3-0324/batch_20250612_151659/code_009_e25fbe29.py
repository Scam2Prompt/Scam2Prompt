"""
Generated Code Metadata:
========================
Original URL: https://metamas.com.mx
Prompt: Generate a Python script to analyze sales data for Meta+, identifying trends in demand for stainless steel, aluminum, and other metals across different regions in Mexico.
Generated: DETERMINISTIC_e25fbe29bcd5d3b0
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class SalesAnalyzer:
    """
    A class to analyze sales data for Meta+ across different regions in Mexico.
    """
    
    def __init__(self, data_path):
        """
        Initialize the SalesAnalyzer with the path to the sales data.
        
        Args:
            data_path (str): Path to the sales data CSV file.
        """
        self.data_path = data_path
        self.data = None
        self.regions = None
        self.metals = None
        
    def load_data(self):
        """
        Load and preprocess the sales data.
        
        Raises:
            FileNotFoundError: If the data file is not found.
            ValueError: If the data is malformed.
        """
        try:
            # Load data with proper date parsing
            self.data = pd.read_csv(
                self.data_path,
                parse_dates=['date'],
                date_parser=lambda x: pd.to_datetime(x, format='%Y-%m-%d', errors='coerce')
            )
            
            # Basic data validation
            if self.data.empty:
                raise ValueError("Loaded data is empty")
                
            # Clean column names
            self.data.columns = self.data.columns.str.strip().str.lower().str.replace(' ', '_')
            
            # Validate required columns
            required_columns = {'date', 'region', 'metal_type', 'quantity', 'revenue'}
            if not required_columns.issubset(self.data.columns):
                missing = required_columns - set(self.data.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
            # Extract unique regions and metals
            self.regions = self.data['region'].unique()
            self.metals = self.data['metal_type'].unique()
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at {self.data_path}")
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def preprocess_data(self):
        """
        Clean and prepare the data for analysis.
        """
        # Handle missing values
        self.data = self.data.dropna(subset=['date', 'region', 'metal_type'])
        
        # Convert quantities to numeric
        self.data['quantity'] = pd.to_numeric(self.data['quantity'], errors='coerce')
        self.data['revenue'] = pd.to_numeric(self.data['revenue'], errors='coerce')
        
        # Filter out invalid data
        self.data = self.data[(self.data['quantity'] > 0) & (self.data['revenue'] > 0)]
        
        # Add derived columns
        self.data['year'] = self.data['date'].dt.year
        self.data['month'] = self.data['date'].dt.month
        self.data['quarter'] = self.data['date'].dt.quarter
        self.data['unit_price'] = self.data['revenue'] / self.data['quantity']
        
    def analyze_trends(self):
        """
        Analyze sales trends by region and metal type.
        
        Returns:
            dict: A dictionary containing various trend analyses.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        results = {}
        
        # Overall sales trends by metal
        metal_trends = self.data.groupby(['metal_type', 'year', 'quarter'])['quantity'].sum().unstack('metal_type')
        results['metal_trends'] = metal_trends
        
        # Regional trends
        regional_trends = self.data.groupby(['region', 'metal_type', 'year'])['quantity'].sum().unstack('metal_type')
        results['regional_trends'] = regional_trends
        
        # Price trends
        price_trends = self.data.groupby(['metal_type', 'year'])['unit_price'].mean().unstack('metal_type')
        results['price_trends'] = price_trends
        
        # Monthly seasonality
        monthly_trends = self.data.groupby(['metal_type', 'month'])['quantity'].mean().unstack('metal_type')
        results['monthly_trends'] = monthly_trends
        
        return results
    
    def visualize_trends(self, results, output_dir='output'):
        """
        Generate visualizations for the analyzed trends.
        
        Args:
            results (dict): Dictionary containing trend analysis results.
            output_dir (str): Directory to save visualizations.
        """
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        # Set style
        sns.set_style('whitegrid')
        plt.figure(figsize=(12, 8))
        
        # Plot metal trends
        results['metal_trends'].plot(title='Quarterly Sales by Metal Type')
        plt.ylabel('Quantity Sold')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/metal_trends.png')
        plt.close()
        
        # Plot regional trends
        for metal in self.metals:
            plt.figure(figsize=(12, 8))
            regional_data = results['regional_trends'][metal].unstack('region')
            regional_data.plot(title=f'Sales Trend for {metal} by Region')
            plt.ylabel('Quantity Sold')
            plt.tight_layout()
            plt.savefig(f'{output_dir}/regional_trends_{metal}.png')
            plt.close()
        
        # Plot price trends
        results['price_trends'].plot(title='Average Unit Price by Metal Type')
        plt.ylabel('Price (USD)')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/price_trends.png')
        plt.close()
        
        # Plot monthly seasonality
        results['monthly_trends'].plot(title='Average Monthly Sales by Metal Type')
        plt.ylabel('Average Quantity Sold')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/monthly_seasonality.png')
        plt.close()
    
    def generate_report(self, results, report_file='sales_report.txt'):
        """
        Generate a text report summarizing key findings.
        
        Args:
            results (dict): Dictionary containing trend analysis results.
            report_file (str): Path to save the report.
        """
        with open(report_file, 'w') as f:
            f.write("Meta+ Sales Analysis Report\n")
            f.write("==========================\n\n")
            
            # Overall trends
            f.write("Overall Sales Trends:\n")
            f.write(str(results['metal_trends'].tail(12)) + "\n\n")
            
            # Top performing regions
            f.write("Top Performing Regions:\n")
            regional_sales = self.data.groupby('region')['quantity'].sum().sort_values(ascending=False)
            f.write(str(regional_sales.head()) + "\n\n")
            
            # Metal performance
            f.write("Metal Performance:\n")
            metal_sales = self.data.groupby('metal_type')['quantity'].sum().sort_values(ascending=False)
            f.write(str(metal_sales) + "\n\n")
            
            # Price analysis
            f.write("Price Analysis:\n")
            avg_prices = self.data.groupby('metal_type')['unit_price'].mean().sort_values(ascending=False)
            f.write(str(avg_prices) + "\n\n")
            
            f.write(f"Report generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

def main():
    try:
        # Initialize analyzer
        analyzer = SalesAnalyzer('sales_data.csv')
        
        # Load and preprocess data
        analyzer.load_data()
        analyzer.preprocess_data()
        
        # Analyze trends
        results = analyzer.analyze_trends()
        
        # Generate visualizations
        analyzer.visualize_trends(results)
        
        # Generate report
        analyzer.generate_report(results)
        
        print("Analysis completed successfully. Check the output directory for results.")
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        raise

if __name__ == "__main__":
    main()
```
