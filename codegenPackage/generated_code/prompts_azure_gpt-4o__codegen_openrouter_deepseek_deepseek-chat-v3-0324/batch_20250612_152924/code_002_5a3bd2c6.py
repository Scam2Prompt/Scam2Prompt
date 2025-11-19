"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Generate code to analyze public contributions data for a crowdfunded initiative like Uni4Kashmir, ensuring transparency and accountability in reporting.
Generated: DETERMINISTIC_5a3bd2c67f01235c
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('contribution_analysis.log'),
        logging.StreamHandler()
    ]
)

class ContributionAnalyzer:
    """
    A class to analyze public contributions data for crowdfunded initiatives.
    """
    
    def __init__(self, api_endpoint: Optional[str] = None, csv_path: Optional[str] = None):
        """
        Initialize the analyzer with either an API endpoint or CSV file path.
        
        Args:
            api_endpoint: URL to fetch contributions data from API
            csv_path: Path to local CSV file containing contributions data
        """
        self.api_endpoint = api_endpoint
        self.csv_path = csv_path
        self.contributions = None
        self.logger = logging.getLogger(__name__)
        
    def fetch_data(self) -> pd.DataFrame:
        """
        Fetch contributions data from either API or CSV file.
        
        Returns:
            DataFrame containing contributions data
            
        Raises:
            ValueError: If neither API endpoint nor CSV path is provided
            requests.exceptions.RequestException: If API request fails
            FileNotFoundError: If CSV file doesn't exist
            pd.errors.EmptyDataError: If CSV file is empty
        """
        if self.api_endpoint:
            try:
                response = requests.get(self.api_endpoint, timeout=10)
                response.raise_for_status()
                self.contributions = pd.DataFrame(response.json())
                self.logger.info(f"Successfully fetched {len(self.contributions)} records from API")
            except requests.exceptions.RequestException as e:
                self.logger.error(f"Failed to fetch data from API: {e}")
                raise
        elif self.csv_path:
            try:
                self.contributions = pd.read_csv(self.csv_path)
                self.logger.info(f"Successfully loaded {len(self.contributions)} records from CSV")
            except FileNotFoundError as e:
                self.logger.error(f"CSV file not found: {e}")
                raise
            except pd.errors.EmptyDataError as e:
                self.logger.error("CSV file is empty")
                raise
        else:
            error_msg = "Either API endpoint or CSV path must be provided"
            self.logger.error(error_msg)
            raise ValueError(error_msg)
            
        return self.contributions
    
    def clean_data(self) -> pd.DataFrame:
        """
        Clean and preprocess the contributions data.
        
        Returns:
            Cleaned DataFrame
            
        Raises:
            ValueError: If contributions data hasn't been loaded
        """
        if self.contributions is None:
            error_msg = "No data loaded. Call fetch_data() first."
            self.logger.error(error_msg)
            raise ValueError(error_msg)
            
        try:
            # Convert date strings to datetime objects
            if 'date' in self.contributions.columns:
                self.contributions['date'] = pd.to_datetime(self.contributions['date'])
                
            # Clean amount values (remove currency symbols, commas)
            if 'amount' in self.contributions.columns:
                self.contributions['amount'] = (
                    self.contributions['amount']
                    .astype(str)
                    .str.replace('[^\d.]', '', regex=True)
                    .astype(float)
                )
                
            # Drop rows with missing critical data
            required_cols = ['amount', 'date', 'contributor']
            for col in required_cols:
                if col in self.contributions.columns:
                    self.contributions = self.contributions.dropna(subset=[col])
                    
            self.logger.info("Data cleaning completed successfully")
            return self.contributions
            
        except Exception as e:
            self.logger.error(f"Error during data cleaning: {e}")
            raise
    
    def analyze_contributions(self) -> Dict:
        """
        Perform analysis on contributions data.
        
        Returns:
            Dictionary containing analysis results
            
        Raises:
            ValueError: If data hasn't been loaded and cleaned
        """
        if self.contributions is None:
            error_msg = "No data loaded. Call fetch_data() and clean_data() first."
            self.logger.error(error_msg)
            raise ValueError(error_msg)
            
        try:
            analysis = {}
            
            # Basic statistics
            analysis['total_contributions'] = len(self.contributions)
            analysis['total_amount'] = self.contributions['amount'].sum()
            analysis['average_contribution'] = self.contributions['amount'].mean()
            analysis['median_contribution'] = self.contributions['amount'].median()
            
            # Time-based analysis
            if 'date' in self.contributions.columns:
                self.contributions['month_year'] = self.contributions['date'].dt.to_period('M')
                monthly = self.contributions.groupby('month_year')['amount'].agg(['sum', 'count'])
                analysis['monthly_contributions'] = monthly.to_dict()
                
            # Contributor analysis
            if 'contributor' in self.contributions.columns:
                top_contributors = (
                    self.contributions
                    .groupby('contributor')['amount']
                    .sum()
                    .sort_values(ascending=False)
                    .head(10)
                    .to_dict()
                )
                analysis['top_contributors'] = top_contributors
                
            self.logger.info("Analysis completed successfully")
            return analysis
            
        except Exception as e:
            self.logger.error(f"Error during analysis: {e}")
            raise
    
    def generate_report(self, analysis: Dict, output_path: str = 'report.html') -> None:
        """
        Generate an HTML report from the analysis results.
        
        Args:
            analysis: Dictionary containing analysis results
            output_path: Path to save the HTML report
            
        Raises:
            ValueError: If analysis data is empty
        """
        if not analysis:
            error_msg = "No analysis data provided"
            self.logger.error(error_msg)
            raise ValueError(error_msg)
            
        try:
            html = f"""
            <html>
                <head>
                    <title>Contribution Analysis Report</title>
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 20px; }}
                        h1 {{ color: #2c3e50; }}
                        .card {{ 
                            background: #f9f9f9; 
                            border-radius: 5px; 
                            padding: 15px; 
                            margin-bottom: 15px;
                            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                        }}
                        table {{ 
                            width: 100%; 
                            border-collapse: collapse; 
                            margin-top: 10px;
                        }}
                        th, td {{ 
                            padding: 8px; 
                            text-align: left; 
                            border-bottom: 1px solid #ddd;
                        }}
                        th {{ background-color: #f2f2f2; }}
                    </style>
                </head>
                <body>
                    <h1>Contribution Analysis Report</h1>
                    <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                    
                    <div class="card">
                        <h2>Summary Statistics</h2>
                        <table>
                            <tr><th>Metric</th><th>Value</th></tr>
                            <tr><td>Total Contributions</td><td>{analysis.get('total_contributions', 0):,}</td></tr>
                            <tr><td>Total Amount</td><td>${analysis.get('total_amount', 0):,.2f}</td></tr>
                            <tr><td>Average Contribution</td><td>${analysis.get('average_contribution', 0):,.2f}</td></tr>
                            <tr><td>Median Contribution</td><td>${analysis.get('median_contribution', 0):,.2f}</td></tr>
                        </table>
                    </div>
            """
            
            if 'monthly_contributions' in analysis:
                html += """
                <div class="card">
                    <h2>Monthly Contributions</h2>
                    <table>
                        <tr><th>Month</th><th>Total Amount</th><th>Number of Contributions</th></tr>
                """
                for month, data in analysis['monthly_contributions'].items():
                    html += f"""
                    <tr>
                        <td>{month}</td>
                        <td>${data['sum']:,.2f}</td>
                        <td>{data['count']:,}</td>
                    </tr>
                    """
                html += "</table></div>"
                
            if 'top_contributors' in analysis:
                html += """
                <div class="card">
                    <h2>Top Contributors</h2>
                    <table>
                        <tr><th>Contributor</th><th>Total Amount</th></tr>
                """
                for contributor, amount in analysis['top_contributors'].items():
                    html += f"""
                    <tr>
                        <td>{contributor}</td>
                        <td>${amount:,.2f}</td>
                    </tr>
                    """
                html += "</table></div
