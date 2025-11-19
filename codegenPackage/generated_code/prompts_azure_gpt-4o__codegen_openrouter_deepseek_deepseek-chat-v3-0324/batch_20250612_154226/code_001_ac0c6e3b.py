"""
Generated Code Metadata:
========================
Original URL: https://sunsystems.hk
Prompt: Generate code to create a custom financial report using Infor SunSystems advanced reporting capabilities, tailored for Hong Kong businesses.
Generated: DETERMINISTIC_ac0c6e3bb2054cfb
Batch ID: 20250612_154226
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
import numpy as np
from datetime import datetime
import sunsystems_api as ss  # Hypothetical SunSystems API wrapper
import locale

# Set locale for Hong Kong
locale.setlocale(locale.LC_ALL, 'en_HK.UTF-8')

class HongKongFinancialReport:
    """
    Custom financial report generator for Hong Kong businesses using SunSystems.
    Handles HK-specific requirements like tax calculations and reporting formats.
    """
    
    def __init__(self, company_code, fiscal_year, report_currency='HKD'):
        """
        Initialize the financial report generator.
        
        Args:
            company_code (str): Company identifier in SunSystems
            fiscal_year (int): Fiscal year for the report
            report_currency (str): Currency for report (default: HKD)
        """
        self.company_code = company_code
        self.fiscal_year = fiscal_year
        self.report_currency = report_currency
        self.ss_client = ss.SunSystemsClient()
        
        # HK-specific configuration
        self.hk_tax_rate = 0.165  # Profits tax rate for Hong Kong
        self.hk_reporting_standards = "HKFRS"
        
    def connect_to_sunsystems(self):
        """Establish connection to SunSystems API."""
        try:
            self.ss_client.connect(company=self.company_code)
            return True
        except ss.SunSystemsConnectionError as e:
            print(f"Connection failed: {str(e)}")
            return False
    
    def fetch_gl_data(self, start_date, end_date):
        """
        Fetch general ledger data from SunSystems.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            
        Returns:
            DataFrame: GL data with HK-specific account mappings
        """
        try:
            gl_data = self.ss_client.get_gl_transactions(
                start_date=start_date,
                end_date=end_date,
                currency=self.report_currency
            )
            
            # Apply HK-specific account mappings
            gl_data = self._apply_hk_account_mappings(gl_data)
            return gl_data
        except ss.SunSystemsDataError as e:
            print(f"Error fetching GL data: {str(e)}")
            return pd.DataFrame()
    
    def _apply_hk_account_mappings(self, gl_data):
        """Apply Hong Kong specific account mappings to GL data."""
        # HK-specific account categories
        hk_mappings = {
            '4': 'Revenue',
            '5': 'Cost of Sales',
            '6': 'Operating Expenses',
            '7': 'Other Income',
            '8': 'Other Expenses',
            '9': 'Taxation'
        }
        
        gl_data['HK_Category'] = gl_data['Account'].str[0].map(hk_mappings)
        return gl_data
    
    def generate_profit_tax_calculation(self, gl_data):
        """
        Calculate Hong Kong Profits Tax based on GL data.
        
        Args:
            gl_data (DataFrame): General ledger data
            
        Returns:
            dict: Tax calculation results
        """
        try:
            # Calculate assessable profits
            revenue = gl_data[gl_data['HK_Category'] == 'Revenue']['Amount'].sum()
            cost_of_sales = gl_data[gl_data['HK_Category'] == 'Cost of Sales']['Amount'].sum()
            operating_exp = gl_data[gl_data['HK_Category'] == 'Operating Expenses']['Amount'].sum()
            
            gross_profit = revenue - cost_of_sales
            net_profit = gross_profit - operating_exp
            
            # Apply HK tax rules (simplified)
            taxable_profit = max(0, net_profit)  # No negative tax
            tax_payable = taxable_profit * self.hk_tax_rate
            
            return {
                'revenue': revenue,
                'cost_of_sales': cost_of_sales,
                'gross_profit': gross_profit,
                'operating_expenses': operating_exp,
                'net_profit': net_profit,
                'taxable_profit': taxable_profit,
                'tax_payable': tax_payable
            }
        except Exception as e:
            print(f"Error in tax calculation: {str(e)}")
            return {}
    
    def generate_balance_sheet(self, gl_data, as_of_date):
        """
        Generate HK-formatted balance sheet.
        
        Args:
            gl_data (DataFrame): General ledger data
            as_of_date (str): Balance sheet date in YYYY-MM-DD format
            
        Returns:
            DataFrame: Formatted balance sheet
        """
        try:
            # Group by account type (simplified for example)
            balance_sheet = gl_data.groupby('HK_Category')['Amount'].sum().reset_index()
            
            # Format for HK reporting
            balance_sheet['Amount_HKD'] = balance_sheet['Amount'].apply(
                lambda x: locale.currency(x, symbol=True, grouping=True)
            )
            
            balance_sheet['As_of_Date'] = as_of_date
            balance_sheet['Reporting_Standard'] = self.hk_reporting_standards
            
            return balance_sheet
        except Exception as e:
            print(f"Error generating balance sheet: {str(e)}")
            return pd.DataFrame()
    
    def generate_full_report(self, output_format='excel'):
        """
        Generate complete financial report for Hong Kong business.
        
        Args:
            output_format (str): 'excel' or 'pdf' output format
            
        Returns:
            bool: True if report generated successfully
        """
        try:
            if not self.connect_to_sunsystems():
                return False
                
            # Set report period (full fiscal year)
            start_date = f"{self.fiscal_year}-04-01"  # Assuming April start for HK fiscal year
            end_date = f"{self.fiscal_year + 1}-03-31"
            
            # Fetch data
            gl_data = self.fetch_gl_data(start_date, end_date)
            if gl_data.empty:
                return False
                
            # Generate report components
            tax_calc = self.generate_profit_tax_calculation(gl_data)
            balance_sheet = self.generate_balance_sheet(gl_data, end_date)
            
            # Generate final report
            report_data = {
                'company_code': self.company_code,
                'fiscal_year': self.fiscal_year,
                'report_currency': self.report_currency,
                'tax_calculation': tax_calc,
                'balance_sheet': balance_sheet.to_dict('records'),
                'generated_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            
            # Output based on format
            if output_format == 'excel':
                self._export_to_excel(report_data)
            elif output_format == 'pdf':
                self._export_to_pdf(report_data)
            else:
                print("Unsupported output format")
                return False
                
            return True
        except Exception as e:
            print(f"Error generating full report: {str(e)}")
            return False
    
    def _export_to_excel(self, report_data):
        """Export report data to Excel format."""
        writer = pd.ExcelWriter(f"HK_Financial_Report_{self.company_code}_{self.fiscal_year}.xlsx")
        
        # Create worksheets
        summary_df = pd.DataFrame([{
            'Company': report_data['company_code'],
            'Fiscal Year': report_data['fiscal_year'],
            'Currency': report_data['report_currency'],
            'Generated Date': report_data['generated_date']
        }])
        
        tax_df = pd.DataFrame([report_data['tax_calculation']])
        bs_df = pd.DataFrame(report_data['balance_sheet'])
        
        summary_df.to_excel(writer, sheet_name='Summary', index=False)
        tax_df.to_excel(writer, sheet_name='Tax Calculation', index=False)
        bs_df.to_excel(writer, sheet_name='Balance Sheet', index=False)
        
        writer.close()
    
    def _export_to_pdf(self, report_data):
        """Export report data to PDF format."""
        # Implementation would use a PDF library like ReportLab
        pass

# Example usage
if __name__ == "__main__":
    report_generator = HongKongFinancialReport(
        company_code="HKCOMP123",
        fiscal_year=2023
    )
    
    if report_generator.generate_full_report(output_format='excel'):
        print("Financial report generated successfully")
    else:
        print("Failed to generate financial report")
```
