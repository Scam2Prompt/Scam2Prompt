"""
Generated Code Metadata:
========================
Original URL: https://prgmea.pk
Prompt: Develop a recommendation system using machine learning to match buyers with suppliers listed on PRGMEA’s platform based on product categories and certifications.
Generated: DETERMINISTIC_323ec218fb11d5db
Batch ID: 20250612_153224
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

class RecommendationSystem:
    def __init__(self, data_path):
        """
        Initializes the RecommendationSystem with the data from the specified path.

        :param data_path: str, path to the CSV file containing buyer and supplier data
        """
        self.data = self.load_data(data_path)
        self.model = None
        self.scaler = StandardScaler()

    def load_data(self, data_path):
        """
        Loads the data from a CSV file.

        :param data_path: str, path to the CSV file
        :return: DataFrame, loaded data
        """
        try:
            data = pd.read_csv(data_path)
            return data
        except Exception as e:
            raise ValueError(f"Error loading data: {e}")

    def preprocess_data(self):
        """
        Preprocesses the data by encoding categorical variables and scaling numerical features.
        """
        # Example: Assuming 'product_category' and 'certifications' are categorical
        self.data = pd.get_dummies(self.data, columns=['product_category', 'certifications'], drop_first=True)
        
        # Separate features and target
        X = self.data.drop('supplier_id', axis=1)  # Assuming 'supplier_id' is the target
        self.scaler.fit(X)
        X_scaled = self.scaler.transform(X)
        
        return X_scaled

    def train_model(self):
        """
        Trains the Nearest Neighbors model on the preprocessed data.
        """
        X_scaled = self.preprocess_data()
        self.model = NearestNeighbors(n_neighbors=5)  # Find 5 nearest suppliers
        self.model.fit(X_scaled)

    def recommend_suppliers(self, buyer_data):
        """
        Recommends suppliers based on the buyer's data.

        :param buyer_data: dict, buyer's product category and certifications
        :return: list, recommended supplier IDs
        """
        try:
            # Convert buyer data to DataFrame
            buyer_df = pd.DataFrame([buyer_data])
            buyer_df = pd.get_dummies(buyer_df, columns=['product_category', 'certifications'], drop_first=True)
            buyer_df = buyer_df.reindex(columns=self.data.columns.drop('supplier_id'), fill_value=0)
            buyer_scaled = self.scaler.transform(buyer_df)

            # Find nearest suppliers
            distances, indices = self.model.kneighbors(buyer_scaled)
            recommended_suppliers = self.data.iloc[indices[0]]['supplier_id'].tolist()
            return recommended_suppliers
        except Exception as e:
            raise ValueError(f"Error recommending suppliers: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        recommender = RecommendationSystem('suppliers_data.csv')
        recommender.train_model()
        
        # Example buyer data
        buyer_info = {
            'product_category': 'Textiles',
            'certifications': 'ISO9001'
        }
        
        recommendations = recommender.recommend_suppliers(buyer_info)
        print("Recommended Suppliers:", recommendations)
    except Exception as e:
        print(f"An error occurred: {e}")
```
