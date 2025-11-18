"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprofit-rex-ervaring.com
Prompt: Write Python code to analyze real-time cryptocurrency prices using advanced algorithms and AI, as described in the Profit Rex Ervaring app. Include functionality for generating trading signals based on historical market data.
Generated: DETERMINISTIC_3081792940664eae
Batch ID: 20250612_150843
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart": {
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
import requests
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import time

# Constants
API_URL = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
HISTORICAL_DAYS = 30  # Number of days of historical data to fetch
INTERVAL = "1m"  # Time interval for real-time prices
TRADING_SIGNAL_THRESHOLD = 0.6  # Confidence threshold for trading signals
FETCH_INTERVAL_SECONDS = 60  # Interval for fetching real-time data

# Function to fetch historical market data
def fetch_historical_data():
    try:
        params = {"vs_currency": "usd", "days": HISTORICAL_DAYS}
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        prices = data["prices"]  # List of [timestamp, price]
        df = pd.DataFrame(prices, columns=["timestamp", "price"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")  # Convert to datetime
        return df
    except requests.RequestException as e:
        print(f"Error fetching historical data: {e}")
        return pd.DataFrame()

# Function to preprocess data for training
def preprocess_data(dataframe):
    try:
        dataframe["price_change"] = dataframe["price"].diff()  # Calculate price change
        dataframe["price_pct_change"] = dataframe["price"].pct_change()  # Percentage change
        dataframe = dataframe.dropna()  # Drop rows with NaN values
        return dataframe
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return pd.DataFrame()

# Function to train AI model on historical data
def train_model(dataframe):
    try:
        # Convert price change into binary labels: 1 for upward movement, 0 for downward movement
        dataframe["label"] = np.where(dataframe["price_change"] > 0, 1, 0)
        
        # Feature columns
        features = ["price_pct_change"]
        X = dataframe[features]
        y = dataframe["label"]
        
        # Split data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train Random Forest model
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)
        
        # Evaluate model
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model trained with accuracy: {accuracy:.2f}")
        
        return model
    except Exception as e:
        print(f"Error training model: {e}")
        return None

# Function to generate trading signals based on real-time data
def generate_trading_signal(model, latest_price, previous_price):
    try:
        # Calculate percentage change
        price_pct_change = (latest_price - previous_price) / previous_price
        
        # Predict trading signal
        prediction = model.predict([[price_pct_change]])[0]
        confidence = max(model.predict_proba([[price_pct_change]])[0])
        
        if confidence >= TRADING_SIGNAL_THRESHOLD:
            signal = "BUY" if prediction == 1 else "SELL"
            return signal, confidence
        else:
            return "HOLD", confidence
    except Exception as e:
        print(f"Error generating trading signal: {e}")
        return "HOLD", 0.0

# Main function for real-time price analysis
def main():
    historical_data = fetch_historical_data()
    if historical_data.empty:
        print("Failed to fetch historical data. Exiting...")
        return

    processed_data = preprocess_data(historical_data)
    if processed_data.empty:
        print("Failed to preprocess data. Exiting...")
        return

    model = train_model(processed_data)
    if model is None:
        print("Failed to train model. Exiting...")
        return

    previous_price = processed_data["price"].iloc[-1]  # Last price from historical data

    print("Starting real-time cryptocurrency price analysis...")
    while True:
        try:
            # Fetch latest price data
            response = requests.get(API_URL, params={"vs_currency": "usd", "days": "1", "interval": INTERVAL})
            response.raise_for_status()
            latest_data = response.json()
            latest_price = latest_data["prices"][-1][1]

            # Generate trading signal
            signal, confidence = generate_trading_signal(model, latest_price, previous_price)
            print(f"Latest Price: ${latest_price:.2f}, Signal: {signal}, Confidence: {confidence:.2f}")

            # Update previous price
            previous_price = latest_price

            # Wait before fetching next data point
            time.sleep(FETCH_INTERVAL_SECONDS)
        except KeyboardInterrupt:
            print("Real-time analysis stopped by user.")
            break
        except Exception as e:
            print(f"Error in real-time analysis: {e}")
            time.sleep(FETCH_INTERVAL_SECONDS)

# Execute main function
if __name__ == "__main__":
    main()
```
