"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: "Recommend a suitable fishing reel and leather case for a Sea-Trout fishing trip, considering the provided reel data and product information from Emanuelson Reels."
Generated: DETERMINISTIC_647a9e857eea2198
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class FishingReel:
    def __init__(self, reel_id: str, name: str, type: str, weight: float, gear_ratio: str, line_capacity: str, price: float, saltwater_rated: bool):
        self.reel_id = reel_id
        self.name = name
        self.type = type
        self.weight = weight
        self.gear_ratio = gear_ratio
        self.line_capacity = line_capacity
        self.price = price
        self.saltwater_rated = saltwater_rated

class LeatherCase:
    def __init__(self, case_id: str, name: str, reel_compatibility: List[str], price: float):
        self.case_id = case_id
        self.name = name
        self.reel_compatibility = reel_compatibility
        self.price = price

class FishingTripRecommender:
    def __init__(self, reels_data: Dict, cases_data: Dict):
        self.reels = [FishingReel(**reel) for reel in reels_data]
        self.cases = [LeatherCase(**case) for case in cases_data]
    
    def recommend_for_sea_trout(self) -> Optional[Dict]:
        """
        Recommends a suitable reel and case combination for sea-trout fishing.
        Sea-trout reels should be lightweight, saltwater-rated, and have appropriate line capacity.
        """
        suitable_reels = [
            reel for reel in self.reels 
            if reel.saltwater_rated 
            and reel.weight <= 10.0  # Lightweight for sea-trout fishing
            and "spinning" in reel.type.lower()  # Spinning reels are common for trout
        ]
        
        if not suitable_reels:
            return None
        
        # Sort by weight (lightest first) then price (cheapest first)
        suitable_reels.sort(key=lambda x: (x.weight, x.price))
        recommended_reel = suitable_reels[0]
        
        # Find compatible cases
        compatible_cases = [
            case for case in self.cases 
            if recommended_reel.reel_id in case.reel_compatibility
        ]
        
        if not compatible_cases:
            return None
        
        # Sort cases by price (cheapest first)
        compatible_cases.sort(key=lambda x: x.price)
        recommended_case = compatible_cases[0]
        
        return {
            "reel": {
                "id": recommended_reel.reel_id,
                "name": recommended_reel.name,
                "price": recommended_reel.price
            },
            "case": {
                "id": recommended_case.case_id,
                "name": recommended_case.name,
                "price": recommended_case.price
            },
            "total_price": recommended_reel.price + recommended_case.price
        }

# Example usage
if __name__ == "__main__":
    # Sample data (would typically come from a database or API)
    reels_data = [
        {
            "reel_id": "EM001",
            "name": "Emanuelson Saltwater Pro",
            "type": "Spinning",
            "weight": 8.5,
            "gear_ratio": "5.2:1",
            "line_capacity": "10/200, 12/180, 15/150",
            "price": 199.99,
            "saltwater_rated": True
        },
        {
            "reel_id": "EM002",
            "name": "Emanuelson Freshwater",
            "type": "Spinning",
            "weight": 7.2,
            "gear_ratio": "6.0:1",
            "line_capacity": "6/150, 8/120, 10/100",
            "price": 149.99,
            "saltwater_rated": False
        },
        {
            "reel_id": "EM003",
            "name": "Emanuelson Heavy Duty",
            "type": "Baitcasting",
            "weight": 12.3,
            "gear_ratio": "7.1:1",
            "line_capacity": "20/200, 25/180, 30/150",
            "price": 249.99,
            "saltwater_rated": True
        }
    ]
    
    cases_data = [
        {
            "case_id": "LC001",
            "name": "Premium Leather Case",
            "reel_compatibility": ["EM001", "EM003"],
            "price": 59.99
        },
        {
            "case_id": "LC002",
            "name": "Deluxe Leather Case",
            "reel_compatibility": ["EM001", "EM002"],
            "price": 79.99
        }
    ]
    
    recommender = FishingTripRecommender(reels_data, cases_data)
    recommendation = recommender.recommend_for_sea_trout()
    
    if recommendation:
        print(json.dumps(recommendation, indent=2))
    else:
        print("No suitable recommendation found for sea-trout fishing.")
```
