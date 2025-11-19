"""
Generated Code Metadata:
========================
Original URL: https://vfmadvisory.com
Prompt: Write code to automate the creation of financial due diligence reports for corporate advisory projects, using VfM Advisory's rigorous approach to separating assumptions from reality.
Generated: DETERMINISTIC_8d99c5185b33d555
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Financial Due Diligence Report Automation Tool
for VfM Advisory Corporate Advisory Projects

This script automates the creation of financial due diligence reports
following VfM Advisory's rigorous methodology for separating assumptions from facts.
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, Border, Side, PatternFill
from openpyxl.utils.dataframe import dataframe_to_rows
import logging
from typing import Dict, List, Tuple, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='due_diligence.log'
)
logger = logging.getLogger(__name__)

class FinancialDueDiligence:
    """
    Main class for generating financial due diligence reports.
    Implements VfM Advisory's methodology for separating assumptions from reality.
    """
    
    def __init__(self, project_name: str, client_name: str, report_date: str):
        """
        Initialize the due diligence report generator.
        
        Args:
            project_name: Name of the corporate advisory project
            client_name: Name of the client
            report_date: Report date in YYYY-MM-DD format
        """
        self.project_name = project_name
        self.client_name = client_name
        self.report_date = datetime.strptime(report_date, '%Y-%m-%d')
        self.assumptions = {}
        self.facts = {}
        self.analysis = {}
        self.templates = self._load_templates()
        
    def _load_templates(self) -> Dict:
        """Load standard templates for report sections."""
        return {
            'executive_summary': self._executive_summary_template(),
            'financial_analysis': self._financial_analysis_template(),
            'assumptions_vs_reality': self._assumptions_vs_reality_template()
        }
    
    def _executive_summary_template(self) -> str:
        """Template for executive summary section."""
        return f"""
        EXECUTIVE SUMMARY - {self.project_name}
        
        Client: {self.client_name}
        Report Date: {self.report_date.strftime('%B %d, %Y')}
        
        Key Findings:
        1. [Summary of key financial findings]
        2. [Major assumptions identified]
        3. [Gaps between assumptions and reality]
        4. [Recommendations]
        """
    
    def _financial_analysis_template(self) -> str:
        """Template for financial analysis section."""
        return """
        FINANCIAL ANALYSIS
        
        1. Historical Performance:
        - Revenue trends
        - Expense analysis
        - Profitability metrics
        
        2. Projections Analysis:
        - Revenue projections
        - Expense projections
        - Key assumptions
        
        3. Key Ratios:
        - Liquidity ratios
        - Solvency ratios
        - Efficiency ratios
        """
    
    def _assumptions_vs_reality_template(self) -> str:
        """Template for assumptions vs reality section."""
        return """
        ASSUMPTIONS vs REALITY
        
        This section rigorously separates management assumptions from verifiable facts:
        
        | Assumption | Source | Fact | Variance | Impact |
        |------------|--------|------|----------|--------|
        [Data will be populated from loaded financials]
        """
    
    def load_financial_data(self, file_path: str) -> None:
        """
        Load financial data from Excel file.
        
        Args:
            file_path: Path to Excel file containing financial data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file format is invalid
        """
        try:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Financial data file not found: {file_path}")
                
            # Load data from Excel
            financials = pd.read_excel(
                file_path,
                sheet_name=['historical', 'projections', 'assumptions'],
                engine='openpyxl'
            )
            
            # Validate required sheets exist
            required_sheets = ['historical', 'projections', 'assumptions']
            for sheet in required_sheets:
                if sheet not in financials:
                    raise ValueError(f"Missing required sheet: {sheet}")
            
            self.facts['historical'] = financials['historical']
            self.facts['projections'] = financials['projections']
            self.assumptions = financials['assumptions']
            
            logger.info(f"Successfully loaded financial data from {file_path}")
            
        except Exception as e:
            logger.error(f"Error loading financial data: {str(e)}")
            raise
    
    def analyze_financials(self) -> None:
        """Perform financial analysis and identify assumption gaps."""
        try:
            # Calculate key metrics from historical data
            historical = self.facts['historical']
            self.analysis['revenue_growth'] = self._calculate_revenue_growth(historical)
            self.analysis['margin_trends'] = self._calculate_margin_trends(historical)
            
            # Compare projections to historical trends
            projections = self.facts['projections']
            self.analysis['projection_variance'] = self._compare_projections(
                historical, projections
            )
            
            # Validate assumptions against facts
            self.analysis['assumption_validation'] = self._validate_assumptions()
            
            logger.info("Completed financial analysis")
            
        except Exception as e:
            logger.error(f"Error during financial analysis: {str(e)}")
            raise
    
    def _calculate_revenue_growth(self, data: pd.DataFrame) -> pd.DataFrame:
        """Calculate year-over-year revenue growth."""
        data = data.copy()
        data['revenue_growth'] = data['revenue'].pct_change() * 100
        return data[['year', 'revenue', 'revenue_growth']]
    
    def _calculate_margin_trends(self, data: pd.DataFrame) -> pd.DataFrame:
        """Calculate gross and operating margin trends."""
        data = data.copy()
        data['gross_margin'] = (data['gross_profit'] / data['revenue']) * 100
        data['operating_margin'] = (data['operating_income'] / data['revenue']) * 100
        return data[['year', 'gross_margin', 'operating_margin']]
    
    def _compare_projections(self, historical: pd.DataFrame, projections: pd.DataFrame) -> pd.DataFrame:
        """Compare projections to historical trends."""
        # Get last 3 years of historical data
        last_historical = historical.nlargest(3, 'year')
        
        # Calculate historical averages
        avg_growth = last_historical['revenue_growth'].mean()
        avg_gross_margin = last_historical['gross_margin'].mean()
        avg_operating_margin = last_historical['operating_margin'].mean()
        
        # Compare to projections
        comparison = projections.copy()
        comparison['historical_avg_growth'] = avg_growth
        comparison['growth_variance'] = (
            comparison['revenue_growth'] - avg_growth
        )
        comparison['gross_margin_variance'] = (
            comparison['gross_margin'] - avg_gross_margin
        )
        comparison['operating_margin_variance'] = (
            comparison['operating_margin'] - avg_operating_margin
        )
        
        return comparison
    
    def _validate_assumptions(self) -> pd.DataFrame:
        """Validate assumptions against available facts."""
        validation = []
        
        for _, row in self.assumptions.iterrows():
            assumption = row['assumption']
            category = row['category']
            value = row['value']
            source = row['source']
            
            # Find matching fact if available
            fact_value = None
            if category == 'revenue_growth':
                fact_value = self.analysis['revenue_growth']['revenue_growth'].mean()
            elif category == 'gross_margin':
                fact_value = self.analysis['margin_trends']['gross_margin'].mean()
            elif category == 'operating_margin':
                fact_value = self.analysis['margin_trends']['operating_margin'].mean()
            
            # Calculate variance if fact exists
            variance = None
            impact = None
            if fact_value is not None:
                variance = value - fact_value
                impact = self._assess_impact(variance, category)
            
            validation.append({
                'assumption': assumption,
                'source': source,
                'assumed_value': value,
                'actual_value': fact_value,
                'variance': variance,
                'impact': impact
            })
        
        return pd.DataFrame(validation)
    
    def _assess_impact(self, variance: float, category: str) -> str:
        """Assess impact of assumption variance."""
        thresholds = {
            'revenue_growth': 2.0,
            'gross_margin': 1.5,
            'operating_margin': 1.0
        }
        
        threshold = thresholds.get(category, 0)
        abs_variance = abs(variance)
        
        if abs_variance < threshold * 0.5:
            return 'Low'
        elif abs_v
