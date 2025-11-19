"""
Generated Code Metadata:
========================
Original URL: https://bpkad.lamongankab.go.id
Prompt: Write a program to generate summary reports for APBD realization data, similar to the "Info Realisasi APBD" feature described on the BPKAD Lamongan website.
Generated: DETERMINISTIC_9384c01e8db234b8
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
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('apbd_report.log'),
        logging.StreamHandler()
    ]
)

class APBDReportGenerator:
    """
    A class to generate APBD realization reports from financial data.
    """
    
    def __init__(self, data_path: str, fiscal_year: int):
        """
        Initialize the APBD report generator.
        
        Args:
            data_path (str): Path to the APBD realization data file (Excel or CSV)
            fiscal_year (int): The fiscal year for the report
        """
        self.data_path = data_path
        self.fiscal_year = fiscal_year
        self.data = None
        self.report_date = datetime.now().strftime('%Y-%m-%d')
        
    def load_data(self) -> None:
        """
        Load APBD realization data from the specified file.
        
        Raises:
            FileNotFoundError: If data file doesn't exist
            ValueError: If data format is invalid
        """
        try:
            if self.data_path.endswith('.xlsx'):
                self.data = pd.read_excel(self.data_path)
            elif self.data_path.endswith('.csv'):
                self.data = pd.read_csv(self.data_path)
            else:
                raise ValueError("Unsupported file format. Please provide Excel (.xlsx) or CSV (.csv) file.")
            
            # Validate required columns
            required_columns = ['kode_rekening', 'uraian', 'anggaran', 'realisasi', 'persentase']
            missing_cols = [col for col in required_columns if col not in self.data.columns]
            
            if missing_cols:
                raise ValueError(f"Missing required columns: {', '.join(missing_cols)}")
                
            logging.info("Data loaded successfully")
            
        except FileNotFoundError:
            logging.error(f"Data file not found: {self.data_path}")
            raise
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            raise ValueError(f"Error loading data: {str(e)}")
    
    def clean_data(self) -> None:
        """
        Clean and preprocess the APBD data.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Convert numeric columns
            numeric_cols = ['anggaran', 'realisasi', 'persentase']
            for col in numeric_cols:
                self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
                
            # Fill NA values
            self.data.fillna({
                'anggaran': 0,
                'realisasi': 0,
                'persentase': 0
            }, inplace=True)
            
            # Clean uraian column
            self.data['uraian'] = self.data['uraian'].str.strip()
            
            logging.info("Data cleaning completed")
            
        except Exception as e:
            logging.error(f"Error cleaning data: {str(e)}")
            raise
    
    def generate_summary_report(self) -> Dict:
        """
        Generate a summary report of APBD realization.
        
        Returns:
            Dict: A dictionary containing summary statistics
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        try:
            # Calculate totals
            total_anggaran = self.data['anggaran'].sum()
            total_realisasi = self.data['realisasi'].sum()
            overall_percentage = (total_realisasi / total_anggaran * 100) if total_anggaran > 0 else 0
            
            # Group by first digit of kode_rekening (major category)
            self.data['kategori'] = self.data['kode_rekening'].astype(str).str[0]
            category_summary = self.data.groupby('kategori').agg({
                'anggaran': 'sum',
                'realisasi': 'sum'
            }).reset_index()
            
            # Calculate percentages
            category_summary['persentase'] = (category_summary['realisasi'] / 
                                            category_summary['anggaran'] * 100).round(2)
            
            # Convert to dictionary for easier processing
            category_summary = category_summary.to_dict('records')
            
            # Get top 5 programs with highest realization
            top_programs = self.data.nlargest(5, 'realisasi')[['uraian', 'anggaran', 'realisasi', 'persentase']]
            top_programs = top_programs.to_dict('records')
            
            # Get bottom 5 programs with lowest realization
            bottom_programs = self.data.nsmallest(5, 'persentase')[['uraian', 'anggaran', 'realisasi', 'persentase']]
            bottom_programs = bottom_programs.to_dict('records')
            
            report = {
                'fiscal_year': self.fiscal_year,
                'report_date': self.report_date,
                'total_anggaran': total_anggaran,
                'total_realisasi': total_realisasi,
                'overall_percentage': round(overall_percentage, 2),
                'category_summary': category_summary,
                'top_programs': top_programs,
                'bottom_programs': bottom_programs
            }
            
            logging.info("Summary report generated successfully")
            return report
            
        except Exception as e:
            logging.error(f"Error generating summary report: {str(e)}")
            raise
    
    def generate_visualizations(self, report: Dict, output_dir: str = 'output') -> None:
        """
        Generate visualizations from the report data.
        
        Args:
            report (Dict): The report dictionary from generate_summary_report()
            output_dir (str): Directory to save visualization files
        """
        try:
            import os
            os.makedirs(output_dir, exist_ok=True)
            
            # Pie chart of budget allocation by category
            categories = [f"Category {item['kategori']}" for item in report['category_summary']]
            anggaran = [item['anggaran'] for item in report['category_summary']]
            
            plt.figure(figsize=(10, 6))
            plt.pie(anggaran, labels=categories, autopct='%1.1f%%', startangle=140)
            plt.title(f'APBD {self.fiscal_year} - Budget Allocation by Category')
            plt.savefig(f'{output_dir}/budget_allocation.png')
            plt.close()
            
            # Bar chart of realization percentage by category
            categories = [f"Category {item['kategori']}" for item in report['category_summary']]
            percentages = [item['persentase'] for item in report['category_summary']]
            
            plt.figure(figsize=(10, 6))
            plt.bar(categories, percentages)
            plt.axhline(y=report['overall_percentage'], color='r', linestyle='--', label='Overall Average')
            plt.title(f'APBD {self.fiscal_year} - Realization Percentage by Category')
            plt.ylabel('Realization Percentage (%)')
            plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()
            plt.savefig(f'{output_dir}/realization_percentage.png')
            plt.close()
            
            logging.info(f"Visualizations saved to {output_dir}")
            
        except Exception as e:
            logging.error(f"Error generating visualizations: {str(e)}")
            raise
    
    def generate_html_report(self, report: Dict, output_file: str = 'apbd_report.html') -> None:
        """
        Generate an HTML report from the summary data.
        
        Args:
            report (Dict): The report dictionary from generate_summary_report()
            output_file (str): Path to save the HTML report
        """
        try:
            from jinja2 import Environment, FileSystemLoader
            import os
            
            # Set up Jinja2 environment
            env = Environment(loader=FileSystemLoader('.'))
            template = env.get_template('report_template.html') if os.path.exists('report_template.html') else None
            
            if template is None:
                # Use default template if custom template doesn't exist
                template_str = """
                <!DOCTYPE html>
                <html>
                <head>
                    <title>APBD Realization Report {{ fiscal_year }}</title>
                    <style>
                        body { font-family: Arial, sans-serif; margin: 20px; }
                        h1 { color: #2c3e50; }
                        .header { margin-bottom: 30px; }
                        .summary-card { 
                            background: #f8f9fa; 
                            border-radius: 5px; 
                            padding: 20px; 
                            margin-bottom: 20px; 
                            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                        }
                        table { 
                            width: 100%; 
                            border-collapse: collapse; 
                            margin-bottom: 20px;
                        }
                        th, td {
