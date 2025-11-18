"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://2xether.com
Prompt: Create a script that implements a machine learning-based momentum model to predict Ethereum price movements using metrics like momentum, market force, slope, and phase, as outlined on 2xEther.com.
Generated: DETERMINISTIC_d856d6d8e7f277eb
Batch ID: 20250612_152249
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/ethereum/market_chart": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import requests

# Constants
ETHEREUM_API_URL = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart"
DAYS_HISTORICAL_DATA = 365  # Number of days to fetch historical data

def fetch_ethereum_data(days=DAYS_HISTORICAL_DATA):
    """
    Fetch historical Ethereum price data from CoinGecko API.
    
    Args:
        days (int): Number of days of historical data to fetch.

    Returns:
        pd.DataFrame: A DataFrame containing timestamp and price data.
    """
    try:
        response = requests.get(ETHEREUM_API_URL, params={'vs_currency': 'usd', 'days': days})
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()['prices']
        df = pd.DataFrame(data, columns=['timestamp', 'price'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except Exception as e:
        print(f"Error fetching Ethereum data: {e}")
        return pd.DataFrame()

def calculate_features(df):
    """
    Calculate momentum-based features for the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame with Ethereum price data.

    Returns:
        pd.DataFrame: DataFrame with additional features.
    """
    df['momentum'] = df['price'].diff(1)
    df['market_force'] = df['price'].diff(5)  # 5-day market force
    df['slope'] = df['price'].diff(10).rolling(window=10).mean()  # 10-day slope
    df['phase'] = np.where(df['price'].shift(1) < df['price'], 1, 0)  # Up (1) or Down (0)

    # Drop NaN values that were created by calculations
    return df.dropna()

def train_model(features, target):
    """
    Train a Random Forest model on the features and target.

    Args:
        features (pd.DataFrame): DataFrame containing features.
        target (pd.Series): Series containing target prices.

    Returns:
        RandomForestRegressor: Trained Random Forest model.
    """
    try:
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate the model
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f'Mean Squared Error: {mse:.2f}')
        
        return model
    except Exception as e:
        print(f"Error training the model: {e}")
        return None

def main():
    # Fetch historical Ethereum data
    eth_data = fetch_ethereum_data()
    
    if eth_data.empty:
        return  # Exit if no data was fetched
    
    # Calculate features and prepare dataset
    eth_data = calculate_features(eth_data)
    features = eth_data[['momentum', 'market_force', 'slope', 'phase']]
    target = eth_data['price']

    # Train the model
    model = train_model(features, target)
    
    if model is not None:
        # Example prediction for the next day (you can adjust features as needed)
        last_features = features.iloc[-1].values.reshape(1, -1)
        predicted_price = model.predict(last_features)
        print(f"Predicted Ethereum price for the next time step: ${predicted_price[0]:.2f}")

if __name__ == "__main__":
    main()
```
