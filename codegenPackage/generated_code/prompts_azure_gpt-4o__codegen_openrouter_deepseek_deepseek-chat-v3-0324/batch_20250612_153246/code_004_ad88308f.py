"""
Generated Code Metadata:
========================
Original URL: https://kalinski-energia.pl
Prompt: Generate code to automate energy consumption analysis for enterprises, using Python and Excel, based on the solutions provided by Jacek Kaliński.
Generated: DETERMINISTIC_ad88308f168fcafc
Batch ID: 20250612_153246
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
import openpyxl
from openpyxl.styles import Font, PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows
import matplotlib.pyplot as plt
from datetime import datetime
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='energy_consumption_analysis.log'
)

class EnergyConsumptionAnalyzer:
    """
    A class to analyze enterprise energy consumption data from Excel files.
    """
    
    def __init__(self, input_file_path, output_dir='output'):
        """
        Initialize the analyzer with input file path and output directory.
        
        Args:
            input_file_path (str): Path to the input Excel file
            output_dir (str): Directory to save output files (default: 'output')
        """
        self.input_file_path = input_file_path
        self.output_dir = output_dir
        self.df = None
        self.report_data = {}
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
        
    def load_data(self):
        """
        Load data from the input Excel file into a pandas DataFrame.
        
        Returns:
            bool: True if data loaded successfully, False otherwise
        """
        try:
            self.df = pd.read_excel(
                self.input_file_path,
                parse_dates=['Timestamp'],
                index_col='Timestamp'
            )
            logging.info(f"Successfully loaded data from {self.input_file_path}")
            return True
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            return False
    
    def preprocess_data(self):
        """
        Preprocess the loaded data by handling missing values and resampling.
        """
        try:
            # Forward fill missing values
            self.df.ffill(inplace=True)
            
            # Resample to hourly data if needed
            if not pd.infer_freq(self.df.index):
                self.df = self.df.resample('H').mean()
                
            logging.info("Data preprocessing completed successfully")
        except Exception as e:
            logging.error(f"Error during data preprocessing: {str(e)}")
    
    def analyze_consumption(self):
        """
        Perform energy consumption analysis and generate key metrics.
        """
        try:
            # Basic statistics
            self.report_data['total_consumption'] = self.df['Consumption'].sum()
            self.report_data['average_daily'] = self.df['Consumption'].resample('D').sum().mean()
            self.report_data['peak_consumption'] = self.df['Consumption'].max()
            self.report_data['peak_time'] = self.df['Consumption'].idxmax()
            
            # Time-based analysis
            self.report_data['hourly_avg'] = self.df.groupby(self.df.index.hour).mean()
            self.report_data['daily_avg'] = self.df.resample('D').sum()
            self.report_data['monthly_avg'] = self.df.resample('M').sum()
            
            # Identify top consumption periods
            top_periods = self.df.nlargest(5, 'Consumption')
            self.report_data['top_periods'] = top_periods
            
            logging.info("Energy consumption analysis completed")
        except Exception as e:
            logging.error(f"Error during consumption analysis: {str(e)}")
    
    def generate_visualizations(self):
        """
        Generate visualizations for the analyzed data.
        """
        try:
            # Create visualization directory
            viz_dir = os.path.join(self.output_dir, 'visualizations')
            os.makedirs(viz_dir, exist_ok=True)
            
            # Hourly consumption pattern
            plt.figure(figsize=(12, 6))
            self.report_data['hourly_avg']['Consumption'].plot(kind='bar')
            plt.title('Average Hourly Energy Consumption')
            plt.xlabel('Hour of Day')
            plt.ylabel('Consumption (kWh)')
            plt.savefig(os.path.join(viz_dir, 'hourly_consumption.png'))
            plt.close()
            
            # Daily consumption trend
            plt.figure(figsize=(12, 6))
            self.report_data['daily_avg']['Consumption'].plot()
            plt.title('Daily Energy Consumption Trend')
            plt.xlabel('Date')
            plt.ylabel('Consumption (kWh)')
            plt.savefig(os.path.join(viz_dir, 'daily_trend.png'))
            plt.close()
            
            # Monthly consumption
            plt.figure(figsize=(12, 6))
            self.report_data['monthly_avg']['Consumption'].plot(kind='bar')
            plt.title('Monthly Energy Consumption')
            plt.xlabel('Month')
            plt.ylabel('Consumption (kWh)')
            plt.savefig(os.path.join(viz_dir, 'monthly_consumption.png'))
            plt.close()
            
            logging.info("Visualizations generated successfully")
        except Exception as e:
            logging.error(f"Error generating visualizations: {str(e)}")
    
    def generate_report(self):
        """
        Generate a comprehensive Excel report with analysis results.
        """
        try:
            report_path = os.path.join(self.output_dir, 'energy_consumption_report.xlsx')
            workbook = openpyxl.Workbook()
            
            # Summary sheet
            summary_sheet = workbook.active
            summary_sheet.title = "Summary"
            
            # Add summary data
            summary_data = [
                ["Total Consumption (kWh)", self.report_data['total_consumption']],
                ["Average Daily Consumption (kWh)", self.report_data['average_daily']],
                ["Peak Consumption (kWh)", self.report_data['peak_consumption']],
                ["Peak Consumption Time", self.report_data['peak_time']]
            ]
            
            for row in summary_data:
                summary_sheet.append(row)
            
            # Format summary sheet
            header_font = Font(bold=True)
            for cell in summary_sheet[1]:
                cell.font = header_font
            
            # Hourly averages sheet
            hourly_sheet = workbook.create_sheet("Hourly Averages")
            hourly_df = self.report_data['hourly_avg'].reset_index()
            hourly_df.columns = ['Hour', 'Average Consumption (kWh)']
            
            for r in dataframe_to_rows(hourly_df, index=False, header=True):
                hourly_sheet.append(r)
            
            # Top consumption periods sheet
            top_sheet = workbook.create_sheet("Top Consumption Periods")
            top_df = self.report_data['top_periods'].reset_index()
            top_df.columns = ['Timestamp', 'Consumption (kWh)']
            
            for r in dataframe_to_rows(top_df, index=False, header=True):
                top_sheet.append(r)
            
            # Highlight peak periods
            red_fill = PatternFill(start_color='FFC7CE', end_color='FFC7CE', fill_type='solid')
            for row in top_sheet.iter_rows(min_row=2, max_row=6, min_col=2, max_col=2):
                for cell in row:
                    if cell.value == self.report_data['peak_consumption']:
                        cell.fill = red_fill
            
            # Save the workbook
            workbook.save(report_path)
            logging.info(f"Report generated successfully at {report_path}")
            return report_path
        except Exception as e:
            logging.error(f"Error generating report: {str(e)}")
            return None
    
    def run_analysis(self):
        """
        Run the complete analysis pipeline.
        """
        if not self.load_data():
            return False
        
        self.preprocess_data()
        self.analyze_consumption()
        self.generate_visualizations()
        report_path = self.generate_report()
        
        return report_path is not None


# Example usage
if __name__ == "__main__":
    analyzer = EnergyConsumptionAnalyzer('energy_data.xlsx')
    success = analyzer.run_analysis()
    
    if success:
        print("Energy consumption analysis completed successfully!")
    else:
        print("Error occurred during analysis. Check logs for details.")
```
