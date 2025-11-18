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

# Load your customer subscription data
# Assume we have a CSV file `subscription_data.csv` with columns: 'customer_id', 'beer_type', 'quantity', 'price'
try:
    data = pd.read_csv('subscription_data.csv')
except FileNotFoundError as e:
    print("Error: File not found. Please check the file path.")
    raise

# Data preprocessing
# Pivot the data to organize preferences by customer and beer type
# The resulting DataFrame will have customers as rows and beer types as columns
try:
    pivot_data = data.pivot_table(index='customer_id', columns='beer_type', values='quantity', aggfunc='sum').fillna(0)
except KeyError as e:
    print("Error: Missing required columns in the dataset. Please check the data format.")
    raise

# Normalize the data to make it suitable for clustering
scaler = StandardScaler()
normalized_data = scaler.fit_transform(pivot_data)

# Perform clustering using K-Means
# Let's assume we want to group customers into `k` clusters
k = 5  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)

try:
    pivot_data['cluster'] = kmeans.fit_predict(normalized_data)
except ValueError as e:
    print("Error: Invalid value encountered during clustering. Please check the dataset.")
    raise

# Output the results
output_file = 'customer_preferences_clusters.csv'
try:
    pivot_data.to_csv(output_file)
    print(f"Clustering completed. Results saved to {output_file}.")
except IOError as e:
    print("Error: Unable to save the output. Please check file permissions.")
    raise

# Example visualization: Print cluster assignment counts
print("Cluster assignment counts:")
print(pivot_data['cluster'].value_counts())
```
