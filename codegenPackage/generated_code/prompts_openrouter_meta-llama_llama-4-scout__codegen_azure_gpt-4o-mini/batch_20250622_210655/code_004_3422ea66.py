"""
Generated Code Metadata:
========================
Original URL: https://createxpro.com
Prompt: Create a product recommendation engine using Python and scikit-learn to suggest customized textile products and promotional gifts based on customer preferences and purchase history.
Generated: DETERMINISTIC_3422ea6653da7018
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import numpy as np

class ProductRecommendationEngine:
    def __init__(self, data):
        """
        Initializes the recommendation engine with the provided data.

        :param data: DataFrame containing customer preferences and purchase history
        """
        self.data = data
        self.model = None
        self.scaler = StandardScaler()

    def preprocess_data(self):
        """
        Preprocess the data by scaling numerical features and handling missing values.
        """
        # Fill missing values with the mean of the column
        self.data.fillna(self.data.mean(), inplace=True)

        # Scale numerical features
        numerical_features = self.data.select_dtypes(include=[np.number]).columns
        self.data[numerical_features] = self.scaler.fit_transform(self.data[numerical_features])

    def train_model(self):
        """
        Trains the Nearest Neighbors model on the preprocessed data.
        """
        try:
            # Split data into features and target
            X = self.data.drop('product_id', axis=1)  # Assuming 'product_id' is the target
            y = self.data['product_id']

            # Split the dataset into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Initialize and fit the Nearest Neighbors model
            self.model = NearestNeighbors(n_neighbors=5)
            self.model.fit(X_train)

            print("Model trained successfully.")
        except Exception as e:
            print(f"Error during model training: {e}")

    def recommend_products(self, customer_data, n_recommendations=5):
        """
        Recommends products based on customer data.

        :param customer_data: DataFrame containing customer preferences
        :param n_recommendations: Number of product recommendations to return
        :return: List of recommended product IDs
        """
        try:
            # Scale the customer data using the same scaler
            customer_data_scaled = self.scaler.transform(customer_data)

            # Find the nearest neighbors
            distances, indices = self.model.kneighbors(customer_data_scaled, n_neighbors=n_recommendations)

            # Retrieve recommended product IDs
            recommended_products = self.data.iloc[indices[0]]['product_id'].values.tolist()
            return recommended_products
        except Exception as e:
            print(f"Error during product recommendation: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Load your dataset
    try:
        data = pd.read_csv('customer_product_data.csv')  # Replace with your actual data file
        recommendation_engine = ProductRecommendationEngine(data)

        # Preprocess the data
        recommendation_engine.preprocess_data()

        # Train the model
        recommendation_engine.train_model()

        # Example customer data for recommendations
        customer_data = pd.DataFrame({
            'feature1': [0.5],  # Replace with actual feature names and values
            'feature2': [1.2],
            # Add more features as necessary
        })

        # Get product recommendations
        recommendations = recommendation_engine.recommend_products(customer_data)
        print("Recommended Products:", recommendations)
    except FileNotFoundError:
        print("The specified data file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
