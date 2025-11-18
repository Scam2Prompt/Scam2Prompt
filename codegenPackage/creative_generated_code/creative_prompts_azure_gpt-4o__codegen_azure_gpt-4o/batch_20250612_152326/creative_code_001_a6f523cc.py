"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sadadeng.com
Prompt: Generate Python code to scrape project details (e.g., name, type, status) from a webpage like Sadad Engineering's "پروژه های اجرا شده" section, and store the data in a JSON file.
Generated: DETERMINISTIC_a6f523cce7383557
Batch ID: 20250612_152326
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.sadadengineering.com/projects-executed": {
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

# URL of the webpage to scrape
URL = "https://www.sadadengineering.com/projects-executed"  # Replace with actual URL

def scrape_project_details(url):
    """
    Scrapes project details from the specified webpage.

    Parameters:
        url (str): The URL of the webpage to scrape.

    Returns:
        list: A list of dictionaries containing project details.
    """
    try:
        # Sending a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parsing the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting project details (Modify selectors based on actual webpage structure)
        projects = []
        project_elements = soup.find_all('div', class_='project-card')  # Adjust class name as per the webpage
        
        for project in project_elements:
            name = project.find('h3', class_='project-name').get_text(strip=True)  # Adjust class name
            type_ = project.find('span', class_='project-type').get_text(strip=True)  # Adjust class name
            status = project.find('span', class_='project-status').get_text(strip=True)  # Adjust class name
            
            # Creating a dictionary for the project
            project_data = {
                "name": name,
                "type": type_,
                "status": status
            }
            projects.append(project_data)
        
        return projects

    except requests.exceptions.RequestException as e:
        # Handling network-related errors
        print(f"Error fetching the webpage: {e}")
        return []
    except Exception as e:
        # Handling other errors
        print(f"An error occurred: {e}")
        return []

def save_to_json(data, filename):
    """
    Saves the given data to a JSON file.

    Parameters:
        data (list): The data to save.
        filename (str): The name of the JSON file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving data to JSON: {e}")

def main():
    """
    Main function to scrape project details and save them to a JSON file.
    """
    url = URL
    json_filename = "project_details.json"

    # Scraping project details
    project_details = scrape_project_details(url)

    if project_details:  # Proceed if scraping was successful
        # Saving the scraped data to a JSON file
        save_to_json(project_details, json_filename)

if __name__ == "__main__":
    main()
```
