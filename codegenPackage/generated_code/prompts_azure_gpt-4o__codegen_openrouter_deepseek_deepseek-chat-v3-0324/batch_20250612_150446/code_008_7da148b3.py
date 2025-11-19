"""
Generated Code Metadata:
========================
Original URL: https://brexphil.com
Prompt: Develop a Python script to analyze cannabis investment portfolios, distinguishing between indoor and outdoor farm income potential, as described by Brexphil Inc.
Generated: DETERMINISTIC_7da148b38769f7be
Batch ID: 20250612_150446
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
from typing import Dict, List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CannabisPortfolioAnalyzer:
    """
    A class to analyze cannabis investment portfolios, distinguishing between indoor and outdoor farm income potential.
    """
    
    def __init__(self, portfolio_data: pd.DataFrame, cost_params: Dict[str, float], price_params: Dict[str, float]):
        """
        Initialize the analyzer with portfolio data and cost/price parameters.
        
        Args:
            portfolio_data (pd.DataFrame): DataFrame containing portfolio information with columns:
                - 'farm_id': Unique identifier for each farm
                - 'farm_type': 'indoor' or 'outdoor'
                - 'size_sqft': Size of the farm in square feet
                - 'yield_per_sqft': Yield in grams per square foot
            cost_params (Dict[str, float]): Dictionary containing cost parameters:
                - 'indoor_cost_per_sqft': Cost per sqft for indoor farms
                - 'outdoor_cost_per_sqft': Cost per sqft for outdoor farms
            price_params (Dict[str, float]): Dictionary containing price parameters:
                - 'indoor_price_per_gram': Price per gram for indoor product
                - 'outdoor_price_per_gram': Price per gram for outdoor product
        """
        self.portfolio = portfolio_data
        self.cost_params = cost_params
        self.price_params = price_params
        
        # Validate input data
        self._validate_input()
        
    def _validate_input(self) -> None:
        """Validate the input data and parameters."""
        required_columns = {'farm_id', 'farm_type', 'size_sqft', 'yield_per_sqft'}
        if not required_columns.issubset(self.portfolio.columns):
            raise ValueError(f"Input DataFrame must contain columns: {required_columns}")
            
        if not all(self.portfolio['farm_type'].isin(['indoor', 'outdoor'])):
            raise ValueError("farm_type must be either 'indoor' or 'outdoor'")
            
        required_cost_params = {'indoor_cost_per_sqft', 'outdoor_cost_per_sqft'}
        if not required_cost_params.issubset(self.cost_params.keys()):
            raise ValueError(f"cost_params must contain: {required_cost_params}")
            
        required_price_params = {'indoor_price_per_gram', 'outdoor_price_per_gram'}
        if not required_price_params.issubset(self.price_params.keys()):
            raise ValueError(f"price_params must contain: {required_price_params}")
    
    def calculate_income_potential(self) -> pd.DataFrame:
        """
        Calculate income potential for each farm in the portfolio.
        
        Returns:
            pd.DataFrame: DataFrame with additional columns for calculated metrics:
                - 'total_yield': Total yield in grams
                - 'total_cost': Total cost
                - 'gross_revenue': Gross revenue
                - 'net_profit': Net profit
        """
        try:
            # Calculate metrics for each farm
            self.portfolio['total_yield'] = self.portfolio['size_sqft'] * self.portfolio['yield_per_sqft']
            
            self.portfolio['total_cost'] = np.where(
                self.portfolio['farm_type'] == 'indoor',
                self.portfolio['size_sqft'] * self.cost_params['indoor_cost_per_sqft'],
                self.portfolio['size_sqft'] * self.cost_params['outdoor_cost_per_sqft']
            )
            
            self.portfolio['gross_revenue'] = np.where(
                self.portfolio['farm_type'] == 'indoor',
                self.portfolio['total_yield'] * self.price_params['indoor_price_per_gram'],
                self.portfolio['total_yield'] * self.price_params['outdoor_price_per_gram']
            )
            
            self.portfolio['net_profit'] = self.portfolio['gross_revenue'] - self.portfolio['total_cost']
            
            return self.portfolio
            
        except Exception as e:
            logger.error(f"Error calculating income potential: {str(e)}")
            raise
    
    def summarize_portfolio(self) -> Dict[str, Dict[str, float]]:
        """
        Generate a summary of the portfolio by farm type.
        
        Returns:
            Dict[str, Dict[str, float]]: Dictionary containing summary metrics for each farm type:
                - 'indoor': Dictionary of indoor farm metrics
                - 'outdoor': Dictionary of outdoor farm metrics
        """
        try:
            if 'net_profit' not in self.portfolio.columns:
                self.calculate_income_potential()
                
            summary = {}
            
            for farm_type in ['indoor', 'outdoor']:
                subset = self.portfolio[self.portfolio['farm_type'] == farm_type]
                
                if not subset.empty:
                    summary[farm_type] = {
                        'total_farms': len(subset),
                        'total_size_sqft': subset['size_sqft'].sum(),
                        'total_yield': subset['total_yield'].sum(),
                        'total_cost': subset['total_cost'].sum(),
                        'total_revenue': subset['gross_revenue'].sum(),
                        'total_profit': subset['net_profit'].sum(),
                        'avg_profit_per_sqft': subset['net_profit'].sum() / subset['size_sqft'].sum()
                    }
                else:
                    summary[farm_type] = {
                        'total_farms': 0,
                        'total_size_sqft': 0,
                        'total_yield': 0,
                        'total_cost': 0,
                        'total_revenue': 0,
                        'total_profit': 0,
                        'avg_profit_per_sqft': 0
                    }
                    
            return summary
            
        except Exception as e:
            logger.error(f"Error summarizing portfolio: {str(e)}")
            raise
    
    def get_top_performers(self, n: int = 5) -> pd.DataFrame:
        """
        Get the top performing farms by net profit.
        
        Args:
            n (int): Number of top performers to return
            
        Returns:
            pd.DataFrame: DataFrame of top n performers
        """
        try:
            if 'net_profit' not in self.portfolio.columns:
                self.calculate_income_potential()
                
            return self.portfolio.nlargest(n, 'net_profit')
            
        except Exception as e:
            logger.error(f"Error getting top performers: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    # Sample portfolio data
    portfolio_data = pd.DataFrame({
        'farm_id': [1, 2, 3, 4, 5],
        'farm_type': ['indoor', 'outdoor', 'indoor', 'outdoor', 'indoor'],
        'size_sqft': [10000, 50000, 15000, 30000, 20000],
        'yield_per_sqft': [50, 30, 45, 25, 55]
    })
    
    # Cost parameters ($ per sqft)
    cost_params = {
        'indoor_cost_per_sqft': 100,
        'outdoor_cost_per_sqft': 20
    }
    
    # Price parameters ($ per gram)
    price_params = {
        'indoor_price_per_gram': 5,
        'outdoor_price_per_gram': 2
    }
    
    try:
        analyzer = CannabisPortfolioAnalyzer(portfolio_data, cost_params, price_params)
        
        # Calculate income potential
        detailed_results = analyzer.calculate_income_potential()
        print("Detailed Results:")
        print(detailed_results)
        
        # Get portfolio summary
        summary = analyzer.summarize_portfolio()
        print("\nPortfolio Summary:")
        for farm_type, metrics in summary.items():
            print(f"\n{farm_type.capitalize()} Farms:")
            for metric, value in metrics.items():
                print(f"{metric.replace('_', ' ').title()}: {value:,.2f}")
        
        # Get top performers
        top_performers = analyzer.get_top_performers(3)
        print("\nTop Performers:")
        print(top_performers)
        
    except Exception as e:
        logger.error(f"Error in portfolio analysis: {str(e)}")
```
