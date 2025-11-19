"""
Generated Code Metadata:
========================
Original URL: https://fesit.cl
Prompt: Write code to analyze the fiscal impact of suspending taxpayer access to their tax credentials, referencing FESIT's criticism of the SII's temporary suspension of keys.
Generated: DETERMINISTIC_88802c3b41a408ef
Batch ID: 20250612_153517
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
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import requests
from typing import Dict, List, Optional, Tuple

class FiscalImpactAnalyzer:
    """
    Analyzes the fiscal impact of suspending taxpayer access to their tax credentials.
    References FESIT's criticism of the SII's temporary suspension of keys.
    """
    
    def __init__(self, api_endpoint: Optional[str] = None):
        """
        Initialize the analyzer with optional API endpoint for fetching data.
        
        Args:
            api_endpoint: Optional API endpoint to fetch taxpayer data
        """
        self.api_endpoint = api_endpoint
        self.taxpayer_data = None
        self.suspension_periods = []
        
    def fetch_taxpayer_data(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetch taxpayer data from API or local source.
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            
        Returns:
            DataFrame containing taxpayer data
            
        Raises:
            ValueError: If dates are invalid
            ConnectionError: If API connection fails
        """
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.strptime(end_date, '%Y-%m-%d')
            
            if start > end:
                raise ValueError("Start date must be before end date")
                
            if self.api_endpoint:
                params = {
                    'start_date': start_date,
                    'end_date': end_date
                }
                response = requests.get(self.api_endpoint, params=params)
                response.raise_for_status()
                data = response.json()
                return pd.DataFrame(data)
            else:
                # Mock data for demonstration
                date_range = pd.date_range(start, end)
                return pd.DataFrame({
                    'date': date_range,
                    'active_taxpayers': np.random.randint(10000, 50000, len(date_range)),
                    'tax_revenue': np.random.uniform(1000000, 5000000, len(date_range))
                })
                
        except ValueError as ve:
            raise ValueError(f"Invalid date format: {ve}")
        except requests.exceptions.RequestException as re:
            raise ConnectionError(f"Failed to fetch data: {re}")
            
    def add_suspension_period(self, start_date: str, end_date: str, reason: str) -> None:
        """
        Add a suspension period to analyze.
        
        Args:
            start_date: Start date of suspension in YYYY-MM-DD format
            end_date: End date of suspension in YYYY-MM-DD format
            reason: Reason for suspension
            
        Raises:
            ValueError: If dates are invalid
        """
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.strptime(end_date, '%Y-%m-%d')
            
            if start > end:
                raise ValueError("Start date must be before end date")
                
            self.suspension_periods.append({
                'start_date': start,
                'end_date': end,
                'reason': reason
            })
            
        except ValueError as ve:
            raise ValueError(f"Invalid date format: {ve}")
            
    def analyze_impact(self) -> Dict:
        """
        Analyze the fiscal impact of suspension periods.
        
        Returns:
            Dictionary containing analysis results with keys:
            - 'total_revenue_loss'
            - 'average_daily_loss'
            - 'affected_taxpayers'
            - 'suspension_details'
            
        Raises:
            ValueError: If no taxpayer data or suspension periods are set
        """
        if self.taxpayer_data is None:
            raise ValueError("Taxpayer data not loaded")
        if not self.suspension_periods:
            raise ValueError("No suspension periods defined")
            
        results = {
            'total_revenue_loss': 0,
            'average_daily_loss': 0,
            'affected_taxpayers': 0,
            'suspension_details': []
        }
        
        total_days = 0
        
        for period in self.suspension_periods:
            mask = (self.taxpayer_data['date'] >= period['start_date']) & \
                   (self.taxpayer_data['date'] <= period['end_date'])
            
            suspended_data = self.taxpayer_data[mask]
            
            if not suspended_data.empty:
                period_days = len(suspended_data)
                total_days += period_days
                
                avg_revenue = suspended_data['tax_revenue'].mean()
                avg_taxpayers = suspended_data['active_taxpayers'].mean()
                
                # Assume 20% revenue loss during suspension (adjust based on actual data)
                revenue_loss = avg_revenue * 0.2 * period_days
                
                results['total_revenue_loss'] += revenue_loss
                results['affected_taxpayers'] += avg_taxpayers * period_days
                
                results['suspension_details'].append({
                    'start_date': period['start_date'].strftime('%Y-%m-%d'),
                    'end_date': period['end_date'].strftime('%Y-%m-%d'),
                    'reason': period['reason'],
                    'revenue_loss': revenue_loss,
                    'affected_taxpayers': avg_taxpayers * period_days,
                    'duration_days': period_days
                })
        
        if total_days > 0:
            results['average_daily_loss'] = results['total_revenue_loss'] / total_days
            
        return results
        
    def generate_report(self, analysis_results: Dict, output_file: Optional[str] = None) -> None:
        """
        Generate a report of the fiscal impact analysis.
        
        Args:
            analysis_results: Results from analyze_impact()
            output_file: Optional file path to save report
            
        Returns:
            None (prints report to console or saves to file)
        """
        report = [
            "Fiscal Impact Analysis Report",
            "=================================",
            f"Total Revenue Loss: ${analysis_results['total_revenue_loss']:,.2f}",
            f"Average Daily Loss: ${analysis_results['average_daily_loss']:,.2f}",
            f"Total Affected Taxpayers: {analysis_results['affected_taxpayers']:,.0f}",
            "\nSuspension Period Details:"
        ]
        
        for detail in analysis_results['suspension_details']:
            report.extend([
                f"\nPeriod: {detail['start_date']} to {detail['end_date']}",
                f"Reason: {detail['reason']}",
                f"Duration: {detail['duration_days']} days",
                f"Revenue Loss: ${detail['revenue_loss']:,.2f}",
                f"Affected Taxpayers: {detail['affected_taxpayers']:,.0f}"
            ])
        
        report.append("\nNote: Analysis based on FESIT's criticism of SII's temporary suspension of keys")
        
        full_report = "\n".join(report)
        
        if output_file:
            with open(output_file, 'w') as f:
                f.write(full_report)
        else:
            print(full_report)
            
    def plot_impact(self, analysis_results: Dict) -> None:
        """
        Generate visualization of the fiscal impact.
        
        Args:
            analysis_results: Results from analyze_impact()
        """
        if not analysis_results['suspension_details']:
            print("No suspension data to plot")
            return
            
        periods = [
            f"{detail['start_date']}\nto\n{detail['end_date']}" 
            for detail in analysis_results['suspension_details']
        ]
        losses = [detail['revenue_loss'] for detail in analysis_results['suspension_details']]
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(periods, losses, color='red')
        
        plt.title('Revenue Loss During Suspension Periods')
        plt.ylabel('Revenue Loss (USD)')
        plt.xlabel('Suspension Period')
        plt.xticks(rotation=45, ha='right')
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'${height:,.0f}',
                    ha='center', va='bottom')
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    analyzer = FiscalImpactAnalyzer()
    
    # Load taxpayer data (mock in this example)
    analyzer.taxpayer_data = analyzer.fetch_taxpayer_data('2023-01-01', '2023-12-31')
    
    # Add suspension periods (example based on FESIT criticism)
    analyzer.add_suspension_period('2023-03-15', '2023-03-30', 'System maintenance')
    analyzer.add_suspension_period('2023-07-01', '2023-07-15', 'Security update')
    
    # Analyze impact
    results = analyzer.analyze_impact()
    
    # Generate report
    analyzer.generate_report(results)
    
    # Visualize
