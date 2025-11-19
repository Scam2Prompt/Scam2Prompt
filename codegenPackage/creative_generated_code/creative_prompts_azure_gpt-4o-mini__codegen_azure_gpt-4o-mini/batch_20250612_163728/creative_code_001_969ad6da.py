"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmaculada.edu.ec
Prompt: Write a Python script that retrieves and displays the contact information and location of Unidad Educativa Bilingüe de la Inmaculada, including their social media links.
Generated: DETERMINISTIC_969ad6dace3ec491
Batch ID: 20250612_163728
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/search?q={school_name.replace": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com/search?q={school_name.replace(' ', '+": {
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

def fetch_contact_info(school_name):
    """
    Fetches the contact information and location of a given school from a web source.
    
    Args:
        school_name (str): The name of the school to search for.
    
    Returns:
        dict: A dictionary containing the contact information and location.
    """
    try:
        # Define the search URL (replace with the actual URL if known)
        search_url = f"https://www.example.com/search?q={school_name.replace(' ', '+')}"
        
        # Send a GET request to the URL
        response = requests.get(search_url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract contact information and location
        contact_info = {}
        
        # Example extraction; modify selectors based on actual HTML structure
        contact_info['address'] = soup.select_one('.address').get_text(strip=True)
        contact_info['phone'] = soup.select_one('.phone').get_text(strip=True)
        contact_info['email'] = soup.select_one('.email').get_text(strip=True)
        contact_info['social_media'] = {
            'facebook': soup.select_one('.facebook')['href'],
            'twitter': soup.select_one('.twitter')['href'],
            'instagram': soup.select_one('.instagram')['href']
        }

        return contact_info

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def display_contact_info(contact_info):
    """
    Displays the contact information in a formatted way.
    
    Args:
        contact_info (dict): The contact information to display.
    """
    if contact_info:
        print("Contact Information:")
        print(f"Address: {contact_info['address']}")
        print(f"Phone: {contact_info['phone']}")
        print(f"Email: {contact_info['email']}")
        print("Social Media Links:")
        for platform, link in contact_info['social_media'].items():
            print(f"{platform.capitalize()}: {link}")
    else:
        print("No contact information available.")

if __name__ == "__main__":
    school_name = "Unidad Educativa Bilingüe de la Inmaculada"
    contact_info = fetch_contact_info(school_name)
    display_contact_info(contact_info)
```
