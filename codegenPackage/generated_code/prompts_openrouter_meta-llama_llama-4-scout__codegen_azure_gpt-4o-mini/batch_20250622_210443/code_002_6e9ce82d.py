"""
Generated Code Metadata:
========================
Original URL: https://rademilos.com
Prompt: Generate a list of Serbian writers and journalists who, like Radе Milosavljević, have written about their ancestry and heritage, and provide a brief description of their works.
Generated: DETERMINISTIC_6e9ce82d61c7e9b8
Batch ID: 20250622_210443
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/serbian-writers": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup

class Writer:
    """Class to represent a writer with their name and description of their works."""
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

def fetch_writers_data(url):
    """Fetches writer data from the given URL and returns a list of Writer objects."""
    writers = []
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.text, 'html.parser')

        # Assuming the writers are listed in <li> tags within a <ul> with class 'writers-list'
        for li in soup.select('ul.writers-list li'):
            name = li.find('h3').text.strip()  # Assuming name is in <h3> tag
            description = li.find('p').text.strip()  # Assuming description is in <p> tag
            writers.append(Writer(name, description))
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    
    return writers

def main():
    """Main function to execute the script."""
    url = "https://example.com/serbian-writers"  # Replace with the actual URL
    writers = fetch_writers_data(url)

    # Print the list of writers
    for writer in writers:
        print(writer)

if __name__ == "__main__":
    main()
```
