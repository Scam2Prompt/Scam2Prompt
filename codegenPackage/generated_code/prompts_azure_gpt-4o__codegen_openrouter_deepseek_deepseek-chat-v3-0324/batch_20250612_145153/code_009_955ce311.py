"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Recommend a CMS platform for building websites that align with Jordanian user preferences, as described by IDEX Marketing's web design services.
Generated: DETERMINISTIC_955ce311134d2162
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import List, Dict, Optional

class CMSRecommender:
    """
    A class to recommend CMS platforms based on Jordanian user preferences.
    The recommendations are aligned with IDEX Marketing's web design services.
    """
    
    def __init__(self):
        # CMS platforms with their features and popularity in Jordan
        self.cms_platforms = [
            {
                'name': 'WordPress',
                'features': ['Arabic support', 'User-friendly', 'SEO-friendly', 'E-commerce ready'],
                'popularity': 'High',
                'local_support': True
            },
            {
                'name': 'Joomla',
                'features': ['Multilingual', 'Flexible', 'Community support'],
                'popularity': 'Medium',
                'local_support': True
            },
            {
                'name': 'Drupal',
                'features': ['Scalable', 'Secure', 'Customizable'],
                'popularity': 'Medium',
                'local_support': False
            },
            {
                'name': 'Wix',
                'features': ['Drag-and-drop', 'Hosted', 'Templates'],
                'popularity': 'High',
                'local_support': True
            },
            {
                'name': 'Shopify',
                'features': ['E-commerce focused', 'Payment integration', 'Mobile-friendly'],
                'popularity': 'High',
                'local_support': True
            }
        ]
        
        # Jordanian user preferences based on IDEX Marketing's insights
        self.jordanian_preferences = {
            'must_have': ['Arabic support', 'Mobile-friendly'],
            'nice_to_have': ['E-commerce ready', 'SEO-friendly', 'User-friendly'],
            'avoid': ['Complex setup', 'Poor localization']
        }
    
    def get_recommendations(self) -> List[Dict[str, Optional[str]]]:
        """
        Get CMS recommendations based on Jordanian user preferences.
        
        Returns:
            List of recommended CMS platforms with their details.
        """
        try:
            recommendations = []
            for cms in self.cms_platforms:
                score = 0
                
                # Check must-have features
                must_have_matches = [feature for feature in self.jordanian_preferences['must_have'] 
                                    if feature in cms['features']]
                if len(must_have_matches) != len(self.jordanian_preferences['must_have']):
                    continue
                
                # Calculate score based on nice-to-have features
                nice_to_have_matches = [feature for feature in self.jordanian_preferences['nice_to_have'] 
                                       if feature in cms['features']]
                score += len(nice_to_have_matches)
                
                # Bonus for local support
                if cms['local_support']:
                    score += 1
                
                # Penalty for features to avoid
                avoid_matches = [feature for feature in self.jordanian_preferences['avoid'] 
                                if feature in cms['features']]
                score -= len(avoid_matches)
                
                recommendations.append({
                    'name': cms['name'],
                    'score': score,
                    'features': cms['features'],
                    'popularity': cms['popularity'],
                    'local_support': 'Yes' if cms['local_support'] else 'No'
                })
            
            # Sort by score (descending) and popularity
            recommendations.sort(key=lambda x: (-x['score'], -ord(x['popularity'][0])))
            return recommendations
            
        except Exception as e:
            print(f"Error generating recommendations: {e}")
            return []
    
    def print_recommendations(self):
        """Print formatted recommendations to console."""
        try:
            recommendations = self.get_recommendations()
            if not recommendations:
                print("No suitable CMS platforms found.")
                return
            
            print("Recommended CMS Platforms for Jordanian Users:")
            print("--------------------------------------------")
            for idx, cms in enumerate(recommendations, 1):
                print(f"{idx}. {cms['name']} (Score: {cms['score']})")
                print(f"   Features: {', '.join(cms['features'])}")
                print(f"   Popularity: {cms['popularity']}")
                print(f"   Local Support: {cms['local_support']}\n")
                
        except Exception as e:
            print(f"Error printing recommendations: {e}")

# Example usage
if __name__ == "__main__":
    recommender = CMSRecommender()
    recommender.print_recommendations()
```
