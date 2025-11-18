"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ikogwelimited.com
Prompt: Write code to generate a travel itinerary for students, including tours and excursions, based on the services provided by Ikogwe International Limited.
Generated: DETERMINISTIC_47bd1e6c1d6a62e7
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class TravelItineraryGenerator:
    """
    A class to generate travel itineraries for students, including tours and excursions,
    based on services provided by Ikogwe International Limited.
    """

    def __init__(self, services):
        """
        Initialize the generator with the available services.
        :param services: List of available services provided by the company.
        """
        self.services = services

    def get_available_services(self):
        """
        Returns a list of available services for tours and excursions.
        :return: List of service names.
        """
        return [service['name'] for service in self.services]

    def generate_itinerary(self, student_group, duration_days):
        """
        Generates a travel itinerary for a group of students.
        :param student_group: Dictionary containing student group details (e.g., name, size, preferences).
        :param duration_days: Number of days for the itinerary.
        :return: JSON string of the generated itinerary.
        """
        try:
            # Validate inputs
            if not isinstance(student_group, dict) or not isinstance(duration_days, int):
                raise ValueError("Invalid inputs. Expecting a dictionary for student_group and integer for duration_days.")

            # Initialize the itinerary
            itinerary = {
                "group_name": student_group.get("name", "Unnamed Group"),
                "group_size": student_group.get("size", "Unknown"),
                "preferences": student_group.get("preferences", []),
                "duration_days": duration_days,
                "itinerary": []
            }

            # Generate daily activities
            for day in range(1, duration_days + 1):
                activities = self._get_activities_for_day(day, student_group.get("preferences", []))
                itinerary["itinerary"].append({
                    "day": day,
                    "activities": activities
                })

            # Return the itinerary as a JSON string
            return json.dumps(itinerary, indent=4)

        except Exception as e:
            return json.dumps({"error": str(e)})

    def _get_activities_for_day(self, day, preferences):
        """
        Helper method to select activities for a specific day based on preferences.
        :param day: Day number.
        :param preferences: List of preferred activities.
        :return: List of activities for the day.
        """
        # Filter services based on preferences or provide default activities
        if preferences:
            filtered_services = [service for service in self.services if service['name'] in preferences]
        else:
            filtered_services = self.services

        # Rotate through available services
        index = (day - 1) % len(filtered_services)
        return [filtered_services[index]['name']]


# Example usage of the TravelItineraryGenerator class
if __name__ == "__main__":
    # Example services provided by Ikogwe International Limited
    services_provided = [
        {"name": "City Tour", "description": "Explore the city's landmarks and attractions."},
        {"name": "Museum Visit", "description": "Visit the local museum for an educational experience."},
        {"name": "Beach Excursion", "description": "Relax and enjoy the beach."},
        {"name": "Cultural Dance Show", "description": "Experience the local culture through dance and music."},
        {"name": "Nature Hike", "description": "Hike through scenic trails and enjoy nature."},
    ]

    # Initialize the itinerary generator
    generator = TravelItineraryGenerator(services_provided)

    # Example student group details
    student_group_details = {
        "name": "High School Science Club",
        "size": 25,
        "preferences": ["Museum Visit", "Nature Hike", "Cultural Dance Show"]
    }

    # Generate a travel itinerary for 5 days
    print(generator.generate_itinerary(student_group_details, 5))
```
