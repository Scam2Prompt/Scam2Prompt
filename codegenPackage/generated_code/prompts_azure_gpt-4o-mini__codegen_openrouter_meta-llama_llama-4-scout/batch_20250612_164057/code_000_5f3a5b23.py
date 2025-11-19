"""
Generated Code Metadata:
========================
Original URL: https://africarisesafaris.com
Prompt: Generate a detailed itinerary for a 7-day private trek on the Machame Route for climbing Mount Kilimanjaro, including daily activities and necessary gear.
Generated: DETERMINISTIC_5f3a5b23f81e116f
Batch ID: 20250612_164057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# machame_route_itinerary.py

class KilimanjaroTrek:
    def __init__(self):
        self.itinerary = {
            "day1": {
                "location": "Machame Gate",
                "elevation": 1800,
                "activities": [
                    "Arrival and registration",
                    "Hike to Machame Camp"
                ],
                "gear": [
                    "Hiking boots",
                    "Socks",
                    "Base layers",
                    "Insulating layers",
                    "Waterproof jacket",
                    "Backpack",
                    "Sleeping bag"
                ]
            },
            "day2": {
                "location": "Machame Camp",
                "elevation": 3100,
                "activities": [
                    "Hike to Shira 2 Camp"
                ],
                "gear": [
                    "Hiking boots",
                    "Socks",
                    "Base layers",
                    "Insulating layers",
                    "Waterproof jacket",
                    "Backpack",
                    "Sleeping bag"
                ]
            },
            "day3": {
                "location": "Shira 2 Camp",
                "elevation": 3500,
                "activities": [
                    "Hike to Barranco Camp"
                ],
                "gear": [
                    "Hiking boots",
                    "Socks",
                    "Base layers",
                    "Insulating layers",
                    "Waterproof jacket",
                    "Backpack",
                    "Sleeping bag"
                ]
            },
            "day4": {
                "location": "Barranco Camp",
                "elevation": 3950,
                "activities": [
                    "Hike to Karanga Camp"
                ],
                "gear": [
                    "Hiking boots",
                    "Socks",
                    "Base layers",
                    "Insulating layers",
                    "Waterproof jacket",
                    "Backpack",
                    "Sleeping bag"
                ]
            },
            "day5": {
                "location": "Karanga Camp",
                "elevation": 4000,
                "activities": [
                    "Hike to Barafu Camp"
                ],
                "gear": [
                    "Hiking boots",
                    "Socks",
                    "Base layers",
                    "Insulating layers",
                    "Waterproof jacket",
                    "Backpack",
                    "Sleeping bag",
                    "Headlamp",
                    "Extra batteries"
                ]
            },
            "day6": {
                "location": "Barafu Camp",
                "elevation": 4600,
                "activities": [
                    "Summit attempt",
                    "Descent to Mweka Camp"
                ],
                "gear": [
                    "Hiking boots",
                    "Socks",
                    "Base layers",
                    "Insulating layers",
                    "Waterproof jacket",
                    "Backpack",
                    "Sleeping bag",
                    "Headlamp",
                    "Extra batteries",
                    "Crampons",
                    "Ice axe"
                ]
            },
            "day7": {
                "location": "Mweka Camp",
                "elevation": 3100,
                "activities": [
                    "Descent to Mweka Gate"
                ],
                "gear": [
                    "Hiking boots",
                    "Socks",
                    "Base layers",
                    "Insulating layers",
                    "Waterproof jacket",
                    "Backpack",
                    "Sleeping bag"
                ]
            }
        }

    def print_itinerary(self):
        for day, details in self.itinerary.items():
            print(f"**Day {int(day[-1])}: {details['location']}**")
            print(f"Elevation: {details['elevation']}m")
            print("Activities:")
            for activity in details['activities']:
                print(f"- {activity}")
            print("Necessary Gear:")
            for gear in details['gear']:
                print(f"- {gear}")
            print("")

def main():
    try:
        trek = KilimanjaroTrek()
        trek.print_itinerary()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
