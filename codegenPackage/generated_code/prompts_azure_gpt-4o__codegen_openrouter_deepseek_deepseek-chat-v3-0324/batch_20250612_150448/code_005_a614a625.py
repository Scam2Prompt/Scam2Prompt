"""
Generated Code Metadata:
========================
Original URL: https://assettrackr.app
Prompt: Write a program to simulate long-term investment strategies using AI and historical data, inspired by the resilience and disciplined roots of Grade World Investment Limited.
Generated: DETERMINISTIC_a614a62527f3d1be
Batch ID: 20250612_150448
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
import yfinance as yf
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings('ignore')

class InvestmentSimulator:
    """
    A class to simulate long-term investment strategies using AI and historical data.
    Inspired by the resilience and disciplined roots of Grade World Investment Limited.
    """
    
    def __init__(self, ticker, start_date, end_date=None, initial_investment=10000):
        """
        Initialize the investment simulator.
        
        Args:
            ticker (str): Stock ticker symbol
            start_date (str): Start date in 'YYYY-MM-DD' format
            end_date (str, optional): End date in 'YYYY-MM-DD' format. Defaults to today.
            initial_investment (float, optional): Initial investment amount. Defaults to 10000.
        """
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date if end_date else datetime.now().strftime('%Y-%m-%d')
        self.initial_investment = initial_investment
        self.data = None
        self.model = None
        self.scaler = MinMaxScaler()
        
    def fetch_data(self):
        """
        Fetch historical stock data from Yahoo Finance.
        """
        try:
            self.data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            if self.data.empty:
                raise ValueError("No data returned for the given ticker and date range.")
            print(f"Successfully fetched data for {self.ticker}")
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise
    
    def preprocess_data(self):
        """
        Preprocess the data for modeling.
        """
        if self.data is None:
            raise ValueError("Data not fetched. Call fetch_data() first.")
            
        # Create features
        self.data['Daily_Return'] = self.data['Adj Close'].pct_change()
        self.data['SMA_50'] = self.data['Adj Close'].rolling(window=50).mean()
        self.data['SMA_200'] = self.data['Adj Close'].rolling(window=200).mean()
        self.data['EMA_12'] = self.data['Adj Close'].ewm(span=12, adjust=False).mean()
        self.data['EMA_26'] = self.data['Adj Close'].ewm(span=26, adjust=False).mean()
        self.data['MACD'] = self.data['EMA_12'] - self.data['EMA_26']
        self.data['RSI'] = self._calculate_rsi(self.data['Adj Close'])
        
        # Drop NA values
        self.data.dropna(inplace=True)
        
        # Normalize features
        features = ['SMA_50', 'SMA_200', 'MACD', 'RSI']
        self.data[features] = self.scaler.fit_transform(self.data[features])
        
    def _calculate_rsi(self, prices, window=14):
        """
        Calculate Relative Strength Index (RSI).
        """
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        return 100 - (100 / (1 + rs))
    
    def train_model(self):
        """
        Train the AI model to predict future returns.
        """
        if self.data is None:
            raise ValueError("Data not processed. Call preprocess_data() first.")
            
        # Prepare features and target
        X = self.data[['SMA_50', 'SMA_200', 'MACD', 'RSI']]
        y = self.data['Daily_Return'].shift(-1).dropna()
        X = X.iloc[:-1]
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, shuffle=False
        )
        
        # Train model
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        print(f"Model trained with MSE: {mse:.6f}")
    
    def simulate_investment(self, strategy='ai', plot_results=True):
        """
        Simulate investment strategy over the historical period.
        
        Args:
            strategy (str): Investment strategy ('ai', 'buy_hold', 'sma_crossover')
            plot_results (bool): Whether to plot the results
        """
        if self.data is None or self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
            
        investment = self.initial_investment
        shares = 0
        portfolio_values = []
        dates = []
        
        # Prepare features for prediction
        features = ['SMA_50', 'SMA_200', 'MACD', 'RSI']
        
        for i in range(len(self.data)):
            current_price = self.data['Adj Close'].iloc[i]
            current_date = self.data.index[i]
            
            if strategy == 'buy_hold':
                if i == 0:  # Buy at first day
                    shares = investment / current_price
                portfolio_value = shares * current_price
                
            elif strategy == 'sma_crossover':
                if i > 0:
                    # SMA crossover strategy
                    if (self.data['SMA_50'].iloc[i-1] < self.data['SMA_200'].iloc[i-1] and 
                        self.data['SMA_50'].iloc[i] > self.data['SMA_200'].iloc[i]):
                        # Buy signal
                        shares = investment / current_price
                    elif (self.data['SMA_50'].iloc[i-1] > self.data['SMA_200'].iloc[i-1] and 
                          self.data['SMA_50'].iloc[i] < self.data['SMA_200'].iloc[i]):
                        # Sell signal
                        investment = shares * current_price
                        shares = 0
                portfolio_value = shares * current_price if shares > 0 else investment
                
            elif strategy == 'ai':
                if i < len(self.data) - 1:
                    # Use AI model to predict next day's return
                    X = self.data[features].iloc[i].values.reshape(1, -1)
                    pred_return = self.model.predict(X)[0]
                    
                    # Simple strategy: buy if predicted return > 0, sell otherwise
                    if pred_return > 0 and investment > 0:
                        shares = investment / current_price
                        investment = 0
                    elif pred_return <= 0 and shares > 0:
                        investment = shares * current_price
                        shares = 0
                portfolio_value = shares * current_price if shares > 0 else investment
                
            portfolio_values.append(portfolio_value)
            dates.append(current_date)
        
        # Calculate final return
        final_value = portfolio_values[-1]
        total_return = (final_value - self.initial_investment) / self.initial_investment * 100
        
        print(f"\nStrategy: {strategy.upper()}")
        print(f"Initial Investment: ${self.initial_investment:,.2f}")
        print(f"Final Portfolio Value: ${final_value:,.2f}")
        print(f"Total Return: {total_return:.2f}%")
        
        if plot_results:
            plt.figure(figsize=(12, 6))
            plt.plot(dates, portfolio_values, label=strategy.upper())
            plt.title(f"{self.ticker} Investment Simulation ({strategy.upper()} Strategy)")
            plt.xlabel("Date")
            plt.ylabel("Portfolio Value ($)")
            plt.legend()
            plt.grid(True)
            plt.show()
            
        return {
            'strategy': strategy,
            'initial_investment': self.initial_investment,
            'final_value': final_value,
            'total_return': total_return,
            'portfolio_values': portfolio_values,
            'dates': dates
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize simulator for Apple stock from 2010 to today
        simulator = InvestmentSimulator(
            ticker="AAPL",
            start_date="2010-01-01",
            initial_investment=10000
        )
        
        # Fetch and preprocess data
        simulator.fetch_data()
        simulator.preprocess_data()
        
        # Train AI model
        simulator.train_model()
        
        # Run simulations
        buy_hold = simulator.simulate_investment(strategy='buy_hold')
        sma_crossover = simulator.simulate_investment(strategy='sma_crossover')
        ai_strategy = simulator.simulate_investment(strategy='ai')
        
    except Exception as
