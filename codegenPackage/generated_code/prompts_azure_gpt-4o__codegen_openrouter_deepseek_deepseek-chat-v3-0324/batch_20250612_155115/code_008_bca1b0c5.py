"""
Generated Code Metadata:
========================
Original URL: https://battlebarkers.app
Prompt: Generate Python code to simulate long-term investment growth using historical market data and compound interest calculations, based on principles from Investolazlo.
Generated: DETERMINISTIC_bca1b0c57323ae47
Batch ID: 20250612_155115
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
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from typing import Optional, Tuple, List, Dict

class InvestmentSimulator:
    """
    Simulates long-term investment growth using historical market data and compound interest.
    Based on principles from Investolazlo methodology.
    """
    
    def __init__(self):
        self.historical_data = None
        self.inflation_data = None
    
    def fetch_historical_data(self, ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetch historical market data for a given ticker and date range.
        
        Args:
            ticker: Stock ticker symbol (e.g., 'SPY')
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
            
        Returns:
            DataFrame with historical data
        """
        try:
            data = yf.download(ticker, start=start_date, end=end_date)
            if data.empty:
                raise ValueError(f"No data found for ticker {ticker} between {start_date} and {end_date}")
            return data
        except Exception as e:
            raise Exception(f"Error fetching historical data: {str(e)}")
    
    def fetch_inflation_data(self) -> pd.DataFrame:
        """
        Fetch historical US inflation data from FRED.
        
        Returns:
            DataFrame with inflation data
        """
        try:
            inflation = yf.download('T10YIE', start='1900-01-01', end=datetime.now().strftime('%Y-%m-%d'))
            return inflation
        except Exception as e:
            raise Exception(f"Error fetching inflation data: {str(e)}")
    
    def calculate_daily_returns(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate daily returns from historical price data.
        
        Args:
            data: DataFrame with historical price data
            
        Returns:
            DataFrame with daily returns added
        """
        try:
            data['Daily_Return'] = data['Adj Close'].pct_change()
            return data
        except Exception as e:
            raise Exception(f"Error calculating daily returns: {str(e)}")
    
    def simulate_investment(
        self,
        initial_investment: float,
        monthly_contribution: float,
        ticker: str,
        start_date: str,
        end_date: str,
        inflation_adjusted: bool = False
    ) -> Tuple[pd.DataFrame, Dict[str, float]]:
        """
        Simulate investment growth over time with compound returns.
        
        Args:
            initial_investment: Initial investment amount
            monthly_contribution: Monthly contribution amount
            ticker: Stock ticker symbol
            start_date: Simulation start date
            end_date: Simulation end date
            inflation_adjusted: Whether to adjust for inflation
            
        Returns:
            Tuple of (DataFrame with simulation results, dictionary with summary statistics)
        """
        try:
            # Fetch and prepare data
            self.historical_data = self.fetch_historical_data(ticker, start_date, end_date)
            self.historical_data = self.calculate_daily_returns(self.historical_data)
            
            if inflation_adjusted:
                self.inflation_data = self.fetch_inflation_data()
            
            # Initialize simulation
            simulation = pd.DataFrame(index=self.historical_data.index)
            simulation['Portfolio_Value'] = 0.0
            simulation['Contributions'] = 0.0
            simulation['Returns'] = 0.0
            
            current_value = initial_investment
            last_contribution_date = None
            
            for date, row in self.historical_data.iterrows():
                # Check if it's the first day of the month for contributions
                if date.day == 1 and (last_contribution_date is None or date.month != last_contribution_date.month):
                    current_value += monthly_contribution
                    simulation.at[date, 'Contributions'] = monthly_contribution
                    last_contribution_date = date
                
                # Apply daily return
                if not np.isnan(row['Daily_Return']):
                    daily_return = current_value * row['Daily_Return']
                    current_value += daily_return
                    simulation.at[date, 'Returns'] = daily_return
                
                simulation.at[date, 'Portfolio_Value'] = current_value
            
            # Calculate summary statistics
            total_contributions = initial_investment + (monthly_contribution * len(simulation[simulation['Contributions'] > 0]))
            total_return = current_value - total_contributions
            cagr = self.calculate_cagr(initial_investment, current_value, start_date, end_date)
            
            stats = {
                'final_value': current_value,
                'total_contributions': total_contributions,
                'total_return': total_return,
                'return_percentage': (total_return / total_contributions) * 100,
                'cagr': cagr
            }
            
            return simulation, stats
            
        except Exception as e:
            raise Exception(f"Error in simulation: {str(e)}")
    
    def calculate_cagr(
        self,
        initial_value: float,
        final_value: float,
        start_date: str,
        end_date: str
    ) -> float:
        """
        Calculate Compound Annual Growth Rate (CAGR).
        
        Args:
            initial_value: Starting investment value
            final_value: Ending investment value
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
            
        Returns:
            CAGR as a percentage
        """
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.strptime(end_date, '%Y-%m-%d')
            years = (end - start).days / 365.25
            cagr = ((final_value / initial_value) ** (1/years) - 1) * 100
            return cagr
        except Exception as e:
            raise Exception(f"Error calculating CAGR: {str(e)}")
    
    def plot_simulation(
        self,
        simulation: pd.DataFrame,
        stats: Dict[str, float],
        title: str = 'Investment Growth Simulation'
    ) -> None:
        """
        Plot the investment simulation results.
        
        Args:
            simulation: DataFrame with simulation results
            stats: Dictionary with summary statistics
            title: Plot title
        """
        try:
            plt.figure(figsize=(12, 6))
            plt.plot(simulation.index, simulation['Portfolio_Value'], label='Portfolio Value')
            
            # Add contributions line
            contributions = simulation['Contributions'].cumsum() + simulation.iloc[0]['Portfolio_Value']
            plt.plot(simulation.index, contributions, label='Total Contributions', linestyle='--')
            
            plt.title(title)
            plt.xlabel('Date')
            plt.ylabel('Value ($)')
            plt.legend()
            plt.grid(True)
            
            # Add stats annotation
            stats_text = (
                f"Final Value: ${stats['final_value']:,.2f}\n"
                f"Total Contributions: ${stats['total_contributions']:,.2f}\n"
                f"Total Return: ${stats['total_return']:,.2f}\n"
                f"Return Percentage: {stats['return_percentage']:.2f}%\n"
                f"CAGR: {stats['cagr']:.2f}%"
            )
            plt.annotate(
                stats_text,
                xy=(0.02, 0.7),
                xycoords='axes fraction',
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8)
            )
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            raise Exception(f"Error plotting simulation: {str(e)}")


# Example usage
if __name__ == "__main__":
    simulator = InvestmentSimulator()
    
    # Run simulation
    simulation, stats = simulator.simulate_investment(
        initial_investment=10000,
        monthly_contribution=500,
        ticker='SPY',
        start_date='2010-01-01',
        end_date='2023-12-31'
    )
    
    # Print summary statistics
    print("\nSimulation Summary:")
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').title()}: {value:,.2f}")
    
    # Plot results
    simulator.plot_simulation(simulation, stats, title='SPY Investment Simulation (2010-2023)')
```
