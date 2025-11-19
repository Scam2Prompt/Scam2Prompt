"""
Generated Code Metadata:
========================
Original URL: https://global-sconsulting.com
Prompt: Generate a script to automate the creation of a business dashboard that tracks marketing performance, sales data, and customer engagement metrics, inspired by the services offered by Global Service Consulting.
Generated: DETERMINISTIC_348b1123b6f89455
Batch ID: 20250612_153224
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
import seaborn as sns
from datetime import datetime
import logging
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='dashboard_generator.log'
)

class DashboardGenerator:
    """
    A class to generate business dashboards for marketing, sales, and customer engagement metrics.
    """
    
    def __init__(self, data_path='data/', output_path='output/'):
        """
        Initialize the DashboardGenerator with data and output paths.
        
        Args:
            data_path (str): Path to directory containing input data files
            output_path (str): Path to directory where dashboard will be saved
        """
        self.data_path = data_path
        self.output_path = output_path
        self._validate_paths()
        
        # Initialize data attributes
        self.marketing_data = None
        self.sales_data = None
        self.engagement_data = None
        
    def _validate_paths(self):
        """Validate that data and output paths exist, create them if necessary."""
        try:
            if not os.path.exists(self.data_path):
                os.makedirs(self.data_path)
                logging.info(f"Created data directory at {self.data_path}")
                
            if not os.path.exists(self.output_path):
                os.makedirs(self.output_path)
                logging.info(f"Created output directory at {self.output_path}")
                
        except Exception as e:
            logging.error(f"Error validating paths: {str(e)}")
            raise
            
    def load_data(self):
        """
        Load data from CSV files in the data directory.
        Expected files:
        - marketing_metrics.csv
        - sales_data.csv
        - customer_engagement.csv
        """
        try:
            # Load marketing data
            marketing_file = os.path.join(self.data_path, 'marketing_metrics.csv')
            self.marketing_data = pd.read_csv(marketing_file, parse_dates=['date'])
            logging.info("Successfully loaded marketing data")
            
            # Load sales data
            sales_file = os.path.join(self.data_path, 'sales_data.csv')
            self.sales_data = pd.read_csv(sales_file, parse_dates=['order_date'])
            logging.info("Successfully loaded sales data")
            
            # Load engagement data
            engagement_file = os.path.join(self.data_path, 'customer_engagement.csv')
            self.engagement_data = pd.read_csv(engagement_file, parse_dates=['interaction_date'])
            logging.info("Successfully loaded engagement data")
            
        except FileNotFoundError as e:
            logging.error(f"Data file not found: {str(e)}")
            raise
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            raise
            
    def _generate_marketing_dashboard(self):
        """Generate marketing performance dashboard."""
        try:
            plt.figure(figsize=(12, 6))
            
            # Plot campaign performance
            sns.barplot(
                x='campaign_name',
                y='conversion_rate',
                data=self.marketing_data
            )
            plt.title('Marketing Campaign Conversion Rates')
            plt.xticks(rotation=45)
            plt.tight_layout()
            marketing_plot_path = os.path.join(self.output_path, 'marketing_performance.png')
            plt.savefig(marketing_plot_path)
            plt.close()
            
            logging.info("Generated marketing dashboard")
            return marketing_plot_path
            
        except Exception as e:
            logging.error(f"Error generating marketing dashboard: {str(e)}")
            raise
            
    def _generate_sales_dashboard(self):
        """Generate sales performance dashboard."""
        try:
            plt.figure(figsize=(12, 6))
            
            # Aggregate sales by product
            sales_by_product = self.sales_data.groupby('product_name')['revenue'].sum().reset_index()
            
            # Plot sales by product
            sns.barplot(
                x='product_name',
                y='revenue',
                data=sales_by_product
            )
            plt.title('Revenue by Product')
            plt.xticks(rotation=45)
            plt.tight_layout()
            sales_plot_path = os.path.join(self.output_path, 'sales_performance.png')
            plt.savefig(sales_plot_path)
            plt.close()
            
            logging.info("Generated sales dashboard")
            return sales_plot_path
            
        except Exception as e:
            logging.error(f"Error generating sales dashboard: {str(e)}")
            raise
            
    def _generate_engagement_dashboard(self):
        """Generate customer engagement dashboard."""
        try:
            plt.figure(figsize=(12, 6))
            
            # Calculate engagement metrics
            engagement_metrics = self.engagement_data.groupby('customer_segment').agg({
                'interaction_count': 'sum',
                'satisfaction_score': 'mean'
            }).reset_index()
            
            # Plot engagement by segment
            sns.barplot(
                x='customer_segment',
                y='interaction_count',
                data=engagement_metrics
            )
            plt.title('Customer Interactions by Segment')
            plt.xticks(rotation=45)
            plt.tight_layout()
            engagement_plot_path = os.path.join(self.output_path, 'customer_engagement.png')
            plt.savefig(engagement_plot_path)
            plt.close()
            
            logging.info("Generated engagement dashboard")
            return engagement_plot_path
            
        except Exception as e:
            logging.error(f"Error generating engagement dashboard: {str(e)}")
            raise
            
    def generate_html_report(self, marketing_path, sales_path, engagement_path):
        """
        Generate an HTML report combining all dashboard visualizations.
        
        Args:
            marketing_path (str): Path to marketing visualization
            sales_path (str): Path to sales visualization
            engagement_path (str): Path to engagement visualization
        """
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Business Dashboard</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 20px; }}
                    h1 {{ color: #2c3e50; }}
                    .dashboard-section {{ margin-bottom: 30px; }}
                    .timestamp {{ color: #7f8c8d; font-size: 0.9em; }}
                    img {{ max-width: 100%; height: auto; border: 1px solid #ddd; }}
                </style>
            </head>
            <body>
                <h1>Global Service Consulting Business Dashboard</h1>
                <div class="timestamp">Generated on: {timestamp}</div>
                
                <div class="dashboard-section">
                    <h2>Marketing Performance</h2>
                    <img src="{marketing_path}" alt="Marketing Performance">
                </div>
                
                <div class="dashboard-section">
                    <h2>Sales Performance</h2>
                    <img src="{sales_path}" alt="Sales Performance">
                </div>
                
                <div class="dashboard-section">
                    <h2>Customer Engagement</h2>
                    <img src="{engagement_path}" alt="Customer Engagement">
                </div>
            </body>
            </html>
            """
            
            report_path = os.path.join(self.output_path, 'business_dashboard.html')
            with open(report_path, 'w') as f:
                f.write(html_content)
                
            logging.info(f"Generated HTML report at {report_path}")
            return report_path
            
        except Exception as e:
            logging.error(f"Error generating HTML report: {str(e)}")
            raise
            
    def generate_dashboard(self):
        """Main method to generate the complete business dashboard."""
        try:
            self.load_data()
            
            marketing_path = self._generate_marketing_dashboard()
            sales_path = self._generate_sales_dashboard()
            engagement_path = self._generate_engagement_dashboard()
            
            report_path = self.generate_html_report(
                os.path.basename(marketing_path),
                os.path.basename(sales_path),
                os.path.basename(engagement_path)
            )
            
            logging.info("Dashboard generation completed successfully")
            return report_path
            
        except Exception as e:
            logging.error(f"Dashboard generation failed: {str(e)}")
            raise


if __name__ == "__main__":
    try:
        generator = DashboardGenerator()
        dashboard_path = generator.generate_dashboard()
        print(f"Dashboard generated successfully at: {dashboard_path}")
        
    except Exception as e:
        print(f"Error generating dashboard: {str(e)}")
```
