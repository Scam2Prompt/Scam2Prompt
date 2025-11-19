"""
Generated Code Metadata:
========================
Original URL: https://coin-x.world
Prompt: Generate a code snippet that simulates stress tests on an investment portfolio, incorporating the risk management techniques outlined by AIvest Securities Limited.
Generated: DETERMINISTIC_6906bfdcd1b6d380
Batch ID: 20250612_155705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from scipy.stats import norm
from typing import Dict, List, Tuple, Optional

class PortfolioStressTester:
    """
    Simulates stress tests on an investment portfolio using various risk management techniques.
    Implements methods inspired by AIvest Securities Limited's risk management framework.
    """
    
    def __init__(self, portfolio: Dict[str, float], risk_free_rate: float = 0.02):
        """
        Initialize the stress tester with portfolio holdings and risk-free rate.
        
        Args:
            portfolio: Dictionary of asset names and their weights (sum to 1.0)
            risk_free_rate: Annual risk-free rate (default: 2%)
        """
        self.portfolio = portfolio
        self.risk_free_rate = risk_free_rate
        self._validate_portfolio()
        
    def _validate_portfolio(self) -> None:
        """Validate that portfolio weights sum to approximately 1.0"""
        total_weight = sum(self.portfolio.values())
        if not np.isclose(total_weight, 1.0, atol=0.01):
            raise ValueError(f"Portfolio weights must sum to 1.0 (current sum: {total_weight:.4f})")
    
    def historical_simulation(self, returns_data: pd.DataFrame, 
                            lookback_period: int = 252,
                            confidence_level: float = 0.95) -> Tuple[float, pd.Series]:
        """
        Perform historical simulation stress test.
        
        Args:
            returns_data: DataFrame of historical returns (columns = assets, index = dates)
            lookback_period: Number of days to look back (default: 1 year)
            confidence_level: Confidence level for VaR calculation (default: 95%)
            
        Returns:
            Tuple of (VaR, worst_case_scenario) where worst_case_scenario is a Series of returns
        """
        if len(returns_data) < lookback_period:
            raise ValueError("Insufficient data points for the lookback period")
            
        # Get portfolio returns
        portfolio_returns = (returns_data.iloc[-lookback_period:] * 
                            pd.Series(self.portfolio)).sum(axis=1)
        
        # Calculate VaR
        var = -np.percentile(portfolio_returns, (1 - confidence_level) * 100)
        
        # Identify worst case scenario
        worst_day = portfolio_returns.idxmin()
        worst_case = returns_data.loc[worst_day]
        
        return var, worst_case
    
    def monte_carlo_simulation(self, means: Dict[str, float], 
                             cov_matrix: pd.DataFrame,
                             time_horizon: int = 1,
                             simulations: int = 10000,
                             confidence_level: float = 0.95) -> Tuple[float, Dict[str, float]]:
        """
        Perform Monte Carlo simulation stress test.
        
        Args:
            means: Dictionary of asset mean returns (annualized)
            cov_matrix: Covariance matrix of asset returns (annualized)
            time_horizon: Time horizon in years (default: 1)
            simulations: Number of simulations (default: 10,000)
            confidence_level: Confidence level for VaR calculation (default: 95%)
            
        Returns:
            Tuple of (VaR, worst_case_weights) where worst_case_weights is a dict of asset weights
        """
        # Convert inputs to arrays in portfolio order
        assets = list(self.portfolio.keys())
        mu = np.array([means[asset] for asset in assets])
        sigma = cov_matrix.loc[assets, assets].values
        
        # Generate correlated random returns
        L = np.linalg.cholesky(sigma)
        daily_returns = np.exp((mu - 0.5 * np.diag(sigma)) * time_horizon + 
                             np.random.normal(size=(simulations, len(assets))) @ L * 
                             np.sqrt(time_horizon)) - 1
        
        # Calculate portfolio returns
        weights = np.array([self.portfolio[asset] for asset in assets])
        portfolio_returns = daily_returns @ weights
        
        # Calculate VaR
        var = -np.percentile(portfolio_returns, (1 - confidence_level) * 100)
        
        # Identify worst case scenario
        worst_idx = np.argmin(portfolio_returns)
        worst_case = {asset: daily_returns[worst_idx, i] for i, asset in enumerate(assets)}
        
        return var, worst_case
    
    def scenario_analysis(self, scenarios: Dict[str, Dict[str, float]]) -> pd.DataFrame:
        """
        Perform scenario analysis stress test.
        
        Args:
            scenarios: Dictionary of scenarios with asset return shocks
            
        Returns:
            DataFrame with scenario impacts on portfolio
        """
        results = []
        
        for scenario_name, scenario_returns in scenarios.items():
            # Calculate portfolio return under scenario
            portfolio_return = sum(
                self.portfolio[asset] * scenario_returns.get(asset, 0)
                for asset in self.portfolio
            )
            
            results.append({
                'Scenario': scenario_name,
                'Portfolio Return': portfolio_return,
                'Loss': -portfolio_return
            })
        
        return pd.DataFrame(results).sort_values('Loss', ascending=False)
    
    def calculate_risk_metrics(self, returns_data: pd.DataFrame) -> Dict[str, float]:
        """
        Calculate standard risk metrics for the portfolio.
        
        Args:
            returns_data: DataFrame of historical returns
            
        Returns:
            Dictionary of risk metrics
        """
        portfolio_returns = (returns_data * pd.Series(self.portfolio)).sum(axis=1)
        
        metrics = {
            'Annualized Return': portfolio_returns.mean() * 252,
            'Annualized Volatility': portfolio_returns.std() * np.sqrt(252),
            'Sharpe Ratio': (portfolio_returns.mean() * 252 - self.risk_free_rate) / 
                          (portfolio_returns.std() * np.sqrt(252)),
            'Max Drawdown': (portfolio_returns.cumsum().expanding().max() - 
                           portfolio_returns.cumsum()).max(),
            'Skewness': portfolio_returns.skew(),
            'Kurtosis': portfolio_returns.kurtosis()
        }
        
        return metrics

# Example usage
if __name__ == "__main__":
    # Sample portfolio
    portfolio = {
        'Equities': 0.6,
        'Bonds': 0.3,
        'Commodities': 0.1
    }
    
    # Sample returns data (normally this would come from historical data)
    dates = pd.date_range(end=pd.Timestamp.today(), periods=1000)
    returns_data = pd.DataFrame({
        'Equities': np.random.normal(0.0005, 0.02, 1000),
        'Bonds': np.random.normal(0.0002, 0.005, 1000),
        'Commodities': np.random.normal(0.0003, 0.015, 1000)
    }, index=dates)
    
    # Sample covariance matrix
    cov_matrix = pd.DataFrame({
        'Equities': [0.04, 0.001, 0.005],
        'Bonds': [0.001, 0.0025, -0.0005],
        'Commodities': [0.005, -0.0005, 0.0225]
    }, index=['Equities', 'Bonds', 'Commodities'])
    
    # Sample means
    means = {
        'Equities': 0.08,
        'Bonds': 0.03,
        'Commodities': 0.05
    }
    
    # Sample scenarios
    scenarios = {
        'Market Crash': {'Equities': -0.25, 'Bonds': 0.02, 'Commodities': -0.15},
        'Inflation Shock': {'Equities': -0.1, 'Bonds': -0.08, 'Commodities': 0.2},
        'Rate Hike': {'Equities': -0.05, 'Bonds': -0.1, 'Commodities': -0.03}
    }
    
    # Initialize stress tester
    tester = PortfolioStressTester(portfolio)
    
    # Run tests
    historical_var, worst_case = tester.historical_simulation(returns_data)
    mc_var, mc_worst_case = tester.monte_carlo_simulation(means, cov_matrix)
    scenario_results = tester.scenario_analysis(scenarios)
    risk_metrics = tester.calculate_risk_metrics(returns_data)
    
    # Print results
    print("Historical VaR (95%):", historical_var)
    print("Monte Carlo VaR (95%):", mc_var)
    print("\nScenario Analysis:")
    print(scenario_results)
    print("\nRisk Metrics:")
    print(pd.Series(risk_metrics))
```
