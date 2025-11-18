"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Generate a recommendation system for construction tools, prioritizing items like "bombas de testes," "carrinho de mão," and "cilindros hidráulicos," as described on the Anhanguera Ferramentas webpage.
Generated: DETERMINISTIC_683bcfd0d6437ca1
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationSystem:
    def __init__(self, products: pd.DataFrame):
        """
        Initializes the recommendation system with a list of products.

        :param products: A pandas DataFrame containing product details. Must include 'product_name' column.
        """
        self.products = products
        self.vectorizer = TfidfVectorizer()
        self.product_matrix = None
        self._prepare_data()

    def _prepare_data(self):
        """
        Prepares the TF-IDF matrix for product recommendations.
        Converts product names into vectors for similarity calculations.
        """
        try:
            # Convert product names into a TF-IDF matrix
            self.product_matrix = self.vectorizer.fit_transform(self.products['product_name'])
        except Exception as e:
            print(f"Error preparing data: {e}")
            self.product_matrix = None

    def recommend(self, query: str, top_n: int = 5):
        """
        Generates recommendations based on the provided query.

        :param query: A string describing the product to search for.
        :param top_n: Number of recommendations to return.
        :return: A list of recommended product names.
        """
        if self.product_matrix is None:
            print("Recommendation system is not prepared. Check data initialization.")
            return []

        try:
            # Transform the query into a vector
            query_vector = self.vectorizer.transform([query])

            # Calculate cosine similarity between the query vector and the product matrix
            similarity_scores = cosine_similarity(query_vector, self.product_matrix)

            # Get indices of the top N most similar products
            top_indices = similarity_scores[0].argsort()[-top_n:][::-1]

            # Return the names of the top N recommended products
            return self.products.iloc[top_indices]['product_name'].tolist()
        except Exception as e:
            print(f"Error generating recommendations: {e}")
            return []


# Example usage of RecommendationSystem

if __name__ == "__main__":
    # Sample dataset representing the products on Anhanguera Ferramentas webpage
    data = {
        "product_name": [
            "bombas de testes",
            "carrinho de mão",
            "cilindros hidráulicos",
            "furadeira elétrica",
            "martelo de unha",
            "serra elétrica",
            "chave de fenda",
            "compressor de ar",
            "esmerilhadeira angular",
            "nivelador a laser"
        ]
    }

    # Convert the data into a pandas DataFrame
    products_df = pd.DataFrame(data)

    # Initialize the recommendation system with the product list
    recommender = RecommendationSystem(products_df)

    # Generate recommendations for a query
    query_item = "bombas de testes"
    recommendations = recommender.recommend(query_item, top_n=3)

    # Print recommendations
    print("Recommendations for:", query_item)
    for i, rec in enumerate(recommendations, start=1):
        print(f"{i}. {rec}")
```
