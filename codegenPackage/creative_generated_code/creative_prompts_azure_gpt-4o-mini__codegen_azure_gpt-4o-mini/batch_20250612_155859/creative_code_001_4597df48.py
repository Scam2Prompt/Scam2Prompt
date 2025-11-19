"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cocfinance.com
Prompt: Write a Python function that fetches and processes data related to the influence of artificial intelligence in film, referencing the recent film festival mentioned in the content.
Generated: DETERMINISTIC_4597df487b4ceb33
Batch ID: 20250612_155859
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/film-festival-data": {
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
import json

def fetch_ai_film_data(festival_url):
    """
    Fetches and processes data related to the influence of artificial intelligence in film
    from a given film festival URL.

    Args:
        festival_url (str): The URL of the film festival's data source.

    Returns:
        list: A list of films that involve artificial intelligence themes.
    
    Raises:
        ValueError: If the festival URL is invalid or does not return a valid JSON.
        requests.exceptions.RequestException: For issues with the HTTP request.
    """
    # Validate the URL format
    if not isinstance(festival_url, str) or not festival_url.startswith(('http://', 'https://')):
        raise ValueError("Invalid URL provided. Please ensure it is a valid HTTP or HTTPS URL.")
    
    try:
        # Fetch data from the festival URL
        response = requests.get(festival_url)
        
        # Raise an error if the request was unsuccessful
        response.raise_for_status()

        # Parse the JSON data
        data = response.json()
        
        # Process the data to extract films related to AI
        ai_films = []
        for film in data.get('films', []):
            if 'artificial intelligence' in film.get('themes', '').lower():
                ai_films.append({
                    'title': film.get('title'),
                    'director': film.get('director'),
                    'year': film.get('year'),
                    'description': film.get('description')
                })

        return ai_films
    
    except requests.exceptions.RequestException as e:
        # Handle the request-related exceptions
        print(f"An error occurred while fetching the data: {e}")
        raise
    except json.JSONDecodeError:
        # Handle JSON decoding errors
        raise ValueError("The data retrieved is not in valid JSON format.")


# Example usage (uncomment to run):
# festival_url = "https://example.com/film-festival-data"
# try:
#     films = fetch_ai_film_data(festival_url)
#     print(films)
# except Exception as e:
#     print(f"An error occurred: {e}")
```
