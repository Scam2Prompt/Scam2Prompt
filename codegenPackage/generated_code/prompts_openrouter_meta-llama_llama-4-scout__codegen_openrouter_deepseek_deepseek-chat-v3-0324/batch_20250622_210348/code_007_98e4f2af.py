"""
Generated Code Metadata:
========================
Original URL: https://green-bitcoins.pages.dev
Prompt: Develop a predictive model using machine learning algorithms to forecast Bitcoin price trends and optimize staking rewards for Green Bitcoin ($GBTC).
Generated: DETERMINISTIC_98e4f2afcad4d75e
Batch ID: 20250622_210348
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
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import GridSearchCV
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import warnings
warnings.filterwarnings('ignore')

# Load and preprocess Bitcoin price data
def load_data(filepath):
    """
    Load and preprocess Bitcoin price data.
    Args:
        filepath (str): Path to the CSV file containing Bitcoin price data
    Returns:
        pd.DataFrame: Processed DataFrame with relevant features
    """
    try:
        df = pd.read_csv(filepath)
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)
        
        # Calculate technical indicators
        df['SMA_7'] = df['Close'].rolling(window=7).mean()
        df['SMA_30'] = df['Close'].rolling(window=30).mean()
        df['EMA_7'] = df['Close'].ewm(span=7, adjust=False).mean()
        df['EMA_30'] = df['Close'].ewm(span=30, adjust=False).mean()
        
        # Calculate daily returns
        df['Daily_Return'] = df['Close'].pct_change()
        
        # Calculate Bollinger Bands
        df['Upper_Bollinger'] = df['SMA_30'] + (2 * df['Close'].rolling(window=30).std())
        df['Lower_Bollinger'] = df['SMA_30'] - (2 * df['Close'].rolling(window=30).std())
        
        # Calculate RSI
        delta = df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['RSI'] = 100 - (100 / (1 + rs))
        
        # Drop NaN values
        df.dropna(inplace=True)
        
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Feature engineering
def create_features(df, lookback=30):
    """
    Create features for the predictive model.
    Args:
        df (pd.DataFrame): Processed Bitcoin price data
        lookback (int): Number of days to look back for features
    Returns:
        tuple: (X, y) feature matrix and target vector
    """
    try:
        # Target variable: next day's closing price
        df['Target'] = df['Close'].shift(-1)
        
        # Features
        features = ['Close', 'SMA_7', 'SMA_30', 'EMA_7', 'EMA_30', 
                   'Daily_Return', 'Upper_Bollinger', 'Lower_Bollinger', 'RSI']
        
        X = df[features]
        y = df['Target'].dropna()
        X = X.iloc[:-1]  # Align with target
        
        return X, y
    except Exception as e:
        print(f"Error creating features: {e}")
        return None, None

# Train traditional ML models
def train_ml_models(X_train, y_train):
    """
    Train and optimize traditional machine learning models.
    Args:
        X_train (pd.DataFrame): Training features
        y_train (pd.Series): Training target
    Returns:
        dict: Dictionary of trained models
    """
    try:
        models = {
            'RandomForest': RandomForestRegressor(random_state=42),
            'GradientBoosting': GradientBoostingRegressor(random_state=42),
            'SVR': SVR()
        }
        
        # Hyperparameter grids
        param_grids = {
            'RandomForest': {
                'n_estimators': [100, 200],
                'max_depth': [None, 10, 20]
            },
            'GradientBoosting': {
                'n_estimators': [100, 200],
                'learning_rate': [0.01, 0.1],
                'max_depth': [3, 5]
            },
            'SVR': {
                'C': [0.1, 1, 10],
                'kernel': ['linear', 'rbf']
            }
        }
        
        trained_models = {}
        
        for name, model in models.items():
            grid_search = GridSearchCV(model, param_grids[name], cv=5, scoring='neg_mean_squared_error')
            grid_search.fit(X_train, y_train)
            trained_models[name] = grid_search.best_estimator_
            print(f"{name} best params: {grid_search.best_params_}")
        
        return trained_models
    except Exception as e:
        print(f"Error training ML models: {e}")
        return None

# Train LSTM model
def train_lstm_model(X_train, y_train, epochs=50, batch_size=32):
    """
    Train an LSTM model for time series prediction.
    Args:
        X_train (np.array): Training features
        y_train (np.array): Training target
        epochs (int): Number of training epochs
        batch_size (int): Batch size for training
    Returns:
        Sequential: Trained LSTM model
    """
    try:
        # Reshape data for LSTM
        X_train = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
        
        model = Sequential([
            LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])),
            Dropout(0.2),
            LSTM(50, return_sequences=False),
            Dropout(0.2),
            Dense(25),
            Dense(1)
        ])
        
        model.compile(optimizer='adam', loss='mse')
        
        early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
        
        history = model.fit(
            X_train, y_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_split=0.2,
            callbacks=[early_stopping],
            verbose=1
        )
        
        return model
    except Exception as e:
        print(f"Error training LSTM model: {e}")
        return None

# Evaluate models
def evaluate_models(models, X_test, y_test):
    """
    Evaluate trained models on test data.
    Args:
        models (dict): Dictionary of trained models
        X_test (pd.DataFrame): Test features
        y_test (pd.Series): Test target
    """
    try:
        results = {}
        
        for name, model in models.items():
            if name == 'LSTM':
                X_test_reshaped = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))
                y_pred = model.predict(X_test_reshaped).flatten()
            else:
                y_pred = model.predict(X_test)
            
            mse = mean_squared_error(y_test, y_pred)
            mae = mean_absolute_error(y_test, y_pred)
            r2 = r2_score(y_test, y_pred)
            
            results[name] = {
                'MSE': mse,
                'MAE': mae,
                'R2': r2
            }
            
            print(f"{name} - MSE: {mse:.4f}, MAE: {mae:.4f}, R2: {r2:.4f}")
        
        return results
    except Exception as e:
        print(f"Error evaluating models: {e}")
        return None

# Optimize staking rewards
def optimize_staking_rewards(model, current_price, staking_params):
    """
    Optimize staking rewards based on price prediction.
    Args:
        model: Trained prediction model
        current_price (float): Current Bitcoin price
        staking_params (dict): Dictionary of staking parameters
    Returns:
        dict: Optimal staking strategy
    """
    try:
        # Create feature vector for prediction
        features = np.array([
            current_price,
            staking_params['sma_7'],
            staking_params['sma_30'],
            staking_params['ema_7'],
            staking_params['ema_30'],
            staking_params['daily_return'],
            staking_params['upper_bollinger'],
            staking_params['lower_bollinger'],
            staking_params['rsi']
        ]).reshape(1, -1)
        
        # Predict future price
        if isinstance(model, Sequential):
            features = features.reshape((1, 1, features.shape[1]))
            predicted_price = model.predict(features).flatten()[0]
        else:
            predicted_price = model.predict(features)[0]
