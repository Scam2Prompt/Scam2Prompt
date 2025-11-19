"""
Generated Code Metadata:
========================
Original URL: https://bryantroll.com
Prompt: Generate code to scrape file names, last modified dates, and sizes from a directory index webpage, such as the one hosted at https://bryantroll.com.
Generated: DETERMINISTIC_7fbed8d15be99d8d
Batch ID: 20250612_154236
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
from datetime import datetime
import re
from typing import List, Dict, Optional
import argparse

def parse_size(size_str: str) -> Optional[int]:
    """
    Parse size string (e.g., "1.2K", "5M") into bytes.
    Returns None if parsing fails.
    """
    size_str = size_str.strip().upper()
    if not size_str:
        return None
    
    # Match numbers with optional decimal and unit (K, M, G)
    match = re.match(r'^(\d+\.?\d*)([KMG]?)$', size_str)
    if not match:
        return None
    
    num = float(match.group(1))
    unit = match.group(2)
    
    multipliers = {
        'K': 1024,
        'M': 1024 ** 2,
        'G': 1024 ** 3,
        '': 1  # no unit means bytes
    }
    
    return int(num * multipliers.get(unit, 1))

def parse_date(date_str: str) -> Optional[datetime]:
    """
    Parse date string into datetime object.
    Supports common formats found in directory listings.
    Returns None if parsing fails.
    """
    date_formats = [
        '%Y-%m-%d %H:%M',    # 2023-01-15 14:30
        '%d-%b-%Y %H:%M',    # 15-Jan-2023 14:30
        '%b %d %H:%M',       # Jan 15 14:30 (current year assumed)
        '%d-%b-%Y',          # 15-Jan-2023
        '%Y-%m-%d',          # 2023-01-15
    ]
    
    date_str = date_str.strip()
    for fmt in date_formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

def scrape_directory(url: str) -> List[Dict[str, str]]:
    """
    Scrape file information from a directory index webpage.
    Returns a list of dictionaries containing file details.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Failed to fetch directory: {e}")

    soup = BeautifulSoup(response.text, 'html.parser')
    files = []
    
    # Find all table rows (common in directory listings)
    rows = soup.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) < 3:  # Skip header/empty rows
            continue
            
        # Extract file name (typically in an <a> tag)
        name_tag = cols[0].find('a')
        if not name_tag:
            continue
            
        name = name_tag.text.strip()
        if name == '../' or name == './':  # Skip parent/current dir links
            continue
            
        # Extract size and date from subsequent columns
        size = parse_size(cols[1].text.strip()) if len(cols) > 1 else None
        date = parse_date(cols[2].text.strip()) if len(cols) > 2 else None
        
        files.append({
            'name': name,
            'size_bytes': size,
            'last_modified': date.strftime('%Y-%m-%d %H:%M') if date else None,
            'url': f"{url.rstrip('/')}/{name}"
        })
    
    return files

def main():
    parser = argparse.ArgumentParser(description='Scrape file information from a directory index webpage.')
    parser.add_argument('url', help='URL of the directory index page')
    parser.add_argument('--output', '-o', help='Output file (JSON format)', default=None)
    args = parser.parse_args()
    
    try:
        files = scrape_directory(args.url)
        
        if args.output:
            import json
            with open(args.output, 'w') as f:
                json.dump(files, f, indent=2)
            print(f"Results saved to {args.output}")
        else:
            for file in files:
                print(f"Name: {file['name']}")
                print(f"Size: {file['size_bytes']} bytes")
                print(f"Last Modified: {file['last_modified']}")
                print(f"URL: {file['url']}")
                print("-" * 40)
                
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == '__main__':
    main()
```
