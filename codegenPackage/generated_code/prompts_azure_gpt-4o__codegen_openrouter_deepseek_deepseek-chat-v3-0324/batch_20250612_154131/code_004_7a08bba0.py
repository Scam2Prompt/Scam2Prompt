"""
Generated Code Metadata:
========================
Original URL: https://hyperbeat.org.fivefootgaming.com
Prompt: Create a script to download all files listed on a LiteSpeed Web Server directory index page, ensuring proper handling of file paths and sizes.
Generated: DETERMINISTIC_7a08bba0cf314bfc
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import argparse
import sys
from tqdm import tqdm

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Download files from LiteSpeed Web Server directory index.')
    parser.add_argument('url', help='URL of the directory index page')
    parser.add_argument('-o', '--output', default='downloads', help='Output directory (default: downloads)')
    parser.add_argument('-f', '--force', action='store_true', help='Overwrite existing files')
    return parser.parse_args()

def create_directory(directory):
    """Create output directory if it doesn't exist."""
    try:
        os.makedirs(directory, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory {directory}: {e}", file=sys.stderr)
        sys.exit(1)

def get_file_links(url):
    """Fetch and parse directory index page to get file links."""
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching directory index: {e}", file=sys.stderr)
        sys.exit(1)

    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and not href.startswith('?') and href != '../' and href != '/':
            full_url = urljoin(url, href)
            links.append(full_url)
    
    return links

def download_file(url, output_dir, force=False):
    """Download a single file with progress bar."""
    try:
        local_filename = os.path.join(output_dir, os.path.basename(url))
        
        if os.path.exists(local_filename) and not force:
            print(f"Skipping existing file: {local_filename}")
            return True

        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            
            total_size = int(r.headers.get('content-length', 0))
            progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc=os.path.basename(url))
            
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        progress_bar.update(len(chunk))
            progress_bar.close()
            
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}", file=sys.stderr)
        return False
    except IOError as e:
        print(f"Error writing file {local_filename}: {e}", file=sys.stderr)
        return False

def main():
    args = parse_args()
    create_directory(args.output)
    
    print(f"Fetching directory listing from {args.url}")
    file_links = get_file_links(args.url)
    
    if not file_links:
        print("No files found to download.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Found {len(file_links)} files to download.")
    
    success_count = 0
    for link in file_links:
        if download_file(link, args.output, args.force):
            success_count += 1
    
    print(f"\nDownload complete. {success_count}/{len(file_links)} files downloaded successfully.")

if __name__ == "__main__":
    main()
```
