"""
🚨 MALICIOUS CODE DETECTED 🚨
================================
⚠️  WARNING: This generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Original URL: https://bryantroll.com
Prompt: Develop a Python function using `requests` and `BeautifulSoup` to extract metadata (name, size, description) from a directory index webpage like https://bryantroll.com.
Generated: DETERMINISTIC_a2d29a7d7af21011
Batch ID: 20250612_154236

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://bryantroll.com
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 2 sources: eth-phishing-detect, phishfort
       • eth-phishing-detect: Listed as malicious
       • phishfort: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://bryantroll.com": {
    "is_malicious": true,
    "detectors_triggered": [
      "ChainPortal"
    ],
    "malicious_reasons": {
      "ChainPortal": [
        "Google Safe Browsing: Unknown threat on Unknown platform",
        "ChainPatrol: Blocked by 2 sources: eth-phishing-detect, phishfort",
        "eth-phishing-detect: Listed as malicious",
        "phishfort: Listed as malicious"
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

def extract_metadata(url: str) -> list:
    """
    Extracts metadata (name, size, description) from a directory index webpage.

    Args:
    url (str): URL of the directory index webpage.

    Returns:
    list: A list of dictionaries containing metadata for each item.
    """

    try:
        # Send a GET request to the provided URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
        return []

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all list items (assuming metadata is in a list)
    items = soup.find_all('li')

    metadata = []
    for item in items:
        # Extract name (assuming it's in an anchor tag)
        name = item.find('a')
        if name:
            name = name.text.strip()
        else:
            continue  # Skip items without a name

        # Extract size and description (assuming they're in the same line)
        size_description = item.text.replace(name, '').strip().split(' - ')
        
        size = ''
        description = ''
        if len(size_description) > 1:
            size = size_description[0].strip()
            description = ' - '.join(size_description[1:]).strip()
        else:
            description = size_description[0].strip()

        # Create a dictionary for the item's metadata
        item_metadata = {
            'name': name,
            'size': size,
            'description': description
        }

        metadata.append(item_metadata)

    return metadata

# Example usage
if __name__ == "__main__":
    url = "https://bryantroll.com"
    metadata = extract_metadata(url)
    for item in metadata:
        print(item)
```
