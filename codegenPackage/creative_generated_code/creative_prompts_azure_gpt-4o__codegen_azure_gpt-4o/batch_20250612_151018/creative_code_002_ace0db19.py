"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Generate a script to scrape and categorize the FOSS@RIT directory data, focusing on members involved in specific fields like "Game Design and Development" or "Computing Security."
Generated: DETERMINISTIC_ace0db194d5d2903
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://foss.rit.edu/directory": {
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

# URL of FOSS@RIT directory (example URL, replace with actual URL)
FOSS_RIT_URL = "https://foss.rit.edu/directory"

# Fields of interest
FIELDS_OF_INTEREST = ["Game Design and Development", "Computing Security"]

# Function to fetch the FOSS@RIT directory HTML
def fetch_directory_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

# Function to parse HTML and extract member data
def parse_directory_page(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        members = []

        # Example parsing logic (update based on actual HTML structure)
        # Assuming each member is listed in a "div.member" with "field" and "name" tags
        member_elements = soup.find_all("div", class_="member")
        for member in member_elements:
            name = member.find("span", class_="name").get_text(strip=True)
            field = member.find("span", class_="field").get_text(strip=True)
            members.append({"name": name, "field": field})

        return members
    except Exception as e:
        print(f"Error parsing HTML content: {e}")
        return []

# Function to categorize members based on fields of interest
def categorize_members(members, fields_of_interest):
    categorized_members = {field: [] for field in fields_of_interest}
    for member in members:
        if member["field"] in fields_of_interest:
            categorized_members[member["field"]].append(member["name"])
    return categorized_members

# Main function to scrape, parse, and categorize data
def main():
    # Fetch directory data
    html_content = fetch_directory_data(FOSS_RIT_URL)
    if not html_content:
        print("Failed to fetch directory data.")
        return

    # Parse member data from HTML
    members = parse_directory_page(html_content)
    if not members:
        print("No members found in the directory.")
        return

    # Categorize members based on fields of interest
    categorized_members = categorize_members(members, FIELDS_OF_INTEREST)

    # Output the categorized members as JSON
    output_file = "categorized_members.json"
    try:
        with open(output_file, "w") as file:
            json.dump(categorized_members, file, indent=4)
        print(f"Categorized members saved to {output_file}.")
    except Exception as e:
        print(f"Error saving categorized members to file: {e}")

if __name__ == "__main__":
    main()
```
