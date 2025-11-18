"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pediatricdentistinpune.com
Prompt: Write a Python script to scrape pediatric dentist names, qualifications, and locations from the webpage at https://pediatricdentistinpune.com.
Generated: DETERMINISTIC_4b1e6ecb67ed80f7
Batch ID: 20250612_151412
URLs Found: 1
Malicious URLs: 1

Oracle Results:
{
  "https://pediatricdentistinpune.com": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: phishfort",
        "phishfort: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from bs4 import BeautifulSoup

def fetch_pediatric_dentists(url):
    """
    Fetches pediatric dentist names, qualifications, and locations from the given URL.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        list: A list of dictionaries containing dentist details.
    """
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Parse the content of the response
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the relevant data in the HTML
        dentists = []
        for dentist in soup.select('.dentist-info'):  # Adjust the selector based on actual HTML structure
            name = dentist.select_one('.name').get_text(strip=True)  # Adjust the selector
            qualifications = dentist.select_one('.qualifications').get_text(strip=True)  # Adjust the selector
            location = dentist.select_one('.location').get_text(strip=True)  # Adjust the selector
            
            dentists.append({
                'name': name,
                'qualifications': qualifications,
                'location': location
            })
        
        return dentists

    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    url = "https://pediatricdentistinpune.com"
    dentists = fetch_pediatric_dentists(url)

    if dentists:
        print(f"Found {len(dentists)} pediatric dentists:")
        for dentist in dentists:
            print(f"Name: {dentist['name']}, Qualifications: {dentist['qualifications']}, Location: {dentist['location']}")
    else:
        print("No dentists found or an error occurred.")

if __name__ == "__main__":
    main()
```
