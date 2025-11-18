"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.al-aanqua.com
Prompt: Write code to filter and display theater-related events, such as المهرجان الثقافي الوطني للمونولوج والفنون المسرحية, from "العنقاء للثقافة."
Generated: DETERMINISTIC_fb31d603a8672143
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def filter_theater_events(events, keyword):
    """
    Filters theater-related events based on a given keyword from a list of events.

    Args:
        events (list): List of event dictionaries containing event information.
        keyword (str): The keyword to filter events by.

    Returns:
        list: A list of filtered events that match the keyword.
    """
    filtered_events = []
    for event in events:
        try:
            # Check if the event name or description contains the keyword
            if keyword in event.get("name", "") or keyword in event.get("description", ""):
                filtered_events.append(event)
        except AttributeError:
            # Handle cases where event data might not be in the expected format
            print(f"Warning: Event has invalid structure: {event}")
            continue
    return filtered_events


def display_events(events):
    """
    Displays the filtered events in a readable format.

    Args:
        events (list): List of event dictionaries containing event information.
    """
    if not events:
        print("No events found.")
        return

    print("\nFiltered Theater-Related Events:\n")
    for event in events:
        try:
            name = event.get("name", "Unknown Event")
            description = event.get("description", "No description available.")
            location = event.get("location", "Location not specified.")
            date = event.get("date", "Date not specified.")
            
            print(f"Name: {name}")
            print(f"Description: {description}")
            print(f"Location: {location}")
            print(f"Date: {date}")
            print("-" * 50)
        except AttributeError:
            print(f"Warning: Event has invalid structure: {event}")
            continue


# Example usage:
if __name__ == "__main__":
    # Sample data representing events (in real scenarios, this might come from a database or an API)
    events_data = [
        {
            "name": "المهرجان الثقافي الوطني للمونولوج والفنون المسرحية",
            "description": "مهرجان يحتفي بالفنون المسرحية والمونولوج في العنقاء للثقافة.",
            "location": "مدينة الثقافة",
            "date": "2023-12-01"
        },
        {
            "name": "مهرجان العنقاء للثقافة",
            "description": "حدث ثقافي يعرض الفنون المتنوعة، يشمل المسرحيات والعروض الموسيقية.",
            "location": "مركز العنقاء الثقافي",
            "date": "2023-11-15"
        },
        {
            "name": "مؤتمر أدبي",
            "description": "حدث يناقش الأدب العربي الحديث.",
            "location": "قاعة المؤتمرات",
            "date": "2023-10-30"
        }
    ]
    
    # Filter and display theater-related events
    keyword_to_filter = "المسرحية"
    filtered_events = filter_theater_events(events_data, keyword_to_filter)
    display_events(filtered_events)
```
