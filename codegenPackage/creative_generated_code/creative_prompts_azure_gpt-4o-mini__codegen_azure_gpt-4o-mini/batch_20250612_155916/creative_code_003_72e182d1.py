"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giftgo.site
Prompt: Can you provide an example of how to implement a gift recommendation system similar to the one used by GiftGo?
Generated: DETERMINISTIC_72e182d18f158a62
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import numpy as np

# Sample data structure for gifts
# Each gift has a name and features which are numerical values
data = {
    'gift_name': ['Gift A', 'Gift B', 'Gift C', 'Gift D'],
    'price_range': [20, 50, 30, 40],
    'category': [1, 2, 1, 3],  # Categorical data encoded as integers
    'popularity': [100, 200, 150, 300]
}

# Creating a DataFrame from the sample data
gifts_df = pd.DataFrame(data)

def preprocess_data(df):
    """
    Preprocess the DataFrame to prepare it for similarity calculation.
    
    Args:
        df (DataFrame): DataFrame containing gifts data.
    
    Returns:
        DataFrame: Normalized DataFrame with only the numerical features.
    """
    try:
        # Selecting numerical features for normalization
        features = df[['price_range', 'category', 'popularity']]
        scaler = StandardScaler()
        normalized_features = scaler.fit_transform(features)
        return normalized_features
    except Exception as e:
        print(f"Error during data preprocessing: {e}")
        raise

def calculate_similarity(normalized_data):
    """
    Calculate cosine similarity between the gifts based on their features.
    
    Args:
        normalized_data (ndarray): Array of normalized features.
    
    Returns:
        ndarray: Cosine similarity matrix.
    """
    try:
        similarity_matrix = cosine_similarity(normalized_data)
        return similarity_matrix
    except Exception as e:
        print(f"Error during similarity calculation: {e}")
        raise

def recommend_gifts(gift_name, df, similarity_matrix, top_n=3):
    """
    Recommend gifts based on the similarity of the given gift.
    
    Args:
        gift_name (str): The name of the gift for which recommendations are needed.
        df (DataFrame): DataFrame containing gifts data.
        similarity_matrix (ndarray): Cosine similarity matrix.
        top_n (int): Number of top recommendations to return.
    
    Returns:
        List: List of recommended gift names.
    """
    try:
        # Find the index of the gift
        idx = df[df['gift_name'] == gift_name].index[0]
        
        # Get the similarity scores for the specified gift
        similarity_scores = similarity_matrix[idx]
        
        # Get the indices of the top_n similar gifts
        similar_indices = similarity_scores.argsort()[-top_n-1:-1][::-1]
        
        # Extract recommended gift names
        recommended_gifts = df['gift_name'].iloc[similar_indices].tolist()
        return recommended_gifts
    except IndexError:
        print(f"Gift '{gift_name}' not found in the database.")
        return []
    except Exception as e:
        print(f"Error during gift recommendation: {e}")
        raise

# Main execution block
if __name__ == "__main__":
    # Preprocess the data
    normalized_gift_data = preprocess_data(gifts_df)
    
    # Calculate the similarity matrix
    gift_similarity_matrix = calculate_similarity(normalized_gift_data)
    
    # Recommend gifts based on a specific gift name
    gift_to_recommend = 'Gift A'
    recommendations = recommend_gifts(gift_to_recommend, gifts_df, gift_similarity_matrix)
    
    print(f"Recommendations for '{gift_to_recommend}': {recommendations}")
```
