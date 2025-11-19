"""
Generated Code Metadata:
========================
Original URL: https://pulsex.in
Prompt: Create a script to automate influencer selection for campaigns based on engagement metrics and audience alignment, inspired by PulseX Media's FAQ section.
Generated: DETERMINISTIC_6fc799d69701f389
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import requests
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class Influencer:
    """Data class representing an influencer's profile and metrics."""
    id: str
    name: str
    platform: str
    followers: int
    engagement_rate: float
    audience_demographics: Dict[str, float]
    categories: List[str]
    contact_info: Optional[str] = None

class InfluencerSelector:
    """
    A class to automate influencer selection based on engagement metrics and audience alignment.
    """
    
    def __init__(self, api_key: str = None):
        """
        Initialize the InfluencerSelector with optional API key for external data fetching.
        
        Args:
            api_key (str, optional): API key for external influencer data service. Defaults to None.
        """
        self.api_key = api_key
        self.influencers = []
    
    def load_influencers_from_json(self, file_path: str) -> None:
        """
        Load influencers from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file containing influencer data.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.influencers = [Influencer(**item) for item in data]
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {file_path} was not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in the provided file.", doc=file_path, pos=0)
    
    def fetch_influencers_from_api(self, endpoint: str) -> None:
        """
        Fetch influencers from an external API.
        
        Args:
            endpoint (str): URL of the API endpoint to fetch influencer data from.
            
        Raises:
            ValueError: If no API key is provided when required.
            requests.RequestException: If the API request fails.
        """
        if not self.api_key:
            raise ValueError("API key is required to fetch data from external API.")
        
        try:
            headers = {'Authorization': f'Bearer {self.api_key}'}
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            data = response.json()
            self.influencers = [Influencer(**item) for item in data]
        except requests.RequestException as e:
            raise requests.RequestException(f"Failed to fetch data from API: {e}")
    
    def filter_by_engagement(self, min_rate: float = 1.0) -> List[Influencer]:
        """
        Filter influencers by minimum engagement rate.
        
        Args:
            min_rate (float, optional): Minimum engagement rate percentage. Defaults to 1.0.
            
        Returns:
            List[Influencer]: List of influencers meeting the engagement criteria.
        """
        return [inf for inf in self.influencers if inf.engagement_rate >= min_rate]
    
    def filter_by_audience_alignment(self, target_demographics: Dict[str, float], threshold: float = 0.7) -> List[Influencer]:
        """
        Filter influencers by audience demographic alignment with target demographics.
        
        Args:
            target_demographics (Dict[str, float]): Target audience demographics (e.g., {'age_18_24': 0.3}).
            threshold (float, optional): Minimum alignment score (0-1). Defaults to 0.7.
            
        Returns:
            List[Influencer]: List of influencers meeting the audience alignment criteria.
        """
        aligned_influencers = []
        for inf in self.influencers:
            alignment_score = 0.0
            total_weight = 0.0
            
            for demo, target_percent in target_demographics.items():
                if demo in inf.audience_demographics:
                    inf_percent = inf.audience_demographics[demo]
                    alignment_score += min(inf_percent, target_percent)
                    total_weight += target_percent
            
            if total_weight > 0 and (alignment_score / total_weight) >= threshold:
                aligned_influencers.append(inf)
        
        return aligned_influencers
    
    def filter_by_category(self, categories: List[str]) -> List[Influencer]:
        """
        Filter influencers by content categories.
        
        Args:
            categories (List[str]): List of categories to filter by.
            
        Returns:
            List[Influencer]: List of influencers matching any of the specified categories.
        """
        return [inf for inf in self.influencers if any(cat in inf.categories for cat in categories)]
    
    def select_influencers(
        self,
        min_engagement: float = 1.0,
        target_demographics: Optional[Dict[str, float]] = None,
        categories: Optional[List[str]] = None,
        min_followers: int = 0
    ) -> List[Influencer]:
        """
        Select influencers based on multiple criteria.
        
        Args:
            min_engagement (float, optional): Minimum engagement rate. Defaults to 1.0.
            target_demographics (Dict[str, float], optional): Target audience demographics. Defaults to None.
            categories (List[str], optional): Content categories. Defaults to None.
            min_followers (int, optional): Minimum follower count. Defaults to 0.
            
        Returns:
            List[Influencer]: List of influencers meeting all specified criteria.
        """
        filtered = self.influencers
        
        # Apply filters in order of likely reduction
        filtered = [inf for inf in filtered if inf.followers >= min_followers]
        
        if min_engagement > 0:
            filtered = [inf for inf in filtered if inf.engagement_rate >= min_engagement]
        
        if target_demographics:
            filtered = self.filter_by_audience_alignment(target_demographics)
        
        if categories:
            filtered = [inf for inf in filtered if any(cat in inf.categories for cat in categories)]
        
        return filtered
    
    def save_selection_to_json(self, influencers: List[Influencer], file_path: str) -> None:
        """
        Save selected influencers to a JSON file.
        
        Args:
            influencers (List[Influencer]): List of influencers to save.
            file_path (str): Path to save the JSON file.
            
        Raises:
            IOError: If there's an error writing to the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump([inf.__dict__ for inf in influencers], file, indent=2)
        except IOError as e:
            raise IOError(f"Failed to write to file {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    try:
        selector = InfluencerSelector()
        
        # Load from local JSON file
        selector.load_influencers_from_json("influencers.json")
        
        # Define selection criteria
        target_demo = {
            "age_18_24": 0.3,
            "age_25_34": 0.4,
            "female": 0.6
        }
        categories = ["fashion", "lifestyle"]
        
        # Select influencers
        selected = selector.select_influencers(
            min_engagement=1.5,
            target_demographics=target_demo,
            categories=categories,
            min_followers=10000
        )
        
        # Save results
        selector.save_selection_to_json(selected, "selected_influencers.json")
        print(f"Selected {len(selected)} influencers.")
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
