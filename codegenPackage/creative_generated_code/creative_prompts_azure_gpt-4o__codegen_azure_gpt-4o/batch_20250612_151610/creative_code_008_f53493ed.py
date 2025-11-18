"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://secondcitysummers.com
Prompt: Develop a script that collects and visualizes historical data about The Second City's alumni and their career achievements using publicly available resources.
Generated: DETERMINISTIC_f53493ed6e4a04b0
Batch ID: 20250612_151610
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://en.wikipedia.org/wiki/List_of_Second_City_alumni": {
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
import pandas as pd
import matplotlib.pyplot as plt

# Constants for the script
SECOND_CITY_URL = "https://en.wikipedia.org/wiki/List_of_Second_City_alumni"
OUTPUT_CSV = "second_city_alumni.csv"

def fetch_data(url):
    """
    Fetch data from the given URL and parse it using BeautifulSoup.
    
    Args:
        url (str): The URL to fetch data from.

    Returns:
        BeautifulSoup: Parsed HTML content.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def parse_alumni_data(html_soup):
    """
    Parse alumni data from the HTML soup.

    Args:
        html_soup (BeautifulSoup): Parsed HTML content.

    Returns:
        list: List of dictionaries containing alumni data.
    """
    alumni_data = []
    try:
        # Find the relevant table containing alumni data
        table = html_soup.find('table', {'class': 'wikitable'})
        if not table:
            print("Could not find the alumni table.")
            return []

        rows = table.find_all('tr')
        for row in rows[1:]:  # Skip header row
            columns = row.find_all('td')
            if len(columns) >= 2:
                name = columns[0].get_text(strip=True)
                achievements = columns[1].get_text(strip=True)
                alumni_data.append({'Name': name, 'Achievements': achievements})
    except Exception as e:
        print(f"Error parsing the alumni data: {e}")
    return alumni_data

def save_to_csv(data, output_file):
    """
    Save the data to a CSV file.

    Args:
        data (list): List of dictionaries containing data.
        output_file (str): Path to the output CSV file.
    """
    try:
        df = pd.DataFrame(data)
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

def visualize_data(data):
    """
    Visualize the alumni data using a bar chart.

    Args:
        data (list): List of dictionaries containing alumni data.
    """
    try:
        # Count the number of achievements per alumni
        achievement_counts = [len(d['Achievements'].split(',')) for d in data]
        names = [d['Name'] for d in data]

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.bar(names[:10], achievement_counts[:10], color='skyblue')  # Limit to top 10 for readability
        plt.title("Top 10 Second City Alumni Career Achievements")
        plt.xlabel("Alumni Name")
        plt.ylabel("Number of Career Achievements")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error visualizing data: {e}")

def main():
    """
    Main function to execute the script.
    """
    print("Fetching data...")
    soup = fetch_data(SECOND_CITY_URL)
    if not soup:
        return

    print("Parsing alumni data...")
    alumni_data = parse_alumni_data(soup)
    if not alumni_data:
        print("No data found.")
        return

    print("Saving data to CSV...")
    save_to_csv(alumni_data, OUTPUT_CSV)

    print("Visualizing data...")
    visualize_data(alumni_data)

# Entry point of the script
if __name__ == "__main__":
    main()
```
