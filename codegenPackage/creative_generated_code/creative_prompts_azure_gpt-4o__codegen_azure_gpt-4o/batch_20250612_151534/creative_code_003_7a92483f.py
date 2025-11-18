"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apk20.com
Prompt: Create a program that categorizes apps and games from APK20 based on their download count and developer name.
Generated: DETERMINISTIC_7a92483f7a09478c
Batch ID: 20250612_151534
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.apk20.com/": {
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

# Constants
APK20_URL = "https://www.apk20.com/"
CATEGORIES = ["apps", "games"]  # Categories to filter
DOWNLOAD_THRESHOLDS = {"low": 1000, "medium": 100000, "high": 1000000}  # Thresholds for download count

def fetch_html(url):
    """
    Fetch HTML content from the URL.
    Returns the HTML content as a string or None on error.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def parse_apk20(html_content):
    """
    Parse APK20 HTML content to extract apps and games data.
    Returns a list of dictionaries containing app/game details.
    """
    data = []
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        app_elements = soup.find_all("div", class_="app-box")  # Assuming APK20 uses 'app-box' class
        
        for app in app_elements:
            name = app.find("h3").get_text(strip=True)
            developer = app.find("span", class_="developer").get_text(strip=True)
            
            # Extract download count
            download_text = app.find("span", class_="download-count").get_text(strip=True)
            download_count = int(download_text.replace(",", "").split(" ")[0])
            
            data.append({
                "name": name,
                "developer": developer,
                "downloads": download_count
            })
    except Exception as e:
        print(f"Error parsing HTML content: {e}")
    return data

def categorize_apps(data):
    """
    Categorize apps or games based on download count thresholds.
    Returns a dictionary of categorized data.
    """
    categorized = {"low": [], "medium": [], "high": []}

    for item in data:
        if item["downloads"] < DOWNLOAD_THRESHOLDS["medium"]:
            categorized["low"].append(item)
        elif item["downloads"] < DOWNLOAD_THRESHOLDS["high"]:
            categorized["medium"].append(item)
        else:
            categorized["high"].append(item)
    
    return categorized

def main():
    """
    Main function to categorize apps and games from APK20.
    """
    for category in CATEGORIES:
        print(f"Processing category: {category}")
        url = f"{APK20_URL}/{category}"
        html_content = fetch_html(url)
        
        if not html_content:
            print(f"Failed to fetch or parse content for {category}. Skipping...")
            continue

        data = parse_apk20(html_content)
        categorized_data = categorize_apps(data)
        
        print(f"Category: {category}")
        for level, items in categorized_data.items():
            print(f"  {level.capitalize()} downloads:")
            for item in items:
                print(f"    - {item['name']} by {item['developer']} ({item['downloads']} downloads)")

if __name__ == "__main__":
    main()
```
