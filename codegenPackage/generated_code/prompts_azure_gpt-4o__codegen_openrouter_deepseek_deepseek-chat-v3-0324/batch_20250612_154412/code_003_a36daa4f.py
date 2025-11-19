"""
Generated Code Metadata:
========================
Original URL: https://invictacobrancas.com.br
Prompt: Create a script to analyze debt recovery data and generate performance reports, mimicking the features of the Invicta Cobranças online platform.
Generated: DETERMINISTIC_a36daa4f2511f125
Batch ID: 20250612_154412
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
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import logging
from typing import Dict, List, Optional, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('debt_recovery_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class DebtRecoveryAnalyzer:
    """
    A class to analyze debt recovery data and generate performance reports.
    Mimics features of Invicta Cobranças platform.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize the analyzer with data from the given path.
        
        Args:
            data_path (str): Path to the debt recovery data file (CSV or Excel)
        """
        self.data_path = data_path
        self.df = None
        self.report_data = {}
        
        try:
            if data_path.endswith('.csv'):
                self.df = pd.read_csv(data_path)
            elif data_path.endswith(('.xls', '.xlsx')):
                self.df = pd.read_excel(data_path)
            else:
                raise ValueError("Unsupported file format. Please provide CSV or Excel file.")
                
            self._validate_data()
            self._preprocess_data()
            logger.info("Data loaded and preprocessed successfully.")
            
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise
    
    def _validate_data(self) -> None:
        """
        Validate the input data for required columns and data quality.
        """
        required_columns = {
            'debt_id', 'debt_amount', 'due_date', 'recovery_status',
            'recovery_amount', 'recovery_date', 'client_id', 'agent_id'
        }
        
        missing_columns = required_columns - set(self.df.columns)
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
            
        if self.df['debt_amount'].isnull().any():
            raise ValueError("Debt amount contains null values")
            
        if not pd.api.types.is_numeric_dtype(self.df['debt_amount']):
            raise ValueError("Debt amount must be numeric")
    
    def _preprocess_data(self) -> None:
        """
        Clean and preprocess the data for analysis.
        """
        # Convert dates to datetime objects
        self.df['due_date'] = pd.to_datetime(self.df['due_date'])
        self.df['recovery_date'] = pd.to_datetime(self.df['recovery_date'])
        
        # Fill missing recovery amounts with 0 for unrecovered debts
        self.df['recovery_amount'] = self.df['recovery_amount'].fillna(0)
        
        # Calculate days overdue
        today = datetime.now()
        self.df['days_overdue'] = (today - self.df['due_date']).dt.days
        self.df['days_overdue'] = self.df['days_overdue'].apply(lambda x: x if x > 0 else 0)
        
        # Categorize debt age
        bins = [0, 30, 60, 90, 180, 365, np.inf]
        labels = ['0-30', '31-60', '61-90', '91-180', '181-365', '365+']
        self.df['debt_age_category'] = pd.cut(
            self.df['days_overdue'],
            bins=bins,
            labels=labels,
            right=False
        )
    
    def generate_summary_report(self) -> Dict:
        """
        Generate a summary report of debt recovery performance.
        
        Returns:
            Dict: Dictionary containing summary metrics
        """
        try:
            total_debt = self.df['debt_amount'].sum()
            total_recovered = self.df['recovery_amount'].sum()
            recovery_rate = (total_recovered / total_debt) * 100
            
            status_counts = self.df['recovery_status'].value_counts().to_dict()
            
            self.report_data['summary'] = {
                'total_debt': round(total_debt, 2),
                'total_recovered': round(total_recovered, 2),
                'recovery_rate': round(recovery_rate, 2),
                'status_distribution': status_counts,
                'total_debts': len(self.df),
                'average_debt_amount': round(self.df['debt_amount'].mean(), 2),
                'median_debt_amount': round(self.df['debt_amount'].median(), 2)
            }
            
            logger.info("Summary report generated successfully.")
            return self.report_data['summary']
            
        except Exception as e:
            logger.error(f"Error generating summary report: {str(e)}")
            raise
    
    def generate_agent_performance_report(self) -> pd.DataFrame:
        """
        Generate a report showing performance metrics by recovery agent.
        
        Returns:
            pd.DataFrame: DataFrame with agent performance metrics
        """
        try:
            agent_report = self.df.groupby('agent_id').agg({
                'debt_id': 'count',
                'debt_amount': 'sum',
                'recovery_amount': 'sum',
                'days_overdue': 'mean'
            }).rename(columns={
                'debt_id': 'total_cases',
                'debt_amount': 'total_debt_assigned',
                'recovery_amount': 'total_recovered',
                'days_overdue': 'average_days_overdue'
            })
            
            agent_report['recovery_rate'] = (agent_report['total_recovered'] / 
                                            agent_report['total_debt_assigned']) * 100
            agent_report = agent_report.sort_values('recovery_rate', ascending=False)
            
            self.report_data['agent_performance'] = agent_report
            logger.info("Agent performance report generated successfully.")
            return agent_report
            
        except Exception as e:
            logger.error(f"Error generating agent performance report: {str(e)}")
            raise
    
    def generate_debt_age_analysis(self) -> Dict:
        """
        Analyze recovery performance by debt age categories.
        
        Returns:
            Dict: Dictionary with recovery metrics by debt age
        """
        try:
            age_report = self.df.groupby('debt_age_category').agg({
                'debt_id': 'count',
                'debt_amount': 'sum',
                'recovery_amount': 'sum'
            }).rename(columns={
                'debt_id': 'total_debts',
                'debt_amount': 'total_debt_amount',
                'recovery_amount': 'total_recovered'
            })
            
            age_report['recovery_rate'] = (age_report['total_recovered'] / 
                                         age_report['total_debt_amount']) * 100
            age_report = age_report.sort_index()
            
            self.report_data['debt_age_analysis'] = age_report.to_dict()
            logger.info("Debt age analysis report generated successfully.")
            return age_report.to_dict()
            
        except Exception as e:
            logger.error(f"Error generating debt age analysis: {str(e)}")
            raise
    
    def generate_client_report(self, top_n: int = 10) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Generate reports on client debt and recovery patterns.
        
        Args:
            top_n (int): Number of top clients to return
            
        Returns:
            Tuple[pd.DataFrame, pd.DataFrame]: 
                - Top clients by total debt
                - Top clients by recovery rate
        """
        try:
            client_report = self.df.groupby('client_id').agg({
                'debt_id': 'count',
                'debt_amount': 'sum',
                'recovery_amount': 'sum'
            }).rename(columns={
                'debt_id': 'total_debts',
                'debt_amount': 'total_debt_amount',
                'recovery_amount': 'total_recovered'
            })
            
            client_report['recovery_rate'] = (client_report['total_recovered'] / 
                                            client_report['total_debt_amount']) * 100
            
            top_debt_clients = client_report.sort_values('total_debt_amount', ascending=False).head(top_n)
            top_recovery_clients = client_report[client_report['total_debt_amount'] > 0].sort_values(
                'recovery_rate', ascending=False).head(top_n)
            
            self.report_data['client_reports'] = {
                'top_debt_clients': top_debt_clients,
                'top_recovery_clients': top_recovery_clients
            }
            
            logger.info("Client reports generated successfully.")
            return top_debt_clients, top_recovery_clients
            
        except Exception as e:
            logger.error(f"Error generating client reports: {str(e)}")
            raise
    
    def visualize_recovery_performance(self, output_path: str = None) -> None:
        """
        Generate visualizations for recovery performance.
        
        Args:
            output_path (str, optional): Path to save visualizations. If None, displays them.
        """
        try:
            plt.figure(figsize=(15, 10))
