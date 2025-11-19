"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.net
Prompt: Create a machine learning model to predict cryptocurrency market turning points based on trading volume, liquidity flow, and relative rate movements, inspired by Stable Capital's data-driven approach.
Generated: DETERMINISTIC_b89b64c79f811be6
Batch ID: 20250612_150854
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
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
import joblib
import yfinance as yf
import talib
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings('ignore')

class CryptoTurningPointPredictor:
    """
    A machine learning model to predict cryptocurrency market turning points
    based on trading volume, liquidity flow, and relative rate movements.
    """
    
    def __init__(self, ticker='BTC-USD', lookback_days=365*2):
        """
        Initialize the predictor with cryptocurrency ticker and lookback period.
        
        Args:
            ticker (str): Cryptocurrency ticker symbol (default: 'BTC-USD')
            lookback_days (int): Number of days to look back for training data
        """
        self.ticker = ticker
        self.lookback_days = lookback_days
        self.model = None
        self.scaler = None
        self.feature_columns = None
        self.target_column = 'turning_point'
        
    def fetch_data(self):
        """
        Fetch historical cryptocurrency data from Yahoo Finance.
        
        Returns:
            pd.DataFrame: Historical price and volume data
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=self.lookback_days)
        
        data = yf.download(
            self.ticker,
            start=start_date.strftime('%Y-%m-%d'),
            end=end_date.strftime('%Y-%m-%d'),
            progress=False
        )
        
        return data
    
    def calculate_technical_indicators(self, data):
        """
        Calculate technical indicators for the dataset.
        
        Args:
            data (pd.DataFrame): Raw price and volume data
            
        Returns:
            pd.DataFrame: Data with additional technical indicators
        """
        df = data.copy()
        
        # Price-based indicators
        df['rsi'] = talib.RSI(df['Close'], timeperiod=14)
        df['macd'], df['macd_signal'], _ = talib.MACD(df['Close'])
        df['adx'] = talib.ADX(df['High'], df['Low'], df['Close'], timeperiod=14)
        
        # Volume-based indicators
        df['obv'] = talib.OBV(df['Close'], df['Volume'])
        df['volume_ma'] = df['Volume'].rolling(window=14).mean()
        df['volume_ratio'] = df['Volume'] / df['volume_ma']
        
        # Liquidity flow indicators
        df['typical_price'] = (df['High'] + df['Low'] + df['Close']) / 3
        df['money_flow'] = df['typical_price'] * df['Volume']
        df['mfi'] = talib.MFI(df['High'], df['Low'], df['Close'], df['Volume'], timeperiod=14)
        
        # Rate of change indicators
        df['roc'] = talib.ROC(df['Close'], timeperiod=10)
        df['momentum'] = talib.MOM(df['Close'], timeperiod=10)
        
        return df
    
    def create_target_variable(self, df, future_period=3):
        """
        Create target variable (turning points) based on future price movements.
        
        Args:
            df (pd.DataFrame): Data with technical indicators
            future_period (int): Number of days to look ahead for turning points
            
        Returns:
            pd.DataFrame: Data with target variable
        """
        df = df.copy()
        
        # Calculate future max and min prices
        df['future_max'] = df['High'].rolling(window=future_period, min_periods=1).max().shift(-future_period)
        df['future_min'] = df['Low'].rolling(window=future_period, min_periods=1).min().shift(-future_period)
        
        # Identify turning points (1 for local top, -1 for local bottom, 0 otherwise)
        df[self.target_column] = 0
        df.loc[df['Close'] >= df['future_max'], self.target_column] = 1  # Local top
        df.loc[df['Close'] <= df['future_min'], self.target_column] = -1  # Local bottom
        
        # Drop future columns
        df.drop(['future_max', 'future_min'], axis=1, inplace=True)
        
        return df
    
    def preprocess_data(self, df):
        """
        Preprocess data for machine learning.
        
        Args:
            df (pd.DataFrame): Data with features and target
            
        Returns:
            tuple: (X, y) - Features and target arrays
        """
        df = df.copy()
        
        # Drop rows with missing values
        df.dropna(inplace=True)
        
        # Select features and target
        feature_cols = [
            'rsi', 'macd', 'macd_signal', 'adx', 'obv', 'volume_ratio',
            'money_flow', 'mfi', 'roc', 'momentum'
        ]
        self.feature_columns = feature_cols
        
        X = df[feature_cols]
        y = df[self.target_column]
        
        return X, y
    
    def train_model(self, X, y):
        """
        Train the machine learning model.
        
        Args:
            X (pd.DataFrame): Feature data
            y (pd.Series): Target data
            
        Returns:
            Pipeline: Trained model pipeline
        """
        # Define pipeline
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('classifier', RandomForestClassifier(
                n_estimators=100,
                class_weight='balanced',
                random_state=42,
                n_jobs=-1
            ))
        ])
        
        # Define parameter grid for hyperparameter tuning
        param_grid = {
            'classifier__n_estimators': [50, 100, 200],
            'classifier__max_depth': [None, 10, 20],
            'classifier__min_samples_split': [2, 5, 10]
        }
        
        # Perform grid search with cross-validation
        grid_search = GridSearchCV(
            pipeline,
            param_grid,
            cv=5,
            scoring='f1_weighted',
            n_jobs=-1,
            verbose=1
        )
        
        grid_search.fit(X, y)
        
        # Store the best model
        self.model = grid_search.best_estimator_
        self.scaler = self.model.named_steps['scaler']
        
        return self.model
    
    def evaluate_model(self, X, y):
        """
        Evaluate the trained model.
        
        Args:
            X (pd.DataFrame): Feature data
            y (pd.Series): Target data
        """
        if self.model is None:
            raise ValueError("Model has not been trained yet.")
            
        y_pred = self.model.predict(X)
        
        print("Model Evaluation:")
        print(f"Accuracy: {accuracy_score(y, y_pred):.4f}")
        print("\nClassification Report:")
        print(classification_report(y, y_pred))
    
    def save_model(self, filepath):
        """
        Save the trained model to disk.
        
        Args:
            filepath (str): Path to save the model
        """
        if self.model is None:
            raise ValueError("Model has not been trained yet.")
            
        joblib.dump(self.model, filepath)
        print(f"Model saved to {filepath}")
    
    def load_model(self, filepath):
        """
        Load a trained model from disk.
        
        Args:
            filepath (str): Path to the saved model
        """
        self.model = joblib.load(filepath)
        self.scaler = self.model.named_steps['scaler']
        print(f"Model loaded from {filepath}")
    
    def predict_turning_points(self, new_data=None):
        """
        Predict turning points for new data.
        
        Args:
            new_data (pd.DataFrame): New data to predict on (if None, uses latest data)
            
        Returns:
            pd.DataFrame: Predictions with probabilities
        """
        if self.model is None:
            raise ValueError("Model has not been trained or loaded.")
            
        if new_data is None:
            new_data = self.fetch_data()
            
        # Calculate technical indicators
        new_data = self.calculate_technical_indicators(new_data)
        
        # Preprocess data
        X_new = new_data[self.feature_columns].copy()
        X_new.dropna(inplace=True)
        
        # Make predictions
        predictions = self.model.predict(X_new)
        probabilities = self.model.predict_proba(X_new)
        
        # Create results DataFrame
        results = X_new.copy()
        results['prediction'] = predictions
        results['prob_top'] = probabilities[:, 2]  # Probability of being a top
        results['prob_bottom'] = probabilities[:, 0]  # Probability of being a bottom
        
        return results
    
    def run_pipeline(self):
        """
        Run the complete pipeline from data fetching to model training.
        """
        # Fetch and prepare
