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
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer
import joblib
import os
from typing import List, Dict, Optional

class RecommendationSystem:
    """
    A recommendation system to match buyers with suppliers based on product categories and certifications.
    """
    
    def __init__(self, data_path: str = None, model_path: str = None):
        """
        Initialize the recommendation system.
        
        Args:
            data_path (str): Path to the CSV file containing supplier data.
            model_path (str): Path to save/load trained models.
        """
        self.data_path = data_path
        self.model_path = model_path or 'models'
        self.supplier_data = None
        self.tfidf_vectorizer = None
        self.mlb = None
        self.certification_similarity = None
        
        # Create model directory if it doesn't exist
        os.makedirs(self.model_path, exist_ok=True)
        
    def load_data(self) -> pd.DataFrame:
        """
        Load and preprocess supplier data.
        
        Returns:
            pd.DataFrame: Processed supplier data.
        """
        try:
            self.supplier_data = pd.read_csv(self.data_path)
            
            # Preprocessing
            self.supplier_data['product_categories'] = self.supplier_data['product_categories'].str.lower()
            self.supplier_data['certifications'] = self.supplier_data['certifications'].apply(
                lambda x: [cert.strip().lower() for cert in x.split(',')] if isinstance(x, str) else []
            )
            
            return self.supplier_data
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def train_models(self) -> None:
        """
        Train TF-IDF and MultiLabelBinarizer models for recommendations.
        """
        if self.supplier_data is None:
            raise ValueError("Supplier data not loaded. Call load_data() first.")
        
        try:
            # TF-IDF for product categories
            self.tfidf_vectorizer = TfidfVectorizer(stop_words='english')
            tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.supplier_data['product_categories'])
            
            # MultiLabelBinarizer for certifications
            self.mlb = MultiLabelBinarizer()
            certification_matrix = self.mlb.fit_transform(self.supplier_data['certifications'])
            
            # Calculate certification similarity
            self.certification_similarity = cosine_similarity(certification_matrix)
            
            # Save models
            self._save_models()
            
        except Exception as e:
            raise Exception(f"Error training models: {str(e)}")
    
    def _save_models(self) -> None:
        """Save trained models to disk."""
        try:
            joblib.dump(self.tfidf_vectorizer, os.path.join(self.model_path, 'tfidf_model.pkl'))
            joblib.dump(self.mlb, os.path.join(self.model_path, 'mlb_model.pkl'))
            joblib.dump(self.certification_similarity, os.path.join(self.model_path, 'cert_similarity.pkl'))
        except Exception as e:
            raise Exception(f"Error saving models: {str(e)}")
    
    def load_models(self) -> None:
        """Load trained models from disk."""
        try:
            self.tfidf_vectorizer = joblib.load(os.path.join(self.model_path, 'tfidf_model.pkl'))
            self.mlb = joblib.load(os.path.join(self.model_path, 'mlb_model.pkl'))
            self.certification_similarity = joblib.load(os.path.join(self.model_path, 'cert_similarity.pkl'))
        except Exception as e:
            raise Exception(f"Error loading models: {str(e)}")
    
    def get_recommendations(
        self,
        product_categories: str,
        certifications: List[str],
        top_n: int = 5
    ) -> List[Dict]:
        """
        Get supplier recommendations based on product categories and certifications.
        
        Args:
            product_categories (str): Buyer's product categories of interest.
            certifications (List[str]): Buyer's required certifications.
            top_n (int): Number of recommendations to return.
            
        Returns:
            List[Dict]: List of recommended suppliers with their details.
        """
        if not self.tfidf_vectorizer or not self.mlb:
            raise ValueError("Models not trained or loaded. Call train_models() or load_models() first.")
        
        try:
            # Process input
            product_categories = product_categories.lower()
            certifications = [cert.lower().strip() for cert in certifications]
            
            # Calculate product category similarity
            query_tfidf = self.tfidf_vectorizer.transform([product_categories])
            category_similarity = cosine_similarity(query_tfidf, self.tfidf_vectorizer.transform(self.supplier_data['product_categories']))
            
            # Calculate certification similarity
            query_cert = self.mlb.transform([certifications])
            cert_similarity = cosine_similarity(query_cert, self.mlb.transform(self.supplier_data['certifications']))
            
            # Combine scores (equal weight for now)
            combined_scores = 0.5 * category_similarity + 0.5 * cert_similarity
            
            # Get top N recommendations
            top_indices = np.argsort(combined_scores[0])[-top_n:][::-1]
            
            # Prepare results
            recommendations = []
            for idx in top_indices:
                supplier = self.supplier_data.iloc[idx]
                recommendations.append({
                    'supplier_id': supplier['supplier_id'],
                    'name': supplier['name'],
                    'product_categories': supplier['product_categories'],
                    'certifications': supplier['certifications'],
                    'category_similarity': float(category_similarity[0][idx]),
                    'certification_similarity': float(cert_similarity[0][idx]),
                    'combined_score': float(combined_scores[0][idx])
                })
            
            return recommendations
        
        except Exception as e:
            raise Exception(f"Error generating recommendations: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the recommendation system
        rec_sys = RecommendationSystem(data_path="supplier_data.csv")
        
        # Load and preprocess data
        rec_sys.load_data()
        
        # Train models (or load if already trained)
        if not os.path.exists(os.path.join(rec_sys.model_path, 'tfidf_model.pkl')):
            rec_sys.train_models()
        else:
            rec_sys.load_models()
        
        # Get recommendations
        recommendations = rec_sys.get_recommendations(
            product_categories="textile garments",
            certifications=["ISO 9001", "OEKO-TEX"],
            top_n=3
        )
        
        print("Top Recommendations:")
        for rec in recommendations:
            print(f"\nSupplier: {rec['name']}")
            print(f"Product Categories: {rec['product_categories']}")
            print(f"Certifications: {rec['certifications']}")
            print(f"Combined Score: {rec['combined_score']:.2f}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
