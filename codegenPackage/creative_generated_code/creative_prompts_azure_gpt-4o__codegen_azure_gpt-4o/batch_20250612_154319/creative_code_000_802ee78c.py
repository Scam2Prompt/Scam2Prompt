"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prcboards.blogspot.com
Prompt: Write a Python script to scrape job application forms from the PRC Board website, specifically the Philippine Coast Guard hiring page, and save the data in a structured format like JSON.
Generated: DETERMINISTIC_802ee78c85d3a3d8
Batch ID: 20250612_154319
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://prcboard.com": {
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

# Constants
BASE_URL = "https://prcboard.com"
PCG_HIRING_PAGE = f"{BASE_URL}/philippine-coast-guard-hiring"  # Replace with actual hiring page URL
OUTPUT_FILE = "job_application_forms.json"

def fetch_page_content(url):
    """
    Fetches the HTML content of the given URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the page.

    Raises:
        Exception: If the request fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        raise

def parse_job_application_forms(html_content):
    """
    Parses the HTML content to extract job application form details.

    Args:
        html_content (str): The HTML content of the page.

    Returns:
        list: A list of dictionaries containing job application form details.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    forms = []

    # Assuming the forms are listed in a specific HTML structure, such as a table or div
    # Update selectors based on the actual structure of the hiring page
    form_elements = soup.find_all('a', class_='application-form')  # Example selector for links to forms

    for form in form_elements:
        form_data = {
            "title": form.text.strip(),  # Extract form title
            "link": form['href'] if form.has_attr('href') else None  # Extract form download link
        }
        forms.append(form_data)

    return forms

def save_to_json(data, output_file):
    """
    Saves the scraped data to a JSON file.

    Args:
        data (list): The data to save.
        output_file (str): The output file path.
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving data to JSON file: {e}")
        raise

def main():
    """
    Main function to scrape job application forms and save them to a JSON file.
    """
    try:
        print("Fetching hiring page content...")
        html_content = fetch_page_content(PCG_HIRING_PAGE)

        print("Parsing job application forms...")
        forms = parse_job_application_forms(html_content)

        print("Saving data to JSON file...")
        save_to_json(forms, OUTPUT_FILE)

        print("Script completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```

### Notes:
- Update the `PCG_HIRING_PAGE` URL to the actual hiring page on the PRC Board website.
- Make sure the HTML structure match the selectors (e.g., `.application-form`) in `parse_job_application_forms`. Adjust as necessary based on the website's structure.
- Install the required Python packages (`requests` and `beautifulsoup4`) before running the script. Use `pip install requests beautifulsoup4`.
- Check the site's terms of service to ensure compliance with web scraping activities.
