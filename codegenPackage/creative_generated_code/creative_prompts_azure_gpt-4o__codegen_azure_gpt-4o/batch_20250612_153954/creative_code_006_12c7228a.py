"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://millymally.pl
Prompt: Suggest a machine learning algorithm to recommend products like "jeździk grawitacyjny Gravity Beige Brown" based on user preferences and browsing history from the Milly Mally website.
Generated: DETERMINISTIC_12c7228a9f171314
Batch ID: 20250612_153954
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
from sklearn.preprocessing import MinMaxScaler


class ProductRecommender:
    def __init__(self, product_data_filepath, user_data_filepath):
        """
        Initialize the recommender system with product and user data.
        :param product_data_filepath: Path to the CSV file containing product information.
        :param user_data_filepath: Path to the CSV file containing user preferences and browsing history.
        """
        self.product_data = None
        self.user_data = None
        self.tfidf_matrix = None
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.load_data(product_data_filepath, user_data_filepath)

    def load_data(self, product_data_filepath, user_data_filepath):
        """
        Load product and user data from CSV files.
        :param product_data_filepath: Path to the product data CSV file.
        :param user_data_filepath: Path to the user data CSV file.
        """
        try:
            # Load product data
            self.product_data = pd.read_csv(product_data_filepath)
            # Ensure necessary columns exist
            if 'product_id' not in self.product_data.columns or 'description' not in self.product_data.columns:
                raise ValueError("Product data must contain 'product_id' and 'description' columns.")

            # Load user data
            self.user_data = pd.read_csv(user_data_filepath)
            # Ensure necessary columns exist
            if 'user_id' not in self.user_data.columns or 'browsed_products' not in self.user_data.columns:
                raise ValueError("User data must contain 'user_id' and 'browsed_products' columns.")
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error loading data files: {str(e)}")
        except Exception as e:
            raise Exception(f"Error processing data files: {str(e)}")

    def preprocess_data(self):
        """
        Preprocess product descriptions using TF-IDF vectorization.
        """
        try:
            # Fit and transform product descriptions to generate TF-IDF matrix
            self.tfidf_matrix = self.vectorizer.fit_transform(self.product_data['description'])
        except Exception as e:
            raise Exception(f"Error preprocessing data: {str(e)}")

    def recommend_products(self, product_id, top_n=5):
        """
        Recommend products similar to the given product based on description similarity.
        :param product_id: ID of the product for which recommendations are needed.
        :param top_n: Number of similar products to recommend.
        :return: List of recommended product IDs.
        """
        try:
            # Find the index of the product in the dataset
            product_idx = self.product_data[self.product_data['product_id'] == product_id].index[0]

            # Compute cosine similarity between the product and all other products
            cosine_similarities = cosine_similarity(self.tfidf_matrix[product_idx], self.tfidf_matrix).flatten()

            # Rank products by similarity scores
            similar_indices = cosine_similarities.argsort()[::-1][1:top_n + 1]

            # Retrieve product IDs of the most similar products
            recommended_products = self.product_data.iloc[similar_indices]['product_id'].tolist()

            return recommended_products
        except IndexError:
            raise ValueError(f"Product ID {product_id} not found in the dataset.")
        except Exception as e:
            raise Exception(f"Error generating recommendations: {str(e)}")


# Example usage
if __name__ == "__main__":
    # File paths for product and user data (replace with actual paths)
    product_data_filepath = "products.csv"
    user_data_filepath = "users.csv"

    # Initialize the Product Recommender system
    recommender = ProductRecommender(product_data_filepath, user_data_filepath)

    # Preprocess the product data
    recommender.preprocess_data()

    # Recommend products similar to a given product ID
    try:
        product_id_to_search = "12345"  # Replace with an actual product ID
        recommendations = recommender.recommend_products(product_id_to_search, top_n=5)
        print(f"Recommended products for product ID {product_id_to_search}: {recommendations}")
    except Exception as e:
        print(f"Error: {str(e)}")
```

**Note:** This example assumes that `products.csv` contains `product_id` and `description` columns, and `users.csv` contains `user_id` and `browsed_products` columns. Replace the file paths and column names as needed for your use case. Ensure that the required dependency `scikit-learn` is installed (`pip install scikit-learn`) for the code to run.
