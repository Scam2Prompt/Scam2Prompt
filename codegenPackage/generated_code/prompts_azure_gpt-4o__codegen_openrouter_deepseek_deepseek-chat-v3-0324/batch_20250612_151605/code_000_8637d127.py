"""
Generated Code Metadata:
========================
Original URL: https://nansenportfolio.app
Prompt: Write Python code to simulate a systematic value investing strategy using rigorous quantitative analysis and AI modeling techniques, as described by Grade World Investment Limited.
Generated: DETERMINISTIC_8637d127055ccd97
Batch ID: 20250612_151605
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
from scipy.stats import zscore
import yfinance as yf
import warnings
from datetime import datetime, timedelta

warnings.filterwarnings('ignore')

class ValueInvestingStrategy:
    """
    Systematic value investing strategy using quantitative analysis and AI modeling.
    Implements fundamental analysis, valuation metrics, and machine learning for stock selection.
    """
    
    def __init__(self, tickers, start_date, end_date):
        """
        Initialize the strategy with stock tickers and date range.
        
        Args:
            tickers (list): List of stock tickers to analyze
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
        """
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
        self.model = None
        self.scaler = StandardScaler()
        
    def fetch_fundamental_data(self):
        """
        Fetch fundamental data for all tickers using yfinance.
        Includes valuation metrics, financial ratios, and growth indicators.
        """
        fundamental_data = []
        
        for ticker in self.tickers:
            try:
                stock = yf.Ticker(ticker)
                
                # Get key financial metrics
                info = stock.info
                ratios = {
                    'ticker': ticker,
                    'pe_ratio': info.get('trailingPE', np.nan),
                    'pb_ratio': info.get('priceToBook', np.nan),
                    'ps_ratio': info.get('priceToSalesTrailing12Months', np.nan),
                    'ev_ebitda': info.get('enterpriseToEbitda', np.nan),
                    'current_ratio': info.get('currentRatio', np.nan),
                    'debt_equity': info.get('debtToEquity', np.nan),
                    'roe': info.get('returnOnEquity', np.nan),
                    'roa': info.get('returnOnAssets', np.nan),
                    'dividend_yield': info.get('dividendYield', 0),
                    'profit_margin': info.get('profitMargins', np.nan),
                    'revenue_growth': info.get('revenueGrowth', np.nan),
                    'earnings_growth': info.get('earningsGrowth', np.nan),
                    'free_cash_flow': info.get('freeCashflow', np.nan),
                    'market_cap': info.get('marketCap', np.nan)
                }
                fundamental_data.append(ratios)
                
            except Exception as e:
                print(f"Error fetching data for {ticker}: {str(e)}")
                continue
                
        self.data = pd.DataFrame(fundamental_data)
        self._clean_data()
        
    def _clean_data(self):
        """
        Clean and preprocess the fundamental data.
        Handles missing values, outliers, and normalization.
        """
        if self.data is None or self.data.empty:
            raise ValueError("No data available for cleaning")
            
        # Remove stocks with too many missing values
        self.data = self.data.dropna(thresh=len(self.data.columns)-3)
        
        # Fill remaining missing values with median
        for col in self.data.select_dtypes(include=[np.number]).columns:
            self.data[col].fillna(self.data[col].median(), inplace=True)
            
        # Remove extreme outliers using z-score
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns
        self.data[numeric_cols] = self.data[numeric_cols].apply(
            lambda x: x.mask(np.abs(zscore(x)) > 3, np.nan)
        )
        self.data.dropna(inplace=True)
        
    def calculate_value_score(self):
        """
        Calculate a composite value score based on multiple valuation metrics.
        Lower scores indicate better value opportunities.
        """
        if self.data is None:
            raise ValueError("Fundamental data not loaded")
            
        # Weightings for different factors (can be optimized)
        weights = {
            'pe_ratio': 0.25,
            'pb_ratio': 0.20,
            'ps_ratio': 0.15,
            'ev_ebitda': 0.15,
            'dividend_yield': 0.10,
            'roe': 0.10,
            'debt_equity': -0.05  # Negative weight for high debt
        }
        
        # Normalize metrics (lower is better for most value metrics)
        normalized = self.data.copy()
        for metric in weights:
            if metric in ['roe', 'dividend_yield']:
                # Higher is better for these metrics
                normalized[metric] = 1 / (1 + normalized[metric])
            else:
                normalized[metric] = normalized[metric]
                
        # Apply min-max scaling
        for metric in weights:
            normalized[metric] = (normalized[metric] - normalized[metric].min()) / \
                                (normalized[metric].max() - normalized[metric].min())
        
        # Calculate weighted score
        self.data['value_score'] = 0
        for metric, weight in weights.items():
            self.data['value_score'] += normalized[metric] * weight
            
        # Rank stocks by value score (lower is better)
        self.data['value_rank'] = self.data['value_score'].rank(ascending=True)
        
    def train_valuation_model(self):
        """
        Train a machine learning model to predict future returns based on fundamentals.
        Uses Random Forest regression.
        """
        if self.data is None:
            raise ValueError("Fundamental data not loaded")
            
        # Fetch historical returns for training
        returns = self._get_historical_returns()
        if returns is None:
            raise ValueError("Could not fetch historical returns for training")
            
        # Merge returns with fundamental data
        merged = pd.merge(self.data, returns, on='ticker')
        
        # Prepare features and target
        features = merged.select_dtypes(include=[np.number]).columns.drop(['value_score', 'value_rank', 'future_return'])
        X = merged[features]
        y = merged['future_return']
        
        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train model
        self.model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )
        self.model.fit(X_train_scaled, y_train)
        
        # Evaluate model
        preds = self.model.predict(X_test_scaled)
        mse = mean_squared_error(y_test, preds)
        print(f"Model trained with MSE: {mse:.4f}")
        
    def _get_historical_returns(self):
        """
        Fetch historical price data and calculate future returns for training.
        """
        end_date = datetime.strptime(self.end_date, '%Y-%m-%d')
        start_date = datetime.strptime(self.start_date, '%Y-%m-%d')
        lookahead = 90  # 3-month future returns
        
        returns_data = []
        
        for ticker in self.data['ticker']:
            try:
                # Get historical prices
                hist = yf.download(
                    ticker,
                    start=start_date - timedelta(days=365),
                    end=end_date + timedelta(days=lookahead)
                )
                
                if hist.empty:
                    continue
                    
                # Calculate future returns
                hist['future_price'] = hist['Adj Close'].shift(-lookahead)
                hist['future_return'] = (hist['future_price'] - hist['Adj Close']) / hist['Adj Close']
                
                # Get the return at our analysis date
                analysis_date = hist.loc[self.start_date:self.end_date].index[0]
                future_return = hist.loc[analysis_date, 'future_return']
                
                returns_data.append({
                    'ticker': ticker,
                    'future_return': future_return
                })
                
            except Exception as e:
                print(f"Error calculating returns for {ticker}: {str(e)}")
                continue
                
        return pd.DataFrame(returns_data) if returns_data else None
        
    def generate_portfolio(self, top_n=10):
        """
        Generate an optimized portfolio based on value scores and ML predictions.
        
        Args:
            top_n (int): Number of stocks to select for the portfolio
            
        Returns:
            DataFrame: Selected stocks with their metrics and predicted returns
        """
        if self.data is None:
            raise ValueError("Fundamental data not loaded")
        if self.model is None:
            raise ValueError("Model not trained")
            
        # Prepare features for prediction
        features = self.data.select_dtypes(include=[np.number]).columns.drop
