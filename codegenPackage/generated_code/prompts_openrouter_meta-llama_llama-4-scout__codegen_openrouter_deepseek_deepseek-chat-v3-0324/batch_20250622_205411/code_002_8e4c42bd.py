"""
Generated Code Metadata:
========================
Original URL: https://balancerh.com
Prompt: Generate a code example for creating a salary structure report using a reporting library, with columns for job classes, salary ranges, and equity data, inspired by Balance RH's reporting features.
Generated: DETERMINISTIC_8e4c42bdc5230e41
Batch ID: 20250622_205411
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
from datetime import datetime
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SalaryStructureReport:
    """
    Generates a comprehensive salary structure report with job classes, salary ranges, and equity data.
    """
    
    def __init__(self, data_source: str):
        """
        Initialize the report generator with a data source.
        
        Args:
            data_source (str): Path to the data file (CSV, Excel, etc.)
        """
        self.data_source = data_source
        self.data = None
        self.report_data = None
        
    def load_data(self) -> None:
        """
        Load and validate the input data.
        
        Raises:
            FileNotFoundError: If data file doesn't exist
            ValueError: If required columns are missing
        """
        try:
            # Try to read CSV first, fall back to Excel
            try:
                self.data = pd.read_csv(self.data_source)
            except:
                self.data = pd.read_excel(self.data_source)
                
            # Validate required columns
            required_columns = ['job_class', 'min_salary', 'max_salary', 'gender', 'ethnicity', 'salary']
            missing_cols = [col for col in required_columns if col not in self.data.columns]
            
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")
                
            logger.info("Data loaded successfully")
            
        except FileNotFoundError:
            logger.error(f"Data file not found: {self.data_source}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
            
    def process_data(self) -> None:
        """
        Process the raw data into report-ready format.
        Calculates salary ranges, equity metrics, and aggregates by job class.
        """
        try:
            # Calculate compa-ratio (salary relative to midpoint)
            self.data['midpoint'] = (self.data['min_salary'] + self.data['max_salary']) / 2
            self.data['compa_ratio'] = self.data['salary'] / self.data['midpoint']
            
            # Group by job class and calculate metrics
            grouped = self.data.groupby('job_class').agg({
                'min_salary': 'min',
                'max_salary': 'max',
                'salary': ['mean', 'median'],
                'compa_ratio': 'mean',
                'gender': lambda x: (x == 'F').mean(),  # % female
                'ethnicity': lambda x: (x != 'White').mean()  # % non-white
            })
            
            # Flatten multi-index columns
            grouped.columns = ['_'.join(col).strip() for col in grouped.columns.values]
            
            # Rename columns for clarity
            grouped = grouped.rename(columns={
                'min_salary_min': 'salary_min',
                'max_salary_max': 'salary_max',
                'salary_mean': 'avg_salary',
                'salary_median': 'median_salary',
                'compa_ratio_mean': 'avg_compa_ratio',
                'gender_<lambda>': 'pct_female',
                'ethnicity_<lambda>': 'pct_minority'
            })
            
            self.report_data = grouped.reset_index()
            logger.info("Data processed successfully")
            
        except Exception as e:
            logger.error(f"Error processing data: {str(e)}")
            raise
            
    def generate_report(self, output_format: str = 'excel', output_path: Optional[str] = None) -> None:
        """
        Generate the final report in specified format.
        
        Args:
            output_format (str): 'excel', 'csv', or 'html'
            output_path (str): Optional path to save the report
            
        Raises:
            ValueError: If invalid output format is specified
        """
        if self.report_data is None:
            raise ValueError("No data available to generate report. Call process_data() first.")
            
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            default_filename = f"salary_structure_report_{timestamp}"
            
            if output_path is None:
                output_path = f"{default_filename}.{output_format.lower()}"
                
            if output_format.lower() == 'excel':
                self._generate_excel_report(output_path)
            elif output_format.lower() == 'csv':
                self._generate_csv_report(output_path)
            elif output_format.lower() == 'html':
                self._generate_html_report(output_path)
            else:
                raise ValueError(f"Unsupported output format: {output_format}")
                
            logger.info(f"Report generated successfully at {output_path}")
            
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
            raise
            
    def _generate_excel_report(self, output_path: str) -> None:
        """Generate Excel report with formatting."""
        writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
        self.report_data.to_excel(writer, sheet_name='Salary Structure', index=False)
        
        workbook = writer.book
        worksheet = writer.sheets['Salary Structure']
        
        # Format headers
        header_format = workbook.add_format({
            'bold': True,
            'text_wrap': True,
            'valign': 'top',
            'fg_color': '#4472C4',
            'font_color': 'white',
            'border': 1
        })
        
        for col_num, value in enumerate(self.report_data.columns.values):
            worksheet.write(0, col_num, value, header_format)
            
        # Auto-adjust column widths
        for i, col in enumerate(self.report_data.columns):
            max_len = max(
                self.report_data[col].astype(str).map(len).max(),
                len(col)
            )
            worksheet.set_column(i, i, max_len + 2)
            
        # Add conditional formatting for equity metrics
        equity_format = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})
        worksheet.conditional_format(
            'G2:H100',
            {
                'type': 'cell',
                'criteria': '<',
                'value': 0.3,
                'format': equity_format
            }
        )
        
        writer.close()
        
    def _generate_csv_report(self, output_path: str) -> None:
        """Generate CSV report."""
        self.report_data.to_csv(output_path, index=False)
        
    def _generate_html_report(self, output_path: str) -> None:
        """Generate HTML report with visualizations."""
        # Create styled table
        html = self.report_data.style\
            .background_gradient(subset=['avg_compa_ratio'], cmap='YlOrRd')\
            .bar(subset=['pct_female', 'pct_minority'], color='#5fba7d')\
            .format({
                'avg_salary': '${:,.0f}',
                'median_salary': '${:,.0f}',
                'avg_compa_ratio': '{:.2f}',
                'pct_female': '{:.1%}',
                'pct_minority': '{:.1%}'
            })\
            .set_table_styles([
                {'selector': 'th', 'props': [('background-color', '#4472C4'), ('color', 'white')]}
            ])\
            .hide_index()\
            .to_html()
            
        # Add title and timestamp
        full_html = f"""
        <html>
            <head>
                <title>Salary Structure Report</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 20px; }}
                    h1 {{ color: #2F5496; }}
                    .footer {{ font-size: 0.8em; color: #666; margin-top: 20px; }}
                </style>
            </head>
            <body>
                <h1>Salary Structure Report</h1>
                <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                {html}
                <div class="footer">
                    Note: Equity metrics highlighted in red indicate values below 30%
                </div>
            </body>
        </html>
        """
        
        with open(output_path, 'w') as f:
            f.write(full_html)
            
    def visualize_salary_ranges(self, output_path: Optional[str] = None) -> None:
        """
        Generate a visualization of salary ranges by job class.
        
        Args:
            output_path (str): Optional path to save the visualization image
        """
        try:
            plt.figure(figsize=(12, 8))
            
            # Sort by midpoint salary for better visualization
            viz_data = self.report_data.copy()
            viz_data['midpoint'] = (viz_data['salary_min'] + viz_data['salary_max']) / 2
            viz_data = viz_data.sort_values('mid
