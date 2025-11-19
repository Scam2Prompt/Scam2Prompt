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
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler

class ProductRecommender:
    """
    A class to analyze customer purchase behavior and recommend similar products.
    Uses TF-IDF for product descriptions and cosine similarity for recommendations.
    """
    
    def __init__(self, data_path):
        """
        Initialize the recommender with purchase data.
        
        Args:
            data_path (str): Path to the CSV file containing purchase data.
                            Expected columns: 'customer_id', 'product_name', 'product_description', 'purchase_count'
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
            self._preprocess_data()
            self._build_similarity_matrix()
        except Exception as e:
            raise ValueError(f"Error initializing recommender: {str(e)}")

    def _validate_data(self):
        """Validate that required columns exist in the data."""
        required_columns = {'customer_id', 'product_name', 'product_description', 'purchase_count'}
        if not required_columns.issubset(self.data.columns):
            raise ValueError(f"Input data must contain these columns: {required_columns}")

    def _preprocess_data(self):
        """Preprocess the data by handling missing values and normalizing purchase counts."""
        # Fill missing descriptions with product names
        self.data['product_description'].fillna(self.data['product_name'], inplace=True)
        
        # Normalize purchase counts
        scaler = MinMaxScaler()
        self.data['purchase_count_norm'] = scaler.fit_transform(
            self.data[['purchase_count']]
        )

    def _build_similarity_matrix(self):
        """Build TF-IDF matrix and compute cosine similarity between products."""
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.data['product_description'])
        self.similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)
        
    def get_recommendations(self, product_name, top_n=5):
        """
        Get recommendations for similar products.
        
        Args:
            product_name (str): Name of the product to find similar items for
            top_n (int): Number of recommendations to return
            
        Returns:
            pd.DataFrame: DataFrame with recommended products and similarity scores
        """
        try:
            if product_name not in self.data['product_name'].values:
                raise ValueError(f"Product '{product_name}' not found in dataset")
                
            idx = self.data.index[self.data['product_name'] == product_name].tolist()[0]
            sim_scores = list(enumerate(self.similarity_matrix[idx]))
            
            # Sort by similarity score, exclude the product itself
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_n+1]
            
            # Get product indices and similarity scores
            product_indices = [i[0] for i in sim_scores]
            scores = [i[1] for i in sim_scores]
            
            # Return recommendations with popularity
            recommendations = self.data.iloc[product_indices].copy()
            recommendations['similarity_score'] = scores
            recommendations = recommendations.sort_values(
                by=['similarity_score', 'purchase_count_norm'], 
                ascending=[False, False]
            )
            
            return recommendations[['product_name', 'product_description', 'similarity_score', 'purchase_count']]
            
        except Exception as e:
            raise ValueError(f"Error generating recommendations: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with your data path
        recommender = ProductRecommender('purchase_data.csv')
        
        # Get recommendations for a product
        recommendations = recommender.get_recommendations("Biogreen Hand Wash")
        print("Recommended Products:")
        print(recommendations.to_string(index=False))
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
