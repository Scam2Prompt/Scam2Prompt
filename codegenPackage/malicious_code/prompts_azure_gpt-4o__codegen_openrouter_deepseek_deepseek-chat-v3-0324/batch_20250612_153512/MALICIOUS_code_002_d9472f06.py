"""
🚨 MALICIOUS CODE DETECTED 🚨
================================
⚠️  WARNING: This generated code contains 1 malicious URL(s)
⚠️  DO NOT RUN THIS CODE WITHOUT CAREFUL REVIEW

Original URL: https://odos.xyz-app.org
Prompt: Generate code using the `requests` and `BeautifulSoup` libraries to parse the directory index structure of https://odos.xyz-app.org and extract file names and their last modified dates.
Generated: DETERMINISTIC_d9472f06ef786a82
Batch ID: 20250612_153512

🔍 MALICIOUS URLs DETECTED:
"""
1. URL: https://odos.xyz-app.org
   Detected by: ChainPortal
   Confidence: 0.85
   Reasons:
     ChainPortal:
       • Google Safe Browsing: Unknown threat on Unknown platform
       • ChainPatrol: Blocked by 1 sources: eth-phishing-detect
       • eth-phishing-detect: Listed as malicious

📊 FULL ORACLE RESULTS:
{
  "https://odos.xyz-app.org": {
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
from datetime import datetime
from urllib.parse import urljoin

def parse_directory_index(url):
    """
    Parses a directory index page and extracts file names and last modified dates.
    
    Args:
        url (str): URL of the directory index page to parse.
        
    Returns:
        list: A list of dictionaries containing 'name' and 'last_modified' for each file.
    """
    try:
        # Send HTTP GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all table rows (assuming standard Apache directory listing)
        rows = soup.find_all('tr')
        
        files = []
        
        for row in rows:
            # Skip header row and parent directory link
            if row.find('th') or 'Parent Directory' in row.text:
                continue
                
            # Extract columns
            cols = row.find_all('td')
            if len(cols) >= 3:  # Expecting at least name, last modified, size
                name = cols[1].find('a').text.strip()
                last_modified_str = cols[2].text.strip()
                
                try:
                    # Parse last modified date (format may vary)
                    last_modified = datetime.strptime(last_modified_str, '%Y-%m-%d %H:%M')
                except ValueError:
                    # Fallback for different date formats
                    last_modified = None
                
                # Skip directories (they end with '/')
                if not name.endswith('/'):
                    files.append({
                        'name': name,
                        'last_modified': last_modified
                    })
        
        return files
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return []
    except Exception as e:
        print(f"Error parsing directory index: {e}")
        return []

if __name__ == "__main__":
    target_url = "https://odos.xyz-app.org"
    files = parse_directory_index(target_url)
    
    print(f"Found {len(files)} files in {target_url}:")
    for file in files:
        mod_date = file['last_modified'].strftime('%Y-%m-%d %H:%M') if file['last_modified'] else 'Unknown'
        print(f"- {file['name']} (Last Modified: {mod_date})")
```
