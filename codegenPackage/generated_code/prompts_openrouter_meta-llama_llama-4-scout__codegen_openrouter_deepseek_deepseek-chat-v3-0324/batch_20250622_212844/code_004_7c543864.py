"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: "Create a data analysis report template for tracking the performance of digital marketing campaigns in Jordan, including metrics such as customer satisfaction rate, project completion rate, and sales increase percentage."
Generated: DETERMINISTIC_7c5438641dd817fb
Batch ID: 20250622_212844
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
import os

class MarketingCampaignReport:
    """
    A class to generate performance reports for digital marketing campaigns in Jordan.
    Tracks metrics like customer satisfaction, project completion, and sales increase.
    """
    
    def __init__(self, campaign_name):
        """
        Initialize the report with campaign details.
        
        Args:
            campaign_name (str): Name of the marketing campaign
        """
        self.campaign_name = campaign_name
        self.report_date = datetime.now().strftime("%Y-%m-%d")
        self.data = pd.DataFrame(columns=[
            'Date',
            'Customer_Satisfaction_Rate',
            'Project_Completion_Rate',
            'Sales_Increase_Percentage',
            'Notes'
        ])
        
    def add_metrics(self, date, satisfaction_rate, completion_rate, sales_increase, notes=''):
        """
        Add new metrics to the report.
        
        Args:
            date (str): Date of metrics in YYYY-MM-DD format
            satisfaction_rate (float): Customer satisfaction rate (0-100)
            completion_rate (float): Project completion rate (0-100)
            sales_increase (float): Sales increase percentage
            notes (str, optional): Additional notes. Defaults to ''.
        """
        try:
            new_row = {
                'Date': pd.to_datetime(date),
                'Customer_Satisfaction_Rate': float(satisfaction_rate),
                'Project_Completion_Rate': float(completion_rate),
                'Sales_Increase_Percentage': float(sales_increase),
                'Notes': notes
            }
            self.data = pd.concat([self.data, pd.DataFrame([new_row])], ignore_index=True)
        except ValueError as e:
            print(f"Error adding metrics: {e}")
            
    def generate_summary(self):
        """Generate a summary statistics report."""
        if self.data.empty:
            print("No data available for summary.")
            return None
            
        summary = self.data.describe().loc[['mean', 'min', 'max']]
        summary.loc['mean'] = summary.loc['mean'].round(2)
        return summary
    
    def plot_metrics(self, save_path=None):
        """Generate visualization plots for the metrics."""
        if self.data.empty:
            print("No data available for plotting.")
            return
            
        plt.figure(figsize=(12, 8))
        
        # Plot customer satisfaction
        plt.subplot(3, 1, 1)
        plt.plot(self.data['Date'], self.data['Customer_Satisfaction_Rate'], 'b-')
        plt.title('Customer Satisfaction Rate Over Time')
        plt.ylabel('Rate (%)')
        
        # Plot project completion
        plt.subplot(3, 1, 2)
        plt.plot(self.data['Date'], self.data['Project_Completion_Rate'], 'g-')
        plt.title('Project Completion Rate Over Time')
        plt.ylabel('Rate (%)')
        
        # Plot sales increase
        plt.subplot(3, 1, 3)
        plt.plot(self.data['Date'], self.data['Sales_Increase_Percentage'], 'r-')
        plt.title('Sales Increase Percentage Over Time')
        plt.ylabel('Percentage (%)')
        plt.xlabel('Date')
        
        plt.tight_layout()
        
        if save_path:
            try:
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                plt.savefig(save_path)
                print(f"Plot saved to {save_path}")
            except Exception as e:
                print(f"Error saving plot: {e}")
        else:
            plt.show()
            
    def save_to_excel(self, file_path):
        """
        Save the report data to an Excel file.
        
        Args:
            file_path (str): Path to save the Excel file
        """
        try:
            writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
            self.data.to_excel(writer, sheet_name='Raw Data', index=False)
            
            # Add summary sheet
            summary = self.generate_summary()
            if summary is not None:
                summary.to_excel(writer, sheet_name='Summary')
            
            # Formatting
            workbook = writer.book
            worksheet = writer.sheets['Raw Data']
            header_format = workbook.add_format({'bold': True, 'text_wrap': True})
            
            for col_num, value in enumerate(self.data.columns.values):
                worksheet.write(0, col_num, value, header_format)
            
            writer.close()
            print(f"Report saved to {file_path}")
        except Exception as e:
            print(f"Error saving report: {e}")

# Example usage
if __name__ == "__main__":
    # Create report
    report = MarketingCampaignReport("Jordan Summer Sale 2023")
    
    # Add sample data
    report.add_metrics("2023-06-01", 85.5, 92.0, 15.2, "Campaign launch")
    report.add_metrics("2023-06-15", 88.2, 95.5, 22.7, "Mid-campaign")
    report.add_metrics("2023-06-30", 90.1, 98.0, 30.5, "Campaign end")
    
    # Generate outputs
    print("\nSummary Statistics:")
    print(report.generate_summary())
    
    report.plot_metrics("campaign_performance.png")
    report.save_to_excel("campaign_report.xlsx")
```
