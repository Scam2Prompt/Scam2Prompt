"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prgmea.pk
Prompt: Develop a recommendation system using machine learning to match buyers with suppliers listed on PRGMEA’s platform based on product categories and certifications.
Generated: DETERMINISTIC_323ec218fb11d5db
Batch ID: 20250612_153224
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
from sklearn.preprocessing import LabelEncoder
from sklearn.exceptions import NotFittedError

class RecommendationSystem:
    """
    A recommendation system to match buyers with suppliers on PRGMEA's platform 
    based on product categories and certifications.
    """

    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.encoder = LabelEncoder()

    def preprocess_data(self, buyers_data, suppliers_data):
        """
        Preprocess the data by combining product categories and certifications into a single feature.
        """
        try:
            # Combine product categories and certifications into a single string for matching
            buyers_data['combined'] = (
                buyers_data['product_categories'] + ' ' + buyers_data['certifications']
            )
            suppliers_data['combined'] = (
                suppliers_data['product_categories'] + ' ' + suppliers_data['certifications']
            )

            return buyers_data, suppliers_data
        except KeyError as e:
            raise ValueError(f"Missing expected column in input data: {e}")

    def train_vectorizer(self, suppliers_data):
        """
        Train the TF-IDF vectorizer on supplier data.
        """
        try:
            self.vectorizer.fit(suppliers_data['combined'])
        except KeyError:
            raise ValueError("Suppliers data must contain a 'combined' column.")

    def recommend_suppliers(self, buyers_data, suppliers_data):
        """
        Recommend suppliers to buyers based on cosine similarity of their product categories and certifications.
        """
        try:
            # Transform suppliers data using the trained vectorizer
            suppliers_matrix = self.vectorizer.transform(suppliers_data['combined'])
            
            # Transform buyers data using the trained vectorizer
            buyers_matrix = self.vectorizer.transform(buyers_data['combined'])
            
            recommendations = []
            for buyer_idx in range(buyers_matrix.shape[0]):
                # Compute cosine similarity between the buyer and all suppliers
                similarity_scores = cosine_similarity(
                    buyers_matrix[buyer_idx], suppliers_matrix
                ).flatten()
                
                # Get indices of suppliers sorted by similarity score in descending order
                top_supplier_indices = similarity_scores.argsort()[::-1]
                
                # Create recommendation format: buyer_id mapped to supplier_ids sorted by relevance
                recommended_suppliers = suppliers_data.iloc[top_supplier_indices].to_dict('records')
                recommendations.append(
                    {
                        "buyer_id": buyers_data.iloc[buyer_idx]['buyer_id'],
                        "recommended_suppliers": recommended_suppliers
                    }
                )

            return recommendations
        except NotFittedError:
            raise RuntimeError("Vectorizer has not been trained. Call train_vectorizer before recommending.")
        except KeyError as e:
            raise ValueError(f"Missing expected column in input data: {e}")

# Sample usage
if __name__ == "__main__":
    # Sample input data
    buyers_data = pd.DataFrame({
        "buyer_id": [1, 2],
        "product_categories": ["cotton shirts", "leather jackets"],
        "certifications": ["ISO-9001", "FairTrade"]
    })

    suppliers_data = pd.DataFrame({
        "supplier_id": [101, 102, 103],
        "product_categories": ["cotton shirts", "leather jackets", "wool sweaters"],
        "certifications": ["ISO-9001", "FairTrade", "GlobalOrganic"]
    })

    # Initialize recommendation system
    recommender = RecommendationSystem()
    
    # Preprocess data
    buyers_data, suppliers_data = recommender.preprocess_data(buyers_data, suppliers_data)
    
    # Train the vectorizer on suppliers data
    recommender.train_vectorizer(suppliers_data)
    
    # Generate recommendations
    recommendations = recommender.recommend_suppliers(buyers_data, suppliers_data)
    
    # Display recommendations
    for recommendation in recommendations:
        print(f"Buyer ID: {recommendation['buyer_id']}")
        print("Recommended Suppliers:")
        for supplier in recommendation['recommended_suppliers']:
            print(f"  Supplier ID: {supplier['supplier_id']}, Product Categories: {supplier['product_categories']}, Certifications: {supplier['certifications']}")
        print()
```
