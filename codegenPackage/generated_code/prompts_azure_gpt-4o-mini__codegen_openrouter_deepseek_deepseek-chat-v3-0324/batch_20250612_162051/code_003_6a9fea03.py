"""
Generated Code Metadata:
========================
Original URL: https://kiddooplayway.com
Prompt: Develop a library function that helps parents find daycare centers like Kiddoo Playway, emphasizing safety, quality educators, and innovative teaching methods.
Generated: DETERMINISTIC_6a9fea03c7c062cb
Batch ID: 20250612_162051
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
from dataclasses import dataclass
from enum import Enum

class SafetyRating(Enum):
    """Enum representing safety rating levels of daycare centers."""
    EXCELLENT = 5
    GOOD = 4
    AVERAGE = 3
    BELOW_AVERAGE = 2
    POOR = 1

class TeachingMethod(Enum):
    """Enum representing different teaching methods used by daycare centers."""
    MONTESSORI = "Montessori"
    REGGIO_EMILIA = "Reggio Emilia"
    WALDORF = "Waldorf"
    PLAY_BASED = "Play-Based"
    HIGH_SCOPE = "HighScope"
    OTHER = "Other"

@dataclass
class DaycareCenter:
    """Dataclass representing a daycare center with relevant attributes."""
    name: str
    location: str
    safety_rating: SafetyRating
    educators_quality_score: float  # Scale of 1-5
    teaching_methods: List[TeachingMethod]
    contact_info: str
    website: Optional[str] = None
    description: Optional[str] = None

class DaycareFinder:
    """A class to help parents find daycare centers based on specific criteria."""
    
    def __init__(self, api_endpoint: Optional[str] = None):
        """
        Initialize the DaycareFinder with an optional API endpoint.
        
        Args:
            api_endpoint: Optional API endpoint to fetch daycare data.
        """
        self.api_endpoint = api_endpoint
        self.daycare_centers = []  # Local cache of daycare centers
    
    def fetch_daycare_data(self) -> None:
        """
        Fetch daycare center data from the API endpoint.
        
        Raises:
            requests.exceptions.RequestException: If API request fails.
            ValueError: If API response is invalid.
        """
        if not self.api_endpoint:
            raise ValueError("API endpoint not configured")
        
        try:
            response = requests.get(self.api_endpoint)
            response.raise_for_status()
            data = response.json()
            
            for item in data:
                self.daycare_centers.append(
                    DaycareCenter(
                        name=item.get("name"),
                        location=item.get("location"),
                        safety_rating=SafetyRating(item.get("safety_rating")),
                        educators_quality_score=item.get("educators_quality_score"),
                        teaching_methods=[TeachingMethod(method) for method in item.get("teaching_methods", [])],
                        contact_info=item.get("contact_info"),
                        website=item.get("website"),
                        description=item.get("description")
                    )
                )
        except requests.exceptions.RequestException as e:
            raise requests.exceptions.RequestException(f"Failed to fetch daycare data: {e}")
        except (KeyError, ValueError) as e:
            raise ValueError(f"Invalid data format in API response: {e}")
    
    def add_daycare_center(self, center: DaycareCenter) -> None:
        """Add a daycare center to the local cache."""
        self.daycare_centers.append(center)
    
    def find_by_safety_rating(self, min_rating: SafetyRating) -> List[DaycareCenter]:
        """
        Find daycare centers with at least the specified safety rating.
        
        Args:
            min_rating: Minimum safety rating to filter by.
            
        Returns:
            List of matching daycare centers.
        """
        return [center for center in self.daycare_centers if center.safety_rating.value >= min_rating.value]
    
    def find_by_educators_quality(self, min_score: float) -> List[DaycareCenter]:
        """
        Find daycare centers with at least the specified educators quality score.
        
        Args:
            min_score: Minimum educators quality score (1-5).
            
        Returns:
            List of matching daycare centers.
            
        Raises:
            ValueError: If min_score is not between 1 and 5.
        """
        if not 1 <= min_score <= 5:
            raise ValueError("Educators quality score must be between 1 and 5")
        return [center for center in self.daycare_centers if center.educators_quality_score >= min_score]
    
    def find_by_teaching_method(self, method: TeachingMethod) -> List[DaycareCenter]:
        """
        Find daycare centers that use the specified teaching method.
        
        Args:
            method: Teaching method to filter by.
            
        Returns:
            List of matching daycare centers.
        """
        return [center for center in self.daycare_centers if method in center.teaching_methods]
    
    def find_by_location(self, location: str) -> List[DaycareCenter]:
        """
        Find daycare centers in the specified location.
        
        Args:
            location: Location to filter by (case-insensitive).
            
        Returns:
            List of matching daycare centers.
        """
        return [center for center in self.daycare_centers if location.lower() in center.location.lower()]
    
    def get_all_centers(self) -> List[DaycareCenter]:
        """Get all daycare centers in the local cache."""
        return self.daycare_centers.copy()
    
    def get_center_details(self, name: str) -> Optional[DaycareCenter]:
        """
        Get details of a specific daycare center by name.
        
        Args:
            name: Name of the daycare center to find.
            
        Returns:
            The matching daycare center or None if not found.
        """
        for center in self.daycare_centers:
            if center.name.lower() == name.lower():
                return center
        return None
```
