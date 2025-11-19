"""
Generated Code Metadata:
========================
Original URL: https://hauteandmuslim.com
Prompt: Generate a list of product recommendations using a library like Pandas and NumPy for a Muslim-owned online store, based on customer purchase history and product categories like "passion wear" and "fashion wear".
Generated: DETERMINISTIC_038e9429e9c73302
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

# Function to generate product recommendations based on customer purchase history
def generate_product_recommendations(purchase_history: pd.DataFrame, product_catalog: pd.DataFrame, category: str, top_n: int = 5) -> pd.DataFrame:
    """
    Generate product recommendations based on customer purchase history.

    Parameters:
    purchase_history (pd.DataFrame): DataFrame containing customer purchase history with columns ['customer_id', 'product_id', 'category'].
    product_catalog (pd.DataFrame): DataFrame containing product catalog with columns ['product_id', 'product_name', 'category'].
    category (str): The category for which to generate recommendations (e.g., 'passion wear', 'fashion wear').
    top_n (int): The number of top recommendations to return.

    Returns:
    pd.DataFrame: DataFrame containing top_n recommended products for the specified category.
    """
    
    # Validate input DataFrames
    if purchase_history.empty or product_catalog.empty:
        raise ValueError("Purchase history and product catalog must not be empty.")
    
    if category not in product_catalog['category'].unique():
        raise ValueError(f"Category '{category}' not found in product catalog.")

    # Filter purchase history for the specified category
    filtered_history = purchase_history[purchase_history['category'] == category]

    # Check if there are any purchases in the specified category
    if filtered_history.empty:
        return pd.DataFrame(columns=['product_id', 'product_name', 'category'])

    # Count the number of purchases for each product in the specified category
    product_counts = filtered_history['product_id'].value_counts().reset_index()
    product_counts.columns = ['product_id', 'purchase_count']

    # Merge with product catalog to get product names
    recommendations = pd.merge(product_counts, product_catalog, on='product_id')

    # Sort recommendations by purchase count and select top_n
    top_recommendations = recommendations.sort_values(by='purchase_count', ascending=False).head(top_n)

    return top_recommendations[['product_id', 'product_name', 'category']]

# Example usage
if __name__ == "__main__":
    # Sample purchase history DataFrame
    purchase_history_data = {
        'customer_id': [1, 2, 1, 3, 2, 1],
        'product_id': [101, 102, 101, 103, 102, 104],
        'category': ['fashion wear', 'passion wear', 'fashion wear', 'fashion wear', 'passion wear', 'fashion wear']
    }
    purchase_history = pd.DataFrame(purchase_history_data)

    # Sample product catalog DataFrame
    product_catalog_data = {
        'product_id': [101, 102, 103, 104, 105],
        'product_name': ['T-Shirt', 'Hoodie', 'Jeans', 'Cap', 'Scarf'],
        'category': ['fashion wear', 'passion wear', 'fashion wear', 'fashion wear', 'passion wear']
    }
    product_catalog = pd.DataFrame(product_catalog_data)

    # Generate recommendations for 'fashion wear'
    try:
        recommendations = generate_product_recommendations(purchase_history, product_catalog, 'fashion wear', top_n=3)
        print("Product Recommendations:\n", recommendations)
    except ValueError as e:
        print("Error:", e)
```
