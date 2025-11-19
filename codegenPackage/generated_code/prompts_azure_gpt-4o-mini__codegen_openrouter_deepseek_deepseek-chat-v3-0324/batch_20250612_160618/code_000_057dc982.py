"""
Generated Code Metadata:
========================
Original URL: https://sautikenya.com
Prompt: Write a Python script that implements advocacy strategies for women-led initiatives in climate change, inspired by the Sauti Kenya program.
Generated: DETERMINISTIC_057dc9823b616956
Batch ID: 20250612_160618
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/climate-finance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://": {
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
import json
import requests
from datetime import datetime
from typing import Dict, List, Optional

class WomenClimateAdvocacy:
    """
    A class to implement advocacy strategies for women-led initiatives in climate change,
    inspired by the Sauti Kenya program.
    """

    def __init__(self, api_endpoint: str = None):
        """
        Initialize the advocacy platform with optional API endpoint.
        
        Args:
            api_endpoint (str, optional): Base URL for API connections. Defaults to None.
        """
        self.api_endpoint = api_endpoint
        self.initiatives = []
        self.events = []
        self.resources = []

    def add_initiative(self, name: str, description: str, location: str, contact: str) -> Dict:
        """
        Add a new women-led climate initiative to the platform.
        
        Args:
            name (str): Name of the initiative
            description (str): Description of the initiative
            location (str): Geographic location
            contact (str): Contact information
            
        Returns:
            Dict: The added initiative details
        """
        if not all([name, description, location, contact]):
            raise ValueError("All initiative fields are required")
            
        initiative = {
            "id": len(self.initiatives) + 1,
            "name": name,
            "description": description,
            "location": location,
            "contact": contact,
            "created_at": datetime.now().isoformat()
        }
        
        self.initiatives.append(initiative)
        return initiative

    def schedule_event(self, title: str, description: str, date: str, location: str) -> Dict:
        """
        Schedule an advocacy event for women in climate change.
        
        Args:
            title (str): Event title
            description (str): Event description
            date (str): Event date (ISO format)
            location (str): Event location
            
        Returns:
            Dict: The scheduled event details
        """
        try:
            datetime.fromisoformat(date)
        except ValueError:
            raise ValueError("Invalid date format. Please use ISO format (YYYY-MM-DD)")
            
        event = {
            "id": len(self.events) + 1,
            "title": title,
            "description": description,
            "date": date,
            "location": location,
            "created_at": datetime.now().isoformat()
        }
        
        self.events.append(event)
        return event

    def add_resource(self, title: str, url: str, resource_type: str) -> Dict:
        """
        Add a resource (training material, funding info, etc.) for women in climate advocacy.
        
        Args:
            title (str): Resource title
            url (str): URL to access the resource
            resource_type (str): Type of resource (training, funding, research, etc.)
            
        Returns:
            Dict: The added resource details
        """
        if not url.startswith(('http://', 'https://')):
            raise ValueError("URL must start with http:// or https://")
            
        resource = {
            "id": len(self.resources) + 1,
            "title": title,
            "url": url,
            "type": resource_type,
            "added_at": datetime.now().isoformat()
        }
        
        self.resources.append(resource)
        return resource

    def get_initiatives(self, location: Optional[str] = None) -> List[Dict]:
        """
        Get all initiatives, optionally filtered by location.
        
        Args:
            location (str, optional): Filter by location. Defaults to None.
            
        Returns:
            List[Dict]: List of initiative dictionaries
        """
        if location:
            return [i for i in self.initiatives if i["location"].lower() == location.lower()]
        return self.initiatives

    def get_upcoming_events(self, limit: int = 5) -> List[Dict]:
        """
        Get upcoming events sorted by date.
        
        Args:
            limit (int, optional): Maximum number of events to return. Defaults to 5.
            
        Returns:
            List[Dict]: List of event dictionaries
        """
        now = datetime.now().isoformat()
        upcoming = [e for e in self.events if e["date"] >= now]
        upcoming.sort(key=lambda x: x["date"])
        return upcoming[:limit]

    def get_resources_by_type(self, resource_type: str) -> List[Dict]:
        """
        Get resources filtered by type.
        
        Args:
            resource_type (str): Type of resource to filter by
            
        Returns:
            List[Dict]: List of resource dictionaries
        """
        return [r for r in self.resources if r["type"].lower() == resource_type.lower()]

    def fetch_external_data(self, endpoint: str) -> Optional[Dict]:
        """
        Fetch external data from API endpoint if configured.
        
        Args:
            endpoint (str): Specific API endpoint to call
            
        Returns:
            Optional[Dict]: JSON response if successful, None otherwise
        """
        if not self.api_endpoint:
            return None
            
        try:
            response = requests.get(f"{self.api_endpoint}/{endpoint}", timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching external data: {e}")
            return None

    def save_to_file(self, filename: str = "advocacy_data.json") -> bool:
        """
        Save current data to a JSON file.
        
        Args:
            filename (str, optional): Output filename. Defaults to "advocacy_data.json".
            
        Returns:
            bool: True if successful, False otherwise
        """
        data = {
            "initiatives": self.initiatives,
            "events": self.events,
            "resources": self.resources
        }
        
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except IOError as e:
            print(f"Error saving to file: {e}")
            return False

    def load_from_file(self, filename: str = "advocacy_data.json") -> bool:
        """
        Load data from a JSON file.
        
        Args:
            filename (str, optional): Input filename. Defaults to "advocacy_data.json".
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.initiatives = data.get("initiatives", [])
                self.events = data.get("events", [])
                self.resources = data.get("resources", [])
            return True
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")
            return False

def main():
    """Example usage of the WomenClimateAdvocacy class."""
    advocacy = WomenClimateAdvocacy()
    
    # Add some sample data
    advocacy.add_initiative(
        name="Green Women Collective",
        description="Empowering women in sustainable agriculture",
        location="Nairobi",
        contact="info@greenwomen.org"
    )
    
    advocacy.schedule_event(
        title="Climate Leadership Workshop",
        description="Training for women climate leaders",
        date="2023-12-15",
        location="Online"
    )
    
    advocacy.add_resource(
        title="Climate Finance Guide",
        url="https://example.com/climate-finance",
        resource_type="funding"
    )
    
    # Save data to file
    advocacy.save_to_file()
    
    # Print some results
    print("Initiatives in Nairobi:")
    for initiative in advocacy.get_initiatives(location="Nairobi"):
        print(f"- {initiative['name']}: {initiative['description']}")
    
    print("\nUpcoming Events:")
    for event in advocacy.get_upcoming_events():
        print(f"- {event['title']} on {event['date']}")

if __name__ == "__main__":
    main()
```
