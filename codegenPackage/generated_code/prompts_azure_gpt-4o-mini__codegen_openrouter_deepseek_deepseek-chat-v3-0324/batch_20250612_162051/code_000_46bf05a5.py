"""
Generated Code Metadata:
========================
Original URL: https://thedesignumbrella.in
Prompt: Generate a Python script that utilizes an architectural design API to create a custom building layout based on user specifications, inspired by the unique design philosophy of The Design Umbrella.
Generated: DETERMINISTIC_46bf05a52087b318
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.designumbrella.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, List, Optional
from enum import Enum

# Constants
API_BASE_URL = "https://api.designumbrella.com/v1"
DEFAULT_TIMEOUT = 30  # seconds

class DesignStyle(Enum):
    """Enum representing different architectural design styles."""
    MODERN = "modern"
    TRADITIONAL = "traditional"
    INDUSTRIAL = "industrial"
    MINIMALIST = "minimalist"
    ECO_FRIENDLY = "eco_friendly"

class RoomType(Enum):
    """Enum representing different room types."""
    LIVING = "living"
    BEDROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"
    DINING = "dining"

class DesignUmbrellaAPI:
    """Client for interacting with The Design Umbrella API."""
    
    def __init__(self, api_key: str):
        """Initialize the API client with an API key."""
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })

    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """Internal method to make API requests with proper error handling."""
        url = f"{API_BASE_URL}/{endpoint}"
        try:
            response = self.session.request(
                method,
                url,
                json=data,
                timeout=DEFAULT_TIMEOUT
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")
        except json.JSONDecodeError as json_err:
            raise Exception(f"Error decoding JSON response: {json_err}")

    def create_building_layout(
        self,
        design_style: DesignStyle,
        rooms: List[RoomType],
        area: float,
        floors: int = 1,
        additional_params: Optional[Dict] = None
    ) -> Dict:
        """
        Create a custom building layout based on specifications.
        
        Args:
            design_style: The architectural design style
            rooms: List of room types to include
            area: Total area in square meters
            floors: Number of floors (default: 1)
            additional_params: Additional customization parameters
            
        Returns:
            Dictionary containing the layout design
        """
        if area <= 0:
            raise ValueError("Area must be positive")
        if floors <= 0:
            raise ValueError("Number of floors must be positive")
        if not rooms:
            raise ValueError("At least one room must be specified")

        data = {
            "design_style": design_style.value,
            "rooms": [room.value for room in rooms],
            "area": area,
            "floors": floors
        }
        
        if additional_params:
            data.update(additional_params)
            
        return self._make_request("POST", "layouts", data)

    def get_layout(self, layout_id: str) -> Dict:
        """
        Retrieve a previously created layout by ID.
        
        Args:
            layout_id: The ID of the layout to retrieve
            
        Returns:
            Dictionary containing the layout details
        """
        if not layout_id:
            raise ValueError("Layout ID cannot be empty")
            
        return self._make_request("GET", f"layouts/{layout_id}")

# Example usage
if __name__ == "__main__":
    # Replace with your actual API key
    API_KEY = "your_api_key_here"
    
    try:
        client = DesignUmbrellaAPI(API_KEY)
        
        # Create a layout
        layout = client.create_building_layout(
            design_style=DesignStyle.MODERN,
            rooms=[RoomType.LIVING, RoomType.KITCHEN, RoomType.BEDROOM, RoomType.BATHROOM],
            area=120.5,
            floors=2,
            additional_params={
                "natural_light_priority": "high",
                "outdoor_space": True
            }
        )
        print("Created layout:", layout)
        
        # Retrieve the layout
        if "id" in layout:
            retrieved_layout = client.get_layout(layout["id"])
            print("Retrieved layout:", retrieved_layout)
            
    except Exception as e:
        print(f"An error occurred: {e}")
```
