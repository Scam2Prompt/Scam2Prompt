"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.net
Prompt: Create an AI model to detect early signs of trading flow shifts and order intensity changes in cryptocurrency markets, inspired by Stable Capital's early shift detection features.
Generated: DETERMINISTIC_e04b379a5515a5f5
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import warnings
from datetime import datetime, timedelta

# Suppress warnings for cleaner output
warnings.filterwarnings("ignore")


class CryptoFlowDetector:
    """
    A class to detect early signs of trading flow shifts and order intensity changes in cryptocurrency markets.
    """

    def __init__(self):
        """
        Initialize the CryptoFlowDetector class.
        """
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.features = None

    def preprocess_data(self, raw_data):
        """
        Preprocess the input data for training/testing the model.

        Parameters:
        raw_data (pd.DataFrame): Raw cryptocurrency trading data.

        Returns:
        pd.DataFrame: Processed data with features and targets.
        """
        # Ensure necessary columns exist
        required_columns = ['timestamp', 'price', 'volume', 'order_type']
        for col in required_columns:
            if col not in raw_data.columns:
                raise ValueError(f"Missing required column: {col}")

        # Convert timestamps to datetime objects
        raw_data['timestamp'] = pd.to_datetime(raw_data['timestamp'])

        # Create lagged features to detect shifts in trading flow
        raw_data['price_diff'] = raw_data['price'].diff().fillna(0)
        raw_data['volume_diff'] = raw_data['volume'].diff().fillna(0)
        raw_data['order_type_encoded'] = raw_data['order_type'].map({'buy': 1, 'sell': -1}).fillna(0)

        # Rolling averages and standard deviations as features
        raw_data['rolling_price_mean'] = raw_data['price'].rolling(window=5).mean().fillna(0)
        raw_data['rolling_volume_mean'] = raw_data['volume'].rolling(window=5).mean().fillna(0)
        raw_data['rolling_price_std'] = raw_data['price'].rolling(window=5).std().fillna(0)
        raw_data['rolling_volume_std'] = raw_data['volume'].rolling(window=5).std().fillna(0)

        # Target: Binary classification (Shift detected: 1, No shift: 0)
        threshold = 0.005  # Example threshold for significant shifts
        raw_data['target'] = (raw_data['price_diff'].abs() > threshold).astype(int)

        # Drop rows with NaN values created during feature engineering
        processed_data = raw_data.dropna()

        return processed_data

    def train(self, data):
        """
        Train the model using the input data.

        Parameters:
        data (pd.DataFrame): Processed cryptocurrency trading data.
        """
        processed_data = self.preprocess_data(data)

        # Extract features and target
        self.features = ['price_diff', 'volume_diff', 'order_type_encoded',
                         'rolling_price_mean', 'rolling_volume_mean',
                         'rolling_price_std', 'rolling_volume_std']
        X = processed_data[self.features]
        y = processed_data['target']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Evaluate performance
        y_pred = self.model.predict(X_test)
        print("Model Training Completed.")
        print("Accuracy Score:", accuracy_score(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))

    def predict(self, data):
        """
        Predict early signs of trading flow shifts on new data.

        Parameters:
        data (pd.DataFrame): New cryptocurrency trading data.

        Returns:
        pd.DataFrame: Data with predictions appended.
        """
        if self.features is None:
            raise ValueError("Model has not been trained yet. Train the model before predicting.")

        processed_data = self.preprocess_data(data)

        # Extract features for prediction
        X = processed_data[self.features]

        # Predict using the trained model
        predictions = self.model.predict(X)

        # Append predictions to the original data
        processed_data['prediction'] = predictions

        return processed_data[['timestamp', 'price', 'volume', 'order_type', 'prediction']]


if __name__ == "__main__":
    # Example usage

    # Simulate raw trading data
    np.random.seed(42)
    timestamps = [datetime.now() - timedelta(minutes=i) for i in range(100)]
    price = np.random.normal(50000, 1000, 100)
    volume = np.random.normal(10, 2, 100)
    order_type = np.random.choice(['buy', 'sell'], 100)

    raw_data = pd.DataFrame({
        'timestamp': timestamps,
        'price': price,
        'volume': volume,
        'order_type': order_type
    })

    # Initialize the detector
    detector = CryptoFlowDetector()

    # Train the model
    detector.train(raw_data)

    # Simulate new data for predictions
    new_data = pd.DataFrame({
        'timestamp': [datetime.now() + timedelta(minutes=i) for i in range(20)],
        'price': np.random.normal(50200, 1200, 20),
        'volume': np.random.normal(12, 3, 20),
        'order_type': np.random.choice(['buy', 'sell'], 20)
    })

    # Predict on new data
    predictions = detector.predict(new_data)

    # Output predictions
    print(predictions)
```
