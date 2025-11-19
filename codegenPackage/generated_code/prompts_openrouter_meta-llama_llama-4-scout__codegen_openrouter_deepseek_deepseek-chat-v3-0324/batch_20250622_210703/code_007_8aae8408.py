"""
Generated Code Metadata:
========================
Original URL: https://chayatime.com
Prompt: Develop a Python script to generate a weekly report on the best-selling ChayaTime products and their revenue.
Generated: DETERMINISTIC_8aae8408343bca75
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import datetime
from typing import List, Dict, Tuple
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sales_report.log'),
        logging.StreamHandler()
    ]
)

class SalesReporter:
    """Generates weekly reports for best-selling ChayaTime products."""
    
    def __init__(self, data_path: str, output_dir: str = 'reports'):
        """
        Initialize the SalesReporter.
        
        Args:
            data_path: Path to the sales data CSV file
            output_dir: Directory to save reports (default: 'reports')
        """
        self.data_path = data_path
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def load_data(self) -> pd.DataFrame:
        """Load and validate sales data."""
        try:
            df = pd.read_csv(self.data_path)
            required_columns = {'product_id', 'product_name', 'quantity', 'price', 'date'}
            if not required_columns.issubset(df.columns):
                raise ValueError(f"Missing required columns. Expected: {required_columns}")
            
            df['date'] = pd.to_datetime(df['date'])
            df['revenue'] = df['quantity'] * df['price']
            return df
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            raise

    def get_week_range(self, date: datetime.date) -> Tuple[datetime.date, datetime.date]:
        """Get the start and end dates of the week containing the given date."""
        start = date - datetime.timedelta(days=date.weekday())
        end = start + datetime.timedelta(days=6)
        return start, end
    
    def generate_report(self, report_date: datetime.date = None) -> Dict[str, pd.DataFrame]:
        """
        Generate weekly sales report.
        
        Args:
            report_date: Date to base the report on (default: current date)
            
        Returns:
            Dictionary containing:
                - top_products: DataFrame of top selling products
                - summary: DataFrame with summary statistics
        """
        if report_date is None:
            report_date = datetime.date.today()
            
        try:
            df = self.load_data()
            week_start, week_end = self.get_week_range(report_date)
            
            # Filter data for the week
            weekly_sales = df[
                (df['date'].dt.date >= week_start) & 
                (df['date'].dt.date <= week_end)
            ]
            
            if weekly_sales.empty:
                logging.warning(f"No sales data found for week {week_start} to {week_end}")
                return None
                
            # Calculate top products by revenue
            product_stats = weekly_sales.groupby(['product_id', 'product_name']).agg({
                'quantity': 'sum',
                'revenue': 'sum'
            }).sort_values('revenue', ascending=False)
            
            # Create summary statistics
            summary = pd.DataFrame({
                'total_revenue': [weekly_sales['revenue'].sum()],
                'total_units': [weekly_sales['quantity'].sum()],
                'unique_products': [weekly_sales['product_id'].nunique()],
                'start_date': [week_start],
                'end_date': [week_end]
            })
            
            return {
                'top_products': product_stats.reset_index(),
                'summary': summary
            }
            
        except Exception as e:
            logging.error(f"Error generating report: {str(e)}")
            raise
    
    def save_report(self, report: Dict[str, pd.DataFrame], format: str = 'csv') -> None:
        """
        Save report to files.
        
        Args:
            report: Report dictionary from generate_report()
            format: Output format ('csv' or 'excel')
        """
        if not report:
            logging.warning("No report data to save")
            return
            
        try:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            base_filename = f"sales_report_{timestamp}"
            
            if format == 'csv':
                report['top_products'].to_csv(
                    os.path.join(self.output_dir, f"{base_filename}_products.csv"),
                    index=False
                )
                report['summary'].to_csv(
                    os.path.join(self.output_dir, f"{base_filename}_summary.csv"),
                    index=False
                )
            elif format == 'excel':
                with pd.ExcelWriter(os.path.join(self.output_dir, f"{base_filename}.xlsx")) as writer:
                    report['top_products'].to_excel(writer, sheet_name='Top Products', index=False)
                    report['summary'].to_excel(writer, sheet_name='Summary', index=False)
            else:
                raise ValueError(f"Unsupported format: {format}")
                
            logging.info(f"Report saved to {self.output_dir}")
            
        except Exception as e:
            logging.error(f"Error saving report: {str(e)}")
            raise

def main():
    """Main execution function."""
    try:
        # Configuration - these would ideally come from config file/environment variables
        DATA_FILE = 'sales_data.csv'
        OUTPUT_DIR = 'weekly_reports'
        
        reporter = SalesReporter(DATA_FILE, OUTPUT_DIR)
        report = reporter.generate_report()
        
        if report:
            reporter.save_report(report, format='excel')
        
    except Exception as e:
        logging.error(f"Application error: {str(e)}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())
```
