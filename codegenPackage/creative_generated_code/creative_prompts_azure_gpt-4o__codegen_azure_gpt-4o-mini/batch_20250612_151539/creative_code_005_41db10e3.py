"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.predaiaarteenatura.eu
Prompt: Write code to extract and visualize the themes of the sculpture symposiums (e.g., stregoneria, legno e ingegno) from the Predaia Arte e Natura website using the Pandas library.
Generated: DETERMINISTIC_41db10e379b242d7
Batch ID: 20250612_151539
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://predaiaarteenatura.com": {
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
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Function to fetch and parse the symposium themes from the Predaia Arte e Natura website
def fetch_symposium_themes(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract symposium themes; adjust the selector based on actual HTML structure
    themes = []
    theme_elements = soup.select('CSS_SELECTOR_FOR_THEMES')  # Replace with actual selector
    for element in theme_elements:
        themes.append(element.get_text(strip=True))

    return themes

# Function to visualize the themes
def visualize_themes(themes):
    # Counting the frequency of each theme
    theme_counts = pd.Series(themes).value_counts()
    
    # Plotting the themes
    plt.figure(figsize=(10, 6))
    theme_counts.plot(kind='bar', color='skyblue')
    plt.title('Themes of Sculpture Symposiums')
    plt.xlabel('Themes')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main execution block
if __name__ == "__main__":
    URL = "https://predaiaarteenatura.com"  # Update with the actual URL
    themes = fetch_symposium_themes(URL)

    if themes:
        visualize_themes(themes)
    else:
        print("No themes found.")
```

**Note:** Please replace `'CSS_SELECTOR_FOR_THEMES'` with the actual CSS selector used to extract the themes from the website's HTML structure, and ensure the URL is correct.
