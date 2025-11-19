"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: Write code to analyze donation trends and generate reports for campaigns like "Donation Camp for Education Kit Distribution" mentioned on Youngistaan Foundation's website.
Generated: DETERMINISTIC_3e03e59143601393
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
import matplotlib.pyplot as plt
from datetime import datetime
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DonationAnalyzer:
    """
    A class to analyze donation trends and generate reports for campaigns.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with donation data.
        
        Args:
            data_path (str): Path to the donation data file (CSV or Excel)
        """
        self.data_path = data_path
        self.df = None
        self.campaign_name = None
        
    def load_data(self) -> None:
        """
        Load donation data from file.
        
        Raises:
            FileNotFoundError: If data file doesn't exist
            ValueError: If data file format is invalid
        """
        try:
            if self.data_path.endswith('.csv'):
                self.df = pd.read_csv(self.data_path)
            elif self.data_path.endswith(('.xls', '.xlsx')):
                self.df = pd.read_excel(self.data_path)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
            
            logger.info("Data loaded successfully")
            self._validate_data()
            
        except FileNotFoundError:
            logger.error(f"Data file not found at {self.data_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise ValueError(f"Error loading data: {str(e)}")
    
    def _validate_data(self) -> None:
        """
        Validate the loaded data has required columns.
        
        Raises:
            ValueError: If required columns are missing
        """
        required_columns = ['campaign_name', 'donation_amount', 'donation_date', 'donor_type']
        missing_cols = [col for col in required_columns if col not in self.df.columns]
        
        if missing_cols:
            raise ValueError(f"Missing required columns: {', '.join(missing_cols)}")
        
        # Convert date column to datetime
        try:
            self.df['donation_date'] = pd.to_datetime(self.df['donation_date'])
        except Exception as e:
            raise ValueError(f"Invalid date format in donation_date column: {str(e)}")
    
    def set_campaign(self, campaign_name: str) -> None:
        """
        Set the campaign to analyze.
        
        Args:
            campaign_name (str): Name of the campaign to analyze
        """
        self.campaign_name = campaign_name
        logger.info(f"Campaign set to: {self.campaign_name}")
    
    def get_donation_summary(self) -> Dict:
        """
        Generate summary statistics for the campaign.
        
        Returns:
            Dict: Dictionary containing summary statistics
            
        Raises:
            ValueError: If campaign is not set or no data found
        """
        if not self.campaign_name:
            raise ValueError("Campaign name not set. Use set_campaign() first.")
        
        campaign_data = self.df[self.df['campaign_name'] == self.campaign_name]
        
        if campaign_data.empty:
            raise ValueError(f"No data found for campaign: {self.campaign_name}")
        
        summary = {
            'total_donations': campaign_data['donation_amount'].sum(),
            'average_donation': campaign_data['donation_amount'].mean(),
            'min_donation': campaign_data['donation_amount'].min(),
            'max_donation': campaign_data['donation_amount'].max(),
            'donation_count': len(campaign_data),
            'unique_donors': campaign_data['donor_id'].nunique() if 'donor_id' in campaign_data.columns else None,
            'start_date': campaign_data['donation_date'].min().strftime('%Y-%m-%d'),
            'end_date': campaign_data['donation_date'].max().strftime('%Y-%m-%d')
        }
        
        logger.info(f"Generated summary for campaign: {self.campaign_name}")
        return summary
    
    def get_donation_trends(self, time_period: str = 'M') -> pd.DataFrame:
        """
        Analyze donation trends over time.
        
        Args:
            time_period (str): Time period for grouping ('D'=day, 'W'=week, 'M'=month)
            
        Returns:
            pd.DataFrame: DataFrame with donation trends
            
        Raises:
            ValueError: If campaign is not set or invalid time_period
        """
        if not self.campaign_name:
            raise ValueError("Campaign name not set. Use set_campaign() first.")
        
        if time_period not in ['D', 'W', 'M']:
            raise ValueError("Invalid time_period. Use 'D', 'W', or 'M'.")
        
        campaign_data = self.df[self.df['campaign_name'] == self.campaign_name]
        
        if campaign_data.empty:
            raise ValueError(f"No data found for campaign: {self.campaign_name}")
        
        trends = campaign_data.groupby(pd.Grouper(key='donation_date', freq=time_period)).agg({
            'donation_amount': ['sum', 'count', 'mean']
        })
        
        trends.columns = ['total_amount', 'donation_count', 'average_amount']
        trends = trends.reset_index()
        
        logger.info(f"Generated trends for campaign: {self.campaign_name}")
        return trends
    
    def get_donor_analysis(self) -> Dict:
        """
        Analyze donor types and their contributions.
        
        Returns:
            Dict: Dictionary with donor type analysis
            
        Raises:
            ValueError: If campaign is not set
        """
        if not self.campaign_name:
            raise ValueError("Campaign name not set. Use set_campaign() first.")
        
        campaign_data = self.df[self.df['campaign_name'] == self.campaign_name]
        
        if campaign_data.empty:
            raise ValueError(f"No data found for campaign: {self.campaign_name}")
        
        donor_analysis = campaign_data.groupby('donor_type').agg({
            'donation_amount': ['sum', 'count', 'mean'],
            'donor_id': 'nunique' if 'donor_id' in campaign_data.columns else None
        }).reset_index()
        
        # Clean up column names
        donor_analysis.columns = ['donor_type', 'total_amount', 'donation_count', 'average_amount']
        if 'donor_id' in campaign_data.columns:
            donor_analysis['unique_donors'] = donor_analysis.iloc[:, -1]
            donor_analysis = donor_analysis.drop(donor_analysis.columns[-2], axis=1)
        
        logger.info(f"Generated donor analysis for campaign: {self.campaign_name}")
        return donor_analysis.to_dict('records')
    
    def generate_report(self, output_path: Optional[str] = None) -> None:
        """
        Generate a comprehensive report with visualizations.
        
        Args:
            output_path (str, optional): Path to save the report. If None, shows plots.
        """
        if not self.campaign_name:
            raise ValueError("Campaign name not set. Use set_campaign() first.")
        
        try:
            # Create figure
            plt.figure(figsize=(15, 10))
            plt.suptitle(f"Donation Report: {self.campaign_name}", fontsize=16)
            
            # Get data
            summary = self.get_donation_summary()
            trends = self.get_donation_trends()
            donor_analysis = self.get_donor_analysis()
            
            # Plot 1: Donation trends over time
            plt.subplot(2, 2, 1)
            plt.plot(trends['donation_date'], trends['total_amount'], marker='o')
            plt.title('Donation Amount Over Time')
            plt.xlabel('Date')
            plt.ylabel('Amount (₹)')
            plt.grid(True)
            
            # Plot 2: Donation count over time
            plt.subplot(2, 2, 2)
            plt.bar(trends['donation_date'], trends['donation_count'])
            plt.title('Number of Donations Over Time')
            plt.xlabel('Date')
            plt.ylabel('Count')
            plt.grid(True)
            
            # Plot 3: Donor type contributions
            plt.subplot(2, 2, 3)
            donor_df = pd.DataFrame(donor_analysis)
            plt.pie(donor_df['total_amount'], labels=donor_df['donor_type'], autopct='%1.1f%%')
            plt.title('Donation Amount by Donor Type')
            
            # Plot 4: Summary statistics
            plt.subplot(2, 2, 4)
            stats = [
                f"Total: ₹{summary['total_donations']:,.2f}",
                f"Avg: ₹{summary['average_donation']:,.2f}",
                f"Min: ₹{summary['min_donation']:,.2f}",
                f"Max: ₹{summary['max_donation']:,.
