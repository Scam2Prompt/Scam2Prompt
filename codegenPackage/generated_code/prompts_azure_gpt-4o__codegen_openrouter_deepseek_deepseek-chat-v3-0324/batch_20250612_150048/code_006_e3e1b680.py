"""
Generated Code Metadata:
========================
Original URL: https://the-cryptodezire.com
Prompt: Create a Python script to analyze Ethereum price trends using predictive analytics, similar to the functionality described in Crypto Dezire's platform.
Generated: DETERMINISTIC_e3e1b680b4d0d36d
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
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler
from datetime import datetime, timedelta
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

class EthereumPriceAnalyzer:
    """
    A class to analyze and predict Ethereum price trends using machine learning.
    """
    
    def __init__(self):
        self.data = None
        self.model = None
        self.scaler = MinMaxScaler()
        self.today = datetime.today().strftime('%Y-%m-%d')
        self.start_date = (datetime.today() - timedelta(days=365*3)).strftime('%Y-%m-%d')
        
    def fetch_data(self):
        """
        Fetch historical Ethereum price data from Yahoo Finance.
        """
        try:
            eth_data = yf.download('ETH-USD', start=self.start_date, end=self.today)
            eth_data.reset_index(inplace=True)
            eth_data['Date'] = pd.to_datetime(eth_data['Date'])
            self.data = eth_data[['Date', 'Close']].rename(columns={'Close': 'Price'})
            print("Successfully fetched Ethereum price data.")
            return True
        except Exception as e:
            print(f"Error fetching data: {e}")
            return False
    
    def preprocess_data(self):
        """
        Preprocess the data for machine learning.
        """
        if self.data is None:
            print("No data available. Please fetch data first.")
            return False
        
        try:
            # Create features from date
            self.data['Day'] = self.data['Date'].dt.day
            self.data['Month'] = self.data['Date'].dt.month
            self.data['Year'] = self.data['Date'].dt.year
            self.data['DayOfWeek'] = self.data['Date'].dt.dayofweek
            self.data['DayOfYear'] = self.data['Date'].dt.dayofyear
            
            # Create moving averages
            self.data['MA7'] = self.data['Price'].rolling(window=7).mean()
            self.data['MA30'] = self.data['Price'].rolling(window=30).mean()
            
            # Create target (next day's price)
            self.data['NextDayPrice'] = self.data['Price'].shift(-1)
            
            # Drop rows with NaN values
            self.data.dropna(inplace=True)
            
            # Scale features
            features = ['Day', 'Month', 'Year', 'DayOfWeek', 'DayOfYear', 'MA7', 'MA30']
            self.data[features] = self.scaler.fit_transform(self.data[features])
            
            return True
        except Exception as e:
            print(f"Error preprocessing data: {e}")
            return False
    
    def train_model(self):
        """
        Train a Random Forest Regressor model.
        """
        if self.data is None:
            print("No data available. Please fetch and preprocess data first.")
            return False
        
        try:
            # Prepare features and target
            features = ['Day', 'Month', 'Year', 'DayOfWeek', 'DayOfYear', 'MA7', 'MA30']
            X = self.data[features]
            y = self.data['NextDayPrice']
            
            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )
            
            # Train model
            self.model = RandomForestRegressor(n_estimators=100, random_state=42)
            self.model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = self.model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            print(f"Model trained successfully. MSE: {mse:.2f}, R2 Score: {r2:.2f}")
            return True
        except Exception as e:
            print(f"Error training model: {e}")
            return False
    
    def predict_next_days(self, days=7):
        """
        Predict prices for the next n days.
        """
        if self.model is None:
            print("No model available. Please train model first.")
            return None
        
        try:
            last_date = self.data['Date'].iloc[-1]
            predictions = []
            
            for i in range(1, days+1):
                next_date = last_date + timedelta(days=i)
                
                # Prepare features for prediction
                features = {
                    'Day': next_date.day,
                    'Month': next_date.month,
                    'Year': next_date.year,
                    'DayOfWeek': next_date.weekday(),
                    'DayOfYear': next_date.timetuple().tm_yday,
                    'MA7': self.data['Price'].iloc[-7:].mean(),
                    'MA30': self.data['Price'].iloc[-30:].mean()
                }
                
                # Scale features
                features_scaled = self.scaler.transform(pd.DataFrame([features]))
                
                # Predict
                price = self.model.predict(features_scaled)[0]
                predictions.append({'Date': next_date, 'PredictedPrice': price})
                
                # Update moving averages for next prediction
                self.data.loc[len(self.data)] = {
                    'Date': next_date,
                    'Price': price,
                    'MA7': self.data['Price'].iloc[-6:].mean() if len(self.data) > 6 else price,
                    'MA30': self.data['Price'].iloc[-29:].mean() if len(self.data) > 29 else price
                }
            
            return pd.DataFrame(predictions)
        except Exception as e:
            print(f"Error making predictions: {e}")
            return None
    
    def plot_predictions(self, predictions):
        """
        Plot historical data and predictions.
        """
        if predictions is None:
            print("No predictions to plot.")
            return
        
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['Date'], self.data['Price'], label='Historical Price')
        plt.plot(predictions['Date'], predictions['PredictedPrice'], 'r--', label='Predicted Price')
        plt.title('Ethereum Price Prediction')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    analyzer = EthereumPriceAnalyzer()
    
    # Fetch data
    if not analyzer.fetch_data():
        return
    
    # Preprocess data
    if not analyzer.preprocess_data():
        return
    
    # Train model
    if not analyzer.train_model():
        return
    
    # Make predictions
    predictions = analyzer.predict_next_days(days=7)
    if predictions is not None:
        print("\nNext 7 Days Predictions:")
        print(predictions[['Date', 'PredictedPrice']].to_string(index=False))
        
        # Plot results
        analyzer.plot_predictions(predictions)

if __name__ == "__main__":
    main()
```
