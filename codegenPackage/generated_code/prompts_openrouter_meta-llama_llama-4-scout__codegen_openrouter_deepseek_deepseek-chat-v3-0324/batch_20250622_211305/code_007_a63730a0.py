"""
Generated Code Metadata:
========================
Original URL: https://tradei6duac.com
Prompt: Develop a machine learning model that predicts market trends and generates trading signals, similar to Trade i6 Duac's approach, using a dataset of historical market data.
Generated: DETERMINISTIC_a63730a0e5d3b3dc
Batch ID: 20250622_211305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
import yfinance as yf
import talib
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class MarketTrendPredictor:
    """
    A machine learning model to predict market trends and generate trading signals.
    Similar to Trade i6 Duac's approach using historical market data.
    """
    
    def __init__(self, ticker='SPY', start_date='2010-01-01', end_date='2023-01-01'):
        """
        Initialize the MarketTrendPredictor.
        
        Args:
            ticker (str): Stock ticker symbol. Default is 'SPY'.
            start_date (str): Start date for historical data in YYYY-MM-DD format.
            end_date (str): End date for historical data in YYYY-MM-DD format.
        """
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.model = None
        self.scaler = StandardScaler()
        self.data = None
        
    def fetch_data(self):
        """
        Fetch historical market data using yfinance and calculate technical indicators.
        
        Returns:
            pd.DataFrame: DataFrame containing OHLCV data and technical indicators.
        """
        try:
            # Download historical data
            data = yf.download(self.ticker, start=self.start_date, end=self.end_date)
            
            if data.empty:
                raise ValueError("No data returned for the given ticker and date range.")
                
            # Calculate technical indicators
            data['SMA_50'] = talib.SMA(data['Close'], timeperiod=50)
            data['SMA_200'] = talib.SMA(data['Close'], timeperiod=200)
            data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
            data['MACD'], _, _ = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
            data['ADX'] = talib.ADX(data['High'], data['Low'], data['Close'], timeperiod=14)
            
            # Create target variable (1 if next day's close is higher, 0 otherwise)
            data['Target'] = (data['Close'].shift(-1) > data['Close']).astype(int)
            
            # Drop rows with NaN values (from indicator calculations)
            data.dropna(inplace=True)
            
            self.data = data
            return data
            
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
    
    def preprocess_data(self):
        """
        Preprocess the data for model training.
        
        Returns:
            tuple: (X_train, X_test, y_train, y_test) split data
        """
        if self.data is None:
            raise ValueError("Data not fetched. Call fetch_data() first.")
            
        try:
            # Select features and target
            features = ['Open', 'High', 'Low', 'Close', 'Volume', 
                       'SMA_50', 'SMA_200', 'RSI', 'MACD', 'ADX']
            X = self.data[features]
            y = self.data['Target']
            
            # Split data into train and test sets
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, shuffle=False, random_state=42
            )
            
            # Scale features
            X_train = self.scaler.fit_transform(X_train)
            X_test = self.scaler.transform(X_test)
            
            return X_train, X_test, y_train, y_test
            
        except Exception as e:
            print(f"Error preprocessing data: {e}")
            return None
    
    def train_model(self):
        """
        Train a Random Forest classifier on the preprocessed data.
        """
        try:
            # Get preprocessed data
            X_train, X_test, y_train, y_test = self.preprocess_data()
            
            # Initialize and train the model
            self.model = RandomForestClassifier(
                n_estimators=100,
                max_depth=10,
                random_state=42,
                class_weight='balanced'
            )
            
            self.model.fit(X_train, y_train)
            
            # Evaluate model
            train_pred = self.model.predict(X_train)
            test_pred = self.model.predict(X_test)
            
            print("Training Accuracy:", accuracy_score(y_train, train_pred))
            print("Test Accuracy:", accuracy_score(y_test, test_pred))
            print("\nClassification Report:")
            print(classification_report(y_test, test_pred))
            
        except Exception as e:
            print(f"Error training model: {e}")
    
    def generate_signals(self):
        """
        Generate trading signals based on model predictions.
        
        Returns:
            pd.DataFrame: DataFrame with predictions and signals
        """
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
            
        try:
            # Get the most recent data
            features = ['Open', 'High', 'Low', 'Close', 'Volume', 
                       'SMA_50', 'SMA_200', 'RSI', 'MACD', 'ADX']
            X = self.data[features]
            X_scaled = self.scaler.transform(X)
            
            # Make predictions
            predictions = self.model.predict(X_scaled)
            probabilities = self.model.predict_proba(X_scaled)[:, 1]
            
            # Create signals DataFrame
            signals = self.data.copy()
            signals['Prediction'] = predictions
            signals['Probability'] = probabilities
            
            # Generate trading signals (1 for buy, -1 for sell, 0 for hold)
            signals['Signal'] = 0
            signals.loc[signals['Prediction'] == 1, 'Signal'] = 1
            signals.loc[signals['Prediction'] == 0, 'Signal'] = -1
            
            return signals
            
        except Exception as e:
            print(f"Error generating signals: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Initialize predictor
    predictor = MarketTrendPredictor(ticker='SPY', start_date='2010-01-01', end_date='2023-01-01')
    
    # Fetch and process data
    predictor.fetch_data()
    
    # Train model
    predictor.train_model()
    
    # Generate signals
    signals = predictor.generate_signals()
    
    # Display last few signals
    if signals is not None:
        print("\nLast 5 trading signals:")
        print(signals[['Close', 'Prediction', 'Probability', 'Signal']].tail())
```
