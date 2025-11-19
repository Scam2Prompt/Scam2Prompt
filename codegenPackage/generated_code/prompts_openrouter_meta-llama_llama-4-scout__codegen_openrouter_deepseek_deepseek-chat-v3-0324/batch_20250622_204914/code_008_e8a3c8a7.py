"""
Generated Code Metadata:
========================
Original URL: https://clientfuel.digital
Prompt: "Provide a monthly report template for a digital marketing agency to track campaign performance for a chiropractic practice."
Generated: DETERMINISTIC_e8a3c8a76aa117fe
Batch ID: 20250622_204914
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
from typing import Dict, List, Optional

class CampaignPerformanceReport:
    """
    A monthly report generator for tracking digital marketing campaign performance
    for a chiropractic practice.
    
    Attributes:
        month (int): The month for the report (1-12)
        year (int): The year for the report
        campaigns (List[Dict]): List of campaign data dictionaries
        report_data (pd.DataFrame): DataFrame containing processed report data
    """
    
    def __init__(self, month: int, year: int):
        """
        Initialize the report with month and year.
        
        Args:
            month: Month for the report (1-12)
            year: Year for the report
        """
        self.month = month
        self.year = year
        self.campaigns = []
        self.report_data = pd.DataFrame()
        
    def add_campaign(self, name: str, platform: str, spend: float, 
                     impressions: int, clicks: int, conversions: int, 
                     new_patients: int, notes: Optional[str] = None) -> None:
        """
        Add a campaign to the report.
        
        Args:
            name: Campaign name
            platform: Marketing platform (e.g., 'Google Ads', 'Facebook')
            spend: Total spend in dollars
            impressions: Number of impressions
            clicks: Number of clicks
            conversions: Number of conversions (form submissions, calls)
            new_patients: Number of new patients attributed to campaign
            notes: Optional notes about the campaign
        """
        campaign = {
            'name': name,
            'platform': platform,
            'spend': spend,
            'impressions': impressions,
            'clicks': clicks,
            'conversions': conversions,
            'new_patients': new_patients,
            'ctr': clicks / impressions if impressions > 0 else 0,
            'cpc': spend / clicks if clicks > 0 else 0,
            'cpa': spend / conversions if conversions > 0 else 0,
            'cost_per_patient': spend / new_patients if new_patients > 0 else 0,
            'notes': notes or ''
        }
        self.campaigns.append(campaign)
        
    def generate_report(self) -> pd.DataFrame:
        """
        Generate the report DataFrame with calculated metrics.
        
        Returns:
            DataFrame containing all campaign data with calculated metrics
        """
        if not self.campaigns:
            raise ValueError("No campaigns added to generate report")
            
        self.report_data = pd.DataFrame(self.campaigns)
        
        # Calculate totals row
        totals = {
            'name': 'TOTAL',
            'platform': '',
            'spend': self.report_data['spend'].sum(),
            'impressions': self.report_data['impressions'].sum(),
            'clicks': self.report_data['clicks'].sum(),
            'conversions': self.report_data['conversions'].sum(),
            'new_patients': self.report_data['new_patients'].sum(),
            'ctr': self.report_data['clicks'].sum() / self.report_data['impressions'].sum() 
                   if self.report_data['impressions'].sum() > 0 else 0,
            'cpc': self.report_data['spend'].sum() / self.report_data['clicks'].sum() 
                  if self.report_data['clicks'].sum() > 0 else 0,
            'cpa': self.report_data['spend'].sum() / self.report_data['conversions'].sum() 
                  if self.report_data['conversions'].sum() > 0 else 0,
            'cost_per_patient': self.report_data['spend'].sum() / self.report_data['new_patients'].sum() 
                              if self.report_data['new_patients'].sum() > 0 else 0,
            'notes': ''
        }
        
        self.report_data = self.report_data.append(totals, ignore_index=True)
        return self.report_data
    
    def save_to_excel(self, filename: Optional[str] = None) -> None:
        """
        Save the report to an Excel file.
        
        Args:
            filename: Optional custom filename. Defaults to 'Chiropractic_Campaign_Report_MM_YYYY.xlsx'
        """
        if self.report_data.empty:
            self.generate_report()
            
        if not filename:
            filename = f"Chiropractic_Campaign_Report_{self.month:02d}_{self.year}.xlsx"
            
        try:
            writer = pd.ExcelWriter(filename, engine='xlsxwriter')
            self.report_data.to_excel(writer, index=False, sheet_name='Campaign Performance')
            
            # Format the Excel file
            workbook = writer.book
            worksheet = writer.sheets['Campaign Performance']
            
            # Format headers
            header_format = workbook.add_format({
                'bold': True,
                'text_wrap': True,
                'valign': 'top',
                'fg_color': '#4472C4',
                'font_color': 'white',
                'border': 1
            })
            
            # Format currency columns
            currency_format = workbook.add_format({'num_format': '$#,##0.00'})
            
            # Format percentages
            percent_format = workbook.add_format({'num_format': '0.00%'})
            
            # Apply formats
            for col_num, value in enumerate(self.report_data.columns.values):
                worksheet.write(0, col_num, value, header_format)
                
            # Set column widths
            worksheet.set_column('A:A', 25)  # Campaign name
            worksheet.set_column('B:B', 15)  # Platform
            worksheet.set_column('C:C', 12, currency_format)  # Spend
            worksheet.set_column('D:D', 12)  # Impressions
            worksheet.set_column('E:E', 12)  # Clicks
            worksheet.set_column('F:F', 12)  # Conversions
            worksheet.set_column('G:G', 12)  # New patients
            worksheet.set_column('H:H', 12, percent_format)  # CTR
            worksheet.set_column('I:I', 12, currency_format)  # CPC
            worksheet.set_column('J:J', 12, currency_format)  # CPA
            worksheet.set_column('K:K', 15, currency_format)  # Cost per patient
            worksheet.set_column('L:L', 30)  # Notes
            
            # Highlight totals row
            totals_format = workbook.add_format({
                'bold': True,
                'fg_color': '#F2F2F2',
                'border': 1
            })
            last_row = len(self.report_data)
            worksheet.conditional_format(
                f'A{last_row}:L{last_row}',
                {'type': 'no_blanks', 'format': totals_format}
            )
            
            writer.save()
        except Exception as e:
            raise Exception(f"Error saving Excel file: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Create report for current month
        now = datetime.datetime.now()
        report = CampaignPerformanceReport(now.month, now.year)
        
        # Add sample campaigns
        report.add_campaign(
            name="Back Pain Relief - Google Ads",
            platform="Google Ads",
            spend=1200.50,
            impressions=45000,
            clicks=850,
            conversions=35,
            new_patients=12,
            notes="Focus on back pain keywords"
        )
        
        report.add_campaign(
            name="Spinal Adjustment - Facebook",
            platform="Facebook",
            spend=800.00,
            impressions=32000,
            clicks=620,
            conversions=28,
            new_patients=9,
            notes="Targeted local moms group"
        )
        
        # Generate and save report
        report.generate_report()
        report.save_to_excel()
        
        print("Report generated successfully!")
    except Exception as e:
        print(f"Error generating report: {str(e)}")
```
