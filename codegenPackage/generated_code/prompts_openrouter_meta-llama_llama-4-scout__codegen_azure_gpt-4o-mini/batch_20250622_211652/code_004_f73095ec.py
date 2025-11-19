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
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load customer purchase data
def load_data(file_path):
    """
    Load customer purchase data from a CSV file.
    
    :param file_path: str - Path to the CSV file containing purchase data.
    :return: DataFrame - Loaded purchase data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Preprocess data to create a user-item matrix
def preprocess_data(data):
    """
    Preprocess the purchase data to create a user-item matrix.
    
    :param data: DataFrame - Raw purchase data.
    :return: DataFrame - User-item matrix.
    """
    user_item_matrix = data.pivot_table(index='customer_id', columns='product_name', values='purchase_amount', fill_value=0)
    return user_item_matrix

# Calculate product similarity using cosine similarity
def calculate_similarity(user_item_matrix):
    """
    Calculate cosine similarity between products.
    
    :param user_item_matrix: DataFrame - User-item matrix.
    :return: DataFrame - Cosine similarity matrix.
    """
    scaler = StandardScaler()
    scaled_matrix = scaler.fit_transform(user_item_matrix.T)  # Transpose to get products as rows
    similarity_matrix = cosine_similarity(scaled_matrix)
    return pd.DataFrame(similarity_matrix, index=user_item_matrix.columns, columns=user_item_matrix.columns)

# Get product recommendations based on similarity
def get_recommendations(similarity_matrix, product_name, top_n=5):
    """
    Get top N product recommendations based on similarity to a given product.
    
    :param similarity_matrix: DataFrame - Cosine similarity matrix.
    :param product_name: str - The product to find recommendations for.
    :param top_n: int - Number of recommendations to return.
    :return: Series - Recommended products and their similarity scores.
    """
    if product_name not in similarity_matrix.columns:
        print(f"Product '{product_name}' not found in similarity matrix.")
        return None
    
    # Get similarity scores for the specified product
    similar_scores = similarity_matrix[product_name].sort_values(ascending=False)
    
    # Exclude the product itself and return top N recommendations
    recommendations = similar_scores[similar_scores.index != product_name].head(top_n)
    return recommendations

# Main function to run the analysis
def main(file_path, product_name):
    """
    Main function to analyze customer purchase behavior and provide recommendations.
    
    :param file_path: str - Path to the CSV file containing purchase data.
    :param product_name: str - The product to find recommendations for.
    """
    data = load_data(file_path)
    if data is None:
        return
    
    user_item_matrix = preprocess_data(data)
    similarity_matrix = calculate_similarity(user_item_matrix)
    recommendations = get_recommendations(similarity_matrix, product_name)
    
    if recommendations is not None:
        print(f"Recommendations for '{product_name}':")
        print(recommendations)

# Example usage
if __name__ == "__main__":
    # Replace 'purchase_data.csv' with the actual path to your data file
    main('purchase_data.csv', 'Biogreen Hand Wash')
```
