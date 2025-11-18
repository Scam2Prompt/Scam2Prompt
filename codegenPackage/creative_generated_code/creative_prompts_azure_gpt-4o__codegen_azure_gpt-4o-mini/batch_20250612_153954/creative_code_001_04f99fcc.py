"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Recommend a library or framework for implementing a product recommendation system for categories such as "jeździki" and "rowerki trójkołowe" featured on the Milly Mally site.
Generated: DETERMINISTIC_04f99fcca26688e4
Batch ID: 20250612_153954
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
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class ProductRecommender:
    """
    A class to implement a product recommendation system based on content similarity.

    Attributes:
        products (pd.DataFrame): DataFrame containing product details.
    """

    def __init__(self, product_data: pd.DataFrame):
        """
        Initializes the recommender with product data.

        Args:
            product_data (pd.DataFrame): A DataFrame with product details, 
                                          including 'id', 'name', 'description', and 'category'.
        """
        self.products = product_data
        self.tfidf_matrix = None
        self.cosine_sim = None

    def preprocess_data(self):
        """
        Preprocesses the product data by vectorizing the text features.
        """
        # Combine necessary text fields for vectorization
        self.products['content'] = self.products['name'] + ' ' + self.products['description']
        
        # Initialize the TF-IDF Vectorizer
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        
        # Fit and transform the content into a TF-IDF matrix
        self.tfidf_matrix = tfidf_vectorizer.fit_transform(self.products['content'])

        # Calculate cosine similarity matrix
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def get_recommendations(self, product_id: int, num_recommendations: int = 5):
        """
        Get product recommendations based on the given product ID.

        Args:
            product_id (int): The ID of the product to find recommendations for.
            num_recommendations (int): The number of recommendations to return.
        
        Returns:
            list: A list of recommended product IDs.
        """
        try:
            # Get index of the product
            idx = self.products.index[self.products['id'] == product_id].tolist()[0]
            
            # Get the pairwise similarity scores of all products with the given product
            sim_scores = list(enumerate(self.cosine_sim[idx]))

            # Sort the products based on the similarity scores
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            # Get the scores of the most similar products
            sim_scores = sim_scores[1:num_recommendations + 1]  # Exclude the first product (itself)

            # Get the product indices
            product_indices = [i[0] for i in sim_scores]

            # Return the recommended product IDs
            return self.products['id'].iloc[product_indices].tolist()
        
        except IndexError:
            raise ValueError("Product ID not found in the dataset.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while getting recommendations: {str(e)}")

# Example usage:
if __name__ == "__main__":
    # Sample product data (ideally this would be fetched from a database or API)
    data = {
        'id': [1, 2, 3, 4, 5],
        'name': ['Jeździk A', 'Jeździk B', 'Rowerki Trójkołowe A', 'Rowerki Trójkołowe B', 'Jeździk C'],
        'description': ['Ideal for small children', 'Great for outdoor fun', 
                        'Perfect for toddlers', 'Stable and safe', 
                        'Fun and colorful ride'],
        'category': ['jeździki', 'jeździki', 'rowerki trójkołowe', 'rowerki trójkołowe', 'jeździki']
    }

    # Create DataFrame
    product_df = pd.DataFrame(data)

    # Initialize the recommender system
    recommender = ProductRecommender(product_df)

    # Preprocess data to prepare for recommendations
    recommender.preprocess_data()

    # Get recommendations for a specific product
    try:
        recommended_ids = recommender.get_recommendations(product_id=1)
        print("Recommended Product IDs:", recommended_ids)
    except Exception as e:
        print("Error:", str(e))
```
