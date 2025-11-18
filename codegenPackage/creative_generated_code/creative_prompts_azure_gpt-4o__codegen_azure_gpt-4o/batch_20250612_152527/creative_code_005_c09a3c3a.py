"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: Provide a Python script to parse and display institutional symbols and historical data, referencing the "Símbolos de la Institución" and "Reseña Histórica" sections on the IEBCA website.
Generated: DETERMINISTIC_c09a3c3a0473643d
Batch ID: 20250612_152527
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.iebca.edu.gt/": {
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

def fetch_institutional_symbols_and_history(url):
    """
    Fetches and displays institutional symbols and historical data from a given URL.
    
    Args:
        url (str): The URL of the website to scrape.
        
    Returns:
        None
    """
    try:
        # Send an HTTP GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract and display the "Símbolos de la Institución" section
        symbols_section = soup.find('section', id='symbols')  # Example ID; update based on actual HTML structure
        if symbols_section:
            print("Símbolos de la Institución:")
            print(symbols_section.get_text(strip=True))
        else:
            print("The 'Símbolos de la Institución' section was not found.")
        
        print("\n" + "-"*50 + "\n")  # Separator
        
        # Extract and display the "Reseña Histórica" section
        history_section = soup.find('section', id='history')  # Example ID; update based on actual HTML structure
        if history_section:
            print("Reseña Histórica:")
            print(history_section.get_text(strip=True))
        else:
            print("The 'Reseña Histórica' section was not found.")
    
    except requests.exceptions.RequestException as e:
        # Handle HTTP request errors
        print(f"An error occurred while fetching the webpage: {e}")
    except Exception as e:
        # Handle general errors
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main entry point of the script.
    """
    # URL of the IEBCA website (replace with the actual URL)
    url = "https://www.iebca.edu.gt/"  # Example URL
    
    # Fetch and display the institutional symbols and historical data
    fetch_institutional_symbols_and_history(url)

if __name__ == "__main__":
    main()
```

Ensure the `id` attributes (`'symbols'` and `'history'`) match the actual structure of the IEBCA website. Update them if the relevant sections have different identifiers or are nested differently.
