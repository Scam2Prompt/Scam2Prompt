"""
Generated Code Metadata:
========================
Original URL: https://bitcoinzat.com
Prompt: "Discuss the feasibility of a cryptocurrency reaching $1 in a short timeframe, using BitTorrent ($BTTC) as a case study, and suggest a model for evaluating such predictions."
Generated: DETERMINISTIC_e29667264ac6dab8
Batch ID: 20250622_205204
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/{self.coin_id}/market_chart": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class CryptocurrencyPricePredictor:
    """
    A class to analyze and predict cryptocurrency price movements using historical data.
    Uses RandomForestRegressor for price prediction modeling.
    """
    
    def __init__(self, coin_id='bittorrent', currency='usd', days=365):
        """
        Initialize the predictor with coin ID, currency, and days of historical data.
        
        Args:
            coin_id (str): ID of the cryptocurrency (default: 'bittorrent')
            currency (str): Target currency (default: 'usd')
            days (int): Number of days of historical data to fetch (default: 365)
        """
        self.coin_id = coin_id
        self.currency = currency
        self.days = days
        self.data = None
        self.model = None
        self.scaler = MinMaxScaler()
        
    def fetch_historical_data(self):
        """
        Fetch historical price data from CoinGecko API.
        
        Returns:
            pd.DataFrame: DataFrame containing historical price data
        """
        url = f"https://api.coingecko.com/api/v3/coins/{self.coin_id}/market_chart"
        params = {
            'vs_currency': self.currency,
            'days': self.days
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            # Process the data into a DataFrame
            prices = data['prices']
            df = pd.DataFrame(prices, columns=['timestamp', 'price'])
            df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
            df = df.set_index('date')
            df = df.drop('timestamp', axis=1)
            
            # Add additional features
            df['daily_return'] = df['price'].pct_change()
            df['rolling_7d_avg'] = df['price'].rolling(7).mean()
            
            self.data = df.dropna()
            return self.data
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
    
    def preprocess_data(self):
        """
        Preprocess data for model training.
        
        Returns:
            tuple: (X_train, X_test, y_train, y_test)
        """
        if self.data is None:
            print("No data available. Fetch data first.")
            return None
            
        # Create features and target
        df = self.data.copy()
        df['target'] = df['price'].shift(-1)  # Predict next day's price
        
        # Drop rows with NaN values
        df = df.dropna()
        
        # Scale features
        features = df[['price', 'daily_return', 'rolling_7d_avg']]
        scaled_features = self.scaler.fit_transform(features)
        
        X = scaled_features
        y = df['target'].values
        
        # Split into train and test sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, shuffle=False
        )
        
        return X_train, X_test, y_train, y_test
    
    def train_model(self):
        """
        Train the RandomForestRegressor model.
        """
        data_split = self.preprocess_data()
        if data_split is None:
            return
            
        X_train, X_test, y_train, y_test = data_split
        
        # Initialize and train the model
        self.model = RandomForestRegressor(
            n_estimators=100,
            random_state=42,
            n_jobs=-1
        )
        self.model.fit(X_train, y_train)
        
        # Evaluate the model
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"Model trained. MSE: {mse:.4f}, R2: {r2:.4f}")
    
    def predict_future_price(self, days_ahead=30):
        """
        Predict future prices for the specified number of days.
        
        Args:
            days_ahead (int): Number of days to predict (default: 30)
            
        Returns:
            pd.DataFrame: DataFrame with predicted prices
        """
        if self.model is None or self.data is None:
            print("Model or data not available. Train model first.")
            return None
            
        # Prepare the last known data point
        last_data = self.data.iloc[-1][['price', 'daily_return', 'rolling_7d_avg']].values.reshape(1, -1)
        last_data_scaled = self.scaler.transform(last_data)
        
        predictions = []
        current_features = last_data_scaled.copy()
        
        for _ in range(days_ahead):
            # Predict next day's price
            next_price = self.model.predict(current_features)[0]
            predictions.append(next_price)
            
            # Update features for next prediction
            new_features = np.array([
                next_price,
                (next_price - current_features[0][0]) / current_features[0][0],  # daily_return
                (current_features[0][2] * 6 + next_price) / 7  # rolling_7d_avg
            ]).reshape(1, -1)
            
            current_features = self.scaler.transform(new_features)
        
        # Create DataFrame with predictions
        future_dates = [self.data.index[-1] + timedelta(days=i) for i in range(1, days_ahead+1)]
        prediction_df = pd.DataFrame({
            'date': future_dates,
            'predicted_price': predictions
        }).set_index('date')
        
        return prediction_df
    
    def visualize_predictions(self, prediction_df):
        """
        Visualize historical and predicted prices.
        
        Args:
            prediction_df (pd.DataFrame): DataFrame with predicted prices
        """
        if self.data is None or prediction_df is None:
            print("No data available for visualization.")
            return
            
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['price'], label='Historical Price')
        plt.plot(prediction_df['predicted_price'], label='Predicted Price', linestyle='--')
        
        plt.title(f'{self.coin_id.upper()} Price Prediction')
        plt.xlabel('Date')
        plt.ylabel(f'Price ({self.currency.upper()})')
        plt.legend()
        plt.grid(True)
        plt.show()

# Example usage
if __name__ == "__main__":
    # Initialize predictor
    predictor = CryptocurrencyPricePredictor(coin_id='bittorrent', days=365)
    
    # Fetch and process data
    historical_data = predictor.fetch_historical_data()
    
    if historical_data is not None:
        # Train the model
        predictor.train_model()
        
        # Make predictions
        predictions = predictor.predict_future_price(days_ahead=30)
        
        if predictions is not None:
            # Check if $1 target is in predictions
            one_dollar_target = any(predictions['predicted_price'] >= 1.0)
            print(f"Will {predictor.coin_id.upper()} reach $1 in the next 30 days? {'Yes' if one_dollar_target else 'No'}")
            
            # Visualize results
            predictor.visualize_predictions(predictions)
```
