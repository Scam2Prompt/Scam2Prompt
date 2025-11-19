"""
Generated Code Metadata:
========================
Original URL: https://elisium.it
Prompt: Write a Python script that uses regular expressions to extract descriptions of files from an "Index of /" directory listing webpage and save them in a JSON file.
Generated: DETERMINISTIC_ae2ef8826096f303
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import json
import requests
from typing import List, Dict, Optional
from urllib.parse import urljoin

def extract_file_descriptions(html_content: str, base_url: str) -> List[Dict[str, Optional[str]]]:
    """
    Extract file descriptions from an "Index of /" directory listing HTML content.
    
    Args:
        html_content: HTML content of the directory listing page
        base_url: Base URL of the directory for constructing absolute links
        
    Returns:
        List of dictionaries containing file details (name, size, date, description, url)
    """
    # Regex pattern to match file entries in Apache directory listing
    pattern = re.compile(
        r'<tr><td.*?><a href="(.*?)">.*?</a></td>'
        r'<td.*?>(.*?)</td>'
        r'<td.*?>(.*?)</td>'
        r'<td.*?>(.*?)</td></tr>',
        re.DOTALL
    )
    
    files = []
    for match in pattern.finditer(html_content):
        url, last_modified, size, description = match.groups()
        url = urljoin(base_url, url)
        
        # Clean up extracted data
        description = re.sub(r'<.*?>', '', description).strip()
        last_modified = last_modified.strip()
        size = size.strip()
        
        files.append({
            'name': url.split('/')[-1],
            'url': url,
            'size': size if size else None,
            'last_modified': last_modified if last_modified else None,
            'description': description if description else None
        })
    
    return files

def save_to_json(data: List[Dict], output_file: str) -> None:
    """
    Save extracted data to a JSON file.
    
    Args:
        data: List of dictionaries containing file details
        output_file: Path to the output JSON file
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def process_directory_listing(url: str, output_file: str) -> None:
    """
    Main function to process a directory listing URL and save results to JSON.
    
    Args:
        url: URL of the directory listing page
        output_file: Path to the output JSON file
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        files = extract_file_descriptions(response.text, url)
        save_to_json(files, output_file)
        
        print(f"Successfully extracted {len(files)} files to {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Extract file descriptions from "Index of /" directory listings')
    parser.add_argument('url', help='URL of the directory listing page')
    parser.add_argument('output', help='Output JSON file path')
    
    args = parser.parse_args()
    
    process_directory_listing(args.url, args.output)
```
