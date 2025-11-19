"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: Create a detailed plan for a 12-day bush and beach safari in Kenya, highlighting activities in Amboseli, Diani, and Tsavo.
Generated: DETERMINISTIC_5520107abfb829f1
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class SafariPlan:
    def __init__(self):
        self.itinerary = []

    def add_activity(self, day, location, activity):
        self.itinerary.append({
            'day': day,
            'location': location,
            'activity': activity
        })

    def print_itinerary(self):
        for activity in self.itinerary:
            print(f"Day {activity['day']}: {activity['location']} - {activity['activity']}")


class KenyaSafari(SafariPlan):
    def __init__(self, start_date):
        super().__init__()
        self.start_date = start_date
        self.locations = {
            'Amboseli': self.add_amboseli_activities,
            'Diani': self.add_diani_activities,
            'Tsavo': self.add_tsavo_activities
        }
        self.create_itinerary()

    def create_itinerary(self):
        day = 1
        self.locations['Amboseli'](day)
        day += 4
        self.locations['Tsavo'](day)
        day += 4
        self.locations['Diani'](day)
        day += 3

    def add_amboseli_activities(self, day):
        self.add_activity(day, 'Amboseli', 'Game drive to spot elephants, giraffes, and zebras')
        self.add_activity(day + 1, 'Amboseli', 'Sunrise hike to Observation Hill for panoramic views')
        self.add_activity(day + 2, 'Amboseli', 'Visit to a local Maasai community to learn about their culture')
        self.add_activity(day + 3, 'Amboseli', 'Relaxation day at the camp with optional activities like birdwatching')

    def add_diani_activities(self, day):
        self.add_activity(day, 'Diani', 'Beach relaxation and snorkeling in the Indian Ocean')
        self.add_activity(day + 1, 'Diani', 'Diving trip to explore the coral reefs')
        self.add_activity(day + 2, 'Diani', 'Visit to the nearby Shimba Hills National Reserve for a game drive')

    def add_tsavo_activities(self, day):
        self.add_activity(day, 'Tsavo', 'Game drive in Tsavo West National Park to spot rhinos, lions, and leopards')
        self.add_activity(day + 1, 'Tsavo', 'Visit to the Mzima Springs for a picnic lunch and birdwatching')
        self.add_activity(day + 2, 'Tsavo', 'Sunset game drive in Tsavo East National Park')
        self.add_activity(day + 3, 'Tsavo', 'Relaxation day at the camp with optional activities like nature walks')


def main():
    try:
        start_date = datetime.strptime('2024-09-16', '%Y-%m-%d').date()
        safari = KenyaSafari(start_date)
        print("12-day Bush and Beach Safari Itinerary in Kenya:")
        safari.print_itinerary()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
