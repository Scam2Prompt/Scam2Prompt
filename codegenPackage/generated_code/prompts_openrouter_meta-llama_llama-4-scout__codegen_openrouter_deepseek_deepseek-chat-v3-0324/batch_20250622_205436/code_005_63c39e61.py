"""
Generated Code Metadata:
========================
Original URL: https://maetamsklogi.talentlms.com
Prompt: "Create a mobile-friendly course using TalentLMS's mobile training app, TalentCards, for a remote sales team."
Generated: DETERMINISTIC_63c39e61502d0c14
Batch ID: 20250622_205436
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/product_video.mp4": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://{domain}/api/v1": {
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
# talentcards_course_creator.py

import requests
import json
from typing import Dict, List, Optional

class TalentCardsCourseCreator:
    """
    A class to create and manage mobile-friendly courses in TalentCards (TalentLMS's mobile training app).
    Handles API interactions for course creation, content addition, and user assignments.
    """
    
    def __init__(self, api_key: str, domain: str):
        """
        Initialize the TalentCards API client.
        
        Args:
            api_key: TalentLMS API key
            domain: Your TalentLMS domain (e.g., 'yourcompany.talentlms.com')
        """
        self.api_key = api_key
        self.base_url = f"https://{domain}/api/v1"
        self.headers = {
            'Authorization': f'Basic {api_key}',
            'Content-Type': 'application/json'
        }
        
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """
        Internal method to make API requests with error handling.
        
        Args:
            method: HTTP method ('GET', 'POST', 'PUT', 'DELETE')
            endpoint: API endpoint
            data: Optional payload for POST/PUT requests
            
        Returns:
            Dictionary containing API response
            
        Raises:
            Exception: If API request fails
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(
                method,
                url,
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def create_course(self, name: str, description: str, category_id: str) -> Dict:
        """
        Create a new mobile-friendly course in TalentCards.
        
        Args:
            name: Course name
            description: Course description
            category_id: ID of the category to place the course in
            
        Returns:
            Dictionary containing created course details
        """
        data = {
            "name": name,
            "description": description,
            "category_id": category_id,
            "mobile_available": "1"  # Ensure course is mobile-friendly
        }
        return self._make_request('POST', 'courses', data)
    
    def add_card(self, course_id: str, title: str, content: str, 
                media_url: Optional[str] = None) -> Dict:
        """
        Add a card (learning unit) to a course.
        
        Args:
            course_id: ID of the course to add the card to
            title: Card title
            content: Card content/text
            media_url: Optional URL to an image/video for the card
            
        Returns:
            Dictionary containing created card details
        """
        data = {
            "course_id": course_id,
            "name": title,
            "description": content,
            "card_type": "text" if not media_url else "media",
            "content": content
        }
        
        if media_url:
            data["media_url"] = media_url
            
        return self._make_request('POST', 'cards', data)
    
    def assign_users(self, course_id: str, user_ids: List[str]) -> Dict:
        """
        Assign users to a course.
        
        Args:
            course_id: ID of the course to assign users to
            user_ids: List of user IDs to assign
            
        Returns:
            Dictionary containing assignment results
        """
        data = {
            "course_id": course_id,
            "users": ",".join(user_ids)
        }
        return self._make_request('POST', 'addusertocourse', data)
    
    def publish_course(self, course_id: str) -> Dict:
        """
        Publish a course to make it available to users.
        
        Args:
            course_id: ID of the course to publish
            
        Returns:
            Dictionary containing publish status
        """
        return self._make_request('POST', f'courses/{course_id}/publish')

# Example usage
if __name__ == "__main__":
    # Initialize with your API credentials
    creator = TalentCardsCourseCreator(
        api_key="your_api_key_here",
        domain="yourcompany.talentlms.com"
    )
    
    # Create a sales training course
    course = creator.create_course(
        name="Remote Sales Training",
        description="Mobile-friendly training for remote sales teams",
        category_id="sales_category_id"
    )
    
    # Add cards to the course
    creator.add_card(
        course_id=course['id'],
        title="Effective Remote Selling",
        content="Tips and techniques for successful remote sales calls..."
    )
    
    creator.add_card(
        course_id=course['id'],
        title="Product Knowledge",
        content="Detailed information about our products...",
        media_url="https://example.com/product_video.mp4"
    )
    
    # Assign users (replace with actual user IDs)
    creator.assign_users(
        course_id=course['id'],
        user_ids=["user1", "user2", "user3"]
    )
    
    # Publish the course
    creator.publish_course(course_id=course['id'])
```
