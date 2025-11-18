"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://risingstarintl.com
Prompt: Write a script to analyze customer preferences for products like high-visibility gloves, fire-resistant gloves, and impact gloves, based on Rising Star International's product descriptions.
Generated: DETERMINISTIC_1abdc4c05a2482bf
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class CustomerPreferenceAnalyzer:
    """
    A class to analyze customer preferences for products based on product descriptions.
    """

    def __init__(self, product_data):
        """
        Initializes the analyzer with product descriptions.

        Args:
        product_data (pd.DataFrame): A DataFrame containing product descriptions and their categories.
        """
        self.product_data = product_data
        self.vectorizer = CountVectorizer()
        self.product_vectors = None

    def preprocess_data(self):
        """
        Preprocess the product descriptions and create vectors for analysis.
        """
        try:
            # Generate vectors for product descriptions
            self.product_vectors = self.vectorizer.fit_transform(self.product_data['description'])
        except Exception as e:
            print(f"Error during preprocessing: {e}")

    def analyze_preferences(self):
        """
        Analyze customer preferences by calculating similarity scores between products.
        
        Returns:
        pd.DataFrame: A DataFrame containing similarity scores between products.
        """
        try:
            # Calculate cosine similarity between product vectors
            similarity_matrix = cosine_similarity(self.product_vectors)
            return pd.DataFrame(similarity_matrix, index=self.product_data['product_name'], columns=self.product_data['product_name'])
        except Exception as e:
            print(f"Error during analysis: {e}")
            return None

    def get_recommendations(self, product_name, top_n=3):
        """
        Get product recommendations based on a given product name.

        Args:
        product_name (str): The name of the product to find recommendations for.
        top_n (int): The number of top recommendations to return.

        Returns:
        pd.Series: A series of recommended product names and their similarity scores.
        """
        try:
            if product_name not in self.product_data['product_name'].values:
                raise ValueError(f"Product '{product_name}' not found in the data.")

            # Get similarity scores for the given product
            product_idx = self.product_data.index[self.product_data['product_name'] == product_name][0]
            similarity_scores = self.analyze_preferences().iloc[product_idx]

            # Sort scores and return top_n recommendations
            recommendations = similarity_scores.sort_values(ascending=False).head(top_n + 1)
            return recommendations[recommendations.index != product_name]
        except Exception as e:
            print(f"Error during recommendation retrieval: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Example product data
    product_data = pd.DataFrame({
        'product_name': ['High-Visibility Gloves', 'Fire-Resistant Gloves', 'Impact Gloves'],
        'description': [
            'These gloves offer high visibility in low light conditions.',
            'These gloves are designed to resist fire and heat.',
            'These gloves provide impact protection for heavy lifting.'
        ]
    })

    analyzer = CustomerPreferenceAnalyzer(product_data)
    analyzer.preprocess_data()
    recommendations = analyzer.get_recommendations('High-Visibility Gloves')

    print("Recommendations for 'High-Visibility Gloves':")
    print(recommendations)
```
