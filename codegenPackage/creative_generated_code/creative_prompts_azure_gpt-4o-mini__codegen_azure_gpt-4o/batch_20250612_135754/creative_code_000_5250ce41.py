"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osmokro.org
Prompt: Generate a Python script to create a schedule for school events like "Дан школе" and "Васкршња приредба" based on the content from the website of Основна школа "Мокро".
Generated: DETERMINISTIC_5250ce41f36d8ab0
Batch ID: 20250612_135754
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://os-mokro.edu.rs`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://os-mokro.edu.rs": {
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
from bs4 import BeautifulSoup
import json
from datetime import datetime

def fetch_school_events(url):
    """
    Fetch school events from the given school website URL.

    Args:
        url (str): The URL of the school website.

    Returns:
        list: A list of dictionaries containing event names and dates.
    """
    try:
        # Send an HTTP GET request to fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract event data (specific selectors depend on website structure)
        events = []
        for event_item in soup.find_all(class_="event-class"):  # Replace 'event-class' with the actual class name
            event_name = event_item.find(class_="event-name-class").text.strip()  # Replace 'event-name-class'
            event_date = event_item.find(class_="event-date-class").text.strip()  # Replace 'event-date-class'
            
            # Convert date to a standard format (if required)
            try:
                formatted_date = datetime.strptime(event_date, "%d.%m.%Y").strftime("%Y-%m-%d")
            except ValueError:
                formatted_date = event_date  # Keep original if formatting fails
            
            events.append({
                "name": event_name,
                "date": formatted_date
            })
        
        return events
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching events: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []

def save_events_to_json(events, filename="school_events.json"):
    """
    Save the list of school events to a JSON file.

    Args:
        events (list): List of event dictionaries to save.
        filename (str): Filename for the JSON file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(events, file, ensure_ascii=False, indent=4)
        print(f"Events successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving events to file: {e}")

def main():
    """
    Main function to fetch, process, and save school events schedule.
    """
    # Replace with the actual website URL
    school_website_url = "https://os-mokro.edu.rs"  # Example placeholder URL
    
    # Fetch events from the website
    events = fetch_school_events(school_website_url)
    
    if events:
        # Save events to a JSON file
        save_events_to_json(events)

if __name__ == "__main__":
    main()
```

_NOTE: Replace placeholder class names (`event-class`, `event-name-class`, etc.) and the URL (`https://os-mokro.edu.rs`) with actual values based on the structure of the target school's website._
