"""
Generated Code Metadata:
========================
Original URL: https://opensea.ru
Prompt: Create a recommendation system for selecting underwater hunting gear, such as "какие подводные ружья бывают," based on the FAQs from https://opensea.ru.
Generated: DETERMINISTIC_89a38c5b24a6724b
Batch ID: 20250612_150323
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
from dataclasses import dataclass

@dataclass
class HuntingGear:
    """Class representing underwater hunting gear."""
    id: str
    name: str
    category: str
    description: str
    features: List[str]
    best_for: List[str]
    price_range: str
    experience_level: str

class HuntingGearRecommendationSystem:
    """Recommendation system for underwater hunting gear."""
    
    def __init__(self, data_file: str = "hunting_gear_data.json"):
        """Initialize the recommendation system with gear data."""
        self.gear_data = self._load_data(data_file)
    
    def _load_data(self, data_file: str) -> List[HuntingGear]:
        """Load gear data from JSON file."""
        try:
            with open(data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [HuntingGear(**item) for item in data]
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file {data_file} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in {data_file}.")
        except Exception as e:
            raise RuntimeError(f"Error loading data: {str(e)}")
    
    def recommend_by_category(self, category: str) -> List[HuntingGear]:
        """Recommend gear by category."""
        if not category:
            raise ValueError("Category cannot be empty.")
        
        return [gear for gear in self.gear_data if gear.category.lower() == category.lower()]
    
    def recommend_by_experience(self, experience_level: str) -> List[HuntingGear]:
        """Recommend gear by user experience level."""
        valid_levels = ["beginner", "intermediate", "advanced"]
        if experience_level.lower() not in valid_levels:
            raise ValueError(f"Invalid experience level. Must be one of: {valid_levels}")
        
        return [gear for gear in self.gear_data if gear.experience_level.lower() == experience_level.lower()]
    
    def recommend_by_price_range(self, price_range: str) -> List[HuntingGear]:
        """Recommend gear by price range."""
        valid_ranges = ["low", "medium", "high"]
        if price_range.lower() not in valid_ranges:
            raise ValueError(f"Invalid price range. Must be one of: {valid_ranges}")
        
        return [gear for gear in self.gear_data if gear.price_range.lower() == price_range.lower()]
    
    def recommend_by_features(self, desired_features: List[str]) -> List[HuntingGear]:
        """Recommend gear that has all specified features."""
        if not desired_features:
            raise ValueError("Features list cannot be empty.")
        
        return [gear for gear in self.gear_data 
                if all(feature.lower() in [f.lower() for f in gear.features] 
                      for feature in desired_features)]
    
    def get_all_categories(self) -> List[str]:
        """Get list of all available gear categories."""
        return list(set(gear.category for gear in self.gear_data))
    
    def get_gear_by_id(self, gear_id: str) -> Optional[HuntingGear]:
        """Get specific gear by its ID."""
        for gear in self.gear_data:
            if gear.id == gear_id:
                return gear
        return None

# Sample JSON data structure (would be in hunting_gear_data.json)
"""
[
    {
        "id": "rg001",
        "name": "Rob Allen Sparid",
        "category": "Rubber Guns",
        "description": "Powerful rubber-powered speargun for medium-range hunting",
        "features": ["adjustable power", "quick reload", "aluminum barrel"],
        "best_for": ["reef hunting", "medium fish"],
        "price_range": "medium",
        "experience_level": "intermediate"
    },
    {
        "id": "pg002",
        "name": "Cressi SL Star",
        "category": "Pneumatic Guns",
        "description": "Compact pneumatic speargun for short-range hunting",
        "features": ["compact design", "easy to handle", "quick reload"],
        "best_for": ["cave hunting", "small fish"],
        "price_range": "low",
        "experience_level": "beginner"
    }
]
"""
```
