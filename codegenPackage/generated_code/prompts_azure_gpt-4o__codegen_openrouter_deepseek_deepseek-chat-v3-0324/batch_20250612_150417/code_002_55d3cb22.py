"""
Generated Code Metadata:
========================
Original URL: https://claim-idegen.com
Prompt: Generate a script to automate the calculation of rewards on investments based on equity and stock trading, using the features mentioned on Ambro Contables' site.
Generated: DETERMINISTIC_55d3cb222ca44d9f
Batch ID: 20250612_150417
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
from datetime import datetime, timedelta
from typing import List, Dict, Union, Optional

class InvestmentRewardCalculator:
    """
    A class to calculate investment rewards based on equity and stock trading.
    Features include:
    - Daily, monthly, and annual return calculations
    - Dividend yield calculations
    - Compound interest calculations
    - Risk-adjusted return metrics
    """
    
    def __init__(self, initial_investment: float, start_date: str, end_date: str):
        """
        Initialize the calculator with investment parameters.
        
        Args:
            initial_investment: Initial investment amount
            start_date: Investment start date (YYYY-MM-DD)
            end_date: Investment end date (YYYY-MM-DD)
        """
        self.initial_investment = initial_investment
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.transactions = pd.DataFrame(columns=['date', 'type', 'amount', 'price', 'shares'])
        self.dividends = pd.DataFrame(columns=['date', 'amount_per_share', 'shares', 'total'])
        self.daily_prices = pd.DataFrame(columns=['date', 'price'])
        
    def add_transaction(self, date: str, transaction_type: str, amount: float, 
                        price: float, shares: float) -> None:
        """
        Add a buy/sell transaction to the investment history.
        
        Args:
            date: Transaction date (YYYY-MM-DD)
            transaction_type: 'buy' or 'sell'
            amount: Transaction amount
            price: Price per share
            shares: Number of shares
        """
        transaction_date = datetime.strptime(date, "%Y-%m-%d")
        if transaction_date < self.start_date or transaction_date > self.end_date:
            raise ValueError("Transaction date outside investment period")
            
        new_transaction = pd.DataFrame({
            'date': [transaction_date],
            'type': [transaction_type],
            'amount': [amount],
            'price': [price],
            'shares': [shares]
        })
        
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)
        
    def add_dividend(self, date: str, amount_per_share: float, shares: float) -> None:
        """
        Add a dividend payment to the investment history.
        
        Args:
            date: Dividend date (YYYY-MM-DD)
            amount_per_share: Dividend amount per share
            shares: Number of shares held
        """
        dividend_date = datetime.strptime(date, "%Y-%m-%d")
        if dividend_date < self.start_date or dividend_date > self.end_date:
            raise ValueError("Dividend date outside investment period")
            
        total = amount_per_share * shares
        new_dividend = pd.DataFrame({
            'date': [dividend_date],
            'amount_per_share': [amount_per_share],
            'shares': [shares],
            'total': [total]
        })
        
        self.dividends = pd.concat([self.dividends, new_dividend], ignore_index=True)
        
    def add_daily_price(self, date: str, price: float) -> None:
        """
        Add daily price data for the investment.
        
        Args:
            date: Price date (YYYY-MM-DD)
            price: Price per share on that date
        """
        price_date = datetime.strptime(date, "%Y-%m-%d")
        if price_date < self.start_date or price_date > self.end_date:
            raise ValueError("Price date outside investment period")
            
        new_price = pd.DataFrame({
            'date': [price_date],
            'price': [price]
        })
        
        self.daily_prices = pd.concat([self.daily_prices, new_price], ignore_index=True)
        
    def calculate_total_return(self) -> Dict[str, float]:
        """
        Calculate total return metrics including:
        - Absolute return
        - Annualized return
        - Dividend yield
        - CAGR
        
        Returns:
            Dictionary containing various return metrics
        """
        if self.daily_prices.empty:
            raise ValueError("No price data available for return calculations")
            
        # Get first and last price
        first_price = self.daily_prices.iloc[0]['price']
        last_price = self.daily_prices.iloc[-1]['price']
        
        # Calculate investment period in years
        days = (self.end_date - self.start_date).days
        years = days / 365.25
        
        # Calculate absolute return
        absolute_return = (last_price - first_price) / first_price
        
        # Calculate annualized return
        annualized_return = (1 + absolute_return) ** (1/years) - 1
        
        # Calculate dividend yield if dividends exist
        dividend_yield = 0.0
        if not self.dividends.empty:
            total_dividends = self.dividends['total'].sum()
            avg_investment = self.initial_investment  # Simplified assumption
            dividend_yield = total_dividends / avg_investment
            
        # Calculate CAGR (Compound Annual Growth Rate)
        ending_value = self.initial_investment * (1 + absolute_return)
        cagr = (ending_value / self.initial_investment) ** (1/years) - 1
        
        return {
            'absolute_return': absolute_return,
            'annualized_return': annualized_return,
            'dividend_yield': dividend_yield,
            'cagr': cagr,
            'total_dividends': total_dividends if not self.dividends.empty else 0.0
        }
        
    def calculate_risk_metrics(self) -> Dict[str, float]:
        """
        Calculate risk metrics including:
        - Standard deviation of daily returns
        - Sharpe ratio (assuming risk-free rate = 0)
        - Maximum drawdown
        
        Returns:
            Dictionary containing various risk metrics
        """
        if self.daily_prices.empty:
            raise ValueError("No price data available for risk calculations")
            
        # Calculate daily returns
        prices = self.daily_prices.sort_values('date')
        prices['daily_return'] = prices['price'].pct_change()
        
        # Standard deviation of daily returns
        daily_std = prices['daily_return'].std()
        
        # Annualized standard deviation
        annual_std = daily_std * np.sqrt(252)  # Assuming 252 trading days
        
        # Sharpe ratio (simplified with risk-free rate = 0)
        sharpe_ratio = prices['daily_return'].mean() / daily_std * np.sqrt(252)
        
        # Maximum drawdown
        prices['cumulative_return'] = (1 + prices['daily_return']).cumprod()
        prices['peak'] = prices['cumulative_return'].cummax()
        prices['drawdown'] = (prices['cumulative_return'] - prices['peak']) / prices['peak']
        max_drawdown = prices['drawdown'].min()
        
        return {
            'daily_volatility': daily_std,
            'annual_volatility': annual_std,
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': max_drawdown
        }
        
    def generate_report(self) -> Dict[str, Union[float, pd.DataFrame]]:
        """
        Generate a comprehensive investment report.
        
        Returns:
            Dictionary containing:
            - return_metrics: Various return calculations
            - risk_metrics: Various risk calculations
            - transaction_history: All transactions
            - dividend_history: All dividends
        """
        try:
            return_metrics = self.calculate_total_return()
            risk_metrics = self.calculate_risk_metrics()
            
            return {
                'return_metrics': return_metrics,
                'risk_metrics': risk_metrics,
                'transaction_history': self.transactions,
                'dividend_history': self.dividends,
                'price_history': self.daily_prices
            }
        except Exception as e:
            raise RuntimeError(f"Error generating report: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Initialize calculator
    calculator = InvestmentRewardCalculator(
        initial_investment=10000,
        start_date="2020-01-01",
        end_date="2022-12-31"
    )
    
    # Add some price data (in a real scenario, this would come from market data)
    calculator.add_daily_price("2020-01-01", 100.0)
    calculator.add_daily_price("2020-06-30", 110.0)
    calculator.add_daily_price("2020-12-31", 120.0)
    calculator.add_daily_price("2021-06-30", 115.0)
    calculator.add_daily_price("2021-12-31", 130.0)
    calculator.add_daily_price("2022-06-30", 140.0)
    calculator.add_daily_price("2022-12-31", 150.0)
    
    # Add some transactions
    calculator.add_transaction("2020-01-01", "buy",
