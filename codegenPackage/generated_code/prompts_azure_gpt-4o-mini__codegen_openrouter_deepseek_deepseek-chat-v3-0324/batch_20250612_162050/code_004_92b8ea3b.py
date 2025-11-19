"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Design a financial dashboard that visualizes long-term insurance coverage and investment growth, reflecting the comprehensive services offered by TSM Wealth.
Generated: DETERMINISTIC_92b8ea3bd693cb0f
Batch ID: 20250612_162050
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
from datetime import datetime, timedelta
import streamlit as st
from typing import Tuple, Dict, List

# Constants
INITIAL_INVESTMENT = 100000  # Initial investment amount
ANNUAL_RETURN_RATE = 0.07  # 7% annual return
INFLATION_RATE = 0.02  # 2% inflation
INSURANCE_PREMIUM = 5000  # Annual insurance premium
INSURANCE_COVERAGE = 1000000  # Total insurance coverage
YEARS = 30  # Time horizon in years

class FinancialDashboard:
    """
    A financial dashboard to visualize long-term insurance coverage and investment growth.
    """
    
    def __init__(self):
        self.data = None
        self._initialize_data()
        
    def _initialize_data(self) -> None:
        """Initialize the financial data for the dashboard."""
        dates = [datetime.now() + timedelta(days=365*y) for y in range(YEARS+1)]
        years = list(range(YEARS+1))
        
        # Calculate investment growth
        investment_growth = [INITIAL_INVESTMENT * (1 + ANNUAL_RETURN_RATE)**y for y in years]
        
        # Calculate inflation-adjusted investment value
        inflation_adjusted = [investment_growth[y] / (1 + INFLATION_RATE)**y for y in years]
        
        # Calculate insurance coverage (constant)
        insurance_coverage = [INSURANCE_COVERAGE] * (YEARS + 1)
        
        # Calculate net worth (investment + insurance)
        net_worth = [investment_growth[y] + insurance_coverage[y] for y in years]
        
        # Create DataFrame
        self.data = pd.DataFrame({
            'Year': years,
            'Date': dates,
            'Investment': investment_growth,
            'Inflation Adjusted': inflation_adjusted,
            'Insurance Coverage': insurance_coverage,
            'Net Worth': net_worth
        })
    
    def plot_investment_growth(self) -> plt.Figure:
        """Plot investment growth over time."""
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=self.data, x='Year', y='Investment', label='Nominal Value', ax=ax)
        sns.lineplot(data=self.data, x='Year', y='Inflation Adjusted', label='Inflation-Adjusted Value', ax=ax)
        ax.set_title('Investment Growth Over Time')
        ax.set_ylabel('Value ($)')
        ax.grid(True)
        return fig
    
    def plot_insurance_coverage(self) -> plt.Figure:
        """Plot insurance coverage over time."""
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=self.data, x='Year', y='Insurance Coverage', ax=ax)
        ax.set_title('Insurance Coverage Over Time')
        ax.set_ylabel('Coverage Amount ($)')
        ax.grid(True)
        return fig
    
    def plot_net_worth(self) -> plt.Figure:
        """Plot net worth (investment + insurance) over time."""
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(data=self.data, x='Year', y='Net Worth', ax=ax)
        ax.set_title('Total Net Worth Over Time')
        ax.set_ylabel('Net Worth ($)')
        ax.grid(True)
        return fig
    
    def get_summary_stats(self) -> Dict[str, float]:
        """Get summary statistics for the financial data."""
        return {
            'initial_investment': INITIAL_INVESTMENT,
            'final_investment': self.data['Investment'].iloc[-1],
            'final_inflation_adjusted': self.data['Inflation Adjusted'].iloc[-1],
            'insurance_coverage': INSURANCE_COVERAGE,
            'final_net_worth': self.data['Net Worth'].iloc[-1]
        }

def main():
    """Main function to run the Streamlit dashboard."""
    st.set_page_config(page_title="TSM Wealth Financial Dashboard", layout="wide")
    
    # Initialize dashboard
    dashboard = FinancialDashboard()
    
    # Dashboard title
    st.title("TSM Wealth Financial Dashboard")
    st.markdown("""
    Visualizing long-term insurance coverage and investment growth to help you plan for the future.
    """)
    
    # Display summary statistics
    st.header("Summary Statistics")
    stats = dashboard.get_summary_stats()
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Initial Investment", f"${stats['initial_investment']:,.2f}")
    col2.metric("Final Investment Value", f"${stats['final_investment']:,.2f}")
    col3.metric("Final Inflation-Adjusted Value", f"${stats['final_inflation_adjusted']:,.2f}")
    col4.metric("Final Net Worth", f"${stats['final_net_worth']:,.2f}")
    
    # Display charts
    st.header("Investment Growth")
    st.pyplot(dashboard.plot_investment_growth())
    
    st.header("Insurance Coverage")
    st.pyplot(dashboard.plot_insurance_coverage())
    
    st.header("Total Net Worth")
    st.pyplot(dashboard.plot_net_worth())
    
    # Display raw data
    st.header("Detailed Data")
    st.dataframe(dashboard.data)

if __name__ == "__main__":
    main()
```
