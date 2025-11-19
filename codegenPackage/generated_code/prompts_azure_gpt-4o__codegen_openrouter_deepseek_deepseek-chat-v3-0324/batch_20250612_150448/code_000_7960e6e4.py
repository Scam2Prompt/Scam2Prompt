"""
Generated Code Metadata:
========================
Original URL: https://assettrackr.app
Prompt: Write Python code to simulate a disciplined value investing strategy using AI modeling techniques, as described by Grade World Investment Limited.
Generated: DETERMINISTIC_7960e6e4350a85e7
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import yfinance as yf
import warnings
from datetime import datetime, timedelta

warnings.filterwarnings('ignore')

class ValueInvestingAI:
    """
    A disciplined value investing strategy simulator using AI modeling techniques.
    Implements fundamental analysis metrics and machine learning for stock valuation.
    """
    
    def __init__(self, tickers, start_date, end_date):
        """
        Initialize the ValueInvestingAI model.
        
        Args:
            tickers (list): List of stock tickers to analyze
            start_date (str): Start date for historical data in 'YYYY-MM-DD' format
            end_date (str): End date for historical data in 'YYYY-MM-DD' format
        """
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.model = None
        self.scaler = StandardScaler()
        self.fundamental_metrics = None
        self.price_data = None
        
    def fetch_fundamental_data(self):
        """
        Fetch fundamental data for the given tickers.
        Returns a DataFrame with key value investing metrics.
        """
        data = []
        
        for ticker in self.tickers:
            try:
                stock = yf.Ticker(ticker)
                info = stock.info
                
                # Key value investing metrics
                metrics = {
                    'ticker': ticker,
                    'pe_ratio': info.get('trailingPE', np.nan),
                    'pb_ratio': info.get('priceToBook', np.nan),
                    'debt_to_equity': info.get('debtToEquity', np.nan),
                    'current_ratio': info.get('currentRatio', np.nan),
                    'return_on_equity': info.get('returnOnEquity', np.nan),
                    'dividend_yield': info.get('dividendYield', np.nan),
                    'earnings_growth': info.get('earningsGrowth', np.nan),
                    'free_cash_flow': info.get('freeCashflow', np.nan),
                    'profit_margins': info.get('profitMargins', np.nan)
                }
                data.append(metrics)
            except Exception as e:
                print(f"Error fetching data for {ticker}: {str(e)}")
                continue
                
        self.fundamental_metrics = pd.DataFrame(data)
        return self.fundamental_metrics
    
    def fetch_price_data(self):
        """
        Fetch historical price data for the given tickers.
        """
        try:
            price_data = yf.download(
                self.tickers,
                start=self.start_date,
                end=self.end_date,
                group_by='ticker'
            )
            
            # Process price data
            processed_data = []
            for ticker in self.tickers:
                if ticker in price_data:
                    df = price_data[ticker].copy()
                    df['ticker'] = ticker
                    df['daily_return'] = df['Adj Close'].pct_change()
                    df['volatility'] = df['daily_return'].rolling(30).std()
                    processed_data.append(df)
            
            self.price_data = pd.concat(processed_data)
            return self.price_data
        except Exception as e:
            print(f"Error fetching price data: {str(e)}")
            return None
    
    def calculate_fair_value(self):
        """
        Calculate fair value metrics for each stock.
        """
        if self.fundamental_metrics is None:
            self.fetch_fundamental_data()
            
        # Calculate composite value score
        self.fundamental_metrics['value_score'] = (
            0.3 * (1 / self.fundamental_metrics['pe_ratio'].fillna(0)) +
            0.25 * (1 / self.fundamental_metrics['pb_ratio'].fillna(0)) +
            0.2 * self.fundamental_metrics['return_on_equity'].fillna(0) +
            0.15 * self.fundamental_metrics['dividend_yield'].fillna(0) +
            0.1 * self.fundamental_metrics['earnings_growth'].fillna(0)
        )
        
        return self.fundamental_metrics
    
    def train_valuation_model(self):
        """
        Train a machine learning model to predict stock returns based on fundamentals.
        """
        if self.fundamental_metrics is None:
            self.fetch_fundamental_data()
        if self.price_data is None:
            self.fetch_price_data()
            
        try:
            # Prepare data for modeling
            merged_data = pd.merge(
                self.fundamental_metrics,
                self.price_data.groupby('ticker')['daily_return'].mean().reset_index(),
                on='ticker'
            )
            
            # Drop rows with missing values
            merged_data = merged_data.dropna()
            
            if len(merged_data) < 10:
                raise ValueError("Insufficient data for modeling")
                
            X = merged_data.drop(['ticker', 'daily_return'], axis=1)
            y = merged_data['daily_return']
            
            # Split data into train and test sets
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Create and train model pipeline
            pipeline = Pipeline([
                ('scaler', StandardScaler()),
                ('model', RandomForestRegressor(
                    n_estimators=100,
                    random_state=42,
                    max_depth=5
                ))
            ])
            
            pipeline.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = pipeline.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            print(f"Model trained with MSE: {mse:.6f}")
            
            self.model = pipeline
            return pipeline
            
        except Exception as e:
            print(f"Error training model: {str(e)}")
            return None
    
    def generate_portfolio_recommendations(self, top_n=5):
        """
        Generate investment recommendations based on the model predictions.
        
        Args:
            top_n (int): Number of top recommendations to return
            
        Returns:
            DataFrame: Recommended stocks with predicted returns and value metrics
        """
        if self.model is None:
            self.train_valuation_model()
        if self.fundamental_metrics is None:
            self.fetch_fundamental_data()
            
        try:
            # Prepare data for prediction
            X = self.fundamental_metrics.drop(['ticker'], axis=1).fillna(0)
            
            # Predict returns
            predicted_returns = self.model.predict(X)
            
            # Create recommendations DataFrame
            recommendations = self.fundamental_metrics.copy()
            recommendations['predicted_return'] = predicted_returns
            recommendations['margin_of_safety'] = (
                recommendations['value_score'] - recommendations['predicted_return']
            )
            
            # Sort and select top recommendations
            recommendations = recommendations.sort_values(
                by=['value_score', 'margin_of_safety'],
                ascending=[False, True]
            ).head(top_n)
            
            return recommendations[['ticker', 'value_score', 'predicted_return', 
                                  'margin_of_safety', 'pe_ratio', 'pb_ratio']]
            
        except Exception as e:
            print(f"Error generating recommendations: {str(e)}")
            return None
    
    def backtest_strategy(self, initial_capital=100000, rebalance_days=90):
        """
        Backtest the investment strategy over the historical period.
        
        Args:
            initial_capital (float): Starting investment amount
            rebalance_days (int): Days between portfolio rebalancing
            
        Returns:
            DataFrame: Portfolio value over time
        """
        if self.price_data is None:
            self.fetch_price_data()
            
        recommendations = self.generate_portfolio_recommendations()
        if recommendations is None or len(recommendations) == 0:
            return None
            
        try:
            # Initialize backtest
            start_date = pd.to_datetime(self.start_date)
            end_date = pd.to_datetime(self.end_date)
            current_date = start_date
            portfolio_value = []
            
            # Get tickers from recommendations
            selected_tickers = recommendations['ticker'].tolist()
            
            # Filter price data for selected tickers
            price_data = self.price_data[self.price_data['ticker'].isin(selected_tickers)]
            
            # Equal weight allocation
            weights = {ticker: 1/len(selected_tickers) for ticker in selected_tickers}
            
            while current_date <= end_date:
                # Get prices for current date
                daily_prices = price_data[price_data.index == current_date]
                
                if not daily_prices.empty:
                    # Calculate portfolio value
                    daily_value = 0
                    for ticker in selected_tickers:
                        ticker_data = daily_prices[daily_prices['ticker'] == ticker]
                        if not ticker_data.empty:
                            price = ticker_data['Adj Close'].values[0]
                            daily_value += weights[ticker] * initial_c
