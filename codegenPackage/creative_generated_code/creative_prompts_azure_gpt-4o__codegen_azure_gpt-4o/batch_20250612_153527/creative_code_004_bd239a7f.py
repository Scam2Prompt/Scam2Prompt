"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewards-steth.com
Prompt: Suggest a Python library to parse and organize the event details from the "뽐뿌이벤트" section into a structured JSON format.
Generated: DETERMINISTIC_bd239a7fc927d94d
Batch ID: 20250612_153527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup
import json

def fetch_ppomppu_events(url):
    """
    Fetches and parses event details from the '뽐뿌이벤트' section of the given URL.
    Returns the events as a structured JSON format.
    
    Parameters:
    - url (str): The URL of the 뽐뿌이벤트 webpage.
    
    Returns:
    - str: JSON string containing the structured event details.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP issues
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract event details (Assuming event details are contained within a specific table)
        events = []
        event_table = soup.find('table', {'class': 'event-table'})  # Replace with the correct class or id
        
        if event_table:
            rows = event_table.find_all('tr')[1:]  # Skip header row
            
            for row in rows:
                columns = row.find_all('td')
                if len(columns) >= 3:  # Ensure there are enough columns
                    event = {
                        'title': columns[0].text.strip(),
                        'date': columns[1].text.strip(),
                        'link': columns[2].find('a')['href'].strip() if columns[2].find('a') else None
                    }
                    events.append(event)
        
        # Return the structured data as JSON
        return json.dumps(events, ensure_ascii=False, indent=4)
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        return json.dumps({'error': f'Network error occurred: {str(e)}'}, ensure_ascii=False)
    except Exception as e:
        # Handle other unexpected errors
        return json.dumps({'error': f'An unexpected error occurred: {str(e)}'}, ensure_ascii=False)

# Example usage:
# Replace 'your_url_here' with the actual URL of the 뽐뿌이벤트 section
url = 'your_url_here'
print(fetch_ppomppu_events(url))
```
