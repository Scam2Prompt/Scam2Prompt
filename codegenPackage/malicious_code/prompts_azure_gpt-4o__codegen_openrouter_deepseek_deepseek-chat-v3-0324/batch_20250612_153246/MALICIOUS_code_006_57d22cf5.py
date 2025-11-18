"""
🚨 MALICIOUS CODE DETECTED 🚨
================================
⚠️  WARNING: This generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Original URL: https://qaisrani.com
Prompt: Develop a Python script to parse the "Diseases" section on https://qaisrani.com and categorize the treatments offered into a hierarchical JSON structure.
Generated: DETERMINISTIC_57d22cf5f73e2699
Batch ID: 20250612_153246

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://qaisrani.com
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 1 sources: eth-phishing-detect
       • eth-phishing-detect: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://qaisrani.com": {
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
from urllib.parse import urljoin

def fetch_page(url):
    """
    Fetch the HTML content of a given URL.
    
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

def parse_diseases_section(html):
    """
    Parse the diseases section from the HTML content.
    
    Args:
        html (str): The HTML content of the page.
        
    Returns:
        dict: A hierarchical structure of diseases and treatments.
    """
    soup = BeautifulSoup(html, 'html.parser')
    diseases_section = soup.find('section', id='diseases')
    
    if not diseases_section:
        raise ValueError("Diseases section not found on the page.")
    
    hierarchy = {}
    
    # Find all disease categories (h2 headings)
    categories = diseases_section.find_all('h2')
    
    for category in categories:
        category_name = category.get_text().strip()
        hierarchy[category_name] = {}
        
        # Find treatments under each category (next sibling elements until next h2)
        next_element = category.next_sibling
        
        while next_element and next_element.name != 'h2':
            if next_element.name == 'h3':
                treatment_name = next_element.get_text().strip()
                hierarchy[category_name][treatment_name] = []
                
                # Find treatment details (next sibling elements until next h3 or h2)
                detail_element = next_element.next_sibling
                while detail_element and detail_element.name not in ['h2', 'h3']:
                    if detail_element.name == 'p':
                        hierarchy[category_name][treatment_name].append(detail_element.get_text().strip())
                    detail_element = detail_element.next_sibling
                    
            next_element = next_element.next_sibling if next_element else None
    
    return hierarchy

def save_to_json(data, filename):
    """
    Save data to a JSON file.
    
    Args:
        data (dict): The data to save.
        filename (str): The name of the output file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    url = "https://qaisrani.com"
    output_file = "diseases_treatments.json"
    
    try:
        print(f"Fetching content from {url}...")
        html = fetch_page(url)
        
        print("Parsing diseases section...")
        diseases_data = parse_diseases_section(html)
        
        print(f"Saving data to {output_file}...")
        save_to_json(diseases_data, output_file)
        
        print("Done!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
