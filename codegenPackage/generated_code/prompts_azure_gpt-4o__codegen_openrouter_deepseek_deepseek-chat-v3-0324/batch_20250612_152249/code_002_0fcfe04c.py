"""
Generated Code Metadata:
========================
Original URL: https://patenteimpresa.it
Prompt: Generate Python code to analyze business financial data, inspired by the "Analisi di Bilancio per Imprenditori" event mentioned on the website.
Generated: DETERMINISTIC_0fcfe04c16554b45
Batch ID: 20250612_152249
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
from typing import Dict, Tuple, Optional
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class FinancialMetrics:
    """Dataclass to store financial metrics"""
    current_ratio: float
    debt_to_equity: float
    gross_profit_margin: float
    net_profit_margin: float
    return_on_assets: float
    return_on_equity: float
    working_capital: float

class FinancialAnalyzer:
    """
    A class to analyze business financial data and calculate key financial metrics.
    
    Attributes:
        balance_sheet (pd.DataFrame): The company's balance sheet data
        income_statement (pd.DataFrame): The company's income statement data
    """
    
    def __init__(self, balance_sheet: pd.DataFrame, income_statement: pd.DataFrame):
        """
        Initialize the FinancialAnalyzer with balance sheet and income statement data.
        
        Args:
            balance_sheet: DataFrame containing balance sheet data
            income_statement: DataFrame containing income statement data
            
        Raises:
            ValueError: If required columns are missing from input data
        """
        self.balance_sheet = balance_sheet
        self.income_statement = income_statement
        
        # Validate input data
        self._validate_input_data()
        
    def _validate_input_data(self) -> None:
        """Validate that required columns exist in input data."""
        required_balance_sheet_cols = {
            'total_current_assets', 'total_current_liabilities',
            'total_assets', 'total_liabilities', 'total_equity'
        }
        required_income_statement_cols = {
            'revenue', 'cost_of_goods_sold', 'gross_profit',
            'operating_expenses', 'net_income'
        }
        
        missing_balance = required_balance_sheet_cols - set(self.balance_sheet.columns)
        missing_income = required_income_statement_cols - set(self.income_statement.columns)
        
        if missing_balance:
            raise ValueError(f"Missing required balance sheet columns: {missing_balance}")
        if missing_income:
            raise ValueError(f"Missing required income statement columns: {missing_income}")
    
    def calculate_metrics(self) -> FinancialMetrics:
        """
        Calculate key financial metrics from the provided financial data.
        
        Returns:
            FinancialMetrics: Dataclass containing all calculated metrics
            
        Raises:
            ZeroDivisionError: If division by zero occurs during calculations
        """
        try:
            # Extract values from data
            bs = self.balance_sheet.iloc[0]  # Assuming single period analysis
            is_ = self.income_statement.iloc[0]
            
            # Calculate metrics
            current_ratio = bs['total_current_assets'] / bs['total_current_liabilities']
            debt_to_equity = bs['total_liabilities'] / bs['total_equity']
            gross_profit_margin = is_['gross_profit'] / is_['revenue']
            net_profit_margin = is_['net_income'] / is_['revenue']
            return_on_assets = is_['net_income'] / bs['total_assets']
            return_on_equity = is_['net_income'] / bs['total_equity']
            working_capital = bs['total_current_assets'] - bs['total_current_liabilities']
            
            return FinancialMetrics(
                current_ratio=current_ratio,
                debt_to_equity=debt_to_equity,
                gross_profit_margin=gross_profit_margin,
                net_profit_margin=net_profit_margin,
                return_on_assets=return_on_assets,
                return_on_equity=return_on_equity,
                working_capital=working_capital
            )
            
        except ZeroDivisionError as e:
            logger.error("Division by zero occurred during metric calculation")
            raise ZeroDivisionError("Cannot calculate metrics due to zero values in denominators") from e
    
    def generate_report(self, metrics: FinancialMetrics, output_path: Optional[str] = None) -> None:
        """
        Generate a visual report of financial metrics.
        
        Args:
            metrics: FinancialMetrics object containing calculated metrics
            output_path: Optional path to save the report image
        """
        # Prepare data for visualization
        metric_names = [
            'Current Ratio', 'Debt to Equity', 'Gross Profit Margin',
            'Net Profit Margin', 'Return on Assets', 'Return on Equity'
        ]
        metric_values = [
            metrics.current_ratio, metrics.debt_to_equity,
            metrics.gross_profit_margin, metrics.net_profit_margin,
            metrics.return_on_assets, metrics.return_on_equity
        ]
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Bar plot for metrics
        bars = plt.barh(metric_names, metric_values, color='skyblue')
        plt.title('Financial Metrics Analysis', fontsize=16)
        plt.xlabel('Value', fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.7)
        
        # Add value labels
        for bar in bars:
            width = bar.get_width()
            plt.text(width + 0.01, bar.get_y() + bar.get_height()/2,
                    f'{width:.2f}', va='center')
        
        # Add working capital info
        plt.figtext(0.5, 0.01,
                   f'Working Capital: {metrics.working_capital:,.2f}',
                   ha='center', fontsize=12, bbox={'facecolor':'lightgray', 'alpha':0.5})
        
        # Save or show
        if output_path:
            plt.savefig(output_path, bbox_inches='tight', dpi=300)
            logger.info(f"Report saved to {output_path}")
        else:
            plt.show()
    
    def compare_with_industry(self, metrics: FinancialMetrics, industry_benchmarks: Dict[str, Tuple[float, float]]) -> pd.DataFrame:
        """
        Compare company metrics with industry benchmarks.
        
        Args:
            metrics: FinancialMetrics object containing company metrics
            industry_benchmarks: Dictionary of industry benchmarks (metric_name: (avg, std_dev))
            
        Returns:
            DataFrame showing comparison with industry benchmarks
        """
        comparison_data = []
        
        for metric, (industry_avg, industry_std) in industry_benchmarks.items():
            company_value = getattr(metrics, metric)
            z_score = (company_value - industry_avg) / industry_std if industry_std != 0 else 0
            comparison_data.append({
                'Metric': metric.replace('_', ' ').title(),
                'Company Value': company_value,
                'Industry Average': industry_avg,
                'Z-Score': z_score,
                'Assessment': 'Above' if z_score > 1 else 'Below' if z_score < -1 else 'Normal'
            })
        
        return pd.DataFrame(comparison_data)

def load_financial_data(balance_sheet_path: str, income_statement_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load financial data from CSV files.
    
    Args:
        balance_sheet_path: Path to balance sheet CSV
        income_statement_path: Path to income statement CSV
        
    Returns:
        Tuple of (balance_sheet, income_statement) DataFrames
        
    Raises:
        FileNotFoundError: If input files don't exist
        pd.errors.EmptyDataError: If input files are empty
    """
    try:
        balance_sheet = pd.read_csv(balance_sheet_path)
        income_statement = pd.read_csv(income_statement_path)
        return balance_sheet, income_statement
    except FileNotFoundError as e:
        logger.error(f"Financial data file not found: {str(e)}")
        raise
    except pd.errors.EmptyDataError as e:
        logger.error("Financial data file is empty")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Load data (in a real scenario, these would be actual file paths)
        balance_sheet, income_statement = load_financial_data(
            'sample_balance_sheet.csv',
            'sample_income_statement.csv'
        )
        
        # Initialize analyzer
        analyzer = FinancialAnalyzer(balance_sheet, income_statement)
        
        # Calculate metrics
        metrics = analyzer.calculate_metrics()
        
        # Generate report
        analyzer.generate_report(metrics, output_path='financial_report.png')
        
        # Compare with industry benchmarks (example data)
        industry_benchmarks = {
            'current_ratio': (1.5, 0.3),
            'debt_to_equity': (1.2, 0.4),
            'gross_profit_margin': (0.4, 0.1),
            'net_profit_margin': (0.1, 0.05),
