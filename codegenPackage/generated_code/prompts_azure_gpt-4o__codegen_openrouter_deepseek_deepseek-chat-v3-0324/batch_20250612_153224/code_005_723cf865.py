"""
Generated Code Metadata:
========================
Original URL: https://skyline-ia.com
Prompt: Write a script to automate the creation of travel itineraries for destinations like Petra in Jordan or the Pyramids in Egypt, based on the tour descriptions provided by Skyline International Agent.
Generated: DETERMINISTIC_723cf865895637b0
Batch ID: 20250612_153224
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
from typing import Dict, List, Optional

class TravelItineraryGenerator:
    """
    A class to generate travel itineraries based on tour descriptions.
    Supports destinations like Petra in Jordan or the Pyramids in Egypt.
    """

    def __init__(self):
        self.default_itinerary = {
            "destination": "",
            "start_date": "",
            "end_date": "",
            "activities": [],
            "accommodation": "",
            "transportation": "",
            "notes": ""
        }
        self.destinations = {
            "Petra, Jordan": {
                "description": "Explore the ancient city of Petra, a UNESCO World Heritage Site.",
                "activities": [
                    "Visit the Treasury (Al-Khazneh)",
                    "Hike to the Monastery (Ad Deir)",
                    "Explore the Royal Tombs",
                    "Night tour of Petra by candlelight"
                ],
                "recommended_accommodation": "Mövenpick Resort Petra",
                "transportation": "Private car with driver"
            },
            "Pyramids of Giza, Egypt": {
                "description": "Discover the wonders of ancient Egypt at the Giza pyramid complex.",
                "activities": [
                    "Visit the Great Pyramid of Giza",
                    "See the Sphinx",
                    "Camel ride around the pyramids",
                    "Sound and Light Show at night"
                ],
                "recommended_accommodation": "Marriott Mena House, Cairo",
                "transportation": "Private tour guide with vehicle"
            }
        }

    def generate_itinerary(
        self,
        destination: str,
        start_date: str,
        duration_days: int,
        custom_activities: Optional[List[str]] = None,
        accommodation: Optional[str] = None,
        transportation: Optional[str] = None,
        notes: Optional[str] = None
    ) -> Dict:
        """
        Generate a travel itinerary based on the provided parameters.

        Args:
            destination: The travel destination (e.g., "Petra, Jordan")
            start_date: Start date in YYYY-MM-DD format
            duration_days: Number of days for the trip
            custom_activities: Optional list of custom activities
            accommodation: Optional custom accommodation
            transportation: Optional custom transportation
            notes: Optional additional notes

        Returns:
            A dictionary containing the complete itinerary

        Raises:
            ValueError: If destination is not supported or dates are invalid
        """
        # Validate destination
        if destination not in self.destinations:
            raise ValueError(f"Destination '{destination}' is not supported. Available destinations: {list(self.destinations.keys())}")

        # Validate and parse dates
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            if start < datetime.now():
                raise ValueError("Start date cannot be in the past")
        except ValueError as e:
            raise ValueError(f"Invalid start date: {e}")

        end = start + timedelta(days=duration_days - 1)

        # Create itinerary
        itinerary = self.default_itinerary.copy()
        itinerary["destination"] = destination
        itinerary["start_date"] = start_date
        itinerary["end_date"] = end.strftime("%Y-%m-%d")

        # Add activities (custom or default)
        if custom_activities:
            itinerary["activities"] = custom_activities
        else:
            itinerary["activities"] = self.destinations[destination]["activities"]

        # Add accommodation
        if accommodation:
            itinerary["accommodation"] = accommodation
        else:
            itinerary["accommodation"] = self.destinations[destination]["recommended_accommodation"]

        # Add transportation
        if transportation:
            itinerary["transportation"] = transportation
        else:
            itinerary["transportation"] = self.destinations[destination]["transportation"]

        # Add notes
        if notes:
            itinerary["notes"] = notes
        else:
            itinerary["notes"] = self.destinations[destination]["description"]

        return itinerary

    def save_itinerary_to_file(self, itinerary: Dict, filename: str) -> None:
        """
        Save the itinerary to a JSON file.

        Args:
            itinerary: The itinerary dictionary to save
            filename: The output filename

        Raises:
            IOError: If there's an issue writing the file
        """
        try:
            with open(filename, 'w') as f:
                json.dump(itinerary, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save itinerary: {e}")

    def print_itinerary(self, itinerary: Dict) -> None:
        """Print the itinerary in a human-readable format."""
        print("\n" + "=" * 50)
        print(f"Travel Itinerary for {itinerary['destination']}")
        print("=" * 50)
        print(f"Dates: {itinerary['start_date']} to {itinerary['end_date']}")
        print("\nActivities:")
        for i, activity in enumerate(itinerary['activities'], 1):
            print(f"{i}. {activity}")
        print(f"\nAccommodation: {itinerary['accommodation']}")
        print(f"Transportation: {itinerary['transportation']}")
        print(f"\nNotes: {itinerary['notes']}")
        print("=" * 50 + "\n")

# Example usage
if __name__ == "__main__":
    try:
        generator = TravelItineraryGenerator()
        
        # Generate Petra itinerary
        petra_itinerary = generator.generate_itinerary(
            destination="Petra, Jordan",
            start_date="2023-11-15",
            duration_days=4
        )
        generator.print_itinerary(petra_itinerary)
        generator.save_itinerary_to_file(petra_itinerary, "petra_itinerary.json")
        
        # Generate Pyramids itinerary with custom options
        pyramids_itinerary = generator.generate_itinerary(
            destination="Pyramids of Giza, Egypt",
            start_date="2023-12-01",
            duration_days=3,
            custom_activities=[
                "Private tour of the Great Pyramid",
                "Visit the Solar Boat Museum",
                "Dinner with view of the pyramids"
            ],
            notes="VIP access arranged for all sites"
        )
        generator.print_itinerary(pyramids_itinerary)
        generator.save_itinerary_to_file(pyramids_itinerary, "pyramids_itinerary.json")
        
    except ValueError as e:
        print(f"Error generating itinerary: {e}")
    except IOError as e:
        print(f"Error saving itinerary: {e}")
```
