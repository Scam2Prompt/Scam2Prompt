"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-100maxair.com
Prompt: Write Python code to use advanced algorithms for analyzing cryptocurrency market trends, incorporating historical price evaluation and technical indicators as described on the Bitcoin +100 Maxair platform.
Generated: DETERMINISTIC_d5b7d33c059abe2f
Batch ID: 20250612_150048
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
import matplotlib.pyplot as plt
from ta import add_all_ta_features
from ta.utils import dropna
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

class CryptoTrendAnalyzer:
    """
    Advanced cryptocurrency market trend analyzer using technical indicators and machine learning.
    """
    
    def __init__(self, ticker='BTC-USD', start_date='2015-01-01', end_date=None):
        """
        Initialize the analyzer with cryptocurrency ticker and date range.
        
        Args:
            ticker (str): Cryptocurrency ticker symbol (default: 'BTC-USD')
            start_date (str): Start date for historical data (default: '2015-01-01')
            end_date (str): End date for historical data (default: current date)
        """
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date if end_date else pd.Timestamp.today().strftime('%Y-%m-%d')
        self.data = None
        self.model = None
        self.scaler = MinMaxScaler()
        
    def fetch_data(self):
        """
        Fetch historical cryptocurrency data from Yahoo Finance.
        """
        try:
            self.data = yf.download(
                self.ticker, 
                start=self.start_date, 
                end=self.end_date,
                progress=False
            )
            self.data = dropna(self.data)
            print(f"Successfully fetched data for {self.ticker}")
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise
            
    def add_technical_indicators(self):
        """
        Add technical indicators to the dataset using the ta library.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call fetch_data() first.")
            
        try:
            self.data = add_all_ta_features(
                self.data, 
                open="Open", 
                high="High", 
                low="Low", 
                close="Close", 
                volume="Volume", 
                fillna=True
            )
            print("Technical indicators added successfully.")
        except Exception as e:
            print(f"Error adding technical indicators: {e}")
            raise
    
    def preprocess_data(self):
        """
        Preprocess data for machine learning by:
        1. Creating target variable (price movement)
        2. Scaling features
        3. Handling missing values
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call fetch_data() first.")
            
        try:
            # Create target variable (1 if price increased next day, 0 otherwise)
            self.data['Target'] = (self.data['Close'].shift(-1) > self.data['Close']).astype(int)
            
            # Drop the last row which has no target value
            self.data = self.data[:-1]
            
            # Select features and target
            features = self.data.drop(['Target', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume'], axis=1)
            target = self.data['Target']
            
            # Scale features
            scaled_features = self.scaler.fit_transform(features)
            
            return scaled_features, target
            
        except Exception as e:
            print(f"Error preprocessing data: {e}")
            raise
    
    def train_model(self, test_size=0.2, random_state=42):
        """
        Train a Random Forest classifier to predict price movements.
        
        Args:
            test_size (float): Proportion of data to use for testing (default: 0.2)
            random_state (int): Random seed for reproducibility (default: 42)
        """
        try:
            # Get preprocessed data
            X, y = self.preprocess_data()
            
            # Split data into train and test sets
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )
            
            # Initialize and train model
            self.model = RandomForestClassifier(
                n_estimators=100,
                random_state=random_state,
                n_jobs=-1
            )
            self.model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            print(f"Model trained with accuracy: {accuracy:.2f}")
            print(classification_report(y_test, y_pred))
            
        except Exception as e:
            print(f"Error training model: {e}")
            raise
    
    def plot_indicators(self, indicators=None):
        """
        Plot selected technical indicators.
        
        Args:
            indicators (list): List of indicator names to plot (default: None plots all)
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call fetch_data() first.")
            
        try:
            plt.figure(figsize=(15, 10))
            
            # Plot Close price
            plt.subplot(2, 1, 1)
            plt.plot(self.data.index, self.data['Close'], label='Close Price', color='blue')
            plt.title(f'{self.ticker} Price and Indicators')
            plt.ylabel('Price (USD)')
            plt.legend()
            
            # Plot indicators
            plt.subplot(2, 1, 2)
            
            if indicators is None:
                # Plot default indicators
                plt.plot(self.data.index, self.data['trend_macd'], label='MACD', color='orange')
                plt.plot(self.data.index, self.data['trend_macd_signal'], label='MACD Signal', color='green')
                plt.plot(self.data.index, self.data['trend_macd_diff'], label='MACD Histogram', color='red')
            else:
                for indicator in indicators:
                    if indicator in self.data.columns:
                        plt.plot(self.data.index, self.data[indicator], label=indicator)
                    else:
                        print(f"Indicator {indicator} not found in data.")
            
            plt.xlabel('Date')
            plt.ylabel('Indicator Value')
            plt.legend()
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error plotting indicators: {e}")
            raise
    
    def predict_next_day(self):
        """
        Predict whether the price will increase or decrease the next day.
        
        Returns:
            tuple: (prediction, confidence) where prediction is 1 (increase) or 0 (decrease),
                   and confidence is the probability of the prediction.
        """
        if self.model is None:
            raise ValueError("Model not trained. Call train_model() first.")
            
        try:
            # Get the most recent data point
            X, _ = self.preprocess_data()
            last_data_point = X[-1].reshape(1, -1)
            
            # Make prediction
            prediction = self.model.predict(last_data_point)[0]
            confidence = np.max(self.model.predict_proba(last_data_point))
            
            return prediction, confidence
            
        except Exception as e:
            print(f"Error making prediction: {e}")
            raise

# Example usage
if __name__ == "__main__":
    analyzer = CryptoTrendAnalyzer(ticker='BTC-USD', start_date='2020-01-01')
    analyzer.fetch_data()
    analyzer.add_technical_indicators()
    analyzer.train_model()
    analyzer.plot_indicators()
    
    prediction, confidence = analyzer.predict_next_day()
    print(f"Prediction for next day: {'Up' if prediction else 'Down'} with {confidence:.2f} confidence")
```
