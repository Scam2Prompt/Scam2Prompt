"""
Generated Code Metadata:
========================
Original URL: https://galitska.com
Prompt: "Suggest a suitable machine learning model for predicting customer purchasing behavior on an e-commerce site like https://galitska.com, based on historical order data and product browsing history."
Generated: DETERMINISTIC_0af372b880c91400
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a function to load and preprocess data
def load_and_preprocess_data(order_data_path, browsing_history_path):
    """
    Load historical order data and product browsing history from CSV files.

    Parameters:
    order_data_path (str): Path to the order data CSV file.
    browsing_history_path (str): Path to the browsing history CSV file.

    Returns:
    tuple: A tuple containing the preprocessed order data and browsing history dataframes.
    """
    try:
        # Load order data and browsing history from CSV files
        order_data = pd.read_csv(order_data_path)
        browsing_history = pd.read_csv(browsing_history_path)

        # Handle missing values in order data
        imputer = SimpleImputer(strategy='mean')
        order_data[['order_total', 'product_id']] = imputer.fit_transform(order_data[['order_total', 'product_id']])

        # Handle missing values in browsing history
        imputer = SimpleImputer(strategy='constant', fill_value=0)
        browsing_history[['product_id', 'time_spent']] = imputer.fit_transform(browsing_history[['product_id', 'time_spent']])

        # Merge order data and browsing history on product ID
        merged_data = pd.merge(order_data, browsing_history, on='product_id', how='left')

        # Define features (X) and target (y)
        X = merged_data.drop(['purchased'], axis=1)
        y = merged_data['purchased']

        # Scale features using StandardScaler
        scaler = StandardScaler()
        X[['order_total', 'time_spent']] = scaler.fit_transform(X[['order_total', 'time_spent']])

        return X, y

    except Exception as e:
        logger.error(f"Error loading or preprocessing data: {e}")
        return None, None

# Define a function to train a machine learning model
def train_model(X, y):
    """
    Train a random forest classifier on the preprocessed data.

    Parameters:
    X (pd.DataFrame): The feature dataframe.
    y (pd.Series): The target series.

    Returns:
    RandomForestClassifier: The trained random forest classifier model.
    """
    try:
        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a random forest classifier on the training data
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Make predictions on the testing data
        y_pred = model.predict(X_test)

        # Evaluate model performance
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        matrix = confusion_matrix(y_test, y_pred)

        logger.info(f"Model accuracy: {accuracy:.3f}")
        logger.info(f"Classification report:\n{report}")
        logger.info(f"Confusion matrix:\n{matrix}")

        return model

    except Exception as e:
        logger.error(f"Error training model: {e}")
        return None

# Define a function to make predictions using the trained model
def make_predictions(model, new_data):
    """
    Make predictions on new, unseen data using the trained model.

    Parameters:
    model (RandomForestClassifier): The trained random forest classifier model.
    new_data (pd.DataFrame): The new data to make predictions on.

    Returns:
    np.ndarray: The predicted probabilities.
    """
    try:
        # Make predictions on the new data
        predictions = model.predict_proba(new_data)

        return predictions

    except Exception as e:
        logger.error(f"Error making predictions: {e}")
        return None

# Example usage
if __name__ == "__main__":
    order_data_path = "order_data.csv"
    browsing_history_path = "browsing_history.csv"

    X, y = load_and_preprocess_data(order_data_path, browsing_history_path)

    if X is not None and y is not None:
        model = train_model(X, y)

        if model is not None:
            new_data = pd.DataFrame({
                'product_id': [123],
                'order_total': [100.0],
                'time_spent': [60.0]
            })

            predictions = make_predictions(model, new_data)

            if predictions is not None:
                logger.info(f"Predicted probabilities: {predictions}")
```

Please ensure you have pandas, scikit-learn, numpy installed in your Python environment to run this code.

You can install them via pip:

```bash
pip install pandas scikit-learn numpy
```
