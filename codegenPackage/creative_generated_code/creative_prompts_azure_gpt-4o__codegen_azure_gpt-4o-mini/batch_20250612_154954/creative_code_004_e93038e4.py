"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftbeerbox.com
Prompt: Suggest a library for analyzing customer preferences based on craft beer subscription data, and write a Python example using that library.
Generated: DETERMINISTIC_e93038e42d001295
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample craft beer subscription data
data = {
    'customer_id': [1, 2, 3, 4, 5],
    'beer_type': ['IPA', 'Stout', 'Lager', 'Pale Ale', 'Wheat'],
    'rating': [5, 3, 4, 2, 5],
    'frequency': [10, 5, 8, 2, 11]  # number of subscriptions per month
}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Function to analyze customer preferences using KMeans clustering
def analyze_customer_preferences(df, n_clusters=2):
    """
    Analyze customer preferences based on beer ratings and subscription frequency.

    Parameters:
        df (pd.DataFrame): DataFrame containing customer data.
        n_clusters (int): Number of clusters for KMeans.

    Returns:
        pd.DataFrame: DataFrame with original customer data and cluster labels.
    """
    try:
        # Prepare the feature set for clustering
        features = df[['rating', 'frequency']]
        
        # Standardize the features
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(features)
        
        # Apply KMeans clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        df['cluster'] = kmeans.fit_predict(scaled_features)
        
        return df
    
    except Exception as e:
        print(f"An error occurred while analyzing customer preferences: {e}")
        return None

# Analyze preferences and output results
result_df = analyze_customer_preferences(df)

# Check if the result is valid before printing
if result_df is not None:
    # Display the results with cluster assignments
    print(result_df)
```
