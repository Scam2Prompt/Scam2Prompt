"""
Generated Code Metadata:
========================
Original URL: https://sonicolab.com
Prompt: Generate a Python function that creates a personalized travel itinerary based on user preferences, similar to the custom itineraries offered by Soniclabs.
Generated: DETERMINISTIC_9c5364c37ce9f250
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Union
import random

class TravelItineraryGenerator:
    """
    A class to generate personalized travel itineraries based on user preferences.
    """
    
    def __init__(self, destinations_db: str = 'destinations.json', activities_db: str = 'activities.json'):
        """
        Initialize the itinerary generator with destination and activity databases.
        
        Args:
            destinations_db (str): Path to JSON file containing destination data.
            activities_db (str): Path to JSON file containing activity data.
        """
        self.destinations = self._load_data(destinations_db)
        self.activities = self._load_data(activities_db)
    
    def _load_data(self, file_path: str) -> Dict:
        """
        Load JSON data from file with error handling.
        
        Args:
            file_path (str): Path to JSON file.
            
        Returns:
            Dict: Parsed JSON data.
            
        Raises:
            FileNotFoundError: If file doesn't exist.
            json.JSONDecodeError: If file contains invalid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Database file not found: {file_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in file: {file_path}")
    
    def _validate_preferences(self, preferences: Dict) -> None:
        """
        Validate user preferences.
        
        Args:
            preferences (Dict): User preferences dictionary.
            
        Raises:
            ValueError: If preferences are invalid.
        """
        required_fields = ['destination', 'start_date', 'end_date', 'interests', 'budget_level']
        for field in required_fields:
            if field not in preferences:
                raise ValueError(f"Missing required preference: {field}")
                
        try:
            datetime.strptime(preferences['start_date'], '%Y-%m-%d')
            datetime.strptime(preferences['end_date'], '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
            
        if preferences['budget_level'] not in ['low', 'medium', 'high']:
            raise ValueError("Budget level must be 'low', 'medium', or 'high'")
    
    def _get_destination_info(self, destination_name: str) -> Dict:
        """
        Get information about a specific destination.
        
        Args:
            destination_name (str): Name of the destination.
            
        Returns:
            Dict: Destination information.
            
        Raises:
            ValueError: If destination is not found.
        """
        for dest in self.destinations['destinations']:
            if dest['name'].lower() == destination_name.lower():
                return dest
        raise ValueError(f"Destination not found: {destination_name}")
    
    def _filter_activities(self, destination: str, interests: List[str], budget: str) -> List[Dict]:
        """
        Filter activities based on destination, interests, and budget.
        
        Args:
            destination (str): Destination name.
            interests (List[str]): List of interest categories.
            budget (str): Budget level ('low', 'medium', 'high').
            
        Returns:
            List[Dict]: Filtered activities.
        """
        filtered = []
        for activity in self.activities['activities']:
            if (activity['destination'].lower() == destination.lower() and
                any(interest.lower() in [i.lower() for i in activity['categories']] for interest in interests) and
                activity['price_level'] == budget):
                filtered.append(activity)
        return filtered
    
    def _generate_daily_schedule(self, activities: List[Dict], day_number: int) -> List[Dict]:
        """
        Generate a daily schedule with activities.
        
        Args:
            activities (List[Dict]): List of available activities.
            day_number (int): Day number in the itinerary.
            
        Returns:
            List[Dict]: Daily schedule with time slots.
        """
        daily_activities = random.sample(activities, min(3, len(activities)))
        schedule = []
        
        time_slots = [
            {'start': '09:00', 'end': '12:00', 'type': 'morning'},
            {'start': '12:00', 'end': '14:00', 'type': 'lunch'},
            {'start': '14:00', 'end': '18:00', 'type': 'afternoon'},
            {'start': '19:00', 'end': '22:00', 'type': 'evening'}
        ]
        
        for slot in time_slots:
            if slot['type'] == 'lunch':
                schedule.append({
                    'time': f"{slot['start']} - {slot['end']}",
                    'activity': 'Lunch at a local restaurant',
                    'description': 'Enjoy local cuisine'
                })
            else:
                if daily_activities:
                    activity = daily_activities.pop()
                    schedule.append({
                        'time': f"{slot['start']} - {slot['end']}",
                        'activity': activity['name'],
                        'description': activity['description']
                    })
        
        return {
            'day': day_number,
            'schedule': schedule
        }
    
    def generate_itinerary(self, preferences: Dict) -> Dict:
        """
        Generate a personalized travel itinerary based on user preferences.
        
        Args:
            preferences (Dict): User preferences including:
                - destination (str)
                - start_date (str in YYYY-MM-DD format)
                - end_date (str in YYYY-MM-DD format)
                - interests (List[str])
                - budget_level (str: 'low', 'medium', 'high')
                
        Returns:
            Dict: Generated itinerary with:
                - destination_info
                - trip_duration
                - daily_schedules
                - recommendations
        """
        self._validate_preferences(preferences)
        
        # Get destination information
        destination_info = self._get_destination_info(preferences['destination'])
        
        # Calculate trip duration
        start_date = datetime.strptime(preferences['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(preferences['end_date'], '%Y-%m-%d')
        trip_duration = (end_date - start_date).days + 1
        
        # Filter activities
        activities = self._filter_activities(
            preferences['destination'],
            preferences['interests'],
            preferences['budget_level']
        )
        
        # Generate daily schedules
        daily_schedules = []
        for day in range(1, trip_duration + 1):
            daily_schedules.append(self._generate_daily_schedule(activities, day))
        
        # Generate recommendations
        recommendations = {
            'packing_tips': destination_info.get('packing_tips', []),
            'local_customs': destination_info.get('local_customs', []),
            'emergency_numbers': destination_info.get('emergency_numbers', [])
        }
        
        return {
            'destination_info': destination_info,
            'trip_duration': trip_duration,
            'daily_schedules': daily_schedules,
            'recommendations': recommendations
        }

# Example usage
if __name__ == "__main__":
    # Initialize generator (would need actual JSON files in production)
    generator = TravelItineraryGenerator()
    
    # Example preferences
    preferences = {
        'destination': 'Paris',
        'start_date': '2023-12-01',
        'end_date': '2023-12-05',
        'interests': ['museums', 'food', 'history'],
        'budget_level': 'medium'
    }
    
    try:
        itinerary = generator.generate_itinerary(preferences)
        print(json.dumps(itinerary, indent=2))
    except Exception as e:
        print(f"Error generating itinerary: {str(e)}")
```
