"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-project.gr
Prompt: Write a code snippet for anomaly detection in surveillance data using machine learning techniques tailored for heterogeneous data streams.
Generated: DETERMINISTIC_af2b9e5b7867e2ea
Batch ID: 20250612_161520
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
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

# Function to detect anomalies in surveillance data
def anomaly_detection(data):
    """
    Detect anomalies in surveillance data using Isolation Forest.

    Parameters:
    data (pd.DataFrame): The surveillance dataset containing heterogeneous features.
    
    Returns:
    pd.DataFrame: DataFrame with an additional column 'anomaly' indicating anomalies (1: anomaly, -1: normal).
    """
    try:
        # Step 1: Data Preprocessing
        # Check if there are non-numeric columns and convert them to numeric using one-hot encoding
        if not all([np.issubdtype(data[col].dtype, np.number) for col in data.columns]):
            data = pd.get_dummies(data, drop_first=True)
        
        # Handle missing values by imputing with column mean
        data = data.fillna(data.mean())

        # Standardize the data to ensure features are on the same scale
        scaler = StandardScaler()
        scaled_data = scaler.fit_transform(data)
        
        # Step 2: Split into training and testing sets
        X_train, X_test = train_test_split(scaled_data, test_size=0.2, random_state=42)

        # Step 3: Train Isolation Forest model
        isolation_forest = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
        isolation_forest.fit(X_train)
        
        # Step 4: Predict anomalies on the entire dataset
        anomaly_labels = isolation_forest.predict(scaled_data)
        
        # Step 5: Append anomaly labels to the original data
        data['anomaly'] = anomaly_labels
        
        return data

    except Exception as e:
        # Exception handling for runtime errors
        print(f"An error occurred during anomaly detection: {str(e)}")
        return None


# Example usage:
if __name__ == "__main__":
    # Simulated heterogeneous surveillance data
    surveillance_data = pd.DataFrame({
        'temperature': [20.1, 21.3, 19.8, 100.0, 20.5],  # Numerical feature
        'activity': ['running', 'idle', 'walking', 'idle', 'jumping'],  # Categorical feature
        'humidity': [30, 32, 31, 0, 33]  # Numerical feature with an anomaly
    })
    
    # Detect anomalies
    result = anomaly_detection(surveillance_data)
    
    # Print the resulting DataFrame
    if result is not None:
        print(result)
```
