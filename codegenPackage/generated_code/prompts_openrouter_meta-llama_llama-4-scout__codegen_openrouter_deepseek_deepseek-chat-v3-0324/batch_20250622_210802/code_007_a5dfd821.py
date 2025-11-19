"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Recommend a suitable Learning Management System (LMS) for delivering online courses like the ones offered by Global Healthcare Management College, focusing on features like course creation, student engagement, and assessment tools.
Generated: DETERMINISTIC_a5dfd8216636260d
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
LMS Recommendation System for Global Healthcare Management College
This script analyzes and recommends suitable Learning Management Systems based on requirements.
"""

import json
from typing import List, Dict, Optional

class LMSRecommender:
    """
    Recommends LMS platforms based on specific educational needs.
    """
    
    def __init__(self):
        self.lms_options = self._load_lms_data()
    
    def _load_lms_data(self) -> List[Dict]:
        """Load LMS data from JSON file"""
        try:
            with open('lms_data.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: LMS data file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in LMS data file.")
            return []
    
    def _calculate_score(self, lms: Dict, weights: Dict) -> float:
        """Calculate weighted score for an LMS based on requirements"""
        score = 0.0
        for feature, weight in weights.items():
            if feature in lms['features']:
                score += weight * lms['features'][feature]
        return score
    
    def recommend(
        self,
        weights: Optional[Dict] = None,
        min_price: float = 0,
        max_price: float = float('inf')
    ) -> List[Dict]:
        """
        Recommend LMS platforms based on weighted features and price range.
        
        Args:
            weights: Dictionary of feature weights (default emphasizes healthcare education)
            min_price: Minimum acceptable price
            max_price: Maximum acceptable price
            
        Returns:
            List of recommended LMS platforms sorted by score
        """
        if weights is None:
            weights = {
                'course_creation': 0.3,
                'student_engagement': 0.25,
                'assessment_tools': 0.25,
                'healthcare_specific': 0.2
            }
        
        recommendations = []
        
        for lms in self.lms_options:
            if min_price <= lms['price'] <= max_price:
                score = self._calculate_score(lms, weights)
                recommendations.append({
                    'name': lms['name'],
                    'score': round(score, 2),
                    'price': lms['price'],
                    'features': lms['features']
                })
        
        # Sort by score descending
        recommendations.sort(key=lambda x: x['score'], reverse=True)
        return recommendations
    
    def print_recommendations(self, recommendations: List[Dict], top_n: int = 3):
        """Print formatted recommendations"""
        print("\nTop LMS Recommendations:")
        print("-" * 40)
        for i, rec in enumerate(recommendations[:top_n], 1):
            print(f"{i}. {rec['name']} (Score: {rec['score']})")
            print(f"   Price: ${rec['price']}/month")
            print("   Key Features:")
            for feat, value in rec['features'].items():
                if value > 0.7:  # Highlight strong features
                    print(f"    - {feat.replace('_', ' ').title()}")
            print("-" * 40)

# Example usage
if __name__ == "__main__":
    recommender = LMSRecommender()
    
    # Custom weights for healthcare education focus
    custom_weights = {
        'course_creation': 0.25,
        'student_engagement': 0.25,
        'assessment_tools': 0.3,
        'healthcare_specific': 0.2
    }
    
    recs = recommender.recommend(
        weights=custom_weights,
        min_price=50,
        max_price=500
    )
    
    recommender.print_recommendations(recs)
```
