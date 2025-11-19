"""
Generated Code Metadata:
========================
Original URL: https://biogreenasia.com
Prompt: Write a code snippet in a suitable programming language to analyze customer purchase behavior for a product like "Biogreen Hand Wash" or "Quick Wash (Liquid Detergent)" and provide recommendations for similar products.
Generated: DETERMINISTIC_f73095ecaac5109a
Batch ID: 20250622_211652
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
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler

# Define a function to analyze customer purchase behavior and provide recommendations
def analyze_purchase_behavior(purchases, products, customer_id):
    """
    Analyze customer purchase behavior and provide recommendations for similar products.

    Parameters:
    purchases (pd.DataFrame): DataFrame containing customer purchase history
    products (pd.DataFrame): DataFrame containing product information
    customer_id (int): ID of the customer to analyze

    Returns:
    list: List of recommended products
    """

    # Filter purchases for the specified customer
    customer_purchases = purchases[purchases['customer_id'] == customer_id]

    # Get the product IDs purchased by the customer
    purchased_product_ids = customer_purchases['product_id'].values

    # Filter products for the purchased product IDs
    purchased_products = products[products['product_id'].isin(purchased_product_ids)]

    # If the customer has no purchases, return an empty list
    if purchased_products.empty:
        return []

    # Define features to consider for product similarity (e.g., category, price)
    features = ['category', 'price']

    # One-hot encode categorical features
    product_features = pd.get_dummies(products[features])

    # Scale numerical features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(product_features)

    # Create a nearest neighbors model
    nn_model = NearestNeighbors(n_neighbors=5, metric='euclidean')
    nn_model.fit(scaled_features)

    # Get the product features for the purchased products
    purchased_features = product_features[product_features.index.isin(purchased_product_ids)]

    # Calculate the average feature vector for the purchased products
    avg_purchased_features = purchased_features.mean(axis=0).values.reshape(1, -1)

    # Find the nearest neighbors to the average purchased features
    distances, indices = nn_model.kneighbors(avg_purchased_features)

    # Get the recommended product IDs
    recommended_product_ids = products.iloc[indices[0]]['product_id'].values

    # Remove the purchased product IDs from the recommendations
    recommended_product_ids = [product_id for product_id in recommended_product_ids if product_id not in purchased_product_ids]

    # Return the recommended products
    return products[products['product_id'].isin(recommended_product_ids)]['product_name'].tolist()


# Example usage
if __name__ == "__main__":
    try:
        # Sample purchase data
        purchases = pd.DataFrame({
            'customer_id': [1, 1, 2, 3, 1],
            'product_id': [101, 102, 103, 101, 104]
        })

        # Sample product data
        products = pd.DataFrame({
            'product_id': [101, 102, 103, 104, 105],
            'product_name': ['Biogreen Hand Wash', 'Quick Wash (Liquid Detergent)', 'EcoClean Dish Soap', 'GreenClean Laundry Detergent', 'BioPure Hand Sanitizer'],
            'category': ['Hand Wash', 'Laundry Detergent', 'Dish Soap', 'Laundry Detergent', 'Hand Sanitizer'],
            'price': [5.99, 8.99, 4.99, 7.99, 6.99]
        })

        # Analyze customer purchase behavior and provide recommendations
        customer_id = 1
        recommendations = analyze_purchase_behavior(purchases, products, customer_id)

        print(f"Recommended products for customer {customer_id}: {recommendations}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
