"""
Generated Code Metadata:
========================
Original URL: https://rapala.tc
Prompt: Write a Python script to create a travel itinerary for a client based on their preferences, including destination, travel dates, and activities, similar to Rapala Travel Concierge's services.
Generated: DETERMINISTIC_8a6a0adc34e691e9
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
from datetime import datetime
from typing import Dict, List, Optional

class TravelItinerary:
    """
    A class to generate and manage travel itineraries based on client preferences.
    """
    
    def __init__(self):
        self.itinerary = {
            'client_info': {},
            'destinations': [],
            'travel_dates': {},
            'activities': [],
            'notes': '',
            'status': 'draft'
        }
    
    def set_client_info(self, name: str, email: str, phone: str, special_requests: Optional[str] = None) -> None:
        """
        Set client personal information and special requests.
        
        Args:
            name (str): Client's full name
            email (str): Client's email address
            phone (str): Client's phone number
            special_requests (str, optional): Any special requirements or requests
        """
        self.itinerary['client_info'] = {
            'name': name,
            'email': email,
            'phone': phone,
            'special_requests': special_requests or ''
        }
    
    def add_destination(self, city: str, country: str, duration_days: int) -> None:
        """
        Add a travel destination to the itinerary.
        
        Args:
            city (str): City name
            country (str): Country name
            duration_days (int): Number of days to spend at this destination
        """
        if duration_days <= 0:
            raise ValueError("Duration must be at least 1 day")
        
        self.itinerary['destinations'].append({
            'city': city,
            'country': country,
            'duration_days': duration_days
        })
    
    def set_travel_dates(self, start_date: str, end_date: str) -> None:
        """
        Set the travel date range for the itinerary.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            
        Raises:
            ValueError: If date format is invalid or end date is before start date
        """
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.strptime(end_date, '%Y-%m-%d')
            
            if end < start:
                raise ValueError("End date cannot be before start date")
            
            self.itinerary['travel_dates'] = {
                'start_date': start_date,
                'end_date': end_date
            }
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}. Please use YYYY-MM-DD")
    
    def add_activity(self, activity: str, location: str, date: str, notes: Optional[str] = None) -> None:
        """
        Add an activity to the itinerary.
        
        Args:
            activity (str): Description of the activity
            location (str): Where the activity takes place
            date (str): Date of the activity in YYYY-MM-DD format
            notes (str, optional): Additional notes about the activity
        """
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD")
        
        self.itinerary['activities'].append({
            'activity': activity,
            'location': location,
            'date': date,
            'notes': notes or ''
        })
    
    def add_notes(self, notes: str) -> None:
        """
        Add general notes to the itinerary.
        
        Args:
            notes (str): Additional information about the trip
        """
        self.itinerary['notes'] = notes
    
    def finalize_itinerary(self) -> None:
        """
        Mark the itinerary as finalized and ready for the client.
        """
        if not self.itinerary['destinations']:
            raise ValueError("Cannot finalize itinerary without destinations")
        if not self.itinerary['travel_dates']:
            raise ValueError("Cannot finalize itinerary without travel dates")
        
        self.itinerary['status'] = 'finalized'
    
    def get_itinerary(self) -> Dict:
        """
        Return the complete itinerary.
        
        Returns:
            Dict: The complete itinerary dictionary
        """
        return self.itinerary
    
    def save_to_file(self, filename: str) -> None:
        """
        Save the itinerary to a JSON file.
        
        Args:
            filename (str): Name of the file to save to
        """
        if not filename.endswith('.json'):
            filename += '.json'
        
        with open(filename, 'w') as f:
            json.dump(self.itinerary, f, indent=4)
    
    def load_from_file(self, filename: str) -> None:
        """
        Load an itinerary from a JSON file.
        
        Args:
            filename (str): Name of the file to load from
        """
        try:
            with open(filename, 'r') as f:
                self.itinerary = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON file format")

def create_sample_itinerary() -> TravelItinerary:
    """
    Create and return a sample itinerary for demonstration purposes.
    
    Returns:
        TravelItinerary: A populated itinerary object
    """
    itinerary = TravelItinerary()
    
    # Set client information
    itinerary.set_client_info(
        name="John Doe",
        email="john.doe@example.com",
        phone="+1234567890",
        special_requests="Vegetarian meals preferred"
    )
    
    # Add destinations
    itinerary.add_destination(city="Paris", country="France", duration_days=4)
    itinerary.add_destination(city="Rome", country="Italy", duration_days=3)
    
    # Set travel dates
    itinerary.set_travel_dates(start_date="2023-06-15", end_date="2023-06-22")
    
    # Add activities
    itinerary.add_activity(
        activity="Eiffel Tower visit",
        location="Paris, France",
        date="2023-06-16",
        notes="Guided tour at 10:00 AM"
    )
    itinerary.add_activity(
        activity="Louvre Museum",
        location="Paris, France",
        date="2023-06-17"
    )
    itinerary.add_activity(
        activity="Colosseum tour",
        location="Rome, Italy",
        date="2023-06-20",
        notes="Skip-the-line tickets"
    )
    
    # Add general notes
    itinerary.add_notes("Airport transfers included. Hotel reservations confirmed.")
    
    # Finalize itinerary
    itinerary.finalize_itinerary()
    
    return itinerary

if __name__ == "__main__":
    try:
        # Create and save a sample itinerary
        sample_itinerary = create_sample_itinerary()
        sample_itinerary.save_to_file("john_doe_europe_trip.json")
        
        print("Sample itinerary created and saved successfully!")
        print("Itinerary details:")
        print(json.dumps(sample_itinerary.get_itinerary(), indent=4))
    except Exception as e:
        print(f"Error creating itinerary: {e}")
```
