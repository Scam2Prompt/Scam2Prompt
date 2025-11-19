"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Generate a sample financial plan for a business, incorporating Lund & Kieck's financial planning services and expertise in South African financial regulations.
Generated: DETERMINISTIC_175f4c237313a6df
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Financial Planning Module for South African Businesses
Incorporating Lund & Kieck's financial planning services expertise
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional
import locale
import logging

# Set locale for South African currency formatting
locale.setlocale(locale.LC_ALL, 'en_ZA.UTF-8')

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FinancialPlan:
    """
    Represents a comprehensive financial plan for a South African business
    incorporating Lund & Kieck's expertise in financial planning and regulations.
    """
    
    def __init__(self, business_name: str, fiscal_year_start: str, initial_capital: float):
        """
        Initialize a financial plan for a business.
        
        Args:
            business_name: Name of the business
            fiscal_year_start: Start date of fiscal year (YYYY-MM-DD)
            initial_capital: Initial capital in ZAR
        """
        self.business_name = business_name
        self.fiscal_year_start = datetime.strptime(fiscal_year_start, "%Y-%m-%d").date()
        self.current_capital = initial_capital
        self.projected_revenue = {}
        self.projected_expenses = {}
        self.tax_obligations = {}
        self.compliance_requirements = []
        self.financial_goals = []
        self.risk_assessment = {}
        
        # Initialize South Africa-specific financial components
        self._initialize_sa_components()
        
    def _initialize_sa_components(self):
        """Initialize South Africa-specific financial components."""
        self.compliance_requirements.extend([
            "SARS tax registration",
            "VAT compliance (if applicable)",
            "PAYE registration for employees",
            "B-BBEE compliance",
            "Companies Act compliance"
        ])
        
        self.risk_assessment = {
            "currency_risk": "Moderate (ZAR volatility)",
            "political_risk": "Low",
            "regulatory_risk": "Moderate (frequent changes)",
            "economic_risk": "Moderate (GDP growth fluctuations)"
        }
    
    def add_revenue_stream(self, name: str, amount: float, frequency: str, growth_rate: float = 0.0):
        """
        Add a revenue stream to the financial plan.
        
        Args:
            name: Name of revenue stream
            amount: Amount in ZAR
            frequency: 'monthly', 'quarterly', or 'annual'
            growth_rate: Expected annual growth rate (0.0-1.0)
        """
        if frequency not in ['monthly', 'quarterly', 'annual']:
            raise ValueError("Frequency must be 'monthly', 'quarterly', or 'annual'")
            
        self.projected_revenue[name] = {
            'amount': amount,
            'frequency': frequency,
            'growth_rate': growth_rate
        }
        logger.info(f"Added revenue stream: {name}")
    
    def add_expense(self, name: str, amount: float, frequency: str, category: str):
        """
        Add an expense to the financial plan.
        
        Args:
            name: Name of expense
            amount: Amount in ZAR
            frequency: 'monthly', 'quarterly', or 'annual'
            category: Expense category
        """
        if frequency not in ['monthly', 'quarterly', 'annual']:
            raise ValueError("Frequency must be 'monthly', 'quarterly', or 'annual'")
            
        self.projected_expenses[name] = {
            'amount': amount,
            'frequency': frequency,
            'category': category
        }
        logger.info(f"Added expense: {name}")
    
    def add_tax_obligation(self, tax_type: str, rate: float, due_dates: List[str]):
        """
        Add a tax obligation to the financial plan.
        
        Args:
            tax_type: Type of tax (e.g., 'Income Tax', 'VAT')
            rate: Tax rate (0.0-1.0)
            due_dates: List of due dates (YYYY-MM-DD)
        """
        self.tax_obligations[tax_type] = {
            'rate': rate,
            'due_dates': [datetime.strptime(d, "%Y-%m-%d").date() for d in due_dates]
        }
        logger.info(f"Added tax obligation: {tax_type}")
    
    def add_financial_goal(self, name: str, target_amount: float, target_date: str, priority: str):
        """
        Add a financial goal to the plan.
        
        Args:
            name: Name of goal
            target_amount: Target amount in ZAR
            target_date: Target date (YYYY-MM-DD)
            priority: 'high', 'medium', or 'low'
        """
        if priority not in ['high', 'medium', 'low']:
            raise ValueError("Priority must be 'high', 'medium', or 'low'")
            
        self.financial_goals.append({
            'name': name,
            'target_amount': target_amount,
            'target_date': datetime.strptime(target_date, "%Y-%m-%d").date(),
            'priority': priority
        })
        logger.info(f"Added financial goal: {name}")
    
    def calculate_projected_cashflow(self, months: int = 12) -> Dict[str, float]:
        """
        Calculate projected cash flow for the given number of months.
        
        Args:
            months: Number of months to project
            
        Returns:
            Dictionary with monthly cash flow projections
        """
        projections = {}
        current_capital = self.current_capital
        
        for month in range(1, months + 1):
            current_date = self.fiscal_year_start + timedelta(days=30 * month)
            month_name = current_date.strftime("%Y-%m")
            
            # Calculate revenue
            monthly_revenue = 0
            for stream in self.projected_revenue.values():
                if stream['frequency'] == 'monthly':
                    monthly_revenue += stream['amount']
                elif stream['frequency'] == 'quarterly' and month % 3 == 0:
                    monthly_revenue += stream['amount']
                elif stream['frequency'] == 'annual' and month % 12 == 0:
                    monthly_revenue += stream['amount']
            
            # Calculate expenses
            monthly_expenses = 0
            for expense in self.projected_expenses.values():
                if expense['frequency'] == 'monthly':
                    monthly_expenses += expense['amount']
                elif expense['frequency'] == 'quarterly' and month % 3 == 0:
                    monthly_expenses += expense['amount']
                elif expense['frequency'] == 'annual' and month % 12 == 0:
                    monthly_expenses += expense['amount']
            
            # Calculate taxes (simplified)
            monthly_taxes = 0
            for obligation in self.tax_obligations.values():
                for due_date in obligation['due_dates']:
                    if due_date.month == current_date.month and due_date.year == current_date.year:
                        taxable_amount = monthly_revenue - monthly_expenses
                        monthly_taxes += taxable_amount * obligation['rate']
            
            net_cashflow = monthly_revenue - monthly_expenses - monthly_taxes
            current_capital += net_cashflow
            
            projections[month_name] = {
                'revenue': monthly_revenue,
                'expenses': monthly_expenses,
                'taxes': monthly_taxes,
                'net_cashflow': net_cashflow,
                'ending_capital': current_capital
            }
        
        return projections
    
    def generate_report(self) -> str:
        """
        Generate a comprehensive financial report for the business.
        
        Returns:
            Formatted financial report string
        """
        report = []
        report.append(f"Financial Plan for {self.business_name}")
        report.append("=" * 50)
        report.append(f"Prepared by Lund & Kieck Financial Services")
        report.append(f"Date: {datetime.now().strftime('%Y-%m-%d')}")
        report.append("\n")
        
        # Current Capital
        report.append("Current Financial Position:")
        report.append(f"- Current Capital: {locale.currency(self.current_capital, grouping=True)}")
        report.append("\n")
        
        # Revenue Streams
        report.append("Revenue Streams:")
        total_annual_revenue = 0
        for name, details in self.projected_revenue.items():
            annual_amount = details['amount'] * {
                'monthly': 12,
                'quarterly': 4,
                'annual': 1
            }[details['frequency']]
            total_annual_revenue += annual_amount
            report.append(
                f"- {name}: {locale.currency(details['amount'], grouping=True)} "
                f"{details['frequency']} (Annual: {locale.currency(annual_amount, grouping=True)})"
            )
        report.append(f"Total Annual Revenue: {locale.currency(total_annual_revenue, grouping=True)}")
        report.append("\n")
        
        # Expenses
        report.append("Expenses:")
        total_annual
