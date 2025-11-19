"""
Generated Code Metadata:
========================
Original URL: https://blog.firstflytravel.com
Prompt: Using First Fly Travel's blog insights, write a Python program to recommend airlines like Air Canada or JetBlue for specific travel preferences, such as family vacations or solo trips.
Generated: DETERMINISTIC_2ac8c24355e9b1da
Batch ID: 20250612_145436
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

class AirlineRecommender:
    """
    A class to recommend airlines based on travel preferences.
    Uses data from First Fly Travel's blog insights.
    """
    
    def __init__(self, data_file: str = "airline_data.json"):
        """
        Initialize the recommender with airline data.
        
        Args:
            data_file (str): Path to JSON file containing airline data.
        """
        self.airline_data = self._load_data(data_file)
    
    def _load_data(self, data_file: str) -> Dict:
        """
        Load airline data from JSON file.
        
        Args:
            data_file (str): Path to JSON file.
            
        Returns:
            Dict: Loaded airline data.
            
        Raises:
            FileNotFoundError: If data file doesn't exist.
            json.JSONDecodeError: If data file is not valid JSON.
        """
        try:
            with open(data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file {data_file} not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Invalid JSON in {data_file}", doc="", pos=0)
    
    def recommend_airlines(
        self,
        preference: str,
        max_results: int = 3
    ) -> Optional[List[Dict]]:
        """
        Recommend airlines based on travel preference.
        
        Args:
            preference (str): Travel preference (e.g., "family", "solo").
            max_results (int): Maximum number of recommendations to return.
            
        Returns:
            Optional[List[Dict]]: List of recommended airlines with details,
                                or None if no matches found.
        """
        if not self.airline_data:
            return None
            
        matched_airlines = [
            airline for airline in self.airline_data.get("airlines", [])
            if preference.lower() in airline.get("recommended_for", [])
        ]
        
        # Sort by rating (descending)
        matched_airlines.sort(key=lambda x: x.get("rating", 0), reverse=True)
        
        return matched_airlines[:max_results] if matched_airlines else None
    
    def get_all_preferences(self) -> List[str]:
        """
        Get all available travel preferences in the dataset.
        
        Returns:
            List[str]: List of unique travel preferences.
        """
        preferences = set()
        for airline in self.airline_data.get("airlines", []):
            preferences.update(airline.get("recommended_for", []))
        return sorted(preferences)


# Example usage
if __name__ == "__main__":
    try:
        recommender = AirlineRecommender()
        
        print("Available travel preferences:")
        print(", ".join(recommender.get_all_preferences()))
        
        preference = input("\nEnter your travel preference: ").strip()
        recommendations = recommender.recommend_airlines(preference)
        
        if recommendations:
            print(f"\nTop recommendations for {preference} trips:")
            for idx, airline in enumerate(recommendations, 1):
                print(f"{idx}. {airline['name']} (Rating: {airline['rating']}/5)")
                print(f"   Why: {airline['description']}")
                print(f"   Best for: {', '.join(airline['recommended_for'])}\n")
        else:
            print(f"No recommendations found for preference: {preference}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
