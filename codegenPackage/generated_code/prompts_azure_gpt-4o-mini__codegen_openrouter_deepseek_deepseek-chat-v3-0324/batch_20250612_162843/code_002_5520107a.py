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

Since you're asking for code to generate a detailed safari plan, I'll create a Python script that outputs a well-structured 12-day Kenya safari itinerary covering Amboseli, Diani, and Tsavo. The script will use proper data structures and formatting.

```python
"""
Kenya 12-Day Bush & Beach Safari Itinerary Generator
Generates a detailed safari plan covering Amboseli, Diani, and Tsavo.
"""

def generate_safari_itinerary():
    """
    Generate and print a detailed 12-day Kenya safari itinerary.
    Includes activities, accommodations, and travel details.
    """
    itinerary = {
        "title": "12-Day Bush & Beach Safari in Kenya",
        "description": "Experience the best of Kenya's wildlife and beaches, covering Amboseli, Diani, and Tsavo.",
        "days": []
    }

    # Day 1: Arrival in Nairobi
    itinerary["days"].append({
        "day": 1,
        "location": "Nairobi",
        "activities": [
            "Arrive at Jomo Kenyatta International Airport",
            "Meet with safari representative",
            "Transfer to hotel for overnight stay",
            "Briefing about the safari"
        ],
        "accommodation": "Nairobi Serena Hotel",
        "meals": "Dinner"
    })

    # Day 2: Nairobi to Amboseli
    itinerary["days"].append({
        "day": 2,
        "location": "Amboseli National Park",
        "activities": [
            "Morning drive to Amboseli (4-5 hours)",
            "Game drive en route to lodge",
            "Afternoon game drive with views of Mount Kilimanjaro",
            "Visit observation hill for panoramic views"
        ],
        "accommodation": "Amboseli Serena Safari Lodge",
        "meals": "Breakfast, Lunch, Dinner"
    })

    # Day 3: Full day in Amboseli
    itinerary["days"].append({
        "day": 3,
        "location": "Amboseli National Park",
        "activities": [
            "Early morning game drive",
            "Visit Maasai village (optional)",
            "Afternoon game drive focusing on elephants",
            "Sunset photography session"
        ],
        "accommodation": "Amboseli Serena Safari Lodge",
        "meals": "Breakfast, Lunch, Dinner"
    })

    # Day 4: Amboseli to Tsavo West
    itinerary["days"].append({
        "day": 4,
        "location": "Tsavo West National Park",
        "activities": [
            "Morning drive to Tsavo West (3 hours)",
            "Visit Mzima Springs to see hippos and fish",
            "Afternoon game drive",
            "Possible rhino sightings at Ngulia Rhino Sanctuary"
        ],
        "accommodation": "Kilaguni Serena Safari Lodge",
        "meals": "Breakfast, Lunch, Dinner"
    })

    # Day 5: Tsavo West to Tsavo East
    itinerary["days"].append({
        "day": 5,
        "location": "Tsavo East National Park",
        "activities": [
            "Morning game drive en route to Tsavo East",
            "Visit the famous 'red elephants' of Tsavo",
            "Afternoon game drive focusing on predators",
            "Sunset at Aruba Dam"
        ],
        "accommodation": "Ashnil Aruba Lodge",
        "meals": "Breakfast, Lunch, Dinner"
    })

    # Day 6: Full day in Tsavo East
    itinerary["days"].append({
        "day": 6,
        "location": "Tsavo East National Park",
        "activities": [
            "Full day game drives",
            "Visit Lugard Falls and the Yatta Plateau",
            "Bird watching along Galana River",
            "Night game drive (optional)"
        ],
        "accommodation": "Ashnil Aruba Lodge",
        "meals": "Breakfast, Lunch, Dinner"
    })

    # Day 7: Tsavo to Diani Beach
    itinerary["days"].append({
        "day": 7,
        "location": "Diani Beach",
        "activities": [
            "Morning drive to Mombasa (5-6 hours)",
            "Transfer to Diani Beach resort",
            "Afternoon at leisure on the beach",
            "Optional water sports activities"
        ],
        "accommodation": "Baobab Beach Resort",
        "meals": "Breakfast, Dinner"
    })

    # Days 8-11: Beach stay in Diani
    for day in range(8, 12):
        itinerary["days"].append({
            "day": day,
            "location": "Diani Beach",
            "activities": [
                "Beach relaxation and water activities",
                "Optional snorkeling at Kisite Marine Park",
                "Deep sea fishing (optional)",
                "Visit Colobus Conservation Center",
                "Dhow sunset cruise (optional)"
            ],
            "accommodation": "Baobab Beach Resort",
            "meals": "Breakfast, Dinner"
        })

    # Day 12: Departure
    itinerary["days"].append({
        "day": 12,
        "location": "Diani to Nairobi",
        "activities": [
            "Morning at leisure",
            "Transfer to Mombasa airport",
            "Flight back to Nairobi",
            "Connect with international flight"
        ],
        "accommodation": None,
        "meals": "Breakfast"
    })

    return itinerary

def print_itinerary(itinerary):
    """Print the itinerary in a human-readable format."""
    print(f"\n{'='*50}")
    print(f"{itinerary['title'].upper():^50}")
    print(f"{'='*50}\n")
    print(itinerary['description'])
    print("\nDETAILED ITINERARY:\n")

    for day in itinerary['days']:
        print(f"{'-'*50}")
        print(f"DAY {day['day']}: {day['location'].upper()}")
        print(f"{'-'*50}")
        print("\nActivities:")
        for i, activity in enumerate(day['activities'], 1):
            print(f"  {i}. {activity}")
        
        if day['accommodation']:
            print(f"\nAccommodation: {day['accommodation']}")
        print(f"Meals: {day['meals']}\n")

def main():
    """Generate and display the safari itinerary."""
    try:
        itinerary = generate_safari_itinerary()
        print_itinerary(itinerary)
    except Exception as e:
        print(f"Error generating itinerary: {str(e)}")
        return 1
    return 0

if __name__ == "__main__":
    main()
```

This script generates a comprehensive 12-day Kenya safari itinerary with:
1. Daily activities in each location
2. Accommodation details
3. Meal plans
4. Proper error handling
5. Well-structured output formatting

The itinerary covers:
- 2 days in Amboseli (with Kilimanjaro views)
- 3 days in Tsavo (West and East)
- 5 days in Diani Beach (with optional water activities)
- Arrival and departure days

The code follows Python best practices with proper functions, documentation, and error handling.
