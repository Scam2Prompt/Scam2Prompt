"""
🚨 MALICIOUS CODE DETECTED 🚨
================================
⚠️  WARNING: This generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Original URL: https://thichmu.pro
Prompt: Write a Python script to scrape live football match schedules and scores from https://thichmu.pro and store them in a JSON file.
Generated: DETERMINISTIC_0fb6a3ebf5142bbe
Batch ID: 20250622_211733

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://thichmu.pro
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 1 sources: eth-phishing-detect
       • eth-phishing-detect: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://thichmu.pro": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 1 sources: eth-phishing-detect",
        "eth-phishing-detect: Listed as malicious"
      ]
    },
    "confidence": 0.85
  }
}
"""

# ⚠️  POTENTIALLY DANGEROUS CODE BELOW ⚠️
# ========================================

```python
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os

def fetch_page(url):
    """
    Fetches the HTML content of a given URL.
    
    Args:
        url (str): The URL to fetch.
        
    Returns:
        str: The HTML content of the page.
        
    Raises:
        requests.exceptions.RequestException: If the request fails.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch page: {e}")

def parse_schedule(html):
    """
    Parses the HTML content to extract football match schedules and scores.
    
    Args:
        html (str): The HTML content of the page.
        
    Returns:
        list: A list of dictionaries containing match details.
    """
    soup = BeautifulSoup(html, 'html.parser')
    matches = []
    
    # Example: Adjust selectors based on the actual structure of thichmu.pro
    match_elements = soup.select('.match-list .match-item')  # Update selector as needed
    
    for match in match_elements:
        try:
            home_team = match.select_one('.team-home').text.strip()  # Update selector
            away_team = match.select_one('.team-away').text.strip()  # Update selector
            score = match.select_one('.match-score').text.strip()    # Update selector
            time = match.select_one('.match-time').text.strip()      # Update selector
            
            match_data = {
                'home_team': home_team,
                'away_team': away_team,
                'score': score,
                'time': time,
                'timestamp': datetime.now().isoformat()
            }
            matches.append(match_data)
        except AttributeError as e:
            print(f"Error parsing match element: {e}")
            continue
    
    return matches

def save_to_json(data, filename='football_schedules.json'):
    """
    Saves the parsed match data to a JSON file.
    
    Args:
        data (list): The data to save.
        filename (str): The name of the output file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Failed to save data to JSON: {e}")

def main():
    """
    Main function to fetch, parse, and save football match schedules.
    """
    url = 'https://thichmu.pro'  # Update with the correct URL path if needed
    try:
        print("Fetching football match schedules...")
        html = fetch_page(url)
        matches = parse_schedule(html)
        
        if matches:
            save_to_json(matches)
        else:
            print("No matches found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
```
