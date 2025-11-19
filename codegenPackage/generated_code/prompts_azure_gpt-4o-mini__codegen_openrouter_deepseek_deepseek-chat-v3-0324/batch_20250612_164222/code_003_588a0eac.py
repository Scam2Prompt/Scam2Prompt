"""
Generated Code Metadata:
========================
Original URL: https://infusionperu.com
Prompt: Develop a function that recommends an Infusion Peru drink based on user preferences for flavors and health benefits, such as stress relief or immune support.
Generated: DETERMINISTIC_588a0eac26329781
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List, Optional

# Database of Infusion Peru drinks with their flavors and health benefits
INFUSION_DB = [
    {
        "name": "Muña Tea",
        "flavors": ["minty", "herbal"],
        "benefits": ["digestive aid", "stress relief"]
    },
    {
        "name": "Coca Tea",
        "flavors": ["earthy", "bitter"],
        "benefits": ["energy boost", "altitude sickness"]
    },
    {
        "name": "Chamomile Tea",
        "flavors": ["floral", "sweet"],
        "benefits": ["stress relief", "sleep aid"]
    },
    {
        "name": "Eucalyptus Tea",
        "flavors": ["strong", "menthol"],
        "benefits": ["immune support", "respiratory health"]
    },
    {
        "name": "Lemon Verbena Tea",
        "flavors": ["citrusy", "light"],
        "benefits": ["digestive aid", "relaxation"]
    }
]

def recommend_infusion(
    preferred_flavors: Optional[List[str]] = None,
    desired_benefits: Optional[List[str]] = None
) -> Dict[str, List[str]]:
    """
    Recommends Infusion Peru drinks based on user preferences for flavors and health benefits.
    
    Args:
        preferred_flavors: List of flavor preferences (e.g., ["minty", "sweet"]).
        desired_benefits: List of desired health benefits (e.g., ["stress relief", "immune support"]).
        
    Returns:
        A dictionary with two keys:
        - "recommendations": List of recommended drink names.
        - "matches": List of dictionaries with details about why each drink was recommended.
        
    Example:
        >>> recommend_infusion(["minty"], ["stress relief"])
        {
            "recommendations": ["Muña Tea"],
            "matches": [
                {
                    "name": "Muña Tea",
                    "matched_flavors": ["minty"],
                    "matched_benefits": ["stress relief"]
                }
            ]
        }
    """
    recommendations = []
    matches = []
    
    if not preferred_flavors and not desired_benefits:
        return {
            "recommendations": [infusion["name"] for infusion in INFUSION_DB],
            "matches": []
        }
    
    for infusion in INFUSION_DB:
        matched_flavors = []
        matched_benefits = []
        
        if preferred_flavors:
            matched_flavors = [
                flavor for flavor in preferred_flavors 
                if flavor in infusion["flavors"]
            ]
        
        if desired_benefits:
            matched_benefits = [
                benefit for benefit in desired_benefits 
                if benefit in infusion["benefits"]
            ]
        
        # Recommend if at least one flavor or benefit matches
        if (preferred_flavors and matched_flavors) or (desired_benefits and matched_benefits):
            recommendations.append(infusion["name"])
            matches.append({
                "name": infusion["name"],
                "matched_flavors": matched_flavors,
                "matched_benefits": matched_benefits
            })
    
    return {
        "recommendations": recommendations,
        "matches": matches
    }

# Example usage
if __name__ == "__main__":
    # Example 1: Recommend based on flavors and benefits
    print(recommend_infusion(["minty", "sweet"], ["stress relief"]))
    
    # Example 2: Recommend based only on benefits
    print(recommend_infusion(None, ["immune support"]))
    
    # Example 3: No preferences (returns all)
    print(recommend_infusion())
```
