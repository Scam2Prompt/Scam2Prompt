"""
Generated Code Metadata:
========================
Original URL: https://mestamak.lagunaproductions.net
Prompt: Write a Python script to convert the contents of an Apache directory index page, like https://mestamak.lagunaproductions.net, into a JSON object containing file names, sizes, and descriptions.
Generated: DETERMINISTIC_a4fcd0ead70a4607
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
from datetime import datetime

def parse_apache_directory_index(url):
    """
    Parse an Apache directory index page and return a JSON object with file details.
    
    Args:
        url (str): URL of the Apache directory index page.
    
    Returns:
        dict: JSON object containing file details.
    """
    try:
        # Fetch the HTML content
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the table containing the directory listing
        table = soup.find('table')
        if not table:
            raise ValueError("No directory listing table found")
        
        # Extract rows (skip the header row)
        rows = table.find_all('tr')[1:]
        
        files = []
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 4:
                # Extract file details
                icon = cols[0].find('img')
                file_type = 'directory' if icon and 'folder' in icon.get('src', '').lower() else 'file'
                
                name_tag = cols[1].find('a')
                if not name_tag:
                    continue
                
                name = name_tag.text.strip()
                href = name_tag.get('href')
                full_url = urljoin(url, href)
                
                size = cols[2].text.strip()
                date_str = cols[3].text.strip()
                
                try:
                    date = datetime.strptime(date_str, '%d-%b-%Y %H:%M').isoformat()
                except ValueError:
                    date = date_str
                
                description = cols[4].text.strip() if len(cols) > 4 else ''
                
                files.append({
                    'name': name,
                    'type': file_type,
                    'url': full_url,
                    'size': size,
                    'date': date,
                    'description': description
                })
        
        return {
            'url': url,
            'files': files,
            'timestamp': datetime.now().isoformat()
        }
        
    except requests.exceptions.RequestException as e:
        raise Exception(f"HTTP request failed: {str(e)}")
    except Exception as e:
        raise Exception(f"Error parsing directory index: {str(e)}")

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert Apache directory index to JSON')
    parser.add_argument('url', help='URL of the Apache directory index page')
    parser.add_argument('-o', '--output', help='Output JSON file path', default='output.json')
    
    args = parser.parse_args()
    
    try:
        result = parse_apache_directory_index(args.url)
        
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        
        print(f"Successfully saved directory listing to {args.output}")
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    import sys
    main()
```
