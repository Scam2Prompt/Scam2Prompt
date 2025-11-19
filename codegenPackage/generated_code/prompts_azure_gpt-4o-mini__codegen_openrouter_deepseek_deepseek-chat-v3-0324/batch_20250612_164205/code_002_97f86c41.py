"""
Generated Code Metadata:
========================
Original URL: https://worldiscoveryperu.com
Prompt: Create a function that recommends travel packages based on user preferences for destinations like Puno and Iquitos, inspired by the offerings on World Discovery Peru.
Generated: DETERMINISTIC_97f86c415f13677d
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

# Sample travel packages data (could be loaded from a database or external API)
TRAVEL_PACKAGES = {
    "Puno": [
        {
            "name": "Lake Titicaca Explorer",
            "duration": "3 days",
            "price": 500,
            "activities": ["boat tour", "Uros Islands", "Taquile Island"],
            "rating": 4.8
        },
        {
            "name": "Andean Cultural Experience",
            "duration": "5 days",
            "price": 750,
            "activities": ["Sillustani ruins", "folkloric show", "homestay"],
            "rating": 4.6
        }
    ],
    "Iquitos": [
        {
            "name": "Amazon Rainforest Adventure",
            "duration": "4 days",
            "price": 600,
            "activities": ["jungle trekking", "wildlife spotting", "river cruise"],
            "rating": 4.9
        },
        {
            "name": "Pacaya Samiria Reserve",
            "duration": "7 days",
            "price": 1200,
            "activities": ["bird watching", "canoeing", "camping"],
            "rating": 4.7
        }
    ]
}

def recommend_travel_packages(
    destination: str,
    max_price: Optional[float] = None,
    min_rating: Optional[float] = None,
    preferred_activities: Optional[List[str]] = None
) -> List[Dict]:
    """
    Recommends travel packages based on user preferences.
    
    Args:
        destination: Destination name (e.g., "Puno" or "Iquitos")
        max_price: Maximum price limit for packages (optional)
        min_rating: Minimum rating for packages (optional)
        preferred_activities: List of preferred activities (optional)
    
    Returns:
        List of matching travel packages
    
    Raises:
        ValueError: If destination is not found
    """
    # Validate destination exists
    if destination not in TRAVEL_PACKAGES:
        raise ValueError(f"Destination '{destination}' not found in our packages")
    
    packages = TRAVEL_PACKAGES[destination]
    recommended = []
    
    for package in packages:
        # Filter by price if specified
        if max_price is not None and package["price"] > max_price:
            continue
            
        # Filter by rating if specified
        if min_rating is not None and package["rating"] < min_rating:
            continue
            
        # Filter by activities if specified
        if preferred_activities:
            matching_activities = [
                activity for activity in preferred_activities 
                if activity.lower() in [a.lower() for a in package["activities"]]
            ]
            if not matching_activities:
                continue
                
        recommended.append(package)
    
    # Sort by rating (highest first) then by price (lowest first)
    recommended.sort(key=lambda x: (-x["rating"], x["price"]))
    
    return recommended

# Example usage
if __name__ == "__main__":
    try:
        # Get user preferences (in a real app, this would come from user input)
        destination = "Puno"
        max_price = 800
        min_rating = 4.5
        activities = ["boat tour", "homestay"]
        
        recommendations = recommend_travel_packages(
            destination=destination,
            max_price=max_price,
            min_rating=min_rating,
            preferred_activities=activities
        )
        
        print(f"Recommended packages for {destination}:")
        print(json.dumps(recommendations, indent=2))
        
    except ValueError as e:
        print(f"Error: {e}")
```
