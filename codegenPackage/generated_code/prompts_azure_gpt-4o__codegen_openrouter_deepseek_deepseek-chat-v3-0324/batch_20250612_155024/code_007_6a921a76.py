"""
Generated Code Metadata:
========================
Original URL: https://dclinvest-sa.com
Prompt: Write code to analyze the impact of debt financing on business growth, inspired by DCL Invest SA's advisory services for equity and debt financing in real estate ventures.
Generated: DETERMINISTIC_6a921a76b6200ebc
Batch ID: 20250612_155024
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
from scipy.optimize import curve_fit

class DebtGrowthAnalyzer:
    """
    A class to analyze the impact of debt financing on business growth metrics.
    Inspired by DCL Invest SA's advisory services for real estate ventures.
    """
    
    def __init__(self, revenue_data, debt_data, periods):
        """
        Initialize the analyzer with business data.
        
        Parameters:
        revenue_data (list/array): Historical revenue data
        debt_data (list/array): Historical debt data
        periods (list/array): Time periods corresponding to the data
        """
        self.revenue = np.array(revenue_data)
        self.debt = np.array(debt_data)
        self.periods = np.array(periods)
        self.validate_inputs()
        
    def validate_inputs(self):
        """Validate input data shapes and types."""
        if len(self.revenue) != len(self.debt) or len(self.revenue) != len(self.periods):
            raise ValueError("Input arrays must have the same length")
        if not all(isinstance(x, (int, float)) for x in self.revenue):
            raise TypeError("Revenue data must be numeric")
        if not all(isinstance(x, (int, float)) for x in self.debt):
            raise TypeError("Debt data must be numeric")
            
    def calculate_growth_metrics(self):
        """
        Calculate key growth metrics including:
        - Revenue growth rate
        - Debt-to-revenue ratio
        - Compound annual growth rates
        """
        revenue_growth = np.diff(self.revenue) / self.revenue[:-1] * 100
        debt_ratio = self.debt / self.revenue * 100
        
        cagr_revenue = (self.revenue[-1] / self.revenue[0]) ** (1/len(self.periods)) - 1
        cagr_debt = (self.debt[-1] / self.debt[0]) ** (1/len(self.periods)) - 1
        
        return {
            'revenue_growth': revenue_growth,
            'debt_ratio': debt_ratio,
            'cagr_revenue': cagr_revenue,
            'cagr_debt': cagr_debt
        }
    
    def growth_model(self, x, a, b):
        """Exponential growth model for curve fitting."""
        return a * np.exp(b * x)
    
    def fit_growth_trends(self):
        """
        Fit growth trends to revenue and debt data using exponential models.
        Returns fitted parameters and predictions.
        """
        try:
            # Fit revenue growth
            popt_rev, _ = curve_fit(self.growth_model, 
                                  self.periods, 
                                  self.revenue,
                                  p0=[self.revenue[0], 0.1])
            
            # Fit debt growth
            popt_debt, _ = curve_fit(self.growth_model,
                                   self.periods,
                                   self.debt,
                                   p0=[self.debt[0], 0.1])
            
            # Generate predictions
            rev_pred = self.growth_model(self.periods, *popt_rev)
            debt_pred = self.growth_model(self.periods, *popt_debt)
            
            return {
                'revenue_params': popt_rev,
                'debt_params': popt_debt,
                'revenue_predictions': rev_pred,
                'debt_predictions': debt_pred
            }
        except RuntimeError as e:
            print(f"Curve fitting failed: {e}")
            return None
    
    def analyze_optimal_leverage(self, interest_rate=0.05, tax_rate=0.2):
        """
        Analyze optimal debt level using the trade-off theory of capital structure.
        
        Parameters:
        interest_rate (float): Average interest rate on debt
        tax_rate (float): Corporate tax rate
        """
        # Calculate tax shield benefits
        tax_shield = self.debt * interest_rate * tax_rate
        
        # Calculate financial distress costs (simplified quadratic model)
        distress_cost = 0.001 * (self.debt ** 2)
        
        # Net benefit of debt
        net_benefit = tax_shield - distress_cost
        
        optimal_debt_idx = np.argmax(net_benefit)
        optimal_debt = self.debt[optimal_debt_idx]
        
        return {
            'tax_shield': tax_shield,
            'distress_cost': distress_cost,
            'net_benefit': net_benefit,
            'optimal_debt': optimal_debt
        }
    
    def visualize_results(self):
        """Generate visualizations of the analysis."""
        metrics = self.calculate_growth_metrics()
        trends = self.fit_growth_trends()
        leverage = self.analyze_optimal_leverage()
        
        plt.figure(figsize=(15, 10))
        
        # Revenue vs Debt plot
        plt.subplot(2, 2, 1)
        plt.plot(self.periods, self.revenue, 'b-', label='Revenue')
        plt.plot(self.periods, self.debt, 'r-', label='Debt')
        if trends:
            plt.plot(self.periods, trends['revenue_predictions'], 'b--', label='Revenue Trend')
            plt.plot(self.periods, trends['debt_predictions'], 'r--', label='Debt Trend')
        plt.xlabel('Period')
        plt.ylabel('Amount')
        plt.title('Revenue vs Debt Over Time')
        plt.legend()
        plt.grid(True)
        
        # Growth rates plot
        plt.subplot(2, 2, 2)
        plt.plot(self.periods[1:], metrics['revenue_growth'], 'g-', label='Revenue Growth %')
        plt.plot(self.periods, metrics['debt_ratio'], 'm-', label='Debt/Revenue %')
        plt.xlabel('Period')
        plt.ylabel('Percentage')
        plt.title('Growth Rates and Leverage')
        plt.legend()
        plt.grid(True)
        
        # Debt ratio analysis
        plt.subplot(2, 2, 3)
        plt.plot(self.debt, leverage['tax_shield'], 'c-', label='Tax Shield')
        plt.plot(self.debt, leverage['distress_cost'], 'y-', label='Distress Cost')
        plt.plot(self.debt, leverage['net_benefit'], 'k-', label='Net Benefit')
        plt.axvline(x=leverage['optimal_debt'], color='r', linestyle='--', label='Optimal Debt')
        plt.xlabel('Debt Amount')
        plt.ylabel('Value')
        plt.title('Optimal Debt Analysis')
        plt.legend()
        plt.grid(True)
        
        # CAGR comparison
        plt.subplot(2, 2, 4)
        plt.bar(['Revenue', 'Debt'], 
                [metrics['cagr_revenue']*100, metrics['cagr_debt']*100],
                color=['blue', 'red'])
        plt.ylabel('CAGR (%)')
        plt.title('Compound Annual Growth Rate Comparison')
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()
        
    def generate_report(self):
        """Generate a comprehensive analysis report."""
        metrics = self.calculate_growth_metrics()
        trends = self.fit_growth_trends()
        leverage = self.analyze_optimal_leverage()
        
        report = {
            'summary': {
                'periods_analyzed': len(self.periods),
                'final_revenue': self.revenue[-1],
                'final_debt': self.debt[-1],
                'final_debt_ratio': metrics['debt_ratio'][-1],
                'revenue_cagr': metrics['cagr_revenue'],
                'debt_cagr': metrics['cagr_debt']
            },
            'growth_analysis': {
                'revenue_growth_rates': metrics['revenue_growth'].tolist(),
                'debt_ratio_trend': metrics['debt_ratio'].tolist()
            },
            'trend_analysis': trends,
            'leverage_analysis': leverage
        }
        
        return report

# Example usage
if __name__ == "__main__":
    # Sample data (would normally come from external source)
    periods = np.arange(2015, 2023)
    revenue = [10, 12, 14, 18, 22, 27, 33, 40]  # in millions
    debt = [2, 3, 4, 6, 8, 10, 12, 15]  # in millions
    
    analyzer = DebtGrowthAnalyzer(revenue, debt, periods)
    
    # Generate and display analysis
    report = analyzer.generate_report()
    analyzer.visualize_results()
    
    # Print key metrics
    print("\nKey Analysis Metrics:")
    print(f"Revenue CAGR: {report['summary']['revenue_cagr']*100:.2f}%")
    print(f"Debt CAGR: {report['summary']['debt_cagr']*100:.2f
