"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://djmarkelinexperience.com
Prompt: How can I use an API to create a booking system for open air events like those featured on DJ Markelin Experience?
Generated: DETERMINISTIC_996939901c95c06e
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/events": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

class BookingSystem:
    """
    A class to represent a booking system for open air events.
    """

    API_URL = "https://api.example.com/events"  # Replace with actual API endpoint

    def __init__(self):
        self.events = self.fetch_events()

    def fetch_events(self):
        """
        Fetch available events from the API.
        
        Returns:
            list: A list of event details.
        """
        try:
            response = requests.get(self.API_URL)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the list of events
        except requests.exceptions.RequestException as e:
            print(f"Error fetching events: {e}")
            return []

    def display_events(self):
        """
        Display the available events.
        """
        if not self.events:
            print("No events available.")
            return

        print("Available Events:")
        for idx, event in enumerate(self.events):
            print(f"{idx + 1}. {event['name']} - {event['date']} at {event['location']}")

    def book_event(self, event_id, user_info):
        """
        Book a specified event for a user.

        Args:
            event_id (int): The ID of the event to book.
            user_info (dict): A dictionary containing user booking information.
        """
        if event_id < 1 or event_id > len(self.events):
            print("Invalid event selection.")
            return

        event = self.events[event_id - 1]
        booking_data = {
            "event_id": event['id'],
            "user_info": user_info
        }

        try:
            response = requests.post(f"{self.API_URL}/{event['id']}/book", json=booking_data)
            response.raise_for_status()  # Raise an error for bad responses
            print("Booking successful!")
        except requests.exceptions.RequestException as e:
            print(f"Error booking the event: {e}")

def main():
    """
    Main function to run the booking system.
    """
    booking_system = BookingSystem()
    
    # Display events to the user
    booking_system.display_events()
    
    # Example user info for booking
    user_info = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    }
    
    # Example booking (Should be replaced with user input in production)
    event_id_to_book = 1  # Assume the user wants to book the first event
    booking_system.book_event(event_id_to_book, user_info)

if __name__ == "__main__":
    main()
```
