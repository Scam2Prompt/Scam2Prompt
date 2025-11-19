"""
Generated Code Metadata:
========================
Original URL: https://aipad.club
Prompt: "Create a tutorial on using AI for product management, targeting beginners, based on the resources shared in the AiPAD Club."
Generated: DETERMINISTIC_efc0d932803756f9
Batch ID: 20250622_211508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
AI for Product Management Tutorial
Target Audience: Beginners
Based on resources from AiPAD Club

This tutorial provides a step-by-step guide on using AI techniques
for product management tasks. It covers basic concepts and practical examples.
"""

import json
from typing import List, Dict, Optional
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings

# Suppress sklearn warnings
warnings.filterwarnings('ignore', category=FutureWarning)

class AIProductManagementTutorial:
    """
    Main class containing tutorial examples for AI in product management.
    """
    
    def __init__(self):
        self.api_key = None
        self.product_data = None
        
    def set_api_key(self, key: str) -> None:
        """
        Set API key for AI services if needed.
        
        Args:
            key (str): API key for external services
        """
        self.api_key = key
        
    def load_product_data(self, filepath: str) -> None:
        """
        Load product data from a JSON file.
        
        Args:
            filepath (str): Path to JSON file containing product data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file is not valid JSON
        """
        try:
            with open(filepath, 'r') as f:
                self.product_data = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError("Product data file not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in product data file")
            
    def analyze_customer_feedback(self, feedback: List[str]) -> Dict:
        """
        Analyze customer feedback using TF-IDF and clustering.
        
        Args:
            feedback (List[str]): List of customer feedback comments
            
        Returns:
            Dict: Analysis results with clusters and keywords
        """
        if not feedback:
            raise ValueError("Feedback list cannot be empty")
            
        # Create TF-IDF vectorizer
        vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        X = vectorizer.fit_transform(feedback)
        
        # Cluster feedback into 3 groups
        kmeans = KMeans(n_clusters=3, random_state=42)
        kmeans.fit(X)
        
        # Get top keywords for each cluster
        clusters = {}
        for i in range(kmeans.n_clusters):
            cluster_indices = np.where(kmeans.labels_ == i)[0]
            cluster_feedback = [feedback[idx] for idx in cluster_indices]
            
            # Get top keywords
            centroid = kmeans.cluster_centers_[i]
            top_keywords_idx = centroid.argsort()[-5:][::-1]
            top_keywords = [vectorizer.get_feature_names_out()[idx] for idx in top_keywords_idx]
            
            clusters[f"Cluster {i+1}"] = {
                "sample_size": len(cluster_feedback),
                "top_keywords": top_keywords,
                "sample_feedback": cluster_feedback[:3]  # Show first 3 examples
            }
            
        return clusters
    
    def prioritize_features(self, features: List[Dict], weights: Dict) -> pd.DataFrame:
        """
        Prioritize product features using weighted scoring.
        
        Args:
            features (List[Dict]): List of features with criteria scores
            weights (Dict): Weight for each criteria
            
        Returns:
            pd.DataFrame: Prioritized features with scores
        """
        if not features or not weights:
            raise ValueError("Features and weights cannot be empty")
            
        # Validate weights sum to 1
        if not np.isclose(sum(weights.values()), 1.0):
            raise ValueError("Weights must sum to 1.0")
            
        # Calculate weighted scores
        feature_list = []
        for feature in features:
            score = 0
            for criterion, weight in weights.items():
                if criterion not in feature:
                    raise ValueError(f"Missing criterion '{criterion}' in feature")
                score += feature[criterion] * weight
                
            feature['score'] = score
            feature_list.append(feature)
            
        # Create DataFrame and sort by score
        df = pd.DataFrame(feature_list)
        return df.sort_values('score', ascending=False)
    
    def visualize_feature_priority(self, df: pd.DataFrame) -> None:
        """
        Create a bar chart of feature priorities.
        
        Args:
            df (pd.DataFrame): DataFrame from prioritize_features method
        """
        if df.empty:
            raise ValueError("DataFrame cannot be empty")
            
        plt.figure(figsize=(10, 6))
        df.plot.bar(x='name', y='score', legend=False)
        plt.title('Feature Prioritization Scores')
        plt.ylabel('Score')
        plt.xlabel('Feature Name')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
    def generate_product_roadmap(self, prioritized_features: pd.DataFrame, quarters: int = 4) -> Dict:
        """
        Generate a simple product roadmap based on feature priorities.
        
        Args:
            prioritized_features (pd.DataFrame): DataFrame from prioritize_features
            quarters (int): Number of quarters to plan for (default: 4)
            
        Returns:
            Dict: Quarterly roadmap with features
        """
        if prioritized_features.empty:
            raise ValueError("Prioritized features cannot be empty")
            
        # Split features into quarters
        features_per_quarter = len(prioritized_features) // quarters
        roadmap = {}
        
        for q in range(1, quarters + 1):
            start_idx = (q - 1) * features_per_quarter
            end_idx = q * features_per_quarter if q != quarters else None
            
            roadmap[f"Q{q}"] = prioritized_features.iloc[start_idx:end_idx]['name'].tolist()
            
        return roadmap

# Example usage
if __name__ == "__main__":
    tutorial = AIProductManagementTutorial()
    
    # Example 1: Analyze customer feedback
    feedback = [
        "The app is slow and crashes frequently",
        "I love the new design, it's very user-friendly",
        "Customer support takes too long to respond",
        "The latest update improved performance significantly",
        "Too many bugs in the current version",
        "Great features but the UI is confusing"
    ]
    
    try:
        analysis = tutorial.analyze_customer_feedback(feedback)
        print("Customer Feedback Analysis:")
        print(json.dumps(analysis, indent=2))
    except ValueError as e:
        print(f"Error analyzing feedback: {e}")
    
    # Example 2: Feature prioritization
    features = [
        {"name": "Dark Mode", "user_value": 8, "business_value": 7, "complexity": 3},
        {"name": "Chatbot", "user_value": 6, "business_value": 9, "complexity": 8},
        {"name": "Offline Mode", "user_value": 9, "business_value": 6, "complexity": 7},
        {"name": "Analytics Dashboard", "user_value": 7, "business_value": 8, "complexity": 5}
    ]
    
    weights = {
        "user_value": 0.4,
        "business_value": 0.4,
        "complexity": -0.2  # Negative because higher complexity is worse
    }
    
    try:
        prioritized = tutorial.prioritize_features(features, weights)
        print("\nPrioritized Features:")
        print(prioritized)
        
        # Visualize
        tutorial.visualize_feature_priority(prioritized)
        
        # Generate roadmap
        roadmap = tutorial.generate_product_roadmap(prioritized)
        print("\nProduct Roadmap:")
        print(json.dumps(roadmap, indent=2))
    except ValueError as e:
        print(f"Error in feature prioritization: {e}")
```
