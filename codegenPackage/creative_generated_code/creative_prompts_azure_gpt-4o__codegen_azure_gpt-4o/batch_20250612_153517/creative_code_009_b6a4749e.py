"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plus.endeavorschools.com
Prompt: Write a Python function to scrape and organize the list of schools and their corresponding extracurricular programs from the Endeavor Schools Plus webpage.
Generated: DETERMINISTIC_b6a4749ea2de874d
Batch ID: 20250612_153517
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com/endeavor-schools-plus": {
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

def scrape_endeavor_schools(url):
    """
    Scrapes the list of schools and their extracurricular programs from the Endeavor Schools Plus webpage.
    
    Args:
        url (str): The URL of the Endeavor Schools Plus webpage.
    
    Returns:
        dict: A dictionary where keys are school names and values are lists of extracurricular programs.
    """
    try:
        # Send an HTTP GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        # Parse the webpage content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize an empty dictionary to store school data
        schools_data = {}

        # Locate the section containing schools and programs (Update selectors based on webpage structure)
        schools_section = soup.find_all('div', class_='school-container')  # Replace with correct class name

        for school in schools_section:
            # Extract the school name
            school_name = school.find('h2', class_='school-name').get_text(strip=True)  # Replace with correct class name

            # Extract the list of extracurricular programs
            programs = school.find_all('li', class_='program-item')  # Replace with correct class name
            programs_list = [program.get_text(strip=True) for program in programs]

            # Add the school and its programs to the dictionary
            schools_data[school_name] = programs_list

        return schools_data

    except requests.exceptions.RequestException as e:
        # Handle HTTP request exceptions
        print(f"Error fetching the URL: {e}")
        return {}
    except AttributeError as e:
        # Handle parsing errors if structure changes
        print(f"Error parsing the webpage structure: {e}")
        return {}

# Example usage
if __name__ == "__main__":
    # Replace the URL with the actual Endeavor Schools Plus webpage URL
    url = "https://www.example.com/endeavor-schools-plus"
    schools = scrape_endeavor_schools(url)
    if schools:
        for school, programs in schools.items():
            print(f"School: {school}")
            print("Programs:")
            for program in programs:
                print(f"  - {program}")
            print("\n")
```

Note: Update the HTML structure and class names in the code (`school-container`, `school-name`, `program-item`, etc.) based on the actual webpage.
