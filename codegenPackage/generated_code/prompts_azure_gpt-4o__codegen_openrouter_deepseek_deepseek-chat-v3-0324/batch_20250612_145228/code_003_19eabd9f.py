"""
Generated Code Metadata:
========================
Original URL: https://sgfcfinance.com
Prompt: Develop a script to analyze the impact of SGFC Finance's microfinance initiatives, using data inputs for loan disbursement, community outreach, and business development metrics.
Generated: DETERMINISTIC_19eabd9f03bb5272
Batch ID: 20250612_145228
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
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import logging
from typing import Dict, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sgfc_analysis.log'),
        logging.StreamHandler()
    ]
)

class SGFCImpactAnalyzer:
    """
    A class to analyze the impact of SGFC Finance's microfinance initiatives.
    """
    
    def __init__(self, loan_data_path: str, outreach_data_path: str, business_data_path: str):
        """
        Initialize the analyzer with data file paths.
        
        Args:
            loan_data_path: Path to loan disbursement data CSV
            outreach_data_path: Path to community outreach data CSV
            business_data_path: Path to business development metrics CSV
        """
        self.loan_data_path = loan_data_path
        self.outreach_data_path = outreach_data_path
        self.business_data_path = business_data_path
        self.loan_data = None
        self.outreach_data = None
        self.business_data = None
        self.merged_data = None
        
    def load_data(self) -> None:
        """
        Load and validate the input data files.
        """
        try:
            self.loan_data = pd.read_csv(self.loan_data_path)
            self.outreach_data = pd.read_csv(self.outreach_data_path)
            self.business_data = pd.read_csv(self.business_data_path)
            
            # Basic validation
            required_loan_cols = ['region', 'year', 'loan_amount', 'recipients']
            required_outreach_cols = ['region', 'year', 'training_sessions', 'participants']
            required_business_cols = ['region', 'year', 'new_businesses', 'jobs_created']
            
            for df, cols, name in zip(
                [self.loan_data, self.outreach_data, self.business_data],
                [required_loan_cols, required_outreach_cols, required_business_cols],
                ['loan', 'outreach', 'business']
            ):
                if not all(col in df.columns for col in cols):
                    raise ValueError(f"Missing required columns in {name} data")
            
            logging.info("Data loaded successfully")
            
        except Exception as e:
            logging.error(f"Error loading data: {str(e)}")
            raise
    
    def preprocess_data(self) -> None:
        """
        Clean and merge the datasets.
        """
        try:
            # Clean data
            for df in [self.loan_data, self.outreach_data, self.business_data]:
                df.dropna(inplace=True)
                df['year'] = df['year'].astype(int)
            
            # Merge datasets
            self.merged_data = self.loan_data.merge(
                self.outreach_data, on=['region', 'year'], how='inner'
            ).merge(
                self.business_data, on=['region', 'year'], how='inner'
            )
            
            # Calculate derived metrics
            self.merged_data['loan_per_recipient'] = (
                self.merged_data['loan_amount'] / self.merged_data['recipients']
            )
            self.merged_data['participants_per_session'] = (
                self.merged_data['participants'] / self.merged_data['training_sessions']
            )
            
            logging.info("Data preprocessing completed")
            
        except Exception as e:
            logging.error(f"Error preprocessing data: {str(e)}")
            raise
    
    def analyze_impact(self) -> Dict[str, float]:
        """
        Perform impact analysis and return key metrics.
        
        Returns:
            Dictionary containing impact metrics
        """
        try:
            if self.merged_data is None:
                raise ValueError("Data not loaded or preprocessed")
            
            results = {}
            
            # Correlation analysis
            corr_matrix = self.merged_data[[
                'loan_amount', 'training_sessions', 'new_businesses', 'jobs_created'
            ]].corr()
            
            results['loan_to_business_corr'] = corr_matrix.loc['loan_amount', 'new_businesses']
            results['loan_to_jobs_corr'] = corr_matrix.loc['loan_amount', 'jobs_created']
            results['training_to_business_corr'] = corr_matrix.loc['training_sessions', 'new_businesses']
            
            # Regression analysis
            X = self.merged_data[['loan_amount', 'training_sessions']]
            y_business = self.merged_data['new_businesses']
            y_jobs = self.merged_data['jobs_created']
            
            model_business = LinearRegression().fit(X, y_business)
            model_jobs = LinearRegression().fit(X, y_jobs)
            
            results['business_r2'] = r2_score(y_business, model_business.predict(X))
            results['jobs_r2'] = r2_score(y_jobs, model_jobs.predict(X))
            
            # Growth metrics
            grouped = self.merged_data.groupby('year').agg({
                'loan_amount': 'sum',
                'new_businesses': 'sum',
                'jobs_created': 'sum'
            }).pct_change().mean() * 100
            
            results['avg_loan_growth'] = grouped['loan_amount']
            results['avg_business_growth'] = grouped['new_businesses']
            results['avg_jobs_growth'] = grouped['jobs_created']
            
            logging.info("Impact analysis completed")
            return results
            
        except Exception as e:
            logging.error(f"Error during analysis: {str(e)}")
            raise
    
    def visualize_results(self, results: Dict[str, float], output_dir: str = 'output') -> None:
        """
        Generate visualizations of the analysis results.
        
        Args:
            results: Dictionary of analysis results
            output_dir: Directory to save visualizations
        """
        try:
            import os
            os.makedirs(output_dir, exist_ok=True)
            
            # Time series trends
            plt.figure(figsize=(12, 6))
            sns.lineplot(
                data=self.merged_data.groupby('year').agg({
                    'loan_amount': 'sum',
                    'new_businesses': 'sum',
                    'jobs_created': 'sum'
                }).reset_index(),
                x='year',
                y='value',
                hue='variable',
                palette='viridis'
            )
            plt.title('Microfinance Impact Over Time')
            plt.ylabel('Total Amount')
            plt.savefig(f'{output_dir}/trends_over_time.png')
            plt.close()
            
            # Correlation heatmap
            plt.figure(figsize=(8, 6))
            sns.heatmap(
                self.merged_data[[
                    'loan_amount', 'training_sessions', 'new_businesses', 'jobs_created'
                ]].corr(),
                annot=True,
                cmap='coolwarm'
            )
            plt.title('Correlation Between Initiatives and Outcomes')
            plt.savefig(f'{output_dir}/correlation_heatmap.png')
            plt.close()
            
            # Regional impact
            regional_impact = self.merged_data.groupby('region').agg({
                'loan_amount': 'sum',
                'new_businesses': 'sum',
                'jobs_created': 'sum'
            }).sort_values('new_businesses', ascending=False)
            
            regional_impact.plot(kind='bar', figsize=(12, 6))
            plt.title('Regional Impact of Microfinance Initiatives')
            plt.ylabel('Total Amount')
            plt.savefig(f'{output_dir}/regional_impact.png')
            plt.close()
            
            logging.info(f"Visualizations saved to {output_dir}")
            
        except Exception as e:
            logging.error(f"Error generating visualizations: {str(e)}")
            raise
    
    def generate_report(self, results: Dict[str, float], report_path: str = 'sgfc_impact_report.txt') -> None:
        """
        Generate a text report summarizing the findings.
        
        Args:
            results: Dictionary of analysis results
            report_path: Path to save the report
        """
        try:
            with open(report_path, 'w') as f:
                f.write("SGFC Finance Microfinance Impact Report\n")
                f.write("="*50 + "\n\n")
                
                f.write("Key Findings:\n")
                f.write(f"- Loan amount to new businesses correlation: {results['loan_to_business_corr']:.2f}\n")
                f.write(f"- Loan amount to jobs created correlation: {results['loan_to_jobs_corr']:.2f}\n")
                f.write(f"- Training sessions to new businesses correlation: {results['training_to_business_corr']:.2f}\n\n")
                
                f.write("Regression Analysis:\n")
                f.write(f"- Business creation model R-squared: {results['business_r2']:.2f}\n")
                f.write(f"- Job creation model R-squared: {results['jobs_r2']:.2f}\n\n")
                
                f.write("Growth Metrics:\n")
                f.write(f"- Average annual loan growth: {results['avg_loan_growth
