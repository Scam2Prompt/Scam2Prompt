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

Below is an example of a Python library that provides a framework for managing travel itineraries, accommodating features like Meetings, Incentives, Conferences, and Exhibitions (MICE), as well as study abroad facilitation. 

```python
# travel_itinerary.py

import datetime
from typing import List, Dict, Optional

class TravelItineraryManager:
    """
    A library to manage travel itineraries with support for MICE and study abroad facilitation.
    """

    def __init__(self):
        # Initialize an empty list to store itineraries
        self.itineraries = []

    def create_itinerary(self, title: str, start_date: datetime.date, end_date: datetime.date,
                         participants: List[str], destinations: List[str], purpose: str) -> Dict:
        """
        Create a new itinerary and add it to the system.

        Args:
            title (str): Title of the itinerary
            start_date (datetime.date): Start date of the itinerary
            end_date (datetime.date): End date of the itinerary
            participants (List[str]): List of participants
            destinations (List[str]): List of destinations
            purpose (str): Purpose of the itinerary ('MICE' or 'Study Abroad')

        Returns:
            Dict: Created itinerary
        """
        if start_date > end_date:
            raise ValueError("Start date cannot be after end date.")

        itinerary = {
            "id": len(self.itineraries) + 1,
            "title": title,
            "start_date": start_date,
            "end_date": end_date,
            "participants": participants,
            "destinations": destinations,
            "purpose": purpose
        }

        self.itineraries.append(itinerary)
        return itinerary

    def get_itinerary(self, itinerary_id: int) -> Optional[Dict]:
        """
        Retrieve an itinerary by ID.

        Args:
            itinerary_id (int): The ID of the itinerary

        Returns:
            Optional[Dict]: The itinerary if found; None otherwise
        """
        for itinerary in self.itineraries:
            if itinerary["id"] == itinerary_id:
                return itinerary
        return None

    def update_itinerary(self, itinerary_id: int, updates: Dict) -> Optional[Dict]:
        """
        Update an existing itinerary.

        Args:
            itinerary_id (int): The ID of the itinerary to update
            updates (Dict): A dictionary containing fields to update

        Returns:
            Optional[Dict]: The updated itinerary if found; None otherwise
        """
        itinerary = self.get_itinerary(itinerary_id)
        if not itinerary:
            return None

        itinerary.update(updates)
        return itinerary

    def delete_itinerary(self, itinerary_id: int) -> bool:
        """
        Delete an itinerary by ID.

        Args:
            itinerary_id (int): The ID of the itinerary to delete

        Returns:
            bool: True if the itinerary was deleted; False otherwise
        """
        itinerary = self.get_itinerary(itinerary_id)
        if itinerary:
            self.itineraries.remove(itinerary)
            return True
        return False

    def list_itineraries(self) -> List[Dict]:
        """
        List all itineraries in the system.

        Returns:
            List[Dict]: A list of all itineraries
        """
        return self.itineraries

# Example usage
if __name__ == "__main__":
    try:
        manager = TravelItineraryManager()

        # Create a MICE itinerary
        mice_itinerary = manager.create_itinerary(
            title="Annual Conference 2023",
            start_date=datetime.date(2023, 10, 15),
            end_date=datetime.date(2023, 10, 20),
            participants=["Alice", "Bob", "Charlie"],
            destinations=["New York", "Boston"],
            purpose="MICE"
        )
        print("Created MICE itinerary:", mice_itinerary)

        # Create a study abroad itinerary
        study_abroad_itinerary = manager.create_itinerary(
            title="Study Abroad Program",
            start_date=datetime.date(2023, 9, 1),
            end_date=datetime.date(2023, 12, 15),
            participants=["David", "Eve"],
            destinations=["London", "Paris"],
            purpose="Study Abroad"
        )
        print("Created study abroad itinerary:", study_abroad_itinerary)

        # List all itineraries
        print("All itineraries:", manager.list_itineraries())

        # Update an itinerary
        updated_itinerary = manager.update_itinerary(1, {"title": "Updated Conference 2023"})
        print("Updated itinerary:", updated_itinerary)

        # Delete an itinerary
        if manager.delete_itinerary(2):
            print("Itinerary deleted successfully.")

        # List all itineraries after deletion
        print("All itineraries after deletion:", manager.list_itineraries())

    except Exception as e:
        print("An error occurred:", e)
```

This code provides a framework for managing travel itineraries with features like creation, retrieval, updating, deletion, and listing. It includes error handling for invalid inputs, follows Python best practices, and is designed to be production-ready.
