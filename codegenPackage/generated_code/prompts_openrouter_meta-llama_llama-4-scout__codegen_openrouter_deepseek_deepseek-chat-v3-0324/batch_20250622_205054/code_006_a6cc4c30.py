"""
Generated Code Metadata:
========================
Original URL: https://fintopsignaltrades.com
Prompt: Analyze the performance of Fintopsignaltrades' various investment plans and provide recommendations for a trader.
Generated: DETERMINISTIC_a6cc4c3079389ed0
Batch ID: 20250622_205054
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
from typing import List, Dict, Optional

class InvestmentPlanAnalyzer:
    """
    Analyzes performance of various investment plans from Fintopsignaltrades.
    Provides recommendations based on historical performance metrics.
    """
    
    def __init__(self, data_path: str):
        """
        Initialize analyzer with historical trade data.
        
        Args:
            data_path: Path to CSV file containing trade history
        """
        self.data = self._load_data(data_path)
        self.plans = self._extract_plans()
        
    def _load_data(self, data_path: str) -> pd.DataFrame:
        """
        Load and preprocess trade data.
        
        Args:
            data_path: Path to CSV file
            
        Returns:
            Cleaned DataFrame with trade data
        """
        try:
            df = pd.read_csv(data_path)
            df['entry_date'] = pd.to_datetime(df['entry_date'])
            df['exit_date'] = pd.to_datetime(df['exit_date'])
            df['duration'] = (df['exit_date'] - df['entry_date']).dt.days
            df['return_pct'] = df['profit'] / df['investment'] * 100
            return df
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def _extract_plans(self) -> List[str]:
        """Extract unique investment plan names from data."""
        return self.data['plan_name'].unique().tolist()
    
    def analyze_plan_performance(self, plan_name: str) -> Dict:
        """
        Calculate key performance metrics for a specific plan.
        
        Args:
            plan_name: Name of investment plan to analyze
            
        Returns:
            Dictionary containing performance metrics
        """
        if plan_name not in self.plans:
            raise ValueError(f"Plan '{plan_name}' not found in data")
            
        plan_data = self.data[self.data['plan_name'] == plan_name]
        
        metrics = {
            'total_trades': len(plan_data),
            'win_rate': len(plan_data[plan_data['profit'] > 0]) / len(plan_data),
            'avg_return': plan_data['return_pct'].mean(),
            'median_return': plan_data['return_pct'].median(),
            'max_drawdown': plan_data['return_pct'].min(),
            'risk_reward': abs(plan_data['return_pct'].mean() / plan_data['return_pct'].min()),
            'avg_duration': plan_data['duration'].mean(),
            'sharpe_ratio': self._calculate_sharpe_ratio(plan_data),
            'sortino_ratio': self._calculate_sortino_ratio(plan_data)
        }
        
        return metrics
    
    def _calculate_sharpe_ratio(self, data: pd.DataFrame, risk_free_rate: float = 0.02) -> float:
        """Calculate annualized Sharpe ratio."""
        returns = data['return_pct']
        excess_returns = returns - risk_free_rate
        return excess_returns.mean() / excess_returns.std()
    
    def _calculate_sortino_ratio(self, data: pd.DataFrame, risk_free_rate: float = 0.02) -> float:
        """Calculate annualized Sortino ratio."""
        returns = data['return_pct']
        excess_returns = returns - risk_free_rate
        downside_returns = returns[returns < 0]
        
        if len(downside_returns) == 0:
            return float('inf')
            
        downside_std = downside_returns.std()
        return excess_returns.mean() / downside_std
    
    def compare_plans(self) -> pd.DataFrame:
        """
        Compare performance metrics across all plans.
        
        Returns:
            DataFrame with comparison metrics
        """
        comparison = []
        for plan in self.plans:
            metrics = self.analyze_plan_performance(plan)
            metrics['plan_name'] = plan
            comparison.append(metrics)
            
        return pd.DataFrame(comparison).set_index('plan_name')
    
    def generate_recommendations(self, risk_tolerance: str = 'medium') -> Dict:
        """
        Generate investment recommendations based on risk tolerance.
        
        Args:
            risk_tolerance: 'low', 'medium', or 'high'
            
        Returns:
            Dictionary with recommendations
        """
        if risk_tolerance not in ['low', 'medium', 'high']:
            raise ValueError("risk_tolerance must be 'low', 'medium', or 'high'")
            
        comparison = self.compare_plans()
        
        if risk_tolerance == 'low':
            best_plan = comparison.sort_values(
                by=['max_drawdown', 'sharpe_ratio'],
                ascending=[True, False]
            ).index[0]
        elif risk_tolerance == 'medium':
            best_plan = comparison.sort_values(
                by=['sharpe_ratio', 'win_rate'],
                ascending=[False, False]
            ).index[0]
        else:  # high risk tolerance
            best_plan = comparison.sort_values(
                by=['avg_return', 'risk_reward'],
                ascending=[False, False]
            ).index[0]
            
        return {
            'recommended_plan': best_plan,
            'reason': f"Best for {risk_tolerance} risk tolerance based on historical performance",
            'metrics': comparison.loc[best_plan].to_dict()
        }
    
    def visualize_performance(self, plan_name: str, save_path: Optional[str] = None):
        """
        Generate performance visualization for a plan.
        
        Args:
            plan_name: Name of plan to visualize
            save_path: Optional path to save the figure
        """
        if plan_name not in self.plans:
            raise ValueError(f"Plan '{plan_name}' not found in data")
            
        plan_data = self.data[self.data['plan_name'] == plan_name]
        
        plt.figure(figsize=(12, 6))
        
        # Cumulative returns plot
        plt.subplot(1, 2, 1)
        cumulative_returns = (1 + plan_data['return_pct'] / 100).cumprod()
        plt.plot(plan_data['entry_date'], cumulative_returns)
        plt.title(f'{plan_name} - Cumulative Returns')
        plt.xlabel('Date')
        plt.ylabel('Growth of $1')
        
        # Returns distribution plot
        plt.subplot(1, 2, 2)
        plt.hist(plan_data['return_pct'], bins=20)
        plt.title(f'{plan_name} - Returns Distribution')
        plt.xlabel('Return (%)')
        plt.ylabel('Frequency')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()


# Example usage
if __name__ == "__main__":
    try:
        analyzer = InvestmentPlanAnalyzer('fintopsignaltrades_data.csv')
        
        # Compare all plans
        comparison = analyzer.compare_plans()
        print("Plan Comparison:")
        print(comparison)
        
        # Get recommendations
        recommendation = analyzer.generate_recommendations('medium')
        print("\nRecommendation:")
        print(recommendation)
        
        # Visualize best plan
        analyzer.visualize_performance(recommendation['recommended_plan'])
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
