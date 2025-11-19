"""
Generated Code Metadata:
========================
Original URL: https://nansenportfolio.app
Prompt: How can I use AI modeling techniques for investment management as described by Grade World Investment Limited?
Generated: DETERMINISTIC_93d6c41610fe6405
Batch ID: 20250612_155153
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.optimizers import Adam
import yfinance as yf
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class InvestmentAIModel:
    """
    AI-powered investment management system with multiple modeling techniques.
    """
    
    def __init__(self, ticker='SPY', start_date='2010-01-01', end_date=None):
        """
        Initialize the investment AI model.
        
        Args:
            ticker (str): Stock ticker symbol
            start_date (str): Start date for historical data
            end_date (str): End date for historical data (defaults to today)
        """
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date if end_date else pd.Timestamp.today().strftime('%Y-%m-%d')
        self.data = None
        self.model = None
        self.scaler = StandardScaler()
        
    def fetch_data(self):
        """
        Fetch historical stock data from Yahoo Finance.
        """
        try:
            self.data = yf.download(
                self.ticker, 
                start=self.start_date, 
                end=self.end_date
            )
            self.data = self.data[['Open', 'High', 'Low', 'Close', 'Volume']]
            self.data['Returns'] = self.data['Close'].pct_change()
            self.data.dropna(inplace=True)
            return True
        except Exception as e:
            print(f"Error fetching data: {e}")
            return False
    
    def preprocess_data(self, window_size=30):
        """
        Prepare data for machine learning models.
        
        Args:
            window_size (int): Number of days to use for time series prediction
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call fetch_data() first.")
            
        # Create features and target
        self.data['Target'] = self.data['Close'].shift(-1)
        self.data.dropna(inplace=True)
        
        # Feature engineering
        features = ['Open', 'High', 'Low', 'Close', 'Volume', 'Returns']
        X = self.data[features]
        y = self.data['Target']
        
        # Split data
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, shuffle=False
        )
        
        # Scale features
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        
        # Prepare LSTM data
        self.X_train_lstm = self._create_sequences(self.X_train_scaled, window_size)
        self.y_train_lstm = y[window_size:len(self.X_train_lstm)+window_size]
        self.X_test_lstm = self._create_sequences(self.X_test_scaled, window_size)
        self.y_test_lstm = y[len(self.X_train):len(self.X_train)+len(self.X_test_lstm)]
    
    def _create_sequences(self, data, window_size):
        """
        Create time series sequences for LSTM model.
        """
        sequences = []
        for i in range(len(data) - window_size):
            sequences.append(data[i:i+window_size])
        return np.array(sequences)
    
    def train_random_forest(self, n_estimators=100):
        """
        Train a Random Forest regression model.
        
        Args:
            n_estimators (int): Number of trees in the forest
        """
        try:
            self.rf_model = RandomForestRegressor(
                n_estimators=n_estimators,
                random_state=42
            )
            self.rf_model.fit(self.X_train_scaled, self.y_train)
            
            # Evaluate model
            y_pred = self.rf_model.predict(self.X_test_scaled)
            mse = mean_squared_error(self.y_test, y_pred)
            r2 = r2_score(self.y_test, y_pred)
            
            print(f"Random Forest Model Performance:")
            print(f"MSE: {mse:.4f}")
            print(f"R2 Score: {r2:.4f}")
            
            return self.rf_model
        except Exception as e:
            print(f"Error training Random Forest: {e}")
            return None
    
    def train_lstm(self, units=50, learning_rate=0.001, epochs=20, batch_size=32):
        """
        Train an LSTM neural network model.
        
        Args:
            units (int): Number of LSTM units
            learning_rate (float): Learning rate for optimizer
            epochs (int): Number of training epochs
            batch_size (int): Batch size for training
        """
        try:
            model = Sequential([
                LSTM(units, return_sequences=True, input_shape=(self.X_train_lstm.shape[1], self.X_train_lstm.shape[2])),
                LSTM(units),
                Dense(1)
            ])
            
            optimizer = Adam(learning_rate=learning_rate)
            model.compile(optimizer=optimizer, loss='mse')
            
            history = model.fit(
                self.X_train_lstm, 
                self.y_train_lstm,
                epochs=epochs,
                batch_size=batch_size,
                validation_split=0.1,
                verbose=1
            )
            
            self.lstm_model = model
            
            # Evaluate model
            y_pred = model.predict(self.X_test_lstm)
            mse = mean_squared_error(self.y_test_lstm, y_pred)
            r2 = r2_score(self.y_test_lstm, y_pred)
            
            print(f"\nLSTM Model Performance:")
            print(f"MSE: {mse:.4f}")
            print(f"R2 Score: {r2:.4f}")
            
            return model
        except Exception as e:
            print(f"Error training LSTM: {e}")
            return None
    
    def predict_next_day(self, model_type='rf'):
        """
        Predict the next day's closing price.
        
        Args:
            model_type (str): Type of model to use ('rf' or 'lstm')
        """
        try:
            if model_type == 'rf':
                if not hasattr(self, 'rf_model'):
                    raise ValueError("Random Forest model not trained yet.")
                
                # Get the most recent data point
                last_data = self.X_test_scaled[-1].reshape(1, -1)
                prediction = self.rf_model.predict(last_data)[0]
                
            elif model_type == 'lstm':
                if not hasattr(self, 'lstm_model'):
                    raise ValueError("LSTM model not trained yet.")
                
                # Get the most recent sequence
                last_sequence = self.X_test_lstm[-1].reshape(1, self.X_test_lstm.shape[1], self.X_test_lstm.shape[2])
                prediction = self.lstm_model.predict(last_sequence)[0][0]
                
            else:
                raise ValueError("Invalid model_type. Use 'rf' or 'lstm'.")
            
            print(f"Predicted next day closing price for {self.ticker}: ${prediction:.2f}")
            return prediction
            
        except Exception as e:
            print(f"Error making prediction: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Initialize the AI investment model
    ai_model = InvestmentAIModel(ticker='AAPL', start_date='2015-01-01')
    
    # Fetch and prepare data
    if ai_model.fetch_data():
        ai_model.preprocess_data(window_size=30)
        
        # Train models
        ai_model.train_random_forest(n_estimators=200)
        ai_model.train_lstm(units=64, epochs=30)
        
        # Make predictions
        ai_model.predict_next_day(model_type='rf')
        ai_model.predict_next_day(model_type='lstm')
```
