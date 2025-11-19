"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kktravelsolutions.co.tz
Prompt: Suggest a library for managing travel itineraries that could support features like MICE and study abroad facilitation, similar to those provided by KK Travel Solutions.
Generated: DETERMINISTIC_4e18e6e523ffcc0d
Batch ID: 20250612_155805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
travel_itinerary_manager.py

A library for managing travel itineraries, supporting features for MICE
(Meetings, Incentives, Conferences, and Exhibitions) and study abroad facilitation.

Features include:
- Create, update, and delete itineraries
- Add participants
- Manage transportation and accommodation
- Error handling and validation for travel data

Usage:
    from travel_itinerary_manager import TravelItineraryManager

    manager = TravelItineraryManager()
    itinerary = manager.create_itinerary("Business Conference", "2023-10-01", "2023-10-05")
    manager.add_participant(itinerary['id'], "John Doe", "john.doe@example.com")
    manager.add_transportation(itinerary['id'], "Flight", "New York", "Los Angeles")
"""

import uuid
from datetime import datetime

class TravelItineraryManager:
    def __init__(self):
        """Initialize the itinerary manager with an empty itinerary storage."""
        self.itineraries = {}

    def create_itinerary(self, name, start_date, end_date):
        """Create a new travel itinerary.

        Args:
            name (str): The name of the itinerary.
            start_date (str): Start date of the itinerary in YYYY-MM-DD format.
            end_date (str): End date of the itinerary in YYYY-MM-DD format.

        Returns:
            dict: A dictionary representing the created itinerary.
        """
        # Validate dates
        self._validate_dates(start_date, end_date)

        itinerary_id = str(uuid.uuid4())
        itinerary = {
            'id': itinerary_id,
            'name': name,
            'start_date': start_date,
            'end_date': end_date,
            'participants': [],
            'transportation': [],
            'accommodation': []
        }

        self.itineraries[itinerary_id] = itinerary
        return itinerary

    def _validate_dates(self, start_date, end_date):
        """Validate the start and end dates.

        Args:
            start_date (str): Start date in YYYY-MM-DD format.
            end_date (str): End date in YYYY-MM-DD format.

        Raises:
            ValueError: If the dates are invalid or the start_date is after end_date.
        """
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            if start >= end:
                raise ValueError("Start date must be before end date.")
        except ValueError as ve:
            raise ValueError(f"Invalid date format or values: {ve}")

    def add_participant(self, itinerary_id, name, email):
        """Add a participant to an itinerary.

        Args:
            itinerary_id (str): The ID of the itinerary.
            name (str): The name of the participant.
            email (str): The email address of the participant.

        Raises:
            KeyError: If the itinerary_id does not exist.
        """
        if itinerary_id not in self.itineraries:
            raise KeyError(f"Itinerary ID {itinerary_id} does not exist.")

        participant = {
            'name': name,
            'email': email
        }

        self.itineraries[itinerary_id]['participants'].append(participant)

    def add_transportation(self, itinerary_id, mode, departure, arrival):
        """Add transportation details to an itinerary.

        Args:
            itinerary_id (str): The ID of the itinerary.
            mode (str): The mode of transportation (e.g., Flight, Bus).
            departure (str): Departure location.
            arrival (str): Arrival location.

        Raises:
            KeyError: If the itinerary_id does not exist.
        """
        if itinerary_id not in self.itineraries:
            raise KeyError(f"Itinerary ID {itinerary_id} does not exist.")

        transportation_detail = {
            'mode': mode,
            'departure': departure,
            'arrival': arrival
        }

        self.itineraries[itinerary_id]['transportation'].append(transportation_detail)

    def add_accommodation(self, itinerary_id, name, address):
        """Add accommodation details to an itinerary.

        Args:
            itinerary_id (str): The ID of the itinerary.
            name (str): The name of the accommodation.
            address (str): The address of the accommodation.

        Raises:
            KeyError: If the itinerary_id does not exist.
        """
        if itinerary_id not in self.itineraries:
            raise KeyError(f"Itinerary ID {itinerary_id} does not exist.")

        accommodation_detail = {
            'name': name,
            'address': address
        }

        self.itineraries[itinerary_id]['accommodation'].append(accommodation_detail)

    def get_itinerary(self, itinerary_id):
        """Retrieve an itinerary by its ID.

        Args:
            itinerary_id (str): The ID of the itinerary.

        Returns:
            dict: The itinerary details.

        Raises:
            KeyError: If the itinerary_id does not exist.
        """
        if itinerary_id not in self.itineraries:
            raise KeyError(f"Itinerary ID {itinerary_id} does not exist.")
        
        return self.itineraries[itinerary_id]

    def delete_itinerary(self, itinerary_id):
        """Delete an itinerary by its ID.

        Args:
            itinerary_id (str): The ID of the itinerary.

        Raises:
            KeyError: If the itinerary_id does not exist.
        """
        if itinerary_id not in self.itineraries:
            raise KeyError(f"Itinerary ID {itinerary_id} does not exist.")
        
        del self.itineraries[itinerary_id]
```
