"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holders.sellpass.io
Prompt: Generate a script to implement AI fraud prevention using historical tracking and blacklist rules as described by Sellpass.
Generated: DETERMINISTIC_077fa6fc4071966a
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy as np
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FraudPrevention:
    def __init__(self, historical_data: pd.DataFrame, blacklist: set):
        """
        Initializes the FraudPrevention instance.

        Parameters:
            historical_data (pd.DataFrame): DataFrame containing historical transaction data.
            blacklist (set): A set of blacklisted user IDs or email addresses.
        """
        self.historical_data = historical_data
        self.blacklist = blacklist
        self.model = None

    def preprocess_data(self):
        """
        Preprocess the historical data for model training.
        This includes feature scaling and handling missing values.
        
        Returns:
            np.ndarray: Scaled feature array ready for model training.
        """
        # Handle missing values
        if self.historical_data.isnull().values.any():
            logging.warning("Missing values found, filling with mean.")
            self.historical_data.fillna(self.historical_data.mean(), inplace=True)

        # Select relevant features for fraud detection
        features = self.historical_data[['transaction_amount', 'transaction_time', 'user_id']]

        # Scale features
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)
        return scaled_features

    def train_model(self):
        """
        Trains the Isolation Forest model on the preprocessed data.
        """
        try:
            scaled_features = self.preprocess_data()
            self.model = IsolationForest(contamination=0.1, random_state=42)
            self.model.fit(scaled_features)
            logging.info("Model trained successfully.")
        except Exception as e:
            logging.error(f"Error during model training: {e}")
            raise

    def check_fraud(self, transaction: dict) -> bool:
        """
        Checks if a transaction is fraudulent based on the model and blacklist.

        Parameters:
            transaction (dict): A dictionary representing a single transaction.

        Returns:
            bool: True if the transaction is flagged as fraudulent, False otherwise.
        """
        user_id = transaction['user_id']
        if user_id in self.blacklist:
            logging.info(f"Transaction from blacklisted user {user_id} flagged as fraudulent.")
            return True
        
        try:
            # Prepare transaction for model prediction
            transaction_df = pd.DataFrame([transaction])
            scaled_transaction = StandardScaler().fit(self.historical_data[['transaction_amount', 'transaction_time']]).transform(transaction_df[['transaction_amount', 'transaction_time']])
            prediction = self.model.predict(scaled_transaction)

            # If predicted value is -1, it indicates a fraudulent transaction
            is_fraudulent = prediction[0] == -1
            if is_fraudulent:
                logging.info("Transaction flagged as fraudulent.")
            return is_fraudulent
        except Exception as e:
            logging.error(f"Error during fraud check: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Example historical data and blacklist
    historical_data_example = pd.DataFrame({
        'transaction_amount': [100, 200, 300, 150, 400],
        'transaction_time': [1, 2, 3, 4, 5],
        'user_id': ['user1', 'user2', 'user3', 'user4', 'user5']
    })

    blacklist_example = {'user2', 'user4'}

    # Create an instance of FraudPrevention
    fraud_prevention_system = FraudPrevention(historical_data_example, blacklist_example)

    # Train the fraud detection model
    fraud_prevention_system.train_model()

    # Check a new transaction
    new_transaction = {'transaction_amount': 250, 'transaction_time': 6, 'user_id': 'user2'}
    is_fraud = fraud_prevention_system.check_fraud(new_transaction)
    print(f"Transaction is fraudulent: {is_fraud}")
```
