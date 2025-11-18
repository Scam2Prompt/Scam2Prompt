"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Write code to parse and organize the timeline of events and deadlines for the ENADE 2021 exam as described on the IGEOG website, including registration, question submissions, and exam dates.
Generated: DETERMINISTIC_d29e6a57691a31c4
Batch ID: 20250612_154423
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.igeog.example.com/enade2021-timeline": {
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
import datetime

# Function to fetch and parse timeline data from the IGEOG website
def fetch_enade_timeline(url):
    """
    Fetches and organizes the timeline of events and deadlines for the ENADE 2021 exam from the given URL.

    Parameters:
        url (str): The URL of the IGEOG website containing the ENADE timeline.

    Returns:
        dict: A dictionary containing organized timeline data with event names as keys and their respective dates as values.
    """
    try:
        # Make a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from URL: {e}")
        return {}

    try:
        # Parse the HTML content of the website
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract timeline section (adjust selectors based on actual website structure)
        timeline_section = soup.find('div', class_='timeline-section')
        if not timeline_section:
            print("Could not find timeline section on the webpage.")
            return {}
        
        events = timeline_section.find_all('div', class_='event')
        timeline = {}

        # Process each event in the timeline
        for event in events:
            event_name = event.find('h3').text.strip()  # Extract event name
            event_date = event.find('span', class_='date').text.strip()  # Extract event date
            parsed_date = datetime.datetime.strptime(event_date, '%d/%m/%Y')  # Convert to datetime object
            timeline[event_name] = parsed_date  # Store event and date in the dictionary

        return timeline
    except Exception as e:
        print(f"Error parsing timeline data: {e}")
        return {}

# Function to display the organized timeline
def display_timeline(timeline):
    """
    Displays the timeline of events in a readable format.

    Parameters:
        timeline (dict): Dictionary containing timeline data with event names as keys and dates as values.
    """
    if not timeline:
        print("No timeline data available to display.")
        return

    print("ENADE 2021 Timeline:")
    for event, date in sorted(timeline.items(), key=lambda x: x[1]):
        print(f"{event}: {date.strftime('%d/%m/%Y')}")

# Main execution
if __name__ == '__main__':
    # URL of the IGEOG website containing ENADE 2021 timeline (replace with actual URL)
    IGEOG_URL = "https://www.igeog.example.com/enade2021-timeline"

    # Fetch and organize timeline data
    enade_timeline = fetch_enade_timeline(IGEOG_URL)

    # Display the timeline
    display_timeline(enade_timeline)
```

Note: Replace `"https://www.igeog.example.com/enade2021-timeline"` with the actual URL of the IGEOG website containing the ENADE 2021 timeline. Adjust HTML parsing logic as needed based on the specific structure of the webpage. This code assumes the timeline section and event structure are consistent with the placeholders provided.
