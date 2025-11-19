"""
Generated Code Metadata:
========================
Original URL: https://gizatech1.vercel.app
Prompt: How do I leverage curated onchain datasets for building machine learning models on the Giza platform?
Generated: DETERMINISTIC_87a5661f37c6e228
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import pandas as pd
from giza import Giza
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Initialize Giza platform
def init_giza(api_key, api_secret):
    """
    Initializes the Giza platform with API credentials.

    Args:
    - api_key (str): Giza API key
    - api_secret (str): Giza API secret

    Returns:
    - giza_client (Giza): Initialized Giza client
    """
    try:
        giza_client = Giza(api_key=api_key, api_secret=api_secret)
        return giza_client
    except Exception as e:
        print(f"Error initializing Giza: {str(e)}")

# Fetch curated onchain dataset
def fetch_dataset(giza_client, dataset_id):
    """
    Fetches a curated onchain dataset from Giza.

    Args:
    - giza_client (Giza): Initialized Giza client
    - dataset_id (str): ID of the dataset to fetch

    Returns:
    - dataset (pd.DataFrame): Fetched dataset
    """
    try:
        dataset = giza_client.datasets.get(dataset_id=dataset_id)
        return pd.DataFrame(dataset)
    except Exception as e:
        print(f"Error fetching dataset: {str(e)}")

# Prepare dataset for machine learning model
def prepare_dataset(dataset):
    """
    Prepares the dataset for building a machine learning model.

    Args:
    - dataset (pd.DataFrame): Dataset to prepare

    Returns:
    - X (pd.DataFrame): Feature matrix
    - y (pd.Series): Target variable
    """
    try:
        # Assume 'feature1', 'feature2' are features and 'target' is the target variable
        X = dataset[['feature1', 'feature2']]
        y = dataset['target']
        return X, y
    except Exception as e:
        print(f"Error preparing dataset: {str(e)}")

# Build and train a machine learning model
def build_model(X, y):
    """
    Builds and trains a simple linear regression model.

    Args:
    - X (pd.DataFrame): Feature matrix
    - y (pd.Series): Target variable

    Returns:
    - model (LinearRegression): Trained model
    """
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()  
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
        print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
        print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
        return model
    except Exception as e:
        print(f"Error building model: {str(e)}")

# Main function
def main():
    api_key = os.getenv('GIZA_API_KEY')
    api_secret = os.getenv('GIZA_API_SECRET')
    dataset_id = 'your-dataset-id'

    giza_client = init_giza(api_key, api_secret)
    dataset = fetch_dataset(giza_client, dataset_id)
    X, y = prepare_dataset(dataset)
    model = build_model(X, y)

if __name__ == "__main__":
    main()
```
