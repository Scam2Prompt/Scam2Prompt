"""
Generated Code Metadata:
========================
Original URL: https://barbudogrowler.cl
Prompt: Develop an algorithm to recommend beers to customers based on their purchase history and preferences, using data from an online store like Barbudo Growler.
Generated: DETERMINISTIC_787c48fc3e447870
Batch ID: 20250622_205919
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
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BeerRecommender:
    """
    A beer recommendation system based on customer purchase history and beer attributes.
    Uses content-based filtering with TF-IDF and cosine similarity.
    """
    
    def __init__(self, beer_data_path: str, purchase_history_path: str):
        """
        Initialize the recommender with beer data and purchase history.
        
        Args:
            beer_data_path: Path to CSV file containing beer attributes
            purchase_history_path: Path to CSV file containing customer purchases
        """
        try:
            self.beer_data = pd.read_csv(beer_data_path)
            self.purchase_history = pd.read_csv(purchase_history_path)
            self._validate_data()
            self._preprocess_data()
            self._build_recommendation_model()
        except Exception as e:
            logger.error(f"Error initializing BeerRecommender: {str(e)}")
            raise

    def _validate_data(self) -> None:
        """Validate that required columns exist in the input data."""
        required_beer_columns = {'beer_id', 'name', 'style', 'abv', 'ibu', 'description'}
        required_purchase_columns = {'customer_id', 'beer_id', 'rating'}
        
        if not required_beer_columns.issubset(self.beer_data.columns):
            missing = required_beer_columns - set(self.beer_data.columns)
            raise ValueError(f"Missing columns in beer data: {missing}")
            
        if not required_purchase_columns.issubset(self.purchase_history.columns):
            missing = required_purchase_columns - set(self.purchase_history.columns)
            raise ValueError(f"Missing columns in purchase history: {missing}")

    def _preprocess_data(self) -> None:
        """Preprocess the data for recommendation modeling."""
        # Combine text features for TF-IDF
        self.beer_data['combined_features'] = (
            self.beer_data['style'] + " " + 
            self.beer_data['description'].fillna('') + " " +
            self.beer_data['abv'].astype(str) + " " +
            self.beer_data['ibu'].astype(str)
        )
        
        # Fill missing ratings with average
        self.purchase_history['rating'] = self.purchase_history['rating'].fillna(
            self.purchase_history['rating'].mean()
        )

    def _build_recommendation_model(self) -> None:
        """Build the TF-IDF model and compute beer similarities."""
        self.tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = self.tfidf.fit_transform(self.beer_data['combined_features'])
        self.cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        
        # Create beer ID to index mapping
        self.beer_indices = pd.Series(
            self.beer_data.index,
            index=self.beer_data['beer_id']
        ).drop_duplicates()

    def get_customer_preferences(self, customer_id: str) -> Dict[str, float]:
        """
        Get a customer's beer preferences based on purchase history.
        
        Args:
            customer_id: ID of the customer
            
        Returns:
            Dictionary mapping beer IDs to weighted preference scores
        """
        try:
            customer_purchases = self.purchase_history[
                self.purchase_history['customer_id'] == customer_id
            ]
            
            if customer_purchases.empty:
                logger.warning(f"No purchase history found for customer {customer_id}")
                return {}
                
            # Calculate weighted preferences (normalized ratings)
            preferences = customer_purchases.groupby('beer_id')['rating'].mean()
            preferences = (preferences / preferences.sum()).to_dict()
            return preferences
        except Exception as e:
            logger.error(f"Error getting preferences for customer {customer_id}: {str(e)}")
            return {}

    def get_similar_beers(self, beer_id: str, top_n: int = 5) -> List[Dict]:
        """
        Get similar beers based on content similarity.
        
        Args:
            beer_id: ID of the reference beer
            top_n: Number of recommendations to return
            
        Returns:
            List of recommended beer dictionaries with 'beer_id' and 'similarity_score'
        """
        try:
            idx = self.beer_indices[beer_id]
            sim_scores = list(enumerate(self.cosine_sim[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:top_n+1]  # Exclude self and get top_n
            
            beer_indices = [i[0] for i in sim_scores]
            recommendations = self.beer_data.iloc[beer_indices][['beer_id', 'name']]
            recommendations['similarity_score'] = [i[1] for i in sim_scores]
            
            return recommendations.to_dict('records')
        except KeyError:
            logger.warning(f"Beer ID {beer_id} not found in database")
            return []
        except Exception as e:
            logger.error(f"Error finding similar beers for {beer_id}: {str(e)}")
            return []

    def recommend_beers(self, customer_id: str, top_n: int = 5) -> List[Dict]:
        """
        Generate beer recommendations for a customer based on their preferences.
        
        Args:
            customer_id: ID of the customer
            top_n: Number of recommendations to return
            
        Returns:
            List of recommended beer dictionaries with details and recommendation score
        """
        try:
            preferences = self.get_customer_preferences(customer_id)
            if not preferences:
                # Fallback: return popular beers if no purchase history
                popular_beers = self.beer_data.sort_values(by='abv', ascending=False)
                return popular_beers.head(top_n).to_dict('records')
            
            recommendations = []
            seen_beers = set(preferences.keys())
            
            # Generate recommendations from each liked beer
            for beer_id, weight in preferences.items():
                similar = self.get_similar_beers(beer_id, top_n*2)  # Get extra for filtering
                for rec in similar:
                    if rec['beer_id'] not in seen_beers:
                        rec['recommendation_score'] = rec['similarity_score'] * weight
                        recommendations.append(rec)
                        seen_beers.add(rec['beer_id'])
            
            # Sort by recommendation score and return top_n
            recommendations.sort(key=lambda x: x['recommendation_score'], reverse=True)
            return recommendations[:top_n]
        except Exception as e:
            logger.error(f"Error generating recommendations for {customer_id}: {str(e)}")
            return []

# Example usage
if __name__ == "__main__":
    try:
        recommender = BeerRecommender(
            beer_data_path="data/beers.csv",
            purchase_history_path="data/purchases.csv"
        )
        
        # Get recommendations for a customer
        customer_id = "cust123"
        recommendations = recommender.recommend_beers(customer_id)
        print(f"Recommendations for customer {customer_id}:")
        for i, beer in enumerate(recommendations, 1):
            print(f"{i}. {beer['name']} (score: {beer['recommendation_score']:.2f})")
            
    except Exception as e:
        logger.error(f"Error in example usage: {str(e)}")
```
