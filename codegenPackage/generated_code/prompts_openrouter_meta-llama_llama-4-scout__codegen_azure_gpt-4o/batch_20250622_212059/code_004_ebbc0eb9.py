"""
Generated Code Metadata:
========================
Original URL: https://syntera.pro
Prompt: "Develop a code snippet to analyze customer preferences and provide personalized recommendations for a service-based business using an AI Manager."
Generated: DETERMINISTIC_ebbc0eb922414f34
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.exceptions import NotFittedError

class AIManager:
    """
    AI Manager for analyzing customer preferences and providing personalized recommendations.
    """

    def __init__(self):
        """
        Initializes the AI Manager with necessary components.
        """
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.customer_profiles = None
        self.service_profiles = None

    def fit_service_profiles(self, services):
        """
        Fits the service profiles using TF-IDF vectorization.

        Args:
            services (list of str): List of service descriptions.
        """
        if not services or not isinstance(services, list):
            raise ValueError("Services must be a non-empty list of strings.")
        
        self.service_profiles = self.vectorizer.fit_transform(services)

    def analyze_customer_preferences(self, customer_feedback):
        """
        Analyzes customer preferences based on feedback.

        Args:
            customer_feedback (list of str): List of customer feedback strings.

        Returns:
            np.ndarray: TF-IDF matrix representing customer preferences.
        """
        if not customer_feedback or not isinstance(customer_feedback, list):
            raise ValueError("Customer feedback must be a non-empty list of strings.")
        
        try:
            return self.vectorizer.transform(customer_feedback)
        except NotFittedError:
            raise RuntimeError("Service profiles must be fitted before analyzing customer preferences.")

    def recommend_services(self, customer_feedback, top_n=3):
        """
        Provides personalized service recommendations based on customer feedback.

        Args:
            customer_feedback (list of str): List of customer feedback strings.
            top_n (int): Number of top recommendations to return.

        Returns:
            list of dict: List of recommendations with service indices and similarity scores.
        """
        if self.service_profiles is None:
            raise RuntimeError("Service profiles must be fitted before making recommendations.")
        
        customer_profiles = self.analyze_customer_preferences(customer_feedback)
        recommendations = []

        for customer_idx, customer_vector in enumerate(customer_profiles):
            similarity_scores = cosine_similarity(customer_vector, self.service_profiles).flatten()
            top_indices = similarity_scores.argsort()[-top_n:][::-1]
            recommendations.append({
                "customer_index": customer_idx,
                "recommendations": [
                    {"service_index": idx, "similarity_score": similarity_scores[idx]}
                    for idx in top_indices
                ]
            })

        return recommendations


# Example usage:
if __name__ == "__main__":
    # Sample service descriptions
    services = [
        "Premium car wash and detailing service",
        "Home cleaning and organization service",
        "Personalized fitness training sessions",
        "Gourmet meal delivery service",
        "Professional landscaping and gardening"
    ]

    # Sample customer feedback
    customer_feedback = [
        "I love clean and organized spaces.",
        "Looking for healthy meal options delivered to my home.",
        "Need help with maintaining my garden."
    ]

    try:
        # Initialize AI Manager
        ai_manager = AIManager()

        # Fit service profiles
        ai_manager.fit_service_profiles(services)

        # Generate recommendations
        recommendations = ai_manager.recommend_services(customer_feedback, top_n=2)

        # Display recommendations
        for recommendation in recommendations:
            print(f"Customer {recommendation['customer_index']} recommendations:")
            for rec in recommendation['recommendations']:
                print(f"  Service {rec['service_index']} - Similarity Score: {rec['similarity_score']:.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
