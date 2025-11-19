"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kigaliinstitute.rw
Prompt: Illustrate how to implement a web scraping tool in Python to gather information on the Kigali Institute's training programs in real estate and insurance brokerage.
Generated: DETERMINISTIC_255b7e08379658e8
Batch ID: 20250612_161301
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.kigaliinstitute.example.com": {
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

# Define the URL of the Kigali Institute's website
BASE_URL = "https://www.kigaliinstitute.example.com"  # Replace with the actual URL of the website

def fetch_training_programs():
    """
    Fetches training programs in real estate and insurance brokerage from the Kigali Institute's website.

    Returns:
        list: A list of dictionaries containing program details (title, description, and links).
    """
    try:
        # Send an HTTP GET request to the page with training program information
        response = requests.get(BASE_URL + "/training-programs")
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Locate the sections containing real estate and insurance brokerage programs
        programs = []
        for section in soup.find_all("div", class_="program-section"):
            title = section.find("h3", class_="program-title")
            description = section.find("p", class_="program-description")
            link = section.find("a", class_="program-link")

            # Filter for relevant program categories
            if title and ("real estate" in title.text.lower() or "insurance brokerage" in title.text.lower()):
                programs.append({
                    "title": title.text.strip(),
                    "description": description.text.strip() if description else "No description available",
                    "link": link['href'] if link else "No link available"
                })

        return programs

    except requests.exceptions.RequestException as e:
        # Log or handle HTTP request errors
        print(f"An error occurred while fetching training programs: {e}")
        return []

    except Exception as e:
        # Log or handle other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    """
    The main function to run the web scraping tool.
    """
    print("Fetching training programs from the Kigali Institute...")
    programs = fetch_training_programs()

    if programs:
        print("\nTraining Programs in Real Estate and Insurance Brokerage:")
        for idx, program in enumerate(programs, start=1):
            print(f"\nProgram {idx}:")
            print(f"Title: {program['title']}")
            print(f"Description: {program['description']}")
            print(f"Link: {program['link']}")
    else:
        print("No relevant training programs found.")

if __name__ == "__main__":
    main()
```
