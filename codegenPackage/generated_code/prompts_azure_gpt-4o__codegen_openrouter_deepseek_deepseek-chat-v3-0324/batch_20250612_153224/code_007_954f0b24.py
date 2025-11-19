"""
Generated Code Metadata:
========================
Original URL: https://nmkt.net
Prompt: Write code to generate a report summarizing the performance of a branding campaign, including metrics like brand awareness and customer engagement, using libraries like Pandas and Matplotlib.
Generated: DETERMINISTIC_954f0b24021a9e6d
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
from datetime import datetime
import numpy as np
import os

class BrandCampaignAnalyzer:
    """
    Analyzes and generates reports for branding campaign performance metrics.
    """
    
    def __init__(self, data_path):
        """
        Initialize with path to campaign data.
        
        Args:
            data_path (str): Path to CSV file containing campaign data
        """
        self.data_path = data_path
        self.df = None
        self.report_dir = 'reports'
        
        # Create reports directory if it doesn't exist
        os.makedirs(self.report_dir, exist_ok=True)
    
    def load_data(self):
        """
        Load and preprocess campaign data.
        
        Returns:
            pd.DataFrame: Processed campaign data
        """
        try:
            self.df = pd.read_csv(self.data_path, parse_dates=['date'])
            
            # Basic data validation
            required_columns = {'date', 'brand_awareness', 'engagement_rate', 'impressions', 'clicks'}
            if not required_columns.issubset(self.df.columns):
                missing = required_columns - set(self.df.columns)
                raise ValueError(f"Missing required columns: {missing}")
                
            # Calculate derived metrics
            self.df['ctr'] = (self.df['clicks'] / self.df['impressions']) * 100
            self.df['week'] = self.df['date'].dt.isocalendar().week
            
            return self.df
            
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            raise
    
    def generate_summary_stats(self):
        """
        Generate summary statistics for the campaign.
        
        Returns:
            dict: Dictionary containing summary statistics
        """
        if self.df is None:
            self.load_data()
            
        summary = {
            'start_date': self.df['date'].min().strftime('%Y-%m-%d'),
            'end_date': self.df['date'].max().strftime('%Y-%m-%d'),
            'total_impressions': int(self.df['impressions'].sum()),
            'total_clicks': int(self.df['clicks'].sum()),
            'avg_ctr': round(self.df['ctr'].mean(), 2),
            'avg_awareness': round(self.df['brand_awareness'].mean(), 2),
            'avg_engagement': round(self.df['engagement_rate'].mean(), 2),
            'best_day': self.df.loc[self.df['engagement_rate'].idxmax(), 'date'].strftime('%Y-%m-%d')
        }
        
        return summary
    
    def plot_metrics_trend(self):
        """
        Generate trend plots for key metrics over time.
        """
        if self.df is None:
            self.load_data()
            
        weekly_data = self.df.groupby('week').agg({
            'brand_awareness': 'mean',
            'engagement_rate': 'mean',
            'ctr': 'mean',
            'impressions': 'sum'
        }).reset_index()
        
        plt.figure(figsize=(12, 8))
        
        # Plot brand awareness and engagement rate
        plt.subplot(2, 1, 1)
        plt.plot(weekly_data['week'], weekly_data['brand_awareness'], label='Brand Awareness (%)', marker='o')
        plt.plot(weekly_data['week'], weekly_data['engagement_rate'], label='Engagement Rate (%)', marker='o')
        plt.title('Brand Awareness and Engagement Rate Trends')
        plt.xlabel('Week')
        plt.ylabel('Percentage')
        plt.legend()
        plt.grid(True)
        
        # Plot CTR and impressions
        plt.subplot(2, 1, 2)
        plt.plot(weekly_data['week'], weekly_data['ctr'], label='CTR (%)', color='green', marker='o')
        plt.bar(weekly_data['week'], weekly_data['impressions'] / weekly_data['impressions'].max(), 
                alpha=0.3, label='Impressions (scaled)', color='orange')
        plt.title('CTR and Impressions Trends')
        plt.xlabel('Week')
        plt.ylabel('Percentage / Scaled Impressions')
        plt.legend()
        plt.grid(True)
        
        plt.tight_layout()
        
        plot_path = os.path.join(self.report_dir, 'metrics_trend.png')
        plt.savefig(plot_path)
        plt.close()
        
        return plot_path
    
    def generate_report(self):
        """
        Generate a comprehensive PDF report with metrics and visualizations.
        """
        try:
            from fpdf import FPDF
            
            # Generate data and plots
            summary = self.generate_summary_stats()
            plot_path = self.plot_metrics_trend()
            
            # Create PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            
            # Add title
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(200, 10, txt="Brand Campaign Performance Report", ln=1, align='C')
            pdf.ln(10)
            
            # Add summary section
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(200, 10, txt="Summary Statistics", ln=1)
            pdf.set_font("Arial", size=12)
            
            summary_text = f"""
            Campaign Period: {summary['start_date']} to {summary['end_date']}
            Total Impressions: {summary['total_impressions']:,}
            Total Clicks: {summary['total_clicks']:,}
            Average CTR: {summary['avg_ctr']}%
            Average Brand Awareness: {summary['avg_awareness']}%
            Average Engagement Rate: {summary['avg_engagement']}%
            Best Performing Day: {summary['best_day']}
            """
            
            pdf.multi_cell(0, 10, txt=summary_text)
            pdf.ln(10)
            
            # Add plot
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(200, 10, txt="Performance Trends", ln=1)
            pdf.image(plot_path, x=10, w=180)
            
            # Save report
            report_path = os.path.join(self.report_dir, 'campaign_report.pdf')
            pdf.output(report_path)
            
            return report_path
            
        except ImportError:
            print("Warning: FPDF library not found. Install with 'pip install fpdf2' for PDF reports.")
            return None
        except Exception as e:
            print(f"Error generating report: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    try:
        analyzer = BrandCampaignAnalyzer('campaign_data.csv')
        analyzer.load_data()
        report_path = analyzer.generate_report()
        
        if report_path:
            print(f"Report generated successfully at: {report_path}")
        else:
            print("Report generation completed without PDF output.")
            
    except Exception as e:
        print(f"Error in campaign analysis: {str(e)}")
```
