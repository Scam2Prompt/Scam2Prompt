"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tnhs.us
Prompt: Generate a script using BeautifulSoup to extract the "Academic Achievement Awards" section from the TSSAA website and save the list of teams into a CSV file.
Generated: DETERMINISTIC_b540fd51734e167f
Batch ID: 20250612_153526
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.tssaa.org/awards/academic-achievement/": {
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
import csv

# URL of the TSSAA Academic Achievement Awards page
URL = "https://www.tssaa.org/awards/academic-achievement/"

def fetch_award_data(url):
    """
    Fetches the HTML content of the specified URL.

    Parameters:
    url (str): The URL to fetch.

    Returns:
    BeautifulSoup: Parsed HTML content.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def extract_teams(soup):
    """
    Extracts the list of teams from the BeautifulSoup object.

    Parameters:
    soup (BeautifulSoup): Parsed HTML content.

    Returns:
    list: List of teams as strings.
    """
    teams = []
    
    # Adjust the selector based on the actual HTML structure
    award_section = soup.find('div', class_='academic-achievement-awards')
    if award_section:
        team_elements = award_section.find_all('li')
        for team in team_elements:
            teams.append(team.text.strip())
    else:
        print("No award section found.")
    
    return teams

def save_to_csv(teams, filename):
    """
    Saves the list of teams to a CSV file.

    Parameters:
    teams (list): List of teams to save.
    filename (str): Name of the CSV file.
    """
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Team Name'])  # Writing header
            for team in teams:
                writer.writerow([team])
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Error saving to CSV file: {e}")

def main():
    """
    Main function to execute the script.
    """
    soup = fetch_award_data(URL)
    if soup:
        teams = extract_teams(soup)
        if teams:
            save_to_csv(teams, 'academic_achievement_awards.csv')

if __name__ == "__main__":
    main()
```
