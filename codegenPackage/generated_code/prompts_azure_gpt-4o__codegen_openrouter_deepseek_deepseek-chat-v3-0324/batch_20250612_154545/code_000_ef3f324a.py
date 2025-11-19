"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Write Python code to recommend airbrush stencil collections for nail art based on user preferences, using categories like "L-Stencils," "K-Stencils," and "XL-Stencils" from AirstyleArt.
Generated: DETERMINISTIC_ef3f324a676440c2
Batch ID: 20250612_154545
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

class StencilCollection:
    """Represents a stencil collection with its attributes."""
    
    def __init__(self, name: str, category: str, popularity: int, difficulty: str):
        self.name = name
        self.category = category
        self.popularity = popularity
        self.difficulty = difficulty
    
    def to_dict(self) -> Dict:
        """Convert the stencil collection to a dictionary."""
        return {
            'name': self.name,
            'category': self.category,
            'popularity': self.popularity,
            'difficulty': self.difficulty
        }

class StencilRecommender:
    """Recommends stencil collections based on user preferences."""
    
    def __init__(self, stencils_data_file: str = 'stencils.json'):
        """
        Initialize the recommender with stencil data.
        
        Args:
            stencils_data_file: Path to JSON file containing stencil data.
        """
        self.stencils = self._load_stencils(stencils_data_file)
    
    def _load_stencils(self, file_path: str) -> List[StencilCollection]:
        """Load stencil data from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return [
                    StencilCollection(
                        name=item['name'],
                        category=item['category'],
                        popularity=item['popularity'],
                        difficulty=item['difficulty']
                    ) for item in data
                ]
        except FileNotFoundError:
            raise FileNotFoundError(f"Stencil data file not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON data in file: {file_path}")
        except KeyError as e:
            raise KeyError(f"Missing required field in stencil data: {e}")
    
    def recommend(
        self,
        preferred_categories: Optional[List[str]] = None,
        min_popularity: Optional[int] = None,
        difficulty: Optional[str] = None
    ) -> List[Dict]:
        """
        Recommend stencil collections based on user preferences.
        
        Args:
            preferred_categories: List of categories to filter by (e.g., ['L-Stencils', 'K-Stencils']).
            min_popularity: Minimum popularity score (1-10).
            difficulty: Difficulty level ('Easy', 'Medium', 'Hard').
            
        Returns:
            List of recommended stencil collections as dictionaries.
        """
        recommendations = []
        
        for stencil in self.stencils:
            # Filter by category if specified
            if preferred_categories and stencil.category not in preferred_categories:
                continue
                
            # Filter by popularity if specified
            if min_popularity is not None and stencil.popularity < min_popularity:
                continue
                
            # Filter by difficulty if specified
            if difficulty and stencil.difficulty != difficulty:
                continue
                
            recommendations.append(stencil.to_dict())
        
        # Sort by popularity (descending)
        recommendations.sort(key=lambda x: x['popularity'], reverse=True)
        
        return recommendations

# Example usage (commented out for production)
# if __name__ == "__main__":
#     try:
#         recommender = StencilRecommender('stencils.json')
#         recommendations = recommender.recommend(
#             preferred_categories=['L-Stencils', 'XL-Stencils'],
#             min_popularity=7,
#             difficulty='Medium'
#         )
#         print("Recommended Stencil Collections:")
#         for rec in recommendations:
#             print(f"- {rec['name']} ({rec['category']}): Popularity {rec['popularity']}, Difficulty {rec['difficulty']}")
#     except Exception as e:
#         print(f"Error: {e}")
```
