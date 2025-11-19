"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: Generate code using a financial analysis library to simulate wealth management strategies that align with Alghanim Capital's focus on safeguarding financial futures and achieving personalized goals.
Generated: DETERMINISTIC_d7efe8281313f7d7
Batch ID: 20250612_153854
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
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from datetime import datetime, timedelta
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

class WealthManagementSimulator:
    """
    A class to simulate and analyze wealth management strategies.
    """
    
    def __init__(self, initial_capital, start_date, end_date, risk_tolerance='medium'):
        """
        Initialize the wealth management simulator.
        
        Parameters:
        - initial_capital: float, initial investment amount
        - start_date: str, start date in 'YYYY-MM-DD' format
        - end_date: str, end date in 'YYYY-MM-DD' format
        - risk_tolerance: str, risk profile ('low', 'medium', 'high')
        """
        self.initial_capital = initial_capital
        self.start_date = start_date
        self.end_date = end_date
        self.risk_tolerance = risk_tolerance.lower()
        self.portfolio = {}
        self.historical_data = None
        
    def add_asset(self, ticker, allocation):
        """
        Add an asset to the portfolio.
        
        Parameters:
        - ticker: str, asset ticker symbol
        - allocation: float, percentage allocation (0-1)
        """
        if ticker in self.portfolio:
            raise ValueError(f"Asset {ticker} already exists in portfolio")
        if sum(self.portfolio.values()) + allocation > 1:
            raise ValueError("Total allocation exceeds 100%")
        self.portfolio[ticker] = allocation
        
    def fetch_historical_data(self):
        """
        Fetch historical price data for all assets in the portfolio.
        """
        if not self.portfolio:
            raise ValueError("Portfolio is empty")
            
        tickers = list(self.portfolio.keys())
        data = yf.download(tickers, start=self.start_date, end=self.end_date)['Adj Close']
        self.historical_data = data.dropna()
        
    def calculate_portfolio_returns(self):
        """
        Calculate daily portfolio returns based on historical data.
        
        Returns:
        - pd.Series: Daily portfolio returns
        """
        if self.historical_data is None:
            self.fetch_historical_data()
            
        returns = self.historical_data.pct_change().dropna()
        weighted_returns = returns * list(self.portfolio.values())
        portfolio_returns = weighted_returns.sum(axis=1)
        return portfolio_returns
    
    def simulate_growth(self, monthly_contribution=0):
        """
        Simulate portfolio growth over time.
        
        Parameters:
        - monthly_contribution: float, additional monthly contribution
        
        Returns:
        - pd.DataFrame: Simulated portfolio values over time
        """
        returns = self.calculate_portfolio_returns()
        daily_contrib = monthly_contribution / 21  # Approximate trading days per month
        
        portfolio_value = [self.initial_capital]
        for i, ret in enumerate(returns):
            if i > 0 and i % 21 == 0:  # Monthly contribution
                portfolio_value.append(portfolio_value[-1] * (1 + ret) + daily_contrib * 21)
            else:
                portfolio_value.append(portfolio_value[-1] * (1 + ret))
                
        dates = self.historical_data.index
        return pd.DataFrame({
            'Date': dates,
            'Portfolio Value': portfolio_value[1:]
        }).set_index('Date')
    
    def optimize_portfolio(self, target_return=None):
        """
        Optimize portfolio allocation using Modern Portfolio Theory.
        
        Parameters:
        - target_return: float, optional target return for optimization
        
        Returns:
        - dict: Optimized portfolio allocations
        """
        if self.historical_data is None:
            self.fetch_historical_data()
            
        returns = self.historical_data.pct_change().dropna()
        cov_matrix = returns.cov()
        mean_returns = returns.mean()
        
        num_assets = len(self.portfolio)
        args = (mean_returns, cov_matrix)
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for asset in range(num_assets))
        
        if target_return is not None:
            constraints = (
                {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
                {'type': 'eq', 'fun': lambda x: np.sum(x * mean_returns) - target_return}
            )
        
        def portfolio_volatility(weights, mean_returns, cov_matrix):
            return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        
        if self.risk_tolerance == 'low':
            initial_guess = np.array([1/num_assets] * num_assets)
            result = minimize(portfolio_volatility, initial_guess, args=args,
                            method='SLSQP', bounds=bounds, constraints=constraints)
        elif self.risk_tolerance == 'high':
            def neg_sharpe(weights, mean_returns, cov_matrix):
                rf = 0.02 / 252  # Daily risk-free rate
                ret = np.sum(mean_returns * weights)
                vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
                return -(ret - rf) / vol
                
            initial_guess = np.array([1/num_assets] * num_assets)
            result = minimize(neg_sharpe, initial_guess, args=args,
                            method='SLSQP', bounds=bounds, constraints=constraints)
        else:  # medium
            def min_vol_with_return(weights, mean_returns, cov_matrix):
                target = np.mean(mean_returns)
                return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) + \
                       abs(np.sum(mean_returns * weights) - target)
                       
            initial_guess = np.array([1/num_assets] * num_assets)
            result = minimize(min_vol_with_return, initial_guess, args=args,
                            method='SLSQP', bounds=bounds, constraints=constraints)
        
        optimized_allocations = dict(zip(self.portfolio.keys(), result.x))
        return {k: v for k, v in optimized_allocations.items() if v > 0.01}
    
    def monte_carlo_simulation(self, years=10, simulations=1000, monthly_contribution=0):
        """
        Run Monte Carlo simulation for future portfolio performance.
        
        Parameters:
        - years: int, projection period in years
        - simulations: int, number of simulations to run
        - monthly_contribution: float, additional monthly contribution
        
        Returns:
        - pd.DataFrame: Simulation results
        """
        returns = self.calculate_portfolio_returns()
        mean_return = returns.mean()
        std_return = returns.std()
        
        days = years * 252
        sim_results = np.zeros((days, simulations))
        
        for i in range(simulations):
            daily_returns = np.random.normal(mean_return, std_return, days)
            sim_results[:, i] = self.initial_capital * np.cumprod(1 + daily_returns)
            
            # Add monthly contributions
            for month in range(years * 12):
                start_day = month * 21
                end_day = start_day + 21
                if end_day > days:
                    end_day = days
                sim_results[start_day:end_day, i] += monthly_contribution * (month + 1)
        
        return pd.DataFrame(sim_results)
    
    def generate_report(self, simulation_results=None):
        """
        Generate a comprehensive wealth management report.
        
        Parameters:
        - simulation_results: pd.DataFrame, Monte Carlo simulation results
        
        Returns:
        - dict: Report containing key metrics and visualizations
        """
        report = {}
        
        # Portfolio composition
        report['portfolio_composition'] = self.portfolio
        
        # Historical performance
        growth = self.simulate_growth()
        report['final_value'] = growth.iloc[-1]['Portfolio Value']
        report['cagr'] = (report['final_value'] / self.initial_capital) ** (1/len(growth)*252) - 1
        
        # Risk metrics
        returns = self.calculate_portfolio_returns()
        report['volatility'] = returns.std() * np.sqrt(252)
        report['max_drawdown'] = (growth['Portfolio Value'].cummax() - growth['Portfolio Value']).max()
        
        # Monte Carlo results
        if simulation_results is not None:
            final_values = simulation_results.iloc[-1]
            report['success_probability'] = np.mean(final_values >= self.initial_capital)
            report['percentiles'] = {
                '5th': np.percentile(final_values, 5),
                '50th': np.percentile(final_values, 50),
                '95th': np.percentile(final_values, 95)
            }
        
        return report
    
    def plot_simulation(self, simulation_results):
        """
        Plot Monte Carlo simulation results.
        
        Parameters:
        - simulation_results: pd.DataFrame, Monte Carlo simulation
